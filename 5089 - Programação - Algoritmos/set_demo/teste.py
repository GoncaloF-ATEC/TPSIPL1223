import unittest
import main as m


class MyTestCase(unittest.TestCase):
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 1, 9, 10]

    def test_noDups(self):
        self.assertEqual(m.ex1(self.lista), False)

    def test_withDups(self):
        self.assertEqual(m.ex1(self.lista2), True)


if __name__ == '__main__':
    unittest.main()
