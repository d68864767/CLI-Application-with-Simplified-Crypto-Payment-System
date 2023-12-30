```python
# payment_api.py

import requests
from security import Security

class PaymentAPI:
    def __init__(self):
        self.api_key = Security().get_api_key()
        self.base_url = 'https://api.coinbase.com/v2/'

    def generate_payment_link(self, amount, address):
        """
        Generate a payment link for the specified amount of Ethereum to the given address.
        """
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        data = {
            'amount': amount,
            'currency': 'ETH',
            'address': address
        }
        response = requests.post(f'{self.base_url}charges', headers=headers, json=data)

        if response.status_code == 200:
            return response.json()['data']['hosted_url']
        else:
            raise Exception('Failed to generate payment link.')

    def verify_payment(self, address):
        """
        Verify if the payment has been made to the given address.
        """
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        response = requests.get(f'{self.base_url}addresses/{address}/transactions', headers=headers)

        if response.status_code == 200:
            transactions = response.json()['data']
            for transaction in transactions:
                if transaction['status'] == 'completed':
                    return True
            return False
        else:
            raise Exception('Failed to verify payment.')
```
