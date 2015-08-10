"""
Implement 4 functions for the project 4.
"""

##########################################
# code for Matrix functions


def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    """
    input: a set of characters and scores.
    output: return a dictionary of dictionaries.
    """
    score_matrix = dict()
    score_matrix['-'] = dict()
    for key in alphabet:
        score_matrix[key] = dict()
        for element in alphabet:
            if element == key:
                score_matrix[key][element] = diag_score
            else:
                score_matrix[key][element] = off_diag_score
        score_matrix[key]['-'] = dash_score
        score_matrix['-'][key] = dash_score
    score_matrix['-']['-'] = dash_score
    return score_matrix

def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    """
    input: two sequences seq_x and seq_y, scoring_matrix and global_flag.
    output: alignment matrix. If global_flag is true, return the global alignment
            else return the local alignment
    """
    result = [[]]
    result[0].append(0)
    if global_flag:
        xsize, ysize = len(seq_x), len(seq_y)
        for dummy_i in xrange(1, xsize + 1):
            temp = result[dummy_i - 1][0] + scoring_matrix[seq_x[dummy_i - 1]]['-']
            result.append([temp])
        for dummy_j in xrange(1, ysize + 1):
            temp = result[0][dummy_j - 1] + scoring_matrix['-'][seq_y[dummy_j - 1]]
            result[0].append(temp)
        for dummy_i in xrange(1, xsize + 1):
            for dummy_j in xrange(1, ysize + 1):
                temp1 = result[dummy_i - 1][dummy_j - 1] + scoring_matrix[seq_x[dummy_i - 1]][seq_y[dummy_j - 1]]
                temp2 = result[dummy_i - 1][dummy_j] + scoring_matrix[seq_x[dummy_i - 1]]['-']
                temp3 = result[dummy_i][dummy_j - 1] + scoring_matrix['-'][seq_y[dummy_j - 1]]
                result[dummy_i].append(max(temp1, temp2, temp3))
        return result
    else:
        xsize, ysize = len(seq_x), len(seq_y)
        for dummy_i in xrange(1,xsize + 1):
            temp = result[dummy_i - 1][0] + scoring_matrix[seq_x[dummy_i - 1]]['-']
            result.append([max(0,temp)])
        for dummy_j in xrange(1, ysize + 1):
            temp = result[0][dummy_j - 1] + scoring_matrix['-'][seq_y[dummy_j - 1]]
            result[0].append(max(0,temp))
        for dummy_i in xrange(1, xsize + 1):
            for dummy_j in xrange(1, ysize + 1):
                temp1 = result[dummy_i - 1][dummy_j - 1] + scoring_matrix[seq_x[dummy_i - 1]][seq_y[dummy_j - 1]]
                temp2 = result[dummy_i - 1][dummy_j] + scoring_matrix[seq_x[dummy_i - 1]]['-']
                temp3 = result[dummy_i][dummy_j - 1] + scoring_matrix['-'][seq_y[dummy_j - 1]]
                result[dummy_i].append(max(0, temp1, temp2, temp3))
        return result


###############################################
# code for alignment matrix


def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    input: two sequenecs seq_x and seq_y and scoring_matrix and global alignment_matrix
    output: a tuple of the score and aligned x and aligned y
    """
    xsize, ysize = len(seq_x), len(seq_y)
    xsize0, ysize0 = xsize, ysize
    align_x, align_y = '', ''
    while xsize > 0 and ysize > 0:
        if alignment_matrix[xsize][ysize] == alignment_matrix[xsize - 1][ysize - 1] + scoring_matrix[seq_x[xsize - 1]][seq_y[ysize - 1]]:
            align_x = seq_x[xsize - 1] + align_x
            align_y = seq_y[ysize - 1] + align_y
            xsize = xsize - 1
            ysize = ysize - 1
        elif alignment_matrix[xsize][ysize] == alignment_matrix[xsize - 1][ysize] + scoring_matrix[seq_x[xsize -1]]['-']:
            align_x = seq_x[xsize -1] + align_x
            align_y = '-' + align_y
            xsize = xsize - 1
        else:
            align_x = '-' + align_x
            align_y = seq_y[ysize - 1] + align_y
            ysize = ysize - 1
    while xsize > 0:
        align_x = seq_x[xsize - 1] + align_x
        align_y = '-' + align_y
        xsize = xsize - 1
    while ysize > 0:
        align_x = '-' + align_x
        align_y = seq_y[ysize - 1] + align_y
        ysize = ysize - 1
    return (alignment_matrix[xsize0][ysize0], align_x, align_y)


def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    input: two sequenecs seq_x and seq_y and scoring_matrix and local alignment_matrix
    output: a tuple of the score and aligned x and aligned y
    """
    xsize, ysize = len(seq_x), len(seq_y)
    maxl = [max(alignment_matrix[dummy_i]) for dummy_i in range(len(alignment_matrix))]
    startx = maxl.index(max(maxl))
    starty = alignment_matrix[startx].index(max(alignment_matrix[startx]))
    xsize = startx
    ysize = starty
    align_x, align_y = '', ''
    while alignment_matrix[startx][starty] != 0 and startx > 0 and starty > 0:
        if alignment_matrix[startx][starty] == alignment_matrix[startx - 1][starty - 1] + scoring_matrix[seq_x[startx - 1]][seq_y[starty - 1]]:
            align_x = seq_x[startx - 1] + align_x
            align_y = seq_y[starty - 1] + align_y
            startx = startx - 1
            starty = starty - 1
        elif alignment_matrix[startx][starty] == alignment_matrix[startx - 1][starty] + scoring_matrix[seq_x[startx - 1]]['-']:
            align_x = seq_x[startx - 1] + align_x
            align_y = '-' + align_y
            startx = startx - 1
        else:
            align_x = '-' + align_x
            align_y = seq_y[starty - 1] + align_y
            starty = starty - 1
    while alignment_matrix[startx][starty] !=0 and startx > 0:
        align_x = seq_x[startx - 1] + align_x
        align_y = '-' + align_y
        startx = startx - 1
    while alignment_matrix[startx][starty] !=0 and starty > 0:
        align_x = '-' + align_x
        align_y = seq_y[starty - 1] + align_y
        starty = starty - 1
    return (alignment_matrix[xsize][ysize], align_x, align_y)
