from jsonschema import validate

# Based on skills/skill_fetch_trends/README.md
TREND_OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "trends": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "topic": {"type": "string"},
                    "volume": {"type": "integer"},
                    "sentiment": {"type": "number"},
                },
                "required": ["topic", "volume", "sentiment"],
            },
        }
    },
    "required": ["trends"],
}


def test_trend_fetcher_output_contract():
    from skills.skill_fetch_trends.skill import fetch_trends  # expected future module

    result = fetch_trends(region="ethiopia", niche="fashion", time_window="24h")
    validate(instance=result, schema=TREND_OUTPUT_SCHEMA)