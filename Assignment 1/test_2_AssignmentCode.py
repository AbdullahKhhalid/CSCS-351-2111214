import unittest
import AssignmentCode

class TestAssignmentCode(unittest.TestCase):

    def test_Sphere(self):
        self.assertNotEqual(AssignmentCode.Sphere(2), 33.49333333333333)

    def test_Conversion(self):
        self.assertNotEqual(AssignmentCode.Conversion(2), 114.64968152866241)

if __name__ == '__main__':
    unittest.main()
