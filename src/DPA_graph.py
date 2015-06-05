"""
Implement the DAP algorithm and compute the in-degree distribution
"""

# Helper class for implementing efficient version of DPA algorithm

#general imports
import random
import matplotlib.pyplot as plt
import sys,Project1
sys.path.append("/Users/Victor_Hao/Downloads/my study/pypractice/Algorithmic/")



class DPATrial:
    """
    class to encapsulate optimized trials for DPA algoritm
    Maintains a list of node numbers with multiple instacens of each number in the same
    proportion as the desired probabilities

    Uses random.choice() to select a node number from this list for each trial.
    """
    def __init__(self,num_nodes):
        """
        Initialize a DPATrial object corresponding to a complete graph with num_nodes nodes

        Note the initial list of node numbers has num_nodes copies of each node number
        """
        self._num_nodes=num_nodes
        self._node_numbers=[node for node in range(num_nodes) for dummy_idx in range(num_nodes)]

    def run_trial(self,num_nodes):
        """
        Conduct num_node trials using by applying random.choice() to the list of node numbers

        Updates the list of node numbers so that number of instances of each node number is in
        the same ratio as the desired probabilities

        return set of nodes
        """
        #compute the neighbors for the newly-created node
        new_node_neighbors=set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))

        #update the list of node numbers so that each node number appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))

        #update the number of nodes
        self._num_nodes+=1
        return new_node_neighbors

def DPA_graph(n_num,m_num):
    """
    Implement the DPA graph return it

    Use DPATrial's method to add edges to the initialized graph with m nodes
    """
    #Initialize a complete graph with m nodes
    initial_graph=Project1.make_complete_graph(m_num)

    #iterate to add edges to the initial graph
    dpa_trial=DPATrial(m_num)
    for node_num in xrange(m_num,n_num):
        initial_graph[node_num]=dpa_trial.run_trial(node_num)
    return initial_graph

def draw():
    """
    Draw the in-degree distribution
    """
    #number of the nodes NUM_NODES and initial number of nodes M_NODES
    NUM_NODES=27770
    M_NODES=12

    #compute the in-degree distribution
    dpa_graph=DPA_graph(NUM_NODES,M_NODES)
    indegree_distribution=Project1.in_degree_distribution(dpa_graph)

    #delete the nodes with 0 in-degree since we need log(0) is infinity
    if 0 in indegree_distribution:
        del indegree_distribution[0]

    # normalize the distribution and use draw pairs of key:distribution_value
    # note that the pairs are not in order, so we need to sort it. Or we can just
    # draw the scatter plot
    pairs=[]
    total=float(sum(indegree_distribution.values()))
    for key in indegree_distribution:
        indegree_distribution[key]=indegree_distribution[key]/total
        pairs.append([key,indegree_distribution[key]])

    plt.figure(num=1,figsize=(8,8))
    plt.scatter([pairs[i][0] for i in xrange(len(pairs))],[pairs[j][1] for j in xrange(len(pairs))])
    plt.show()
    # draw the pairs
    plt.figure(num=2,figsize=(8,8))

    pairs.sort()
    plt.loglog(*(zip(*pairs)))
    plt.title("in-degree distribution of graph by DPA algorithm")
    plt.xlabel("in-degree number")
    plt.ylabel("distribution value")
    plt.show()

if __name__=="__main__":
    draw()




