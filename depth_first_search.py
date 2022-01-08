from typing import Set


graph ={
      'A': ['B', 'C','D'],
      'B':['E'],
      'C':['D', 'E'],
      'D':[],
      'E':[]
}

visited=set()

def depth_first_search(visited_nodes, graph, root ):
      if root not in visited_nodes: # if the root node has not been visited
            print(root) # print the root node
            visited.add(root) # add the root node to the set of visited nodes
            for neighbor in graph[root]: # for every child or neigboring node of the current root node
                  depth_first_search(visited,graph,neighbor) # perform dfs on each of the chil node

depth_first_search(visited,graph,'A')