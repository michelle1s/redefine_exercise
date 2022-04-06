from block_chain_api import BlockChainApi


class BlockChainSteps(object):

    @staticmethod
    def get_block_timestamp(block_index: int) -> int:
        response = BlockChainApi.get_block(block_index).get('blocks')
        if response:
            return response[0].get('time')

    @staticmethod
    def get_last_block_index() -> int:
        response = BlockChainApi.get_last_block()
        if response:
            return response.get('height')

    @staticmethod
    def get_last_block_timestamp() -> int:
        response = BlockChainApi.get_last_block()
        if response:
            return response.get('time')

    def binary_search(self, timestamp: int, low: int, high: int) -> int:
        while low <= high:
            mid = low + (high - low) // 2
            mid_timestamp = self.get_block_timestamp(mid)
            if mid_timestamp == timestamp:
                return mid - 1

            elif mid_timestamp < timestamp:
                low = mid + 1

            else:
                high = mid - 1

        return high

    def calculate_approximate_nearest_block(self, timestamp: int) -> int:
        average_diff = 600  # 10 minutes in seconds
        genesis_block_timestamp = self.get_block_timestamp(0)
        return (timestamp - genesis_block_timestamp) // average_diff

    def search_nearest_timestamp(self, timestamp: int) -> int:
        genesis_block_timestamp = self.get_block_timestamp(0)
        if timestamp < genesis_block_timestamp:
            return -1

        last_block_index = self.get_last_block_index()
        approx_nearest_block = self.calculate_approximate_nearest_block(timestamp)

        approx_nearest_block_timestamp = self.get_block_timestamp(approx_nearest_block)
        last_block_timestamp = self.get_last_block_timestamp()

        if timestamp > last_block_timestamp:
            return last_block_index

        if approx_nearest_block_timestamp:
            if timestamp <= approx_nearest_block_timestamp:
                if approx_nearest_block_timestamp <= last_block_timestamp:
                    return self.binary_search(timestamp, 0, approx_nearest_block)
            else:
                return self.binary_search(timestamp, approx_nearest_block, last_block_index)

        return self.binary_search(timestamp, 0, last_block_index)
