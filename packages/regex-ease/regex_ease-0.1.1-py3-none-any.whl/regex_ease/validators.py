from .patterns import Patterns

class Validators:
    """Common regex patterns for validation."""

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Checks if an email is valid."""

        return Patterns.email(email)

    @staticmethod
    def get_email_domain(email: str) -> bool:
        """Extracts the domain from an email address."""

        if Validators.is_valid_email(email):
            return email.split('@')[1]
        return None