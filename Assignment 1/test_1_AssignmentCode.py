import unittest
import AssignmentCode

class TestAssignmentCode(unittest.TestCase):

    def test_Square(self):
        self.assertEqual(AssignmentCode.Square(2,2), 4)

    def test_Cylinder(self):
        self.assertEqual(AssignmentCode.Cylinder(2, 3), 37.68)

if __name__ == '__main__':
    unittest.main()
