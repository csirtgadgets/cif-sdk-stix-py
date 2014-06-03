import unittest
from cif.sdk.stix import Stix

class TestClient(unittest.TestCase):

    def setUp(self):
        self.stix = Stix(description='test bad guy')
        
    def test_simple(self):
        self.assertEqual(self.stix._description,'test bad guy','mis-matched discription')
    
    def test_xml(self):
        self.assert_(self.stix.to_xml(),'got some form of xml')

if __name__ == '__main__':
    unittest.main()
