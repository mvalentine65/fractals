import unittest
from cbrot import cbrot
from get_iter import get_iter

class TestCbrot(unittest.TestCase):

    def test_0_0_200_iterations(self):
        c = complex(0,0)
        python = get_iter(c, max_steps=200)
        ctype = cbrot(0.0,0.0,200)
        self.assertEqual(python,ctype)

    def test_x_y_values_200_iterations(self):
        x_list = [x * 0.05 for x in range(-40,40)]
        y_list = [y * 0.05 for y in range(-40,40)]
        for x in x_list:
            for y in y_list:
                with self.subTest(x=x,y=y):
                    c = complex(x,y)
                    python = get_iter(c, max_steps=200)
                    ctype = cbrot(x, y, 200)
                    self.assertEqual(python, ctype)


if __name__ == '__main__':
    unittest.main()
