from web3 import Web3


class Blockchain():

	def __init__(self , url=None):
		"""
		Constructor
		
		Parameters:
		url : string: url of blockchain
		"""
		self.url = url
		self.contract_address = ""

	def connect(self , url=None):
		"""
		Connects app to blockchain

		Parameters: 
		url : string: url of blockchain
		"""
		if url==None:
			self.web3 = Web3(Web3.HTTPProvider(self.url))
		else:
			self.web3 = Web3(Web3.HTTPProvider(url))
		return self.web3.isConnected()		

	def check_hash(self , hash):
		"""
		Checks if hash exists in blockchain

		Parameters:
		hash : string: hash of 256 bits length
		"""
		pass