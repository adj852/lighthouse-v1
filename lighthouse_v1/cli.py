import sys

from loader import load_knowledge_directory
from flow_runner import run_flow
from validator.validator import validate_flow
from search import search_registry
from ui.help import show_help

from ui.render import (
    header,
    section,
    option,
    divider,
    prompt,
    success,
    warn,
)

APP_HEADER = (
    "Lighthouse v1\n"
    "An interactive, Arch-style Linux troubleshooting and learning guide."
)


# ============================================================
# INTERACTIVE MODE
# ============================================================

def interactive_menu(registry):
    while True:
        header(APP_HEADER)

        section("What would you like to do?")
        option("h", "Help")
        option("s", "Search guides")
        option("l", "List available guides")
        option("r", "Run a guide")
        option("q", "Quit")
        divider()

        choice = prompt()

        if choice == "q":
            success("Goodbye.")
            return

        elif choice == "h":
            show_help()
            input("\nPress Enter to continue...")

        elif choice == "s":
            search_prompt(registry)

        elif choice == "l":
            list_guides(registry)

        elif choice == "r":
            run_guide_prompt(registry)

        else:
            warn("Unknown option.")
            input("Press Enter to continue...")


def list_guides(registry):
    header("Available guides")
    for entry_id, entry in registry.items():
        print(f"- {entry_id}: {entry.meta.title}")
    input("\nPress Enter to continue...")


def run_guide_prompt(registry):
    guide_id = input("Enter guide id: ").strip()

    entry = registry.get(guide_id)
    if not entry:
        warn("Unknown guide.")
        input("Press Enter to continue...")
        return

    validate_flow(entry)
    run_flow(entry)


def search_prompt(registry):
    term = input("Search term: ").strip()
    if not term:
        return

    results = search_registry(registry, term)

    section(f"Search results for '{term}'")
    if not results:
        warn("No matching guides found.")
    else:
        for entry_id, meta in results:
            print(f"- {entry_id}: {meta.title} [{meta.category}]")

    input("\nPress Enter to continue...")


# ============================================================
# COMMAND MODE
# ============================================================

def main():
    registry = load_knowledge_directory("knowledge", verbose=False)

    # No arguments → interactive mode
    if len(sys.argv) == 1:
        interactive_menu(registry)
        return

    command = sys.argv[1]

    if command == "list":
        for entry_id, entry in registry.items():
            print(f"{entry_id:20} {entry.meta.title}")
        return

    elif command == "run":
        if len(sys.argv) < 3:
            warn("Missing guide id.")
            return

        entry = registry.get(sys.argv[2])
        if not entry:
            warn("Unknown guide.")
            return

        validate_flow(entry)
        run_flow(entry)
        return

    elif command == "validate":
        if len(sys.argv) < 3:
            warn("Missing guide id.")
            return

        entry = registry.get(sys.argv[2])
        if not entry:
            warn("Unknown guide.")
            return

        validate_flow(entry)
        success("Flow is valid.")
        return

    elif command == "help":
        show_help()
        return

    elif command == "search":
        if len(sys.argv) < 3:
            warn("Please provide a search term.")
            return

        term = " ".join(sys.argv[2:])
        results = search_registry(registry, term)

        if not results:
            warn("No matching guides found.")
            return

        section(f"Search results for '{term}'")
        for entry_id, meta in results:
            print(f"- {entry_id}: {meta.title} [{meta.category}]")
        return

    else:
        warn("Unknown command.")


if __name__ == "__main__":
    main()

