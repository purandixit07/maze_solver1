import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_reset_visited(self):
        num_cols = 15
        num_rows = 16
        m1 = Maze(0, 0, num_rows, num_cols, 15,15)
        self.assertEqual(m1._cells[10][10].visited, False)


if __name__ == "__main__":
    unittest.main()