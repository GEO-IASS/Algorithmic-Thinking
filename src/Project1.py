# Project1.py is for the Project 1
# Construct graphs by dictionaries, make complete graph, compute in-degree distribution
# Author: Weituo Hao  May 31 2015
#====================================================================================

# To construct graph by dictionaries
EX_GRAPH0={0:set([1,2]),\
           1:set([]),\
           2:set([])
           }

EX_GRAPH1={0:set([1,4,5]),\
           1:set([2,6]),\
           2:set([3]),\
           3:set([0]),\
           4:set([1]),\
           5:set([2]),\
           6:set([])
           }

EX_GRAPH2={0:set([1,4,5]),\
          1:set([2,6]),\
          2:set([3,7]),\
          3:set([7]),\
          4:set([1]),\
          5:set([2]),\
          6:set([]),\
          7:set([3]),\
          8:set([1,2]),\
          9:set([0,3,4,5,6,7])
          }



def make_complete_graph(num_nodes):
# Given the number of nodes, construct the complete graph
    if num_nodes<1:
        return {}
    graph=dict()
    for node in xrange(num_nodes):
        graph[node]=set([dummy_i for dummy_i in xrange(0,node)]+[dummy_j for dummy_j in xrange(node+1,num_nodes)])
    return graph


def compute_in_degrees(digraph):
    in_degree=dict()
    for key in digraph:
        for tail in digraph[key]:
            if tail not in in_degree:
                in_degree[tail]=1
            else:
                in_degree[tail]+=1
    for key in digraph:
        if key not in in_degree:
            in_degree[key]=0
    return in_degree

def in_degree_distribution(digraph):
    in_degree=compute_in_degrees(digraph)
    degree_distribution=dict()
    for key in in_degree:
        distribution_key=in_degree[key]
        if distribution_key not in degree_distribution:
            degree_distribution[distribution_key]=1
        else:
            degree_distribution[distribution_key]+=1
    return degree_distribution



if __name__=='__main__':
   print make_complete_graph(4)
   print make_complete_graph(0)
   print compute_in_degrees(EX_GRAPH0)
   print compute_in_degrees(EX_GRAPH1)
   print compute_in_degrees(GRAPH4)
   print compute_in_degrees(EX_GRAPH2)
   print in_degree_distribution(EX_GRAPH0)
   print in_degree_distribution(EX_GRAPH1)
   print in_degree_distribution(EX_GRAPH2)
   print in_degree_distribution(GRAPH4)
