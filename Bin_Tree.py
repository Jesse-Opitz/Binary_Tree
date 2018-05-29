#!/usr/bin/env python
"""
Bin_Tree.py

Description:
    A binary tree structure.

@author: Jesse Opitz
"""

class Node:
    def __init__(self, name):
        self.name = name

class Branch:
    def __init__(self, src, trg):
        self.src = src
        self.trg = trg

class Bin_Tree:
    def __init__(self):
        self.nodes = []
        self.branches = []
    
    def add_node(self, name):
        n = Node(name)
        self.nodes.append(n)
    
    def add_branches(self, src, trg):
        b = Branch(src, trg)
        self.branches.append(b)

