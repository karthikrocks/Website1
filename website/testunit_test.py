import unittest
import sys
class TestStringMethods(unittest.TestCase):
      
    def setUp(self):
        pass
        """Any argument can be passed here in setUp() Ex: self.a = "a" etc"""
  
    # Returns True if the string contains 4 a.
    def test_strings_a(self):
        self.assertEqual( 'a'*5, 'aaaaa')
  
    # Returns True if the string is in upper case.
    def test_upper(self):        
        self.assertEqual('foo'.upper(), 'FOO')
  
    # Returns TRUE if the string is in uppercase
    # else returns False.
    def test_isupper(self):        
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
  
    # Returns true if the string is stripped and 
    # matches the given output.
    def test_strip(self):        
        s = 'karthikeyamaanas'
        self.assertEqual(s.strip('karthik'), 'eyamaanas')
  
    # Returns true if the string splits and matches
    # the given output.
    def test_split(self):        
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
    
    @unittest.skipUnless(not sys.platform.startswith("win"), "requires any operating system exept Windows")
    def test_no_windows_support(self):
        # windows specific testing code
        pass

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual('broken'.upper(), "broken")
if __name__ == '__main__':
    unittest.main()