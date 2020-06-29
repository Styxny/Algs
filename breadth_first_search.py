#! /home/styxny/algs/bin/python
"""
An implementation of breadth first search

Author: Styxny
"""
from collections import deque

def person_is_seller(person):
    return person[-1] == 'm'

def breadth_first_search(name):
    queue = deque()
    queue += graph[name]
    searched = []
    while queue:
        person = queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller")
                return True
            else:
                queue += graph[person]
                searched.append(person)
    return False

if __name__ == '__main__':
    graph = {}
    graph["you"]= ["alice", "bob", "claire"]
    graph["bob"] = ["anju", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "johnny"]
    graph["anju"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["johnny"] = []

    breadth_first_search("you")