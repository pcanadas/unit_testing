# Import the 'unittest' module to create unit tests for your code.
import unittest

# Import the 'square', 'double' and 'add' functions from the 'operations' module.
from operations import square, double, add

# Define a test case class for testing the 'square' function.
# A test case is a single unit of testing. It checks a specific aspect of the code's behavior.
class TestSquare(unittest.TestCase): 

    # Define the first test method for the 'square' function.
    # Test methods should start with the word 'test' so that the test runner recognizes them as test cases.
    def test1(self): 
        
        self.assertEqual(square(2), 4) # test when 2 is given as input the output is 4.
        
        self.assertEqual(square(3.0), 9.0)  # test when 3.0 is given as input the output is 9.0.

        self.assertNotEqual(square(-3), -9)  # test when -3 is given as input the output is not -9.

# Define a test case class for testing the 'double' function.
class TestDouble(unittest.TestCase): 

    # Define the first test method for the 'double' function.
    def test1(self): 
        
        self.assertEqual(double(2), 4) # test when 2 is given as input the output is 4.

        self.assertEqual(double(-3.1), -6.2) # test when -3.1 is given as input the output is -6.2.

        self.assertEqual(double(0), 0) # test when 0 is given as input the output is 0.

# Define a test case class for testing the 'add' function.
class TestAdd(unittest.TestCase): 

    # Define the first test method for the 'add' function.
    def test1(self): 
        
        self.assertEqual(add(2, 4), 6) # test when 2 and 4 is given as input the output is 6.

        self.assertEqual(add(0, 0), 0) # test when 0 and 0 is given as input the output is 0.

        self.assertEqual(add(4.5, 5.3), 9.8) # test when 4.5 and 5.3 is given as input the output is 9.8.

        self.assertEqual(add('hello', 'world'), 'helloworld') # test when 'hello' and 'world' is given as input the output is 'helloworld'. 

        self.assertEqual(add(2.3000, 4.300), 6.6) # test when 2.3000 and 4.300 is given as input the output is 6.6.

        self.assertNotEqual(add(-2, -2), 0) # test when -2 and -2 is given as input the output is not 0.

# Run all the test cases defined in the module when the script is executed.
# This will automatically discover and run all the test cases defined in the module.
unittest.main()
