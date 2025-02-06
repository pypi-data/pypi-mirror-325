from amazon_bedrock import Bedrock


_client = None

def get_client():
    global _client
    if _client is None:
        _client = Bedrock(region="us-west-2")
    return _client
