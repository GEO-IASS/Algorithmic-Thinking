'''
Provided code for Application portion of Module 2
'''

#general imports
import urllib2
import random
import time
import math
import matplotlib.pyplot as plt

##########################################

def copy_graph(graph):
    """
    Make a copy of graph
    """
    new_graph={}
    for ndoe in graph:
        new_graph[node]=set(graph[node])
    return new_graph

def delete_node(ugraph,node):
    """
    Delete a node from an undirected graph
    """
    neighbors=ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)

def target_order(ugraph):
    """
    Compute a targeted attack order consisting of nodes of maximal degree
    Return a list of nodes
    """
    new_graph=copy_graph(ugraph)
    order=[]
    while len(new_graph)>0:
        max_degree=-1
        for node in new_graph:
            if len(new_graph[node])>max_degree:
                max_degree=len(new_graph[node])
                max_degree_node=node
        neighbors=new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)
        order.append(max_degree_node)
    return order

#code for loading computer network graph
NETWORK_URL="http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL for a text representation of the graph
    Return a dictionary that models a graph
    """
    graph_file=urllib2.urlopen(graph_url)
    graph_text=graph_file.read()
    graph_lines=graph_text.split('\n')
    graph_lines=graph_lines[:-1]

    print "Loaded graph with", len(graph_lines),"nodes"

    answer_graph={}
    for line in graph_lines:
        neighbors=line.split(' ')
        node=int(neighbors[0])
        answer_graph[node]=set([])
        for neighbor in neighbors[1:-1]
            answer_graph[node].add(int(neighbor))
    return answer_graph

def make_complete_graph(num_nodes):
    """
    Takes num_nodes as input and output complete undirected graph
    """
    if num_nodes<1:
        return {}
    graph=dict()
    for node in xrange(num_nodes):
        graph[node]=set([dummy_i for dummy_i in xrange(0,node)]+[dummy_j in xrange(node+1,num_nodes)])
    return graph

PROBABILITY=0.5
er_graph=make_complete_graph(1239)
for key in er_graph:
    candidates=list(er_graph[key])
    for candidate in candidates:
        randnum=random.uniform(0,1)
        if randnum>PROBABILITY:
            candidates.remove(candidate)
            er_graph[candidate].remove(key)
    er_graph[key]=set(candidates)

class UPATrial:
    """
    class to encapsulate optimizated trials for the UPA algorithm
    """

    def __init__(self,num_nodes):
        """

        """








