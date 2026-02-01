from edb.common.ordered import OrderedSet


def test_ordered_set_replace_updates_key_and_order() -> None:
    ordered = OrderedSet(["a", "b", "c"])

    ordered.replace("b", "d")

    assert list(ordered) == ["a", "d", "c"]


def test_ordered_set_replace_deduplicates_target() -> None:
    ordered = OrderedSet(["a", "b", "c", "d"])

    ordered.replace("b", "d")

    assert list(ordered) == ["a", "d", "c"]


def test_ordered_set_replace_noop_when_same_key() -> None:
    ordered = OrderedSet(["a", "b"])

    ordered.replace("b", "b")

    assert list(ordered) == ["a", "b"]
