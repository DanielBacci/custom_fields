Django Custom Fields
======================

.. _description:

Simples custom fields.

* CPFCNPJField
* ...


Use
---

.. code:: bash

    from fields import CPFCNPJField
    from django import forms

    Class Customer(forms.Form):

        cpf_cnpj = CPFCNPJField(cpf=True, cnpj=True)

    ..

    To install custom_fileds with all dependencies use ``pip install custom_fields``

Installation
------------

.. code:: bash

    $ make install-dev

..


Tests
-----

.. code:: bash

    $ make test

..
