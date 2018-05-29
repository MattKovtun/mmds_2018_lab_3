def find_max_node_id():
    max_node_id = -1
    google_input_file = open("web-Google.txt")
    google_input_file.readline()
    google_input_file.readline()
    description_line = google_input_file.readline().split()
    google_input_file.readline()

    for line in google_input_file:
        link = list(map(int, line.split()))
        a, b = link
        max_node_id = max(a, b, max_node_id)

    return max_node_id



def create_sparse_matrix(file):
    max_node_id = 17 #916500 # number from previous analysis of data
    google_input_file = open(file)
    google_input_file.readline()
    google_input_file.readline()
    description_line = google_input_file.readline().split()
    google_input_file.readline()
    nodes = int(description_line[2])
    edges = int(description_line[4])
    # print(nodes, edges)

    graph = [[] for i in range(max_node_id)]


    for i in range(min(edges, 100)):
        line = google_input_file.readline()
        link = list(map(int, line.split()))
        a, b = link

        graph[a].append(b)
        # graph[b].append(a)

    # import sys
    # print(sys.getsizeof(graph))
    return graph

if __name__ == "__main__":
    print(find_max_node_id())  # 916427
