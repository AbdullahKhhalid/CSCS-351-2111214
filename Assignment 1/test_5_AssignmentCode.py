import unittest
import AssignmentCode

class TestAssignmentCode(unittest.TestCase):

    def test_Square(self):
        self.assertIsNot(AssignmentCode.Square(6,0), 0)

    def test_Cylinder(self):
        self.assertIsNot(AssignmentCode.Cylinder(10, 5), 50)

if __name__ == '__main__':
    unittest.main()
