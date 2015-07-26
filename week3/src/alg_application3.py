"""
Implement functions in the application
"""
import alg_cluster
import alg_project3_solution
import random
import time
import urllib2
import matplotlib.pyplot as plt
import numpy as np


###################################################
# Code to load data tables

# URLs for cancer risk data tables of various sizes
# Numbers indicate number of counties in data table

DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
DATA_3108_URL = DIRECTORY + "data_clustering/unifiedCancerData_3108.csv"
DATA_896_URL = DIRECTORY + "data_clustering/unifiedCancerData_896.csv"
DATA_290_URL = DIRECTORY + "data_clustering/unifiedCancerData_290.csv"
DATA_111_URL = DIRECTORY + "data_clustering/unifiedCancerData_111.csv"


def load_data_table(data_url):
    """
    Import a table of county-based cancer risk data
    from a csv format file
    """
    data_file = urllib2.urlopen(data_url)
    data = data_file.read()
    data_lines = data.split('\n')
    print "Loaded", len(data_lines), "data points"
    data_tokens = [line.split(',') for line in data_lines]
    return [[tokens[0], float(tokens[1]), float(tokens[2]), int(tokens[3]), float(tokens[4])]
            for tokens in data_tokens]


#####################################################################
# Code to computer the error of each cluster_list
#

def compute_distortion(cluster_list,data_table):
    error_list = list()
    num = len(cluster_list)
    for tmp in xrange(num):
        error_list.append(cluster_list[tmp].cluster_error(data_table))
    return sum(error_list)



def gen_random_clusters(num_clusters):
    cluster_list = list()
    for tmp_i in xrange(num_clusters):
        xcor = random.uniform(-1,1)
        ycor = random.uniform(-1,1)
        cluster_list.append(alg_cluster.Cluster(set([tmp_i]),xcor,ycor,0,0))
    return cluster_list

def test_scp(size1, size2):
    time_list = list()
    for tmp in xrange(size1,size2 + 1):
        cluster_list = gen_random_clusters(tmp)
        time1 = time.time()
        result = alg_project3_solution.slow_closest_pair(cluster_list)
        time2 = time.time()
        time_list.append(time2 - time1)
    return time_list

def test_fcp(size1,size2):
    time_list = list()
    for tmp in xrange(size1,size2 + 1):
        cluster_list = gen_random_clusters(tmp)
        time1 = time.time()
        result = alg_project3_solution.fast_closest_pair(cluster_list)
        time2 = time.time()
        time_list.append(time2 - time1)
    return time_list

def result_plot():
    xaxis = np.linspace(2,200,199)
    time_1 = test_scp(2,200)
    time_2 = test_fcp(2,200)
    plt.figure(num = 1, figsize = (8,8))
    plt.title('Comparison of scp and fcp',size = 14)
    plt.xlabel('size of cluster_list', size = 14)
    plt.ylabel('computing time', size = 14)
    plt.plot(xaxis, time_1, color = 'b', linestyle = '--', label = 'slow data')
    plt.plot(xaxis, time_2, color = 'r', linestyle = '-', label = 'fast data')
    plt.xlim(2,200)
    plt.legend(loc = 'upper left', prop = {'size': 14})
    plt.show()


def comp_plot():
    data_table = load_data_table(DATA_896_URL)
    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster(set([line[0]]),line[1], line[2], line[3], line[4]))
    hie_err,kmean_err = [], []
    singleton_cp = []
    # calculate the error list of hierarchical_clustering
    for tmp in xrange(len(singleton_list)):
        singleton_cp.append(singleton_list[tmp].copy())
    cluster_list = singleton_cp
    num_cl = 20
    while num_cl >= 6:
        cluster_list = alg_project3_solution.hierarchical_clustering(cluster_list, num_cl)
        hie_err.append(compute_distortion(cluster_list,data_table))
        num_cl = num_cl - 1
    hie_err.reverse()



    # calculate the error list of k-means
    for num_cl in range(6,21):
        cluster_list = alg_project3_solution.kmeans_clustering(singleton_list, num_cl, 5)
        kmean_err.append(compute_distortion(cluster_list,data_table))

    # compare the error list
    xaxis = np.linspace(6, 20, 15)
    plt.figure(num =1 , figsize=(8, 8))
    plt.title("Data 896", size = 14)
    plt.xlabel("number of clusters", size = 14)
    plt.ylabel("distortion", size = 14)
    plt.plot(xaxis, hie_err, color = 'b', linestyle = '--', label = 'hierarchical_clustering')
    plt.plot(xaxis, kmean_err, color = 'r', linestyle = '-', label = 'kmeans_clsutering')
    plt.legend(loc = 'upper right', prop ={'size': 10})
    plt.xlim(5,21)
    plt.show()



#result_plot()
comp_plot()
