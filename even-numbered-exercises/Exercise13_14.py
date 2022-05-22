from tkinter import * # Import tkinter
import urllib.request

def displayGraph(canvas, vertices, edges):
    radius = 3
    for vertex, x, y in vertices:
        canvas.create_text(x - 2 * radius, y - 2 * radius, text = str(vertex), tags = "graph")
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill = "black", tags = "graph")

    for v1, v2 in edges:
        canvas.create_line(vertices[v1][1], vertices[v1][2], vertices[v2][1], vertices[v2][2], tags = "graph")
        
def main():
    # Prompt the user to enter a filename
    url = input("Enter an URL for the graph file: ").strip()    
    input = urllib.request.urlopen(url)

    numberOfVertices = int(input.readline().decode()) # Read the first line from the file
    print(numberOfVertices)

    vertices = []
    edges = []
    for i in range(numberOfVertices):
        items = input.readline().strip().split() # Read the info for one vertex
        vertices.append([float(items[0]), float(items[1]), float(items[2])])
        for j in range(3, len(items)):
            edges.append([float(items[0]), float(items[j])])            
    
    print(vertices)
    print(edges)
    
    input.close()  # Close the input file

    window = Tk() # Create a window
    window.title("Display a Graph") # Set title
    
    frame1 = Frame(window) # Hold four labels for displaying cards
    frame1.pack()
    canvas = Canvas(frame1, width = 300, height = 200)
    canvas.pack()
    
    displayGraph(canvas, vertices, edges)
    
    window.mainloop() # Create an event loop

main()
