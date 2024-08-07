from pycpfcnpj import cpfcnpj
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_document(document):
    
    valid = cpfcnpj.validate(document)
    
    if not valid:
        raise ValidationError(
            _("%(document)s não é um CPF/CNPJ válido"),
            params={"document": document},
        )