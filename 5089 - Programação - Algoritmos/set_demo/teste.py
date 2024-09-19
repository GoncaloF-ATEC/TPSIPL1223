import unittest
import main as m
import time as t


class MyTestCase(unittest.TestCase):
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 1, 9, 10]

    def test_isEmpty_noDups(self):
        self.assertGreater(len(self.lista), 0)

    def test_isEmpty_test_withDups(self):
        self.assertGreater(len(self.lista2), 0)

    def test_tsum1(self):
        self.assertEqual(m.ex2(self.lista, 12), (1,2))

    def test_noDups(self):
        self.assertEqual(m.ex1(self.lista), False)

    def test_withDups(self):
        self.assertEqual(m.ex1(self.lista2), True)


if __name__ == '__main__':
    unittest.main()
