from OpenGL.GL import *
class Mesh3D:
    def __init__(self):
        self.vertices = [(0.5,-0.5,0.5),
                        (-0.5,-0.5,0.5),
                        (0.5,0.5,0.5),
                        (-0.5,0.5,0.5),
                        (0.5,0.5,-0.5),
                        (-0.5,0.5,-0.5),]
        self.triangles = [0,2,3,0,3,1]
    def draw(self):
        for t in range(0, len(self.triangles),3):
            glBegin(GL_LINE_LOOP)
            glVertex3fv(self.vertices[self.triangles[t]])
            glVertex3fv(self.vertices[self.triangles[t+1]])
            glVertex3fv(self.vertices[self.triangles[t+2]])
            glEnd()

class Cube:
    def __init__(self):
        self.vertices = [(0.5, -0.5, 0.5),
                        (-0.5, -0.5, 0.5), (0.5, 0.5, 0.5),
                        (-0.5, 0.5, 0.5),(0.5, 0.5, -0.5),
                        (-0.5, 0.5, -0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5),
                        (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5), (0.5, 0.5, -0.5),
                        (-0.5, 0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5),
                        (-0.5, -0.5, 0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5),
                        (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5),
                        (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5),
                        (0.5, -0.5, 0.5)]
        #who types out all this, this is a joke
        self.triangles = [0, 2, 3, 0, 3, 1, 8, 4, 5, 8, 5, 9, 10, 6,7, 10,
                        7, 11, 12, 13, 14, 12, 14, 15, 16, 17, 18, 16,
                        18, 19, 20, 21, 22, 20, 22, 23]

    def draw(self):
        for t in range(0, len(self.triangles), 3):
            glBegin(GL_LINE_LOOP)
            glVertex3fv(self.vertices[self.triangles[t]])
            glVertex3fv(self.vertices[self.triangles[t + 1]])
            glVertex3fv(self.vertices[self.triangles[t + 2]])
            glEnd()