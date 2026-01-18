def search_registry(registry, term):
    term = term.lower()
    results = []

    for entry_id, entry in registry.items():
        meta = entry.meta

        haystack = " ".join([
            entry_id,
            meta.title,
            meta.category,
            " ".join(meta.tags or [])
        ]).lower()

        if term in haystack:
            results.append((entry_id, meta))

    return results

