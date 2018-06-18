from django.core.exceptions import ValidationError
from django.forms.fields import Field
from django.utils.translation import gettext_lazy as _
from pycpfcnpj import cpfcnpj
from pycpfcnpj.cnpj import validate as cnpj_validate
from pycpfcnpj.cpf import validate as cpf_validate


class CPFCNPJField(Field):

    def __init__(self, cpf=True, cnpj=True, **kwargs):
        super().__init__(**kwargs)
        self._set_validator(cpf=cpf, cnpj=cnpj)

    def _validate_cpf(self, value):
        if not cpf_validate(value):
            raise ValidationError(_('CPF está invalido'))

    def _validate_cnpj(self, value):
        if not cnpj_validate(value):
            raise ValidationError(_('CNPJ está invalido'))

    def _validate_cpf_cnpj(self, value):
        if not cpfcnpj.validate(value):
            raise ValidationError(_('Documento invalido'))

    def _set_validator(self, cpf, cnpj):
        if cpf and cnpj:
            self.validators.append(self._validate_cpf_cnpj)

        elif cpf:
            self.validators.append(self._validate_cpf)

        elif cnpj:
            self.validators.append(self._validate_cnpj)

        else:
            raise AssertionError(_('CPF e/ou CNPJ devem ser True'))
