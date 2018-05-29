class PageRank:
    def __init__(self, sparse_matrix, d=0.85):
        self.matrix = sparse_matrix
        self.number_of_nodes = len(sparse_matrix)
        self.d = d

    def init_weights(self):
        # Nodes with zero outbound links are set to 0

        self.weights = [0 for i in range(self.number_of_nodes)]
        non_zero_nodes = 0
        for node in self.matrix:
            if node:
                non_zero_nodes += 1

        initial_weight = 1 / non_zero_nodes
        for i, node in enumerate(self.matrix):
            if node:
                self.weights[i] = initial_weight
                # print(initial_weight)

    def calculate_page_rank(self, num_of_iterations=1):
        for _ in range(num_of_iterations):
            for node in range(self.number_of_nodes):
                self.weights[node] += self.d * self._page_rank(node)



    def _page_rank(self, node):
        updated_weight = 0
        for outbound_link in self.matrix[node]:
            updated_weight += self.weights[outbound_link] / (
            len(self.matrix[outbound_link]) if len(self.matrix[outbound_link]) else 1)
        return updated_weight
