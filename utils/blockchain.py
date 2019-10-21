from web3 import Web3
import json

bytecode = "608060405234801561001057600080fd5b506101c6806100206000396000f3fe608060405260043610610046576000357c01000000000000000000000000000000000000000000000000000000009004806366e34cf11461004b578063af5135fd1461009e575b600080fd5b34801561005757600080fd5b506100846004803603602081101561006e57600080fd5b81019080803590602001909291905050506100f1565b604051808215151515815260200191505060405180910390f35b3480156100aa57600080fd5b506100d7600480360360208110156100c157600080fd5b8101908080359060200190929190505050610140565b604051808215151515815260200191505060405180910390f35b60006100fc82610140565b1561010a576000905061013b565b6000829080600181540180825580915050906001820390600052602060002001600090919290919091505550600190505b919050565b60008060009050600090505b60008054905081101561018f578260008281548110151561016957fe5b90600052602060002001541415610184576001915050610195565b80600101905061014c565b60009150505b91905056fea165627a7a72305820577f0c80bf483610360752f4736f01428e4edf66c5102792faaf73951fb4cf2b0029"
abi = json.loads("""[
    {
        "constant": false,
        "inputs": [
            {
                "name": "hash",
                "type": "bytes32"
            }
        ],
        "name": "add_hash",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "hash",
                "type": "bytes32"
            }
        ],
        "name": "check_existence",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
]""")

class Blockchain():
    def __init__(self, url=None, abi=None, bytecode=None):
        """
        Constructor

        Parameters:
        url : string: url of blockchain
        """
        
        self.url = url
        self.contract_address = ""
        self.abi = abi
        self.bytecode = bytecode
        print("type of abi")
        print(type(self.abi))
        print(abi)

    def connect(self, url=None):
        """
        Connects app to blockchain

        Parameters:
        url : string: url of blockchain
        """
        
        self.web3 = Web3(Web3.HTTPProvider(self.url))
        
        return self.web3.isConnected()


    def instantiate_contract(self):
        """
        Instantiates smart contract object
        """
        self.web3.eth.defaultAccount = self.web3.eth.accounts[0]
        block = self.web3.eth.getBlock('latest')

        if block['number']==0:
            Prescription = self.web3.eth.contract(abi=abi, bytecode=bytecode)
            tx_hash = Prescription.constructor().transact()
            tx_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
            print("Contract creation tx receipt")
            print(tx_receipt)
            
            try:
                self.contract = self.web3.eth.contract(
                address=tx_receipt.contractAddress,
                abi=self.abi,
            )
            except:
                print("Instantiation false")
                return False    
        else:
            block = self.web3.eth.getBlock(1)
            hex_hash = self.web3.toHex(block['transactions'][0])
            tx_hash = self.web3.eth.getTransactionReceipt(hex_hash)
            contract_address = tx_hash['contractAddress']
            try:
                self.contract = self.web3.eth.contract(
                    address=contract_address,
                    abi=abi,
                    )   
            except:
                print("Instantiation false")
                return False    

        return True
                
    def check_hash(self, hash_):
        """
        Checks if hash exists in blockchain

        Parameters:
        hash : string: hash of 256 bits length
        """
        print("Check hash function")
        if self.instantiate_contract():
            # exists = Prescription.functions.check_existence("0x1b16b1df538ba12dc3f97edbb85caa7050d46c148134290feba80f8236c83db9").call()
            exists = self.contract.functions.check_existence(hash_).call()
            # print(exists)
            return exists

    def insert_hash(self, hash_):
        """
        Inserts hash into blockchain
        """
        # print(hash_)
        # print(type(hash_))
        print("Insert hash function")
        if self.instantiate_contract():
            # try:
            #     self.Prescription.functions.add_hash(hash_).transact()
            # except:
            #     return False
            success = self.contract.functions.add_hash(hash_).transact()    
            return success

        # return False    

    def return_hash(self, hash_):
        """
        Returns hash of the text if found
        """
        print("Return hash function")
        if self.instantiate_contract():
            try:
                ret_hash = self.contract.functions.return_hash(hash_).call()
            except:
                # print("Hash does not exists")
                return False
            return ret_hash

if __name__ == "__main__":
    b = Blockchain("http://127.0.0.1:7545", abi, bytecode)
    hash1 = "0x1b16b1df538ba12dc3f97edbb85caa7050d46c148134290feba80f8236c83db9"
    new_hash = "0x1b16b1df538ba12dc3f97edbb85caa7050d46c148134290feba80f8236c83db0"
    print(b.connect())
    # print(b.check_hash(hash1))
    # print(b.check_hash(new_hash))
    print(b.insert_hash(hash1))
    # print(b.return_hash(hash1))