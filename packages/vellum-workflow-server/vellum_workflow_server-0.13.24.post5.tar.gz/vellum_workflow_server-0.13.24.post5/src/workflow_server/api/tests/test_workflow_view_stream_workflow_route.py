import pytest
from contextlib import redirect_stdout
from importlib.metadata import version
import io
import json
from unittest import mock
from uuid import uuid4

from workflow_server.code_exec_runner import run_code_exec_stream
from workflow_server.server import create_app


def flask_stream(request_body: dict) -> tuple[int, list]:
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.post("/workflow/stream", json=request_body)
        status_code = response.status_code
        return status_code, [json.loads(line) for line in response.data.decode().split("\n") if line]


def code_exec_stream(request_body: dict) -> tuple[int, list]:
    output = io.StringIO()

    with mock.patch("os.read") as mocked_os_read, redirect_stdout(output):
        mocked_os_read.return_value = (json.dumps(request_body) + "\n--vellum-input-stop--\n").encode("utf-8")
        run_code_exec_stream()

    lines = output.getvalue().split("\n")
    events = []
    for line in lines:
        if "--event--" in line:
            events.append(json.loads(line.replace("--event--", "")))

    return 200, events


@pytest.fixture(params=[flask_stream, code_exec_stream])
def both_stream_types(request):
    return request.param


def test_stream_workflow_route__happy_path(both_stream_types):
    # GIVEN a valid request body
    span_id = uuid4()
    request_body = {
        "timeout": 360,
        "execution_id": str(span_id),
        "inputs": [],
        "workspace_api_key": "test",
        "module": "workflow",
        "files": {
            "__init__.py": "",
            "workflow.py": """\
from vellum.workflows import BaseWorkflow

class Workflow(BaseWorkflow):
    class Outputs(BaseWorkflow.Outputs):
        foo = "hello"
""",
        },
    }

    # WHEN we call the stream route
    status_code, events = both_stream_types(request_body)

    # THEN we get a 200 response
    assert status_code == 200, events

    # THEN we get the expected events
    assert events[0] == {
        "id": mock.ANY,
        "trace_id": mock.ANY,
        "span_id": str(span_id),
        "timestamp": mock.ANY,
        "api_version": "2024-10-25",
        "parent": None,
        "name": "vembda.execution.initiated",
        "body": {
            "sdk_version": version("vellum-ai"),
            "server_version": "local",
            "display_context": None,
        },
    }

    assert events[1]["name"] == "workflow.execution.initiated", events[1]
    assert events[2]["name"] == "workflow.execution.fulfilled", events[2]

    assert events[3] == {
        "id": mock.ANY,
        "trace_id": events[0]["trace_id"],
        "span_id": str(span_id),
        "timestamp": mock.ANY,
        "api_version": "2024-10-25",
        "parent": None,
        "name": "vembda.execution.fulfilled",
        "body": mock.ANY,
    }
    assert events[3]["body"] == {
        "exit_code": 0,
        "log": "",
        "stderr": "",
        "timed_out": False,
        "container_overhead_latency": mock.ANY,
    }

    assert len(events) == 4


def test_stream_workflow_route__happy_path_with_inputs(both_stream_types):
    # GIVEN a valid request body
    span_id = uuid4()
    request_body = {
        "timeout": 360,
        "execution_id": str(span_id),
        "inputs": [
            {"name": "foo", "type": "STRING", "value": "hello"},
        ],
        "workspace_api_key": "test",
        "module": "workflow",
        "files": {
            "__init__.py": "",
            "workflow.py": """\
from vellum.workflows import BaseWorkflow
from vellum.workflows.state import BaseState
from .inputs import Inputs

class Workflow(BaseWorkflow[Inputs, BaseState]):
    class Outputs(BaseWorkflow.Outputs):
        foo = "hello"
""",
            "inputs.py": """\
from vellum.workflows.inputs import BaseInputs

class Inputs(BaseInputs):
    foo: str
""",
        },
    }

    # WHEN we call the stream route
    status_code, events = both_stream_types(request_body)

    # THEN we get a 200 response
    assert status_code == 200, events

    # THEN we get the expected events
    assert events[0] == {
        "id": mock.ANY,
        "trace_id": mock.ANY,
        "span_id": str(span_id),
        "timestamp": mock.ANY,
        "api_version": "2024-10-25",
        "parent": None,
        "name": "vembda.execution.initiated",
        "body": {
            "sdk_version": version("vellum-ai"),
            "server_version": "local",
            "display_context": None,
        },
    }

    assert events[1]["name"] == "workflow.execution.initiated", events[1]
    assert events[2]["name"] == "workflow.execution.fulfilled", events[2]

    assert events[3] == {
        "id": mock.ANY,
        "trace_id": events[0]["trace_id"],
        "span_id": str(span_id),
        "timestamp": mock.ANY,
        "api_version": "2024-10-25",
        "parent": None,
        "name": "vembda.execution.fulfilled",
        "body": mock.ANY,
    }
    assert events[3]["body"] == {
        "exit_code": 0,
        "log": "",
        "stderr": "",
        "timed_out": False,
        "container_overhead_latency": mock.ANY,
    }

    assert len(events) == 4


def test_stream_workflow_route__bad_indent_in_inputs_file(both_stream_types):
    # GIVEN a valid request body
    span_id = uuid4()
    request_body = {
        "timeout": 360,
        "execution_id": str(span_id),
        "inputs": [
            {"name": "foo", "type": "STRING", "value": "hello"},
        ],
        "workspace_api_key": "test",
        "module": "workflow",
        "files": {
            "__init__.py": "",
            "workflow.py": """\
from vellum.workflows import BaseWorkflow
from vellum.workflows.state import BaseState
from .inputs import Inputs

class Workflow(BaseWorkflow[Inputs, BaseState]):
    class Outputs(BaseWorkflow.Outputs):
        foo = "hello"
""",
            "inputs.py": """\
from vellum.workflows.inputs import BaseInputs

  class Inputs(BaseInputs):
     foo: str
""",
        },
    }

    # WHEN we call the stream route
    status_code, events = both_stream_types(request_body)

    # THEN we get a 200 response
    assert status_code == 200, events

    # THEN we get the expected events
    assert events[0] == {
        "id": mock.ANY,
        "trace_id": mock.ANY,
        "span_id": str(span_id),
        "timestamp": mock.ANY,
        "api_version": "2024-10-25",
        "parent": None,
        "name": "vembda.execution.initiated",
        "body": {
            "sdk_version": version("vellum-ai"),
            "server_version": "local",
            "display_context": None,
        },
    }

    assert events[1] == {
        "id": mock.ANY,
        "trace_id": events[0]["trace_id"],
        "span_id": str(span_id),
        "timestamp": mock.ANY,
        "api_version": "2024-10-25",
        "parent": None,
        "name": "vembda.execution.fulfilled",
        "body": mock.ANY,
    }
    assert events[1]["body"] == {
        "exit_code": -1,
        "log": "",
        "stderr": "Failed to initialize workflow: unexpected indent (<string>, line 3)",
        "timed_out": False,
        "container_overhead_latency": mock.ANY,
    }

    assert len(events) == 2
