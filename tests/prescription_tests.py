import unittest
from context import utils
from utils import prescription

class Prescription_Test(unittest.TestCase):
	def test_upload(self):
		test = prescription.Prescription()
		self.assertTrue(test.upload())

if __name__ == "__main__":
	unittest.main()