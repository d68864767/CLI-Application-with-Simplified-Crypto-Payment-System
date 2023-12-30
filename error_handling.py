```python
# error_handling.py

import click

class ErrorHandler:
    def handle_error(self, error):
        """
        Handle any errors that occurred during the payment process.
        """
        click.echo(f'An error occurred: {str(error)}')
        click.echo('Please try again or contact support if the problem persists.')
```
