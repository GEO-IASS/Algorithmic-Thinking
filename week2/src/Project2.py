'''
Algorithms for project2
'''
#Project2.py is for the Project 2
#Realize BFS,Connected Components and Graph resilience
#Author: Weituo Hao JUN 28th 2015

#General import
from collections import deque

def bfs_visited(ugraph,start_node):
    '''
    realize the breadth-first search return a set of nodes visited
    '''
    queue=deque([])
    visited=set()
    visited.add(start_node)
    queue.append(start_node)
    while queue:
        current_node=queue.popleft()
        if current_node in ugraph:
            for item in ugraph[current_node]:
                if item not in visited:
                    visited.add(item)
                    queue.append(item)
    return visited

def cc_visited(ugraph):
    '''
    takes the undirected graph and returns a list of sets of visited nodes
    '''
    remaining_nodes=set(ugraph.keys())
    con_comp=list()
    while remaining_nodes:
        current_node=remaining_nodes.pop()
        current_comp=bfs_visited(ugraph,current_node)
        con_comp.append(current_comp)
        remaining_nodes.difference_update(current_comp)
    return con_comp

def largest_cc_size(ugraph):
    '''
    takes the undirected graph and returns the largest connected components
    '''
    con_comp=cc_visited(ugraph)
    if con_comp:
        return len(max(con_comp,key=len))
    else:
        return 0

def compute_resilience(ugraph,attack_order):
    '''
    # takes the undirected graph and attacked nodes, and return the largest size of the connected components
    '''
    resilience=list()
    resilience.append(largest_cc_size(ugraph))
    for node in attack_order:
        ugraph.pop(node)
        for key in ugraph:
            ugraph[key].discard(node)
        resilience.append(largest_cc_size(ugraph))
    return resilience


