from pache import lru_cache


def test_cache_item():
    key = "legend"
    value = "Vegeta"
    expected_cache_item_str = f"{key} -> {value}"
    cache_item = lru_cache.CacheItem(key=key, value=value)
    assert str(cache_item) == expected_cache_item_str


def test_cache_item_instance():
    key = "legend"
    value = "Vegeta"
    cache_item = lru_cache.CacheItem(key=key, value=value)
    assert cache_item.key == key
    assert cache_item.value == value
    assert cache_item.next is None
    assert cache_item.prev is None
