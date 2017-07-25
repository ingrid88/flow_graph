# Positive numbers are the source of flow, and negative numbers as sinks.
# Each source should map to the nearest sink.
# So in the output you should fill the matched sink for each source,
# as a relative position.
# (3,-1) is the relative position of the sink corresponding
# to each source point.
import itertools

input_matrix = [
  [0, 0, 0, 0, -1, -1, 0],
  [0, 1, 1, 0, -1, -1, 0],
  [0, 1, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0]
]

output_matrix = [
  [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None)],
  [(None, None), (3, -1), (3, -1), (None, None), (None, None), (None, None), (None, None)],
  [(None, None), (3, -1), (3, -1), (None, None),  (None, None),  (None, None), (None, None)],
  [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None)],
  [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None)]
]


input_matrix = [
    [-1,0,0,0,0,-1],
    [0,1,1,0,0,0],
    [0,1,1,0,0,0],
    [-1,0,0,0,0,0],
    [0,0,0,0,0,-1]
]

output_matrix = [
    [(None,None), (None,None), (None,None), (None,None), (None,None), (None,None)],
    [(None,None), (-1,-1), (4,-1), (None,None), (None,None), (None,None), (None,None)],
    [(None,None), (1,1), (4,2), (None,None), (None,None), (None,None), (None,None)],
    [(None,None), (None,None), (None,None), (None,None), (None,None), (None,None)],
    [(None,None), (None,None), (None,None), (None,None), (None,None), (None,None)]
]


input_matrix = [
    [0,0,1,0,0,0,0,0],
    [0,1,0,0,0,-1,0,0],
    [0,1,0,0,0,0,-1,0],
    [0,0,0,0,0,0,-1, 0]
]


output_matrix = [
    [(None, None),(None, None),(3,1) ,(None, None),(None, None),(None, None),(None, None),(None, None)],
    [(None, None),(5,1),(None, None),(None, None),(None, None),(None, None),(None, None),(None, None)],
    [(None, None),(5,1),(None, None),(None, None),(None, None),(None, None),(None, None),(None, None)],
    [(None, None),(None, None),(None, None),(None, None),(None, None),(None, None),(None, None), (None, None)]
]

def find(input_matrix):
    # return sources / syncs
    # v = 1 (+) source
    # v = -1 (-) sink
    sources = []
    sinks = []
    for i in range(len(input_matrix)):
        for j in range(len(input_matrix[0])):
            if input_matrix[i][j] == 1:
                sources.append([i, j])
            if input_matrix[i][j] == -1:
                sinks.append([i, j])
    return [sources, sinks]


def find_combos(sources, sinks):
    return [zip(x, sources) for x in itertools.permutations(
        sinks,
        len(sources))
    ]


def distances(combos):
    min_group = None
    min_s = 1000000
    min_b = 1000000
    for group in combos:
        summation = 0
        sums = []
        for combo in group:
            sink, source = combo
            # minimize sum (via manhattan distance)
            difference = abs(sink[1] - source[1]) + abs(sink[0] - source[0])
            sums.append(difference)
            summation += difference

        # and minimize differences between distances?
        b = sum([abs(sums[j+1]-sums[j]) for j in range(len(sums)-1)])
        if summation < min_s or (summation == min_s and b < min_b):
            min_b = b
            min_s = summation
            min_group = group
    return [min_b, min_s, min_group]


def get_output(pairs, input_matrix):
    output_matrix = [
        [(None, None)]*len(input_matrix[0]) for _ in xrange(len(input_matrix))
    ]

    for combo in pairs:
        sink, source = combo
        # minimize sum (via manhattan distance)
        difference = ((sink[1] - source[1]), (sink[0] - source[0]))
        output_matrix[source[1]][source[0]] = difference

    return output_matrix


# brute force
def paths(input_matrix):
    # find sources / sinks
    sources, sinks = find(input_matrix)
    print "sources:"
    print sources
    print "sinks:"
    print sinks
    # find pair combos
    combos = find_combos(sources, sinks)
    # find path distances and minimize the sum of the abs(differences)
    min_b, min_s, min_group = distances(combos)
    print "solution:"
    print min_group
    # format data
    output_matrix = get_output(min_group, input_matrix)
    return output_matrix


print paths(input_matrix)

