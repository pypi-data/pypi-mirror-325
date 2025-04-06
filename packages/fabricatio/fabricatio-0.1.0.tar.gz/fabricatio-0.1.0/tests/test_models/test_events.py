from fabricatio.models.events import Event


def test_event_from_string():
    event = Event.from_string("test.event")
    assert event.segments == ["test", "event"]


def test_event_collapse():
    event = Event.from_string("test.event")
    assert event.collapse() == "test.event"


def test_event_push():
    event = Event.from_string("test.event")
    event.push("new_segment")
    assert event.segments == ["test", "event", "new_segment"]


def test_event_pop():
    event = Event.from_string("test.event")
    assert event.pop() == "event"
    assert event.segments == ["test"]


def test_event_clear():
    event = Event.from_string("test.event")
    event.clear()
    assert event.segments == []
