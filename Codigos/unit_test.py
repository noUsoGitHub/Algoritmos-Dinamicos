from MemorizadoRecursivo import rec as Memory
from Recursivo import rec as Recursive
from Tabulado import rec as BottomUp
import unittest

class TestSequenceFunctions(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(Recursive([1]), [1])
        self.assertEqual(Memory([1]), [1])
        self.assertEqual(BottomUp([1]), [1])
    def test_case_1(self):
        self.assertEqual(Recursive([-10, 4]), [4])
        self.assertEqual(Memory([-10, 4]), [4])
        self.assertEqual(BottomUp([-10, 4]), [4])
    def test_case_2(self):
        self.assertEqual(Recursive([8, -9, -9]), [8, -9, -9])
        self.assertEqual(Memory([8, -9, -9]), [8, -9, -9])
        self.assertEqual(BottomUp([8, -9, -9]), [8, -9, -9])
    def test_case_3(self):
        self.assertEqual(Recursive([-6, 9, -2, -10]), [9, -2, -10])
        self.assertEqual(Memory([-6, 9, -2, -10]), [9, -2, -10])
        self.assertEqual(BottomUp([-6, 9, -2, -10]), [9, -2, -10])
    def test_case_4(self):
        self.assertEqual(Recursive([-4, -8, 2, -9, 10]), [-8, 2, -9, 10])
        self.assertEqual(Memory([-4, -8, 2, -9, 10]), [-8, 2, -9, 10])
        self.assertEqual(BottomUp([-4, -8, 2, -9, 10]), [-8, 2, -9, 10])
    def test_case_5(self):       
        self.assertEqual(Recursive([2, -4, 0, -4, -9, 6]), [-4, -9, 6])
        self.assertEqual(Memory([2, -4, 0, -4, -9, 6]), [-4, -9, 6])
        self.assertEqual(BottomUp([2, -4, 0, -4, -9, 6]), [-4, -9, 6])
if __name__ == '__main__':
    unittest.main()