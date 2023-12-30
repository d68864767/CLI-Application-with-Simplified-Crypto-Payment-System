```python
# user_interface.py

import time
import click

class UserInterface:
    def display_payment_link(self, payment_link):
        """
        Display the generated payment link to the user.
        """
        click.echo(f'Please make your payment by visiting the following link: {payment_link}')

    def wait_for_payment(self):
        """
        Wait for the user to make the payment.
        """
        click.echo('Waiting for the payment to be made...')
        time.sleep(60)  # Wait for 60 seconds

    def display_success_message(self):
        """
        Display a success message after the payment has been verified.
        """
        click.echo('Payment successful! Thank you for your transaction.')
```
