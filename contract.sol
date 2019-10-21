pragma solidity ^0.5.1;

contract Prescription{

    bytes32[] hashes;
    
    constructor() public{
        
    }
    
    function check_existence (bytes32 hash) public view returns (bool){
        
        uint i=0;
        for(i=0;i<hashes.length;++i)
        {
            if(hashes[i] == hash)
                return true;
        }
        return false;
    }
    
    function add_hash(bytes32 hash) public returns(bool) {
        if(check_existence(hash))
            return false;
            
            
        hashes.push(hash);
        return true;
    }

}
