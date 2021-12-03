from queue import PriorityQueue



class Tree:
    def __init__(self, num_vertices):
        self.v = num_vertices
        self.edge = [[-1 for i in range(num_vertices)] for j in range(num_vertices)]
        self.visited = []
    
    def add_edge(self, u, v, weight):
        self.edge[u][v] = weight
   
    def dijkstra(self, starting_node, target):
        node_cost = {v:float('inf') for v in range(self.v)}
        node_cost[starting_node] = 0
        visited = {}
        parents = {}

        pq = PriorityQueue()
        pq.put((0, starting_node))
        
        while node_cost:
            min_vertex = min(node_cost, key=node_cost.get)
            (distance, current_vertex) = pq.get()
            self.visited.append(current_vertex)
            for neighbor in range(self.v):
                if self.edge[current_vertex][neighbor] != -1:
                    distance = self.edge[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = node_cost[neighbor]
                        new_cost = node_cost[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            node_cost[neighbor] = new_cost
                            parents[neighbor] = min_vertex
            visited[min_vertex] = node_cost[min_vertex]
            node_cost.pop(min_vertex)
            if min_vertex == target:
                break
        return parents, visited
    
    
    @staticmethod
    def path(parents, starting_node, target):
            path = [target]
            while True:
                key = parents[path[0]]
                path.insert(0, key)
                if key == starting_node:
                    break
            return path
            
      



        
t = Tree(6)
t.add_edge(0, 4, 7)
t.add_edge(4, 3, 11)
t.add_edge(0, 5, 2)
t.add_edge(5, 3, 4)
t.add_edge(5, 2, 1)
t.add_edge(3, 2, 8) 
t.add_edge(0, 1, 5)
t.add_edge(1, 5, 9)
t.add_edge(1, 2, 3)
    
starting_node = 0
target = 3
    
parents, visited = t.dijkstra(starting_node, target)  
print("The shortest distance from %s to %s is: " %(starting_node, target),  visited[target])
print('The shortest path from %s to %s is: ' %(starting_node, target), t.path(parents, starting_node, target))