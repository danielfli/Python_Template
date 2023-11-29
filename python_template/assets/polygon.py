import numpy as np


class Rectangle:
    """Rectangle class to generate a rectangle on a canvas"""

    def __init__(self, canvas, a, b, canvas_height_x, canvas_width_y):
        self.canvas = canvas
        self.a = a
        self.b = b
        self.c_x = canvas_height_x
        self.c_y = canvas_width_y
        self.poly = Polygon(
            self.canvas,
            [
                (0.5 * (self.c_x - self.a), 0.5 * (self.c_y - self.b)),
                (0.5 * (self.c_x + self.a), 0.5 * (self.c_y - self.b)),
                (0.5 * (self.c_x + self.a), 0.5 * (self.c_y + self.b)),
                (0.5 * (self.c_x - self.a), 0.5 * (self.c_y + self.b)),
            ],
            self.c_x,
            self.c_y,
        )

    def _from_tupel_to_list(self, tuple):
        list = []
        for i in tuple:
            for item in i:
                list.append(round(item, 4))
        return list

    def _from_list_to_tuple(self, list):
        _tuple = []
        for i in range(0, len(list), 2):
            _tuple.append((list[i], list[i + 1]))
        return _tuple

    def generate_rectangle(self, color="black", outline=""):
        return self.poly.generate_polygon(color=color, outline=outline)

    def rotate(self, angle):
        """Rotates the rectangle by angle on point 1

        Args:
            angle (_type_): Degree of rotation

        Returns:
            _type_: a list of the four point of the rectangle
        """
        self.poly.rotate(angle)
        return self._from_tupel_to_list(self.poly.get_vertices())

    def update(self,coords_list):
        self.poly.vertices = self._from_list_to_tuple(coords_list)


class Polygon:
    """Classes to generate polygons on a canvas
    Template for this https://gist.github.com/the-lost-explorer/52663794ec852c4e1cc4a84ae5f8bd69

    Returns:
        _type_: _description_
    """

    def __init__(self, canvas, vertices, canvas_height_x, canvas_width_y):
        self.vertices = vertices
        self.canvas = canvas
        self.c_x = canvas_height_x
        self.c_y = canvas_width_y

    def generate_polygon(self, color="black", outline=""):
        return self.canvas.create_polygon(
            self.vertices, outline=outline, fill=color
        )

    def get_vertices(self):
        return self.vertices

    # def rotate(self, angle, xr, yr):
    def rotate(self, angle):
        # print(xr, yr)
        theta = angle * np.pi / 180
        xr = self.vertices[0][0]
        yr = self.vertices[0][1]
        rotation = np.asarray(
            [
                [
                    np.cos(theta),
                    -np.sin(theta),
                    xr * (1 - np.cos(theta)) + yr * np.sin(theta),
                ],
                [
                    np.sin(theta),
                    np.cos(theta),
                    yr * (1 - np.cos(theta)) - xr * np.sin(theta),
                ],
                [0, 0, 1],
            ]
        )

        lst = []
        for stuff in self.vertices:
            lst.append([stuff[0], stuff[1], 1])
        # print(self.vertices)
        m_vertices = np.transpose(np.asarray(lst))

        output_matrix = np.transpose(rotation.dot(m_vertices))

        lst = []
        for stuff in output_matrix:
            lst.append((stuff[0], stuff[1]))

        self.vertices = lst
        return lst

    # ToDo[f] not checked
    # def scale(self, sx, sy, xr, yr):
    #     xr = self.vertices[0][0]
    #     yr = self.vertices[0][1]

    #     scale = np.asarray(
    #         [[sx, 0, xr * (1 - sx)], [0, sy, yr * (1 - sy)], [0, 0, 1]]
    #     )

    #     lst = []
    #     for stuff in self.vertices:
    #         lst.append([stuff[0], stuff[1], 1])
    #     print(self.vertices)
    #     m_vertices = np.transpose(np.asarray(lst))

    #     output_matrix = np.transpose(scale.dot(m_vertices))

    #     lst = []
    #     for stuff in output_matrix:
    #         lst.append((stuff[0], stuff[1]))

    #     self.vertices = lst
    #     print(self.vertices)
    #     self.generate_polygon()
