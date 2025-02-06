# This file is not meant to be included in the final build

import matplotlib.pyplot as plt

from camshell.interfaces import Display, Image, Size


class UIScreen(Display):
    def __init__(self):
        super().__init__()
        self.__is_initialized = False

    def initialize(self) -> None:
        self.__is_initialized = True
        plt.ion()
        self.fig, self.ax = plt.subplots()
        self.ax.axis("off")

    def get_size(self) -> Size:
        return Size(width=60, height=60)

    def render(self, image: Image) -> None:
        assert self.__is_initialized, "Display is not initialized"
        for x in range(image.size.width):
            for y in range(image.size.height):
                b, g, r = image.get_rgb(x, y)
                self.ax.plot(
                    x,
                    image.size.height - y - 1,
                    color=(r / 255, g / 255, b / 255),
                    marker=".",
                )

        plt.draw()
        plt.pause(0.1)
        self.ax.clear()
