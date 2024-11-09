# Unit testing

Unit tests are segments of code written to validate if other units of code are operating as designed.

During code development, each unit is tested in a continuous integration test server environment.

### Code Example

    import unittest
    from mypackage.mymodule import my_function

    class TestMyFunction(unittest.TestCase):

        def test_my_function(self):
            result = my_function(<args>)
            self.assertEqual(result, <response>)

    unittest.main()
