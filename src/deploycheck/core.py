from collections.abc import Iterable, Mapping


def validate(services: Iterable[Mapping[str, object]]) -> list[str]:
    """Return validation errors for simple deployment definitions."""
    errors: list[str] = []
    for index, service in enumerate(services):
        name = str(service.get("name", "")).strip()
        image = str(service.get("image", "")).strip()
        replicas = service.get("replicas", 1)
        if not name:
            errors.append(f"service[{index}]: missing name")
        if not image:
            errors.append(f"service[{index}]: missing image")
        if isinstance(replicas, bool) or not isinstance(replicas, int) or replicas < 1:
            errors.append(f"service[{index}]: replicas must be a positive integer")
    return errors
