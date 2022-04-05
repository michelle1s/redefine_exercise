import requests


class BlockChainApi(object):

    @staticmethod
    def get_block(block_index: int) -> dict:
        url = f'https://blockchain.info/block-height/{block_index}?format=json'
        return requests.get(url).json()

    @staticmethod
    def get_last_block() -> dict:
        url = 'https://blockchain.info/latestblock'
        return requests.get(url).json()
