class Camera:
    def __init__(self, visible_cellrows_at_start):
        self.offset = [0, 0]
        self._zoom_factor = 1

        self.VISIBLE_CELLROWS_AT_START = visible_cellrows_at_start

    def zoom_in(self):
        self._zoom_factor += 0.25

    def zoom_out(self):
        self._zoom_factor -= 0.25

    def get_zoom_factor(self):
        return self._zoom_factor
