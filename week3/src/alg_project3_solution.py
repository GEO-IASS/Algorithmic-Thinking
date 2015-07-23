"""
For Project 3 and implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane
"""

import math
import alg_cluster



######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters

    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """
    result_tuple = (float('inf'), -1, -1)
    for temp_i in xrange(len(cluster_list)):
        for temp_j in xrange(temp_i+1, len(cluster_list)):
            temp_tuple = pair_distance(cluster_list,temp_i,temp_j)
            result_tuple = min(result_tuple,temp_tuple)
    return result_tuple



def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """
    num = len(cluster_list)
    if num <= 3:
        return slow_closest_pair(cluster_list)
    else:
        half = num / 2
        sub_list1 = cluster_list[ : half]
        sub_list2 = cluster_list[half : ]
        tuple_1 = fast_closest_pair(sub_list1)
        tuple_2 = fast_closest_pair(sub_list2)
        result = min(tuple_1,(tuple_2[0],tuple_2[1] + half,tuple_2[2] + half))
        mid = (cluster_list[half - 1].horiz_center() + cluster_list[half].horiz_center()) / 2.0
        result = min(result, closest_pair_strip(cluster_list,mid,result[0]))
    return result


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip

    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.
    """
    indices = list()
    for idx, cluster in enumerate(cluster_list):
        if abs(cluster.horiz_center() - horiz_center) < half_width:
            indices.append(idx)
    indices.sort(key = lambda idx : cluster_list[idx].vert_center())
    para_k = len(indices)
    result = (float('inf'),-1, -1)
    for para_u in xrange(para_k - 1):
        for para_v in xrange(para_u + 1, min(para_u + 4, para_k)):
            idx1 = indices[para_u]
            idx2 = indices[para_v]
            temp_tuple = pair_distance(cluster_list,idx1,idx2)
            result = min(result, temp_tuple)
    return result



######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list

    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """
    result = cluster_list
    while len(result) > num_clusters:
        result.sort(key = lambda cluster : cluster.horiz_center())
        pair = fast_closest_pair(result)
        cluster_i = result[pair[1]]
        cluster_j = result[pair[2]]
        result[pair[1]]= cluster_i.merge_clusters(cluster_j)
        result.remove(cluster_j)
    return result


######################################################################
# Code for k-means clustering


def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list

    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # position initial clusters at the location of clusters with largest populations
    num = len(cluster_list)
    copy_list = [cluster_list[tmp].copy() for tmp in xrange(num)]
    copy_list.sort(key = lambda cluster:cluster.total_population())
    kcenters = copy_list[- num_clusters :]
    for dummy_ in xrange(num_iterations):
        result = [alg_cluster.Cluster(set([]),0,0,0,0) for tmp in xrange(num_clusters)]
        for tmp_j in xrange(len(cluster_list)):
            which_cluster = -1
            distance = float('inf')
            for c_idx in xrange(num_clusters):
                dist = kcenters[c_idx].distance(cluster_list[tmp_j])
                if dist < distance:
                    distance = dist
                    which_cluster =  c_idx
            result[which_cluster] = result[which_cluster].merge_clusters(cluster_list[tmp_j])
        kcenters = result

    return result

