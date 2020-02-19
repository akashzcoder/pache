from __future__ import print_function

"""
QNode -> holds key and value; as well as pointers to previous and next nodes.
"""


class CacheItem(object):
    def __init__(self, key: object, value: object):
        """
        Initialize the Dequeue Node.

        :param key:
        :param value:
        """
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return f"{self.key} -> {self.value}"
