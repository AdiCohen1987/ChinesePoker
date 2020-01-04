import unittest


class SimpleTest(unittest.TestCase):

    def setUp(self):
        pass

    # Returns True or False.
    def test(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()