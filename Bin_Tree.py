#!/usr/bin/env python
"""
Bin_Tree.py

Description:
    A binary tree structure.

@author: Jesse Opitz
"""

import sys

class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

    def get_name(self):
        return self.name
    
    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_left(self, l):
        self.left = l

    def set_right(self, r):
        self.right = r

class Bin_Tree:
    def __init__(self):
        # List of all nodes
        self.nodes = []
        
        # Set root to 0
        self.root = Node(0)
    
        # Pointer for moving through tree
        self.curr_node = self.root

    def in_order_depth_traverse():
        # traverse tree in-order depth first
        # returns list of nodes in this order
        print 'depth traverse'
    
    def add_node(self, name):
        n = Node(name)
        self.nodes.append(n)

    def get_node(self, node):
        for n in self.nodes:
            if n == node:
                return node
        return None

    def get_branches(self, node):
        for n in self.nodes:
            if n == node:
                return (n.get_left, n.get_right)
        return None

    def set_node_left(self, node, left):
        l = Node(left)
        n = get_node(node)
        if n != None:
            n.set_left(l)
        else:
            print >> sys.stderr, "Unable to find node."
            sys.exit(1)

    def set_node_right(self, node, right):
        l = Node(right)
        n = get_node(node)
        if n != None:
            n.set_right(l)
        else:
            print >> sys.stderr, "Unable to find node."
            sys.exit(1)
