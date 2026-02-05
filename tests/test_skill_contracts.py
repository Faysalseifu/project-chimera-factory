import pytest
from jsonschema import ValidationError, validate

# From skills/skill_fetch_and_filter_trends/README.md
TREND_INPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "region": {"type": "string"},
        "niches": {"type": "array", "items": {"type": "string"}},
        "hours": {"type": "integer"},
        "threshold": {"type": "number"},
    },
    "required": ["region", "niches", "hours"],
}


def test_valid_trend_input():
    valid = {
        "region": "ethiopia",
        "niches": ["fashion"],
        "hours": 24,
        "threshold": 0.75,
    }
    validate(instance=valid, schema=TREND_INPUT_SCHEMA)


def test_invalid_trend_input_missing_required():
    invalid = {
        "niches": ["fashion"],
        "hours": 24,
    }
    with pytest.raises(ValidationError):
        validate(instance=invalid, schema=TREND_INPUT_SCHEMA)