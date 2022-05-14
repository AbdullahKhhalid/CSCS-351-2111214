import unittest
import AssignmentCode

class TestAssignmentCode(unittest.TestCase):

    def test_Square(self):
        self.assertEqual(AssignmentCode.Square(2,2), 4)
        self.assertEqual(AssignmentCode.Square(2,4), 8)
        self.assertIsNot(AssignmentCode.Square(6,0), 0)

    def test_Cylinder(self):
        self.assertEqual(AssignmentCode.Cylinder(2, 3), 37.68)
        self.assertEqual(AssignmentCode.Cylinder(4, 6), 28)
        self.assertIsNot(AssignmentCode.Cylinder(10, 5), 50)

    def test_Sphere(self):
        self.assertNotEqual(AssignmentCode.Sphere(2), 33.49333333333333)
        container = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,113.03999999999999]
        self.assertNotIn(AssignmentCode.Sphere(3), container)

    def test_Conversion(self):
        self.assertNotEqual(AssignmentCode.Conversion(2), 114.64968152866241)
        container = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,229.29936305732483]
        self.assertNotIn(AssignmentCode.Conversion(4), container)

if __name__ == '__main__':
    unittest.main()
