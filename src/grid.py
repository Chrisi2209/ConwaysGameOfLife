import numpy as np

class Grid:
    def __init__(self, width, height, shape):
        self._width = width
        self._height = height
        self._grid = np.zeros(shape, dtype=np.bool_)


    def gen_all_cells(self):
        """
        Yields all the coordinates for the squares in a tuple.
        Beginning from top left and going left to right, when the row is finished,
        it iterates the y axis.
        """
        for y in range(self._grid.shape[1]):
            for x in range(self._grid.shape[0]):
                yield (x * self._width, y * self._height, self._width, self._height)

    def get_shape(self):
        return self._grid.shape

    def get_cell(self, x, y):
        return self._grid[x, y]

    def toggle_cell(self, x, y):
        self._grid[x, y] = not self._grid[x, y]

    def get_density(self):
        return self._density

    def get_size(self):
        return self._density
