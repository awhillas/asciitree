import argparse
import sys

import pyconll
from loguru import logger

# See: https://github.com/Delgan/loguru
logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")

class Point:
    x: int
    y: int
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Canvas:
    """
    Cartesian plain that expands as needed and knows how to draw lines.
    Positive numbers only.
    2D array (list of lists).
    Bottom left is (0,0)
    """
    def __init__(self) -> None:
        self.width = 1
        self.height = 1
        self.canvas = [[' ']]

    def hline(self, char: str, start: Point, length: int):
        """
        Draw a vertical line right of a start point

        >>> c = Canvas(); c.hline('-', Point(2, 0), 5); c.render()
        '  -----\\n'
        """
        assert length > 0, f"Length should be positive, given: '{length}'"

        for x in range(length):
            self.put(char, Point(x + start.x, start.y))

    def _expand(self, p: Point):
        """
        Expand canvas to encapsulate the point, if required

        >>> c = Canvas(); c._expand(Point(2,3)); f"{c.width} {len(c.canvas[0])} {c.height} {len(c.canvas)}"
        '3 3 4 4'
        """
        # + 1 here coz x is zero indexed and width is not
        if self.width < p.x + 1:
            delta = p.x - self.width + 1
            for y in range(len(self.canvas)):
                self.canvas[y] += [' '] * delta
            self.width += delta

        if self.height < p.y + 1:
            delta = p.y - self.height + 1
            self.canvas = ([[' '] * self.width] * delta) + self.canvas
            self.height += delta

    def render(self):
        """ Render the canvas as a string """
        return '\n'.join([''.join(row) for row in self.canvas]) + '\n'

    def put(self, char: str, p: Point):
        """ Put a char at a point

        >>> c = Canvas(); c.put('x', Point(3,1)); c.render()
        '   x\\n    \\n'
        """
        self._expand(p)
        self.canvas[self.height - p.y - 1][p.x] = char[0]

def main(file):
    logger.debug("Reading file {}!", file)

    data = pyconll.load_from_file(file)

    for sentence in data:
        logger.info("Word count {}", len(sentence))

        total_chars = sum([len(token.form) for token in sentence])
        logger.info("Total chars: {}", total_chars)

        for token in sentence:
            slots = sum([1 for t in sentence if t.head == token.id])
            print(token, slots)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="CoNULL file to parse")
    args = parser.parse_args()

    main(**vars(args))

