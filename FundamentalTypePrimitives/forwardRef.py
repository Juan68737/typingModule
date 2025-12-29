from __future__ import annotations
from typing import ForwardRef

class Node:
    def __init__(self, node: Node | None, next: Node | None):
        self.node = node
        self.next = next

n = Node(None,None)
n2 = Node(n,None)

