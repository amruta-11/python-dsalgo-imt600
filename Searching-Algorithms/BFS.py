directed_graph = {
  '3' : ['2','5'],
  '2' : ['8'],
  '5' : ['4'],
  '4' : ['8'],
  '8' : []
}

visited_nodes = [] # List for visited nodes.
neighbors_queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  neighbors_queue.append(node)

  while neighbors_queue:          # Creating loop to visit each node
    current_node = neighbors_queue.pop(0) 
    print (current_node, end = " ") 

    for neighbor in graph[current_node]:
      if neighbor not in visited:
        visited.append(neighbor)
        neighbors_queue.append(neighbor)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited_nodes, directed_graph, '3')    # function calling