import inspect


def test_fetch_trends_interface_signature():
    from skills.skill_fetch_trends.skill import fetch_trends  # expected future module

    params = list(inspect.signature(fetch_trends).parameters.keys())
    assert params == ["region", "niche", "time_window"]


def test_fetch_and_filter_trends_interface_signature():
    from skills.skill_fetch_and_filter_trends.skill import (
        fetch_and_filter_trends,
    )  # expected future module

    params = list(inspect.signature(fetch_and_filter_trends).parameters.keys())
    assert params == ["region", "niches", "hours", "threshold"]