import networkx as nx

#-------------------------------------------------------------------
#   The Words/Ladder graph of Section 1.1
#-------------------------------------------------------------------
def generate_graph(words):
    from string import ascii_lowercase as lowercase
    G = nx.Graph(name="words")
    lookup = dict((c,lowercase.index(c)) for c in lowercase)
    def edit_distance_two(word):
        s_word = ''.join(sorted(word))
        for i in range(len(s_word)):
            left, c, right = s_word[0:i], s_word[i], s_word[i+1:]
            j = lookup[c] # lowercase.index(c)
            for cc in lowercase[j+1:]:
                yield left + cc + right
    G.add_nodes_from(words)
    swords=[]
    awords=[]
    for word in sorted(words):
        awords.append(word)
        swords.append(''.join(sorted(word)))
    for word in awords:
        for cand in edit_distance_two(word):
            i = 0
            for sword in swords:
                if cand == sword:
                    G.add_edge(word, awords[i])
                i+=1
    return G

def words_graph():
    """Return the words example graph from the Stanford GraphBase"""
    import gzip
    fh=gzip.open('words_dat.txt.gz','r')
    words=set()
    for line in fh.readlines():
        line = line.decode()
        if line.startswith('*'):
            continue
        w=str(line[0:5])
        words.add(w)
    return generate_graph(words)

if __name__ == '__main__':
    from networkx import *
    G=words_graph()
    print("Loaded words_dat.txt containing 5757 five-letter English words.")
    print("Two words are connected if they differ in one letter.")
    print("Graph has %d nodes with %d edges"
          %(number_of_nodes(G),number_of_edges(G)))
    print("%d connected components" % number_connected_components(G))

    for (source,target) in [('chaos','order'),
                            ('nodes','graph'),
                            ('moron','smart'),
                            ('pound','marks')]:
        print("Shortest path between %s and %s is"%(source,target))
        try:
            sp=shortest_path(G, source, target)
            for n in sp:
                print(n)
        except nx.NetworkXNoPath:
            print("None")
