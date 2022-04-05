from block_chain_steps import BlockChainSteps

if __name__ == '__main__':
    block_chain_steps = BlockChainSteps()
    print(block_chain_steps.search_nearest_timestamp(1232103989))
    print(block_chain_steps.search_nearest_timestamp(1637430034))
