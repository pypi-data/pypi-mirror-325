import re

class Patterns:
    """Common regex patterns for validation."""

    EMAIL_PATTERN = re.compile(
        r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    )

    @staticmethod
    def email(email: str) -> bool:
        """Validates an email address."""
        
        return bool(Patterns.EMAIL_PATTERN.fullmatch(email))