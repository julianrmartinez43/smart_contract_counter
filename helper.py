from web3 import Web3, HTTPProvider, eth
provider_url = "https://ropsten.infura.io/v3/f3d466d278a14e2884135b991c58ef54" # infura mainnet.infura.io/v3 f3d466d278a14e2884135b991c58ef54
web3 = Web3(Web3.HTTPProvider(provider_url))

total_contracts_found = 0
last_block_checked = 0
contract_creation_transactions = [] # used to check if they are actually capturing transactions

def smart_contract_created(txhash): 
    if web3.eth.getTransaction(txhash)['to'] == None:
        contract_creation_transactions.append(txhash)
        return True
    else:
        return False

block_number = 6624125

# counts # of contracts created within a specific block
def count_contracts_in_block(block):
    transactions = web3.eth.getBlock(block).transactions
    global total_contracts_found
    contracts_found_in_block = 0
    for transaction in transactions:
        if smart_contract_created(transaction) == True:
            print(transaction)
            contracts_found_in_block = contracts_found_in_block + 1
            # global total_contracts_found = global total_contracts_found + 1
    total_contracts_found = total_contracts_found + contracts_found_in_block
    print("Contracts found in block:", contracts_found_in_block,"    Total contracts found so far:", total_contracts_found)

# counts smart contracts created within a range of blocks
def count_from_to(starting_block=int, last_block=int):
    global last_block_checked
    stop = last_block + 1
    for block in range(starting_block, stop):
        count_contracts_in_block(block)
        last_block_checked = block
        print(last_block_checked)


    


# future tasks, add asyn
# figure out how to use range for the for loop above
