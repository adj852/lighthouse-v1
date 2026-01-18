                
from ui import render as ui


def run_flow(entry):
    data = entry.data
    nodes = data["nodes"]
    current = data["start"]

    while True:
        if current == "END":
            ui.success("End of flow")
            return

        node = nodes[current]

                       
        if "question" in node:
            ui.section(node["question"])

            for key, label in node["options"].items():
                ui.option(key, label)

            ui.divider()
            choice = ui.prompt()

            if not choice:
                ui.warn("Please enter a choice.")
                continue

            if choice not in node["next"]:
                ui.warn("Invalid option.")
                continue

            current = node["next"][choice]

                     
        else:
            ui.section("Result")

            for item in node["result"]:
                if isinstance(item, dict):
                    ui.text(f"- {item.get('description', '')}")
                    if "command" in item:
                        ui.text(f"  $ {item['command']}")
                else:
                    ui.text(f"- {item}")

            ui.divider()
            return

