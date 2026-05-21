import pytest

from src.sdk.decorators import on_event


def test_on_event_rejects_blank_event_type():
    for event_type in ("", "   ", "\t\n"):
        with pytest.raises(ValueError, match="non-empty string"):
            on_event(event_type)


def test_on_event_rejects_non_string_event_type():
    with pytest.raises(ValueError, match="non-empty string"):
        on_event(None)


def test_on_event_marks_handler_with_event_type():
    @on_event("user.created")
    async def handle_user_created():
        return "ok"

    assert handle_user_created.__event_handler__ == "user.created"
