from pathlib import Path
import yaml

from schema.models import KnowledgeEntry

def derive_metadata(path: Path) -> dict:
    """
    Derive metadata from file path.
    """
    file_id = path.stem
    category = path.parent.name

    title = file_id.replace("_", " ").replace("-", " ").title()

    return {
        "id": file_id,
        "title": title,
        "category": category,
        "type": "flow",
        "tags": [],
        "arch_specific": True,
    }


def load_knowledge_entry(path: str | Path) -> KnowledgeEntry:
    """
    Load a YAML file and wrap it into a KnowledgeEntry.
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    with path.open("r", encoding="utf-8") as f:
        raw_data = yaml.safe_load(f)

    if not isinstance(raw_data, dict):
        raise ValueError(f"Invalid YAML structure in {path}")

    metadata = derive_metadata(path)

    wrapped = {
        "meta": metadata,
        "data": raw_data,
    }

    return KnowledgeEntry(**wrapped)


def load_knowledge_directory(base_path: str | Path, verbose: bool = False) -> dict[str, KnowledgeEntry]:

    """
    Load all YAML knowledge files under a directory.
    Returns a registry of KnowledgeEntry objects.
    """
    base_path = Path(base_path)

    if not base_path.exists():
        raise FileNotFoundError(f"Directory not found: {base_path}")

    registry: dict[str, KnowledgeEntry] = {}
    errors: list[str] = []

    for path in base_path.rglob("*.yaml"):
        try:
            entry = load_knowledge_entry(path)

            entry_id = entry.meta.id

            if entry_id in registry:
                raise ValueError(f"Duplicate knowledge id: {entry_id}")

            registry[entry_id] = entry

        except Exception as e:
            errors.append(f"{path}: {e}")

                                        
    if verbose:
        print("\n=== Knowledge Load Report ===")
        print(f"Loaded entries: {len(registry)}")

        if errors:
            print(f"Errors: {len(errors)}")
            for err in errors:
                print(f" - {err}")
        else:
            print("No errors found.")


    return registry

if __name__ == "__main__":
    print("Loader started")

    registry = load_knowledge_directory("knowledge", verbose=True)

    print("\nAvailable knowledge entries:")
    for entry_id, entry in registry.items():
        print(f"- {entry_id}: {entry.meta.title}")

