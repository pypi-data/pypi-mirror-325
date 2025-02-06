from typing import Callable, Optional

from ._cell import Cell
from .dict import serialize_dict


class DictBuilder:
    def __init__(self, key_size: int):
        if not isinstance(key_size, int):
            raise TypeError(f"expected int, got {type(key_size)}")
        if key_size <= 0:
            raise ValueError("key size should be positive")

        self.key_size = key_size
        self.items = {}
        self.ended = False

    def store(self, index, value):
        assert self.ended is False, 'Already ended'
        if type(index) == bytes:
            index = int(index.hex(), 16)

        assert type(index) == int, 'Invalid index type'
        assert not (index in self.items), f'Item {index} already exist'
        self.items[index] = value
        return self

    def store_cell(self, index, value: Cell):
        return self.store(index, value)

    def store_ref(self, index, value: Cell):
        assert self.ended is False, 'Already ended'

        cell = Cell()
        cell.store_ref(value)
        self.store_cell(index, cell)
        return self

    def end_dict(self, *, serializer: Optional[Callable] = None) -> Cell:
        assert self.ended is False, 'Already ended'
        self.ended = True
        if not self.items:
            return Cell()  # ?

        def default_serializer(src, dest):
            dest.write_cell(src)

        serializer = serializer or default_serializer

        return serialize_dict(self.items, self.key_size, serializer)

    def end_cell(self, *, serializer: Optional[Callable] = None) -> Cell:
        assert self.ended is False, 'Already ended'
        assert self.items, 'Dict is empty'
        return self.end_dict(serializer=serializer)


def begin_dict(key_size):
    return DictBuilder(key_size)
