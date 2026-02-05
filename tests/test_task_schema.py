import pytest
from jsonschema import ValidationError, validate

# Minimal schema based on specs/technical.md
TASK_SCHEMA = {
    "type": "object",
    "properties": {
        "task_id": {"type": "string"},
        "task_type": {
            "type": "string",
            "enum": [
                "perceive_trends",
                "generate_text",
                "generate_image",
                "publish",
                "transfer_usdc",
            ],
        },
        "priority": {"type": "string", "enum": ["high", "medium", "low"]},
        "created_at": {"type": "string"},
        "input": {"type": "object"},
    },
    "required": ["task_id", "task_type", "priority", "created_at"],
    "additionalProperties": True,
}


def test_valid_task_schema():
    valid_task = {
        "task_id": "123e4567-e89b-12d3-a456-426614174000",
        "task_type": "generate_image",
        "priority": "high",
        "created_at": "2026-02-05T17:00:00Z",
        "input": {"prompt": "test"},
    }
    validate(instance=valid_task, schema=TASK_SCHEMA)


def test_invalid_task_schema_missing_required():
    invalid_task = {
        "task_type": "generate_image",
        "priority": "high",
    }
    with pytest.raises(ValidationError):
        validate(instance=invalid_task, schema=TASK_SCHEMA)