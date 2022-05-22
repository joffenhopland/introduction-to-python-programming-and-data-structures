import urllib.request
from Graph import Graph
import os.path
import sys

filename = input("Enter a file: ").strip()
if not os.path.isfile(filename):
    print(filename, "does not exit")
    sys.exit()
    
s = input("Enter two vertices (integer indexes): ")
v = [int(x) for x in s.split()]
v1, v2 = v[0], v[1]
    
inputFile = open(filename, "r")
# Read the number of vertices
lines = inputFile.readlines()
inputFile.close()

numberOfVertices = int(lines[0])

print("The number of vertices is", numberOfVertices)
     
vertices = []
edges = []

for line in lines[1:]:
    tokens = [int(x) for x in line.split()]
         
    startingVertex = tokens[0]
    vertices.append(startingVertex)
    for adjacentVertex in tokens[1:]:
        edges.append([startingVertex, adjacentVertex])
    
graph = Graph(vertices, edges)
graph.printEdges()
tree = graph.bfs(v1)
path = tree.getPath(v2)

print("The path is", end = ' ')
for v in path:
    print(v, end = ' ')