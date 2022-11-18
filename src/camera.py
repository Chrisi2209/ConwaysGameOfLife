class Camera:
    def __init__(self):
        self.offset = [0, 0]
        self._zoom_factor = 1

    def zoom_in(self):
        self._zoom_factor += 0.25

    def zoom_out(self):
        self._zoom_factor -= 0.25

    def get_zoom_factor(self):
        return self._zoom_factor
