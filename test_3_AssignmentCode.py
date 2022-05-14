import unittest
import AssignmentCode

class TestAssignmentCode(unittest.TestCase):

    def test_Square(self):
        self.assertEqual(AssignmentCode.Square(2,4), 8)

    def test_Cylinder(self):
        self.assertEqual(AssignmentCode.Cylinder(4, 6), 28)

if __name__ == '__main__':
    unittest.main()
