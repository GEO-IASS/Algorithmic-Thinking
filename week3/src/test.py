
import alg_project3_solution
import alg_cluster

def test_cps():
    cluster_list = [alg_cluster.Cluster(set([]),1.0,1.0,1,0),alg_cluster.Cluster(set([]),1.0,5.0,1,0),alg_cluster.Cluster(set([]),1.0,4.0,1,0),alg_cluster.Cluster(set([]),1.0,7.0,1,0)]
    horiz_center = 1.0
    half_width = 3.0
    print alg_project3_solution.closest_pair_strip(cluster_list,horiz_center,half_width)


def test_fcp():
    cluster_list = [alg_cluster.Cluster(set([]),0.32,0.16,1,0),alg_cluster.Cluster(set([]),0.39,0.4,1,0),alg_cluster.Cluster(set([]),0.54,0.8,1,0),alg_cluster.Cluster(set([]),0.61,0.8,1,0),alg_cluster.Cluster(set([]),0.76,0.94,1,0)]
    print alg_project3_solution.fast_closest_pair(cluster_list)

test_fcp()
