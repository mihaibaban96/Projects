import unittest
import script


class TestMain(unittest.TestCase):

    def setUp(self):
        print("About to test a function!")

    def test_do_stuff(self):
        '''
        Check if test param = 15
        '''
        test_param = 10
        result = script.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        '''
        Check for a value error if test param is string
        '''
        test_param = 'shkssd'
        result = script.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        '''
        Test what happens if test param is None
        '''
        test_param = None
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def test_do_stuff4(self):
        '''
        Check when input is empty string
        '''
        test_param = ''
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def tearDown(self):
        print("Cleaning up!")


if __name__ == '__main__':
    unittest.main()
