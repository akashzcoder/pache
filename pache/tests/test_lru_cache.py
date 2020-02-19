from pache import lru_cache


def test_dq_node():
    key = "legend"
    value = "Vegeta"
    expected_dq_node_str = f"{key} -> {value}"
    dq_node = lru_cache.DQNode(key=key, value=value)
    assert str(dq_node) == expected_dq_node_str
