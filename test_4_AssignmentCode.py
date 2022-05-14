import unittest
import AssignmentCode

class TestAssignmentCode(unittest.TestCase):

    def test_Sphere(self):
        container = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,113.03999999999999]
        self.assertNotIn(AssignmentCode.Sphere(3), container)

    def test_Conversion(self):
        container = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,229.29936305732483]
        self.assertNotIn(AssignmentCode.Conversion(4), container)

if __name__ == '__main__':
    unittest.main()
