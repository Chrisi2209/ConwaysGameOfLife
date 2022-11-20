import os as np

        self._grid = np.zeros(shape, dtype=np.bool_)


    def gen_all_cell_coors(self):
        """
        Yields all the coordinates for the squares in a tuple.
        Beginning from top left and going left to right, when the row is finished,
        it iterates the y axis.
        """
        for y in range(self._grid.shape[1]):
            for x in range(self._grid.shape[0]):
                yield (x * self._width, y * self._height, self._width, self._height)

    def gen_all_lines(self):
        pass

    def draw_grid(self, window, camera):
        camera._zoom_factor
        """
        for i in range(self._grid.shape[0] * self._grid.shape[1]):
            rect = self.gen_all_cell_coors()
            print(f"{i}/{self._grid.shape[0] * self._grid.shape[1]}")
        """

    def get_shape(self):
        return self._grid.shape

    def get_cell(self, x, y):
        return self._grid[x, y]

    def toggle_cell(self, x, y):
        self._grid[x, y] = not self._grid[x, y]

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height
