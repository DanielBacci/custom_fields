import pytest
from django.core.exceptions import ValidationError

from fields import CPFCNPJField


@pytest.fixture()
def cpf_valid():
    return '06254444852'


@pytest.fixture()
def cnpj_valid():
    return '75265029000102'


@pytest.fixture()
def cpf_invalid():
    return '06254444854'


@pytest.fixture()
def cnpj_invalid():
    return '75265029010102'


class TestCPFCNPJField:

    def test_should_validate_cpf(self, cpf_valid):
        cpf_cnpj_field = CPFCNPJField()
        assert cpf_cnpj_field.clean(cpf_valid) == cpf_valid

    def test_should_validate_cnpj(self, cnpj_valid):
        cpf_cnpj_field = CPFCNPJField()
        assert cpf_cnpj_field.clean(cnpj_valid) == cnpj_valid

    @pytest.mark.parametrize('value', [
        cpf_invalid,
        cnpj_invalid
    ])
    def test_should_validate_raise_validator_error(self, value):
        cpf_cnpj_field = CPFCNPJField()
        with pytest.raises(ValidationError):
            assert cpf_cnpj_field.clean(value) == value

    def test_should_validate_raise_validator_error_invactive_cpf(
        self,
        cpf_valid
    ):
        cpf_cnpj_field = CPFCNPJField(cpf=False)
        with pytest.raises(ValidationError):
            assert cpf_cnpj_field.clean(cpf_valid) == cpf_valid

    def test_should_validate_raise_validator_error_invactive_cnpj(
        self,
        cnpj_valid
    ):
        cpf_cnpj_field = CPFCNPJField(cnpj=False)
        with pytest.raises(ValidationError):
            assert cpf_cnpj_field.clean(cnpj_valid) == cnpj_valid

    def test_should_validate_raise_assert_error(self):
        with pytest.raises(AssertionError):
            CPFCNPJField(cnpj=False, cpf=False)
