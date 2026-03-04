from rest_framework.exceptions import ValidationError

valid_url = "youtube.com"


def validation_url(value: str):
    if valid_url not in value:
        raise ValidationError(f"Ссылка должна вести на ресурсы: '{valid_url}'")
