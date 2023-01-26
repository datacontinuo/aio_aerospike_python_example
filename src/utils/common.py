from aio_aerospike_python import AioAerospikeClient

_aerospike_client = None

def get_aerospike_client() -> AioAerospikeClient:
    global _aerospike_client
    if not _aerospike_client:
        config = {
            'hosts': [('aerospike', 3000)]
        }
        _aerospike_client = AioAerospikeClient(config)
        # _aerospike_client.connect()
    return _aerospike_client
