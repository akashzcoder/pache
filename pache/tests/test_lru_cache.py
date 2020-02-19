from pache import lru_cache


def test_dq_node():
    key = "legend"
    value = "Vegeta"
    expected_dq_node_str = f"{key} -> {value}"
    dq_node = lru_cache.DQNode(key=key, value=value)
    assert str(dq_node) == expected_dq_node_str


def test_dq_node_instance():
    key = "legend"
    value = "Vegeta"
    dq_node = lru_cache.DQNode(key=key, value=value)
    assert dq_node.key == key
    assert dq_node.value == value
    assert dq_node.next is None
    assert dq_node.prev is None
