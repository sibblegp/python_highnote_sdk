from graphql_client.client import Client
from base64 import b64encode

class Highnote():
  
  def __init__(self, api_key, testing=False):
      b64_api_key = b64encode(f"{api_key}:".encode())
      if testing:
        self.client: Client = Client(
          'https://api.us.test.highnote.com/graphql',
          {
            'Authorization': 'Basic '
            + b64_api_key
          },
        )
      else:
        self.client: Client = Client(
        'https://api.us.test.highnote.com/graphql',
        {
            'Authorization': 'Basic '
            + b64_api_key
        },
      )