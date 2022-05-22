from tkinter import *

RADIUS = 20


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Is point (x, y) close to this point
    def is_near(self, x, y):
        return distance(self.x, self.y, x, y) < RADIUS


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Triangle angles")  # Set title

        self.canvas = Canvas(window, width=400, height=200)
        self.canvas.pack(padx=10, pady=10)

        self.p1 = Point(20, 20)
        self.p2 = Point(120, 50)

        self.draw_line()

        self.canvas.bind("<B1-Motion>", self.mouse_moved)

        window.mainloop()  # Create an event loop

    def mouse_moved(self, event):
        if self.close_to_a_point(event.x, event.y):
            self.canvas["cursor"] = "plus"
        else:
            self.canvas["cursor"] = "arrow"

        if self.p1.is_near(event.x, event.y):
            self.p1.x = event.x
            self.p1.y = event.y
            self.draw_line()
        elif self.p2.is_near(event.x, event.y):
            self.p2.x = event.x
            self.p2.y = event.y
            self.draw_line()

    def close_to_a_point(self, x, y):
        return self.p1.is_near(x, y) or self.p2.is_near(x, y)

    def draw_line(self):
        self.dist = distance(self.p1.x, self.p1.y, self.p2.x, self.p2.y)
        if self.dist >= 70:
            self.canvas.delete("line")
            self.canvas.create_line(
                self.p1.x, self.p1.y, self.p2.x, self.p2.y, tags="line"
            )

            self.canvas.delete("circle")
            self.draw_circle(
                self.p1.x, self.p1.y, RADIUS, self.canvas, fill="red", tags="circle"
            )
            self.draw_circle(
                self.p2.x, self.p2.y, RADIUS, self.canvas, fill="red", tags="circle"
            )

            self.canvas.create_text(
                (self.p1.x + self.p2.x) / 2,
                (self.p1.y + self.p2.y) / 2,
                text=str(int(self.dist)),
                tags="line",
            )

    def draw_circle(self, x, y, r, canvas_name, **kwargs):  # center coordinates, RADIUS
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        canvas_name.create_oval(x0, y0, x1, y1, kwargs)


MainGUI()
