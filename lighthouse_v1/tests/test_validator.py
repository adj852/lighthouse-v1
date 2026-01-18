import pytest

from validator.validator import validate_flow, FlowValidationError


class DummyMeta:
    def __init__(self, id="test"):
        self.id = id


class DummyEntry:
    def __init__(self, data, entry_id="test"):
        self.data = data
        self.meta = DummyMeta(entry_id)


# ------------------------
# VALID CASES
# ------------------------

def test_valid_simple_flow():
    entry = DummyEntry({
        "start": "start",
        "nodes": {
            "start": {
                "question": "Continue?",
                "options": {"y": "Yes"},
                "next": {"y": "END"},
            }
        }
    })

    validate_flow(entry)  # should not raise


def test_valid_result_node():
    entry = DummyEntry({
        "start": "done",
        "nodes": {
            "done": {
                "result": ["All good"]
            }
        }
    })

    validate_flow(entry)


def test_valid_result_dict():
    entry = DummyEntry({
        "start": "done",
        "nodes": {
            "done": {
                "result": [
                    {"description": "Run command", "command": "echo hi"}
                ]
            }
        }
    })

    validate_flow(entry)


# ------------------------
# STRUCTURE ERRORS
# ------------------------

def test_missing_start():
    entry = DummyEntry({
        "nodes": {}
    })

    with pytest.raises(FlowValidationError):
        validate_flow(entry)


def test_start_not_found():
    entry = DummyEntry({
        "start": "missing",
        "nodes": {}
    })

    with pytest.raises(FlowValidationError):
        validate_flow(entry)


def test_nodes_not_mapping():
    entry = DummyEntry({
        "start": "a",
        "nodes": []
    })

    with pytest.raises(FlowValidationError):
        validate_flow(entry)


# ------------------------
# QUESTION NODE ERRORS
# ------------------------

def test_question_missing_options():
    entry = DummyEntry({
        "start": "a",
        "nodes": {
            "a": {
                "question": "Broken",
                "next": {"y": "END"}
            }
        }
    })

    with pytest.raises(FlowValidationError):
        validate_flow(entry)


def test_next_references_unknown_node():
    entry = DummyEntry({
        "start": "a",
        "nodes": {
            "a": {
                "question": "Go?",
                "options": {"y": "Yes"},
                "next": {"y": "nope"}
            }
        }
    })

    with pytest.raises(FlowValidationError):
        validate_flow(entry)


def test_next_key_not_in_options():
    entry = DummyEntry({
        "start": "a",
        "nodes": {
            "a": {
                "question": "Go?",
                "options": {"y": "Yes"},
                "next": {"n": "END"}
            }
        }
    })

    with pytest.raises(FlowValidationError):
        validate_flow(entry)


# ------------------------
# RESULT NODE ERRORS
# ------------------------

def test_empty_result_list():
    entry = DummyEntry({
        "start": "a",
        "nodes": {
            "a": {
                "result": []
            }
        }
    })

    with pytest.raises(FlowValidationError):
        validate_flow(entry)


def test_invalid_result_item_type():
    entry = DummyEntry({
        "start": "a",
        "nodes": {
            "a": {
                "result": [123]
            }
        }
    })

    with pytest.raises(FlowValidationError):
        validate_flow(entry)


def test_result_dict_missing_description():
    entry = DummyEntry({
        "start": "a",
        "nodes": {
            "a": {
                "result": [{"command": "ls"}]
            }
        }
    })

    with pytest.raises(FlowValidationError):
        validate_flow(entry)


# ------------------------
# INVALID NODE TYPES
# ------------------------

def test_node_without_question_or_result():
    entry = DummyEntry({
        "start": "a",
        "nodes": {
            "a": {}
        }
    })

    with pytest.raises(FlowValidationError):
        validate_flow(entry)


def test_node_with_both_question_and_result():
    entry = DummyEntry({
        "start": "a",
        "nodes": {
            "a": {
                "question": "Bad",
                "options": {"y": "Yes"},
                "next": {"y": "END"},
                "result": ["oops"]
            }
        }
    })

    with pytest.raises(FlowValidationError):
        validate_flow(entry)

