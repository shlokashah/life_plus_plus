import unittest
from context import utils
from utils import blockchain
from web3 import Web3 

class Blockchain_Tests(unittest.TestCase):

	def test_connect(self):
		b = blockchain.Blockchain("http://127.0.0.1:7545")
		self.assertTrue(b.connect())

if __name__ == "__main__":
	unittest.main()		
