#----------------------------------------------------------
# Lab #2: Ordered Set Class
# Implementation of a generic ordered set class and its
# corresponding operations.
#
# Date: 24-Sep-2025
# Authors:
#           A01801044 Yael Sinuhe Grajeda Martinez
#           A01800840 Tadeo Emanuel Arellano Conde
#----------------------------------------------------------

from __future__ import annotations
from typing import cast
from collections.abc import Iterable, Iterator


class _Node[N]:

    info: N | None
    next: _Node[N]
    prev: _Node[N]

    # Complexity: O(1)
    def __init__(self, value: N | None = None) -> None:
        self.info = value
        self.next = self
        self.prev = self


class OrderedSet[T]:

    __sentinel: _Node[T]
    __count: int

    # Complexity: O(N^2)
    def __init__(self, values: Iterable[T] = []) -> None:
        self.__sentinel = _Node()
        self.__count = 0
        for elem in values:
            self.add(elem)
            
    # Complexity: O(N)
    def __repr__(self) -> str:
        return f"OrderedSet({list(self) if self else ''})"
    
    # Complexity: O(N)
    def __contains__(self, value: T) -> bool:
        for elem in self:
            if elem == value:
                return True
        return False

    # Complexity: O(1)
    def __len__(self) -> int:
        return self.__count


    # Complexity: O(N)
    def add(self, value: T) -> None:
        if value in self:
            return
        self.__count += 1
        new_node: _Node[T] = _Node(value)
        new_node.prev = self.__sentinel.prev
        new_node.next = self.__sentinel
        self.__sentinel.prev.next = new_node
        self.__sentinel.prev = new_node

    # Complexity: O(N)
    def discard(self, value: T) -> None:
        current: _Node[T] = self.__sentinel.next
        while current is not self.__sentinel:
            if current.info == value:
                current.prev.next = current.next
                current.next.prev = current.prev
                self.__count -= 1
                return
            current = current.next
    
    # Complexity: O(N)
    def remove(self, value: T) -> None:
        current: _Node[T] = self.__sentinel.next
        while current is not self.__sentinel:
            if current.info == value:
                current.prev.next = current.next
                current.next.prev = current.prev
                self.__count -= 1
                return
            current = current.next
        raise KeyError("Value not contained in the set")
    
    # Complexity: O(N)
    def __iter__(self) -> Iterator[T]:
        current: _Node[T] = self.__sentinel.next
        while current is not self.__sentinel:
            yield cast(T, current.info)
            current = current.next


    # Complexity: O(N*M) where N = len(self) and M = len(other)
    def __eq__(self, other: object) -> bool:
        if self is other:
            return True
        if not isinstance(other, OrderedSet):
            return False
        if len(self) != len(other):  # type: ignore
            return False
        for elem in self:
            if elem not in other:
                return False
        return True

    # Complexity: O(N*M) where N = len(self) and M = len(other)
    def __le__(self, other: OrderedSet[T]) -> bool:
        if self is other:
            return True
        if len(self) > len(other):
            return False
        for elem in self:
            if elem not in other:
                return False
        return True

    # Complexity: O(N*M) where N = len(self) and M = len(other)
    def __lt__(self, other: OrderedSet[T]) -> bool:
        if self is other:
            return False
        if len(self) >= len(other):
            return False
        for elem in self:
            if elem not in other:
                return False
        return True
    
    # Complexity: O(N*M) where N = len(self) and M = len(other)
    def __ge__(self, other: OrderedSet[T]) -> bool:
        if other is self:
            return True
        if len(self) < len(other):
            return False
        for elem in other:
            if elem not in self:
                return False
        return True
    
    # Complexity: O(N*M) where N = len(self) and M = len(other)
    def __gt__(self, other: OrderedSet[T]) -> bool:
        if other is self:
            return False
        if len(self) <= len(other):
            return False
        for elem in other:
            if elem not in self:
                return False
        return True

    # Complexity: O(N*M) where N = elem in self and M = elem in other
    def isdisjoint(self, other: OrderedSet[T]) -> bool:
        for elem in self:
            if elem in other:
                return False
        return True
    
    # Complexity: O(N*M) where N = len(self) and M = len(other)
    def __and__(self, other: OrderedSet[T]) -> OrderedSet[T]:
        result: OrderedSet[T] = OrderedSet()
        for elem in self:
            if elem in other:
                result.add(elem)
        return result

    # Complexity: O(N+M) where N = elem in self and M = elem in other
    def __or__(self, other: OrderedSet[T]) -> OrderedSet[T]:
        result: OrderedSet[T] = OrderedSet()
        for elem in self:
            result.add(elem)
        for elem in other:
            result.add(elem)
        return result
    
    # Complexity: O(N*M) where N = elem in self and M = elem in other
    def __sub__(self, other: OrderedSet[T]) -> OrderedSet[T]:
        result: OrderedSet[T] = OrderedSet()
        for elem in self:
            if elem not in other:
                result.add(elem)
        return result
    
    # Complexity: O(N*M) where N = elem in self and M = elem in other
    def __xor__(self, other: OrderedSet[T]) -> OrderedSet[T]:
        result: OrderedSet[T] = OrderedSet()
        for elem in self:
            if elem not in other:
                result.add(elem)
        for elem in other:
            if elem not in self:
                result.add(elem)
        return result
    
    # Complexity: O(1)
    def clear(self) -> None:
        self.__sentinel.next = self.__sentinel
        self.__sentinel.prev = self.__sentinel
        self.__count = 0
        
    # Complexity: O(1)
    def pop(self) -> T:
        if self.__sentinel.next is self.__sentinel:
            raise KeyError("Set is empty")

        value = cast(T, self.__sentinel.prev.info)
        last_node = self.__sentinel.prev
        
        last_node.prev.next = self.__sentinel
        self.__sentinel.prev = last_node.prev
        self.__count -= 1
        
        return value