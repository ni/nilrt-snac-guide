"""Load and validate engineer-authored control dispositions."""

from pathlib import Path

import jsonschema
import yaml

STATUSES = {
    "implemented": "Implemented by vendor",
    "not_implemented": "Not implemented by vendor",
    "end_user": "Must be implemented by end user",
    "not_applicable": "Not applicable",
}

CONTROL_ID = r"^3\.[0-9]+\.[0-9]+$"

CONTROL_SCHEMA = {
    "type": "object",
    "properties": {
        "status": {"enum": list(STATUSES)},
        "disposition": {
            "type": "array",
            "minItems": 1,
            "items": {"type": "string", "pattern": r"\S"},
        },
    },
    "required": ["status", "disposition"],
    "additionalProperties": False,
}

FILE_SCHEMA = {
    "type": "object",
    "patternProperties": {CONTROL_ID: CONTROL_SCHEMA},
    "additionalProperties": False,
}


class GenerationError(Exception):
    """Raised with every problem found, one per line."""

    def __init__(self, problems):
        """Store validation problems and format the exception message."""
        self.problems = list(problems)
        super().__init__("\n".join(self.problems))


class _UniqueKeyLoader(yaml.SafeLoader):
    def construct_mapping(self, node, deep=False):
        seen = set()
        for key_node, _ in node.value:
            key = self.construct_object(key_node, deep=deep)
            if key in seen:
                raise yaml.constructor.ConstructorError(
                    None, None, f"duplicate key {key!r}", key_node.start_mark
                )
            seen.add(key)
        return super().construct_mapping(node, deep)


def _load_file(path):
    try:
        with open(path, encoding="utf-8") as handle:
            data = yaml.load(handle, Loader=_UniqueKeyLoader)  # noqa: S506 (safe subclass)
    except yaml.YAMLError as exc:
        raise GenerationError([f"{path}: invalid YAML: {exc}"]) from exc
    return {} if data is None else data


def _validate_file(path, data):
    if not isinstance(data, dict):
        return [f"{path}: expected a mapping of control id to disposition"]
    problems = []
    for key in data:
        if not isinstance(key, str):
            problems.append(f"{path}: control id {key!r} must be a quoted string")
    if problems:
        return problems
    validator = jsonschema.Draft202012Validator(FILE_SCHEMA)
    for error in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        where = ".".join(str(p) for p in error.path) or "<file>"
        problems.append(f"{path}: {where}: {error.message}")
    return problems


def load_dispositions(directory):
    """Return ``{control_id: {status, disposition}}`` for every YAML file."""
    controls, problems = {}, []
    for path in sorted(Path(directory).glob("*.yml")):
        family = path.stem
        data = _load_file(path)
        file_problems = _validate_file(path, data)
        problems.extend(file_problems)
        if file_problems:
            continue
        for control_id, entry in data.items():
            if not control_id.startswith(family + "."):
                problems.append(f"{path}: control {control_id} does not belong in family {family}")
            elif control_id in controls:
                problems.append(f"{path}: control {control_id} is defined more than once")
            controls[control_id] = entry
    if problems:
        raise GenerationError(problems)
    return controls


def check_coverage(nist_data, controls):
    """Every active NIST control needs a disposition, and nothing extra."""
    required, withdrawn = set(), set()
    for family in nist_data["families"]:
        for req in family["requirements"]:
            (withdrawn if "withdrawn" in req else required).add(req["id"])
    problems = [
        f"{cid}: no disposition defined" for cid in sorted(required - set(controls), key=_key)
    ]
    for cid in sorted(set(controls) - required, key=_key):
        reason = (
            "is withdrawn in NIST SP 800-171"
            if cid in withdrawn
            else "is not a NIST SP 800-171 control"
        )
        problems.append(f"{cid}: disposition defined but control {reason}")
    if problems:
        raise GenerationError(problems)


def _key(control_id):
    return [int(p) for p in control_id.split(".")]
