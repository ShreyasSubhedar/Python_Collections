from collections.abc import Sequence
class SortedFrozenSet(Sequence):
    def __init__(self, item=None):
        self._item = tuple(sorted(
           set(item) if item is not None else set()
        ))

    def __contains__(self, item):
        return item in self._item

    def __len__(self):
        return len(self._item)

    def __iter__(self):
        return iter(self._item)

    def __getitem__(self, index):
        result = self._item[index]
        return (SortedFrozenSet(result)
                if isinstance(index, slice)
                else result
                )

    def __repr__(self):
        return "{}({})".format(type(self).__name__, "[{}]".format(", ".join(map(repr, self._item))) if self._item else "")

    def __eq__(self, other):
        items = other._item if isinstance(other, type(self)) else []
        return self._item == items

    def __hash__(self):
        typ = type(self)
        items = self._item
        return hash((typ, items))
