'''
Application portion of Module 1
'''

# general imports
import math
import numpy as np
import urllib2
import matplotlib.pyplot as plt
import sys,Project1
sys.path.append("/Users/Victor_Hao/Downloads/my study/pypractice/Algorithmic")


CITATION_URL="http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    '''
    Function that loads a graph given the url for a text
    representation of the graph

    Returns a dictionary that models a graph
    '''
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
        for neighbor in neighbors[1:-1]:
            answer_graph[node].add(int(neighbor))
    return answer_graph

citation_graph=load_graph(CITATION_URL)

#to compute the out-degree of citation graph
#print sum([len(citation_graph[key]) for key in citation_graph])/(len(citation_graph))

in_degree_distribution=Project1.in_degree_distribution(citation_graph)
if 0 in in_degree_distribution:
    print "There are ",in_degree_distribution[0]," nodes with 0 citations"
    del in_degree_distribution[0]
pairs=[]
total=float(sum(in_degree_distribution.values()))
for key in in_degree_distribution:
    in_degree_distribution[key]=in_degree_distribution[key]/total
    pairs.append([key,in_degree_distribution[key]])
pairs.sort()

#plt.figure(num=1,figsize=(8,8))
#plt.loglog(*zip(*pairs))


# to compute the ER graph
PROBABILITY=0.5
er_graph=Project1.make_complete_graph(2000)
for key in er_graph:
    candidates=list(er_graph[key])
    for candidate in candidates:
        randnum=np.random.rand()
        if randnum>PROBABILITY:
            candidates.remove(candidate)
    er_graph[key]=set(candidates)
er_indegree_distribution=Project1.in_degree_distribution(er_graph)
if 0 in er_indegree_distribution.keys():
    print "There are ",er_indegree_distribution[0]," nodes with 0 citations"
    del in_degree_distribution[0]
er_pairs=[]
er_total=float(sum(er_indegree_distribution.values()))
for key in er_indegree_distribution:
    er_indegree_distribution[key]=er_indegree_distribution[key]/er_total
    er_pairs.append([key,er_indegree_distribution[key]])
er_pairs.sort()


# to draw the comparison picture of citation graph and ER graph
plt.figure()
plt.subplot(121)
plt.loglog(*zip(*pairs))
plt.title("citation graph")
plt.xlabel("in-degree")
plt.ylabel("distribution-value")
plt.subplot(122)
plt.title("ER graph")
plt.xlabel("in-degree")
plt.loglog(*zip(*er_pairs))
plt.show()

