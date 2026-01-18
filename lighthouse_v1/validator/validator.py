class FlowValidationError(Exception):
    pass


def validate_flow(entry):
    data = entry.data

    if not isinstance(data, dict):
        raise FlowValidationError("Flow data must be a mapping")

    if "start" not in data or "nodes" not in data:
        raise FlowValidationError("Flow must contain 'start' and 'nodes'")

    start = data["start"]
    nodes = data["nodes"]

    if not isinstance(start, str):
        raise FlowValidationError("'start' must be a string")

    if not isinstance(nodes, dict):
        raise FlowValidationError("'nodes' must be a mapping")

    if start not in nodes:
        raise FlowValidationError(f"Start node '{start}' not found")

    for node_id, node in nodes.items():
        validate_node(node_id, node, nodes)


def validate_node(node_id, node, all_nodes):
    if not isinstance(node, dict):
        raise FlowValidationError(f"Node '{node_id}' must be a mapping")

    has_question = "question" in node
    has_result = "result" in node

    if has_question and has_result:
        raise FlowValidationError(
            f"Node '{node_id}' cannot contain both 'question' and 'result'"
        )

    if not has_question and not has_result:
        raise FlowValidationError(
            f"Node '{node_id}' must contain either 'question' or 'result'"
        )

    if has_question:
        validate_question_node(node_id, node, all_nodes)

    if has_result:
        validate_result_node(node_id, node)


def validate_question_node(node_id, node, all_nodes):
    if "options" not in node or "next" not in node:
        raise FlowValidationError(
            f"Node '{node_id}' has question but missing options/next"
        )

    if not isinstance(node["question"], str):
        raise FlowValidationError(
            f"Node '{node_id}' question must be a string"
        )

    options = node["options"]
    next_map = node["next"]

    if not isinstance(options, dict) or not options:
        raise FlowValidationError(
            f"Node '{node_id}' options must be a non-empty mapping"
        )

    if not isinstance(next_map, dict):
        raise FlowValidationError(
            f"Node '{node_id}' next must be a mapping"
        )

    for key, target in next_map.items():
        if key not in options:
            raise FlowValidationError(
                f"Node '{node_id}' has next for unknown option '{key}'"
            )

        if target != "END" and target not in all_nodes:
            raise FlowValidationError(
                f"Node '{node_id}' references unknown node '{target}'"
            )


def validate_result_node(node_id, node):
    result = node["result"]

    if not isinstance(result, list) or not result:
        raise FlowValidationError(
            f"Node '{node_id}' result must be a non-empty list"
        )

    for item in result:
        if isinstance(item, str):
            continue

        if isinstance(item, dict):
            if "description" not in item:
                raise FlowValidationError(
                    f"Node '{node_id}' result dict missing 'description'"
                )
            if not isinstance(item["description"], str):
                raise FlowValidationError(
                    f"Node '{node_id}' result description must be a string"
                )
            continue

        raise FlowValidationError(
            f"Node '{node_id}' result items must be strings or dicts"
        )

