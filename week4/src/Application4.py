"""
Provide code and solution for Application 4
"""

DESKTOP = True

import math
import random
import urllib2

if DESKTOP:
    import matplotlib.pyplot as plt
    import alg_project4_solution as student
else:
    import simpleplot
    import userXX_XXXXXXX as student


# URLs for data files
PAM50_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_PAM50.txt"
HUMAN_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_HumanEyelessProtein.txt"
FRUITFLY_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_FruitflyEyelessProtein.txt"
CONSENSUS_PAX_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_ConsensusPAXDomain.txt"
WORD_LIST_URL = "http://storage.googleapis.com/codeskulptor-assets/assets_scrabble_words3.txt"



###############################################
# provided code

def read_scoring_matrix(filename):
    """
    Read a scoring matrix from the file named filename.

    Argument:
    filename -- name of file containing a scoring matrix

    Returns:
    A dictionary of dictionaries mapping X and Y characters to scores
    """
    scoring_dict = {}
    scoring_file = urllib2.urlopen(filename)
    ykeys = scoring_file.readline()
    ykeychars = ykeys.split()
    for line in scoring_file.readlines():
        vals = line.split()
        xkey = vals.pop(0)
        scoring_dict[xkey] = {}
        for ykey, val in zip(ykeychars, vals):
            scoring_dict[xkey][ykey] = int(val)
    return scoring_dict




def read_protein(filename):
    """
    Read a protein sequence from the file named filename.

    Arguments:
    filename -- name of file containing a protein sequence

    Returns:
    A string representing the protein
    """
    protein_file = urllib2.urlopen(filename)
    protein_seq = protein_file.read()
    protein_seq = protein_seq.rstrip()
    return protein_seq


def read_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    # load assets
    word_file = urllib2.urlopen(filename)

    # read in files as string
    words = word_file.read()

    # template lines and solution lines list of line string
    word_list = words.split('\n')
    print "Loaded a dictionary with", len(word_list), "words"
    return word_list


def question1():
    scoring_matrix =read_scoring_matrix(PAM50_URL)
    human = read_protein(HUMAN_EYELESS_URL)
    fly = read_protein(FRUITFLY_EYELESS_URL)
    alignment_matrix = student.compute_alignment_matrix(human, fly, scoring_matrix, False)
    print student.compute_local_alignment(human, fly, scoring_matrix, alignment_matrix)

def question2():
    scoring_matrix =read_scoring_matrix(PAM50_URL)
    human = read_protein(HUMAN_EYELESS_URL)
    fly = read_protein(FRUITFLY_EYELESS_URL)
    # for question 3
#    acids = 'ACBEDGFIHKMLNQPSRTWVYXZ'
#    hlen = len(human)
#    flen = len(fly)
#    human_random, fly_random = '', ''
#    for dummy_i in xrange(hlen):
#        human_random = human_random + human[random.randint(1,23)]
#    for dummy_i in xrange(flen):
#        fly_random = fly_random + fly[random.randint(1,23)]
#    human = human_random
#    fly = fly_random
    consensusPAX = read_protein(CONSENSUS_PAX_URL)
    alignment_matrix = student.compute_alignment_matrix(human, fly, scoring_matrix, False)
    local_result = student.compute_local_alignment(human, fly, scoring_matrix, alignment_matrix)
    local_human = ''.join(local_result[1].split('-'))
    local_fly = ''.join(local_result[2].split('-'))
    human_P = student.compute_alignment_matrix(local_human,consensusPAX,scoring_matrix, True)
    human_result = student.compute_global_alignment(local_human,consensusPAX, scoring_matrix, human_P)
    fly_P = student.compute_alignment_matrix(local_fly,consensusPAX, scoring_matrix, True)
    fly_result = student.compute_global_alignment(local_fly,consensusPAX, scoring_matrix, fly_P)
    total = len(consensusPAX)
    human_count, fly_count =0, 0
    for dummy_i in xrange(total):
        if human_result[1][dummy_i] == human_result[2][dummy_i]:
            human_count += 1
        if fly_result[1][dummy_i] ==fly_result[2][dummy_i]:
            fly_count += 1
    print human_count * 1.0 / total
    print fly_count * 1.0 / total

#question1()
#question2() ps: it will also returns the result of quesiton3


#####################
# for question 4

def generate_null_distribution(seq_x, seq_y, scoring_matrix, num_trials):
    scoring_distribution = dict()
    for num in xrange(num_trials):
        rand_y = ''.join(random.sample(seq_y, len(seq_y)))
        align = student.compute_alignment_matrix(seq_x, rand_y, scoring_matrix, False)
        result = student.compute_local_alignment(seq_x, rand_y, scoring_matrix, align)
        score = result[0]
        if score not in scoring_distribution:
            scoring_distribution[score] = 1
        else:
            scoring_distribution[score] += 1
    return scoring_distribution

def question4():
    NUM_TRIALS = 1000
    scoring_matrix = read_scoring_matrix(PAM50_URL)
    human = read_protein(HUMAN_EYELESS_URL)
    fly = read_protein(FRUITFLY_EYELESS_URL)
    consensusPAX = read_protein(CONSENSUS_PAX_URL)
    score_distribution = generate_null_distribution(human, fly, scoring_matrix, NUM_TRIALS)
    keysl = score_distribution.keys()
    mean = sum(keysl) / len(keysl)
    sigma = math.sqrt(sum([(ele - mean) ** 2 for ele in keysl]) / len(keysl))
    print mean, sigma
    pairs = []
    for key in score_distribution:
        frequency = score_distribution[key]
        pairs.append([key, frequency])
    pairs.sort()
    plt.figure()
    plt.bar(*zip(*pairs))
    plt.show()

#question4()


##########################
# for question 7
def check_spelling(checked_word, dist, word_list):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    scoring_matrix = student.build_scoring_matrix(alphabet, 2, 1, 0)
    result = list()
    for word in word_list:
        align = student.compute_alignment_matrix(checked_word, word, scoring_matrix, True)
        scores = student.compute_global_alignment(checked_word, word, scoring_matrix, align)
        if (len(checked_word) + len(word) - scores[0]) <= dist:
            result.append(word)
    return result

def question8():
    word_list = read_words(WORD_LIST_URL)
    #result1 = check_spelling('humble', 1, word_list)
    result2 = check_spelling('firefly', 2, word_list)
    #print result1
    print result2

question8()
