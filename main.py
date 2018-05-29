from utils import create_sparse_matrix
from pagerank import PageRank


def main():
    google_file = "web-Google.txt"
    simple_test = "web-Matvii.txt"
    sparse_matrix = create_sparse_matrix(simple_test)
    pr = PageRank(sparse_matrix)
    pr.init_weights()
    print("Initial weights\n", pr.weights)
    pr.calculate_page_rank(5)
    print("Weights after 5 iterations\n", pr.weights)


if __name__ == "__main__":
    main()
