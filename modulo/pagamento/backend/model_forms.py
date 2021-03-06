# -*- coding: utf-8 -*-

from django import forms

class DadosCliente(forms.Form):
    nome_cliente = forms.CharField(
        label="Nome do Cliente",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'type': 'name',
                'class': 'form-control',
                'placeholder': "Nome",
                'required': True
            },
        )
    )
    email = forms.CharField(label="Email", max_length=100, widget=forms.TextInput(
        attrs={
            'type': 'email',
            'class': 'form-control',
            'placeholder': "Exemplo: email@email.com",
        }
    ))
    senha = forms.CharField(label="Senha", max_length=100, widget=forms.TextInput(
        attrs={
            'type': 'password',
            'class': 'form-control',
            'placeholder': "Senha",
            'required': True
        }
    ))
    cpf = forms.CharField(
        label="CPF",
        max_length=11,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'pattern': '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]',
                'placeholder': "Exemplo: 12345678912",
                'required': True,
                'title': 'Example: 12312312312'
            }
        ),
        # error_message='sdfhsakdf'
    )
    data_nascimento = forms.CharField(
        label="Data de Nascimento",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': "Exemplo: 01/01/2000",
                'required': True
            },
        )
    )
    telefone = forms.CharField(label="Telefone", max_length=9, widget=forms.TextInput(
        attrs={
            'type': 'tel',
            'class': 'form-control',
            'placeholder': "Exemplo: 123456789",
        }
    ))
    id_grupo = forms.CharField(label="Id do Grupo", max_length=100, widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': "Exemplo: 1"
        }
    ))

class DadosProduto(forms.Form):

    id_produto = forms.CharField(label='ID do Produto', max_length=100)
    name = forms.CharField(label='Nome do Produto' ,max_length=100)
    ownerGroup = forms.CharField(label='Modulo (Pagamento)',max_length=20)
    category = forms.CharField(label='Categoria', max_length=50)
    type_produto = forms.CharField(label='Tipo do Produto', max_length=50)
    manufacturer = forms.CharField(label='Fabricante', max_length=50)
    quantityInStock = forms.IntegerField(label='Quantidade em Estoque')
    value = forms.FloatField(label='Valor do Produto')
    availableToSell = forms.BooleanField(label='Produto Disponivel')
    creationDate = forms.CharField(label='Data de criacao (aaaa-mm-dd)', max_length=20)
    updateDate = forms.CharField(label='Data de atualizacao (aaaa-mm-dd)', max_length=20)
    weight = forms.FloatField(label='Peso do Produto')
    imageURLs = forms.CharField(label='URLs das Imagens (Separar URLs por @)', max_length=100000)
    description = forms.CharField(label='Descricao do Produto', max_length=1000)

class DadosEndereco(forms.Form):
    id = forms.IntegerField(label="Id do Endereco")
    cep = forms.CharField(label="CEP", min_length=8, max_length=8, widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Exemplo: 00000001',
            'minlenght': '8',
            'maxlenght': '8'

        }
    ))
    logradouro = forms.CharField(label="Logradouro", max_length=100)
    inicio = forms.CharField(label="Inicio", max_length=50)
    fim = forms.CharField(label="Fim", max_length=50)
    latitude = forms.CharField(label="Latitude", max_length=12)
    longitude = forms.CharField(label="Longitude", max_length=12)
    bairro = forms.CharField(label="Bairro", max_length=100)
    cidade = forms.CharField(label="Cidade", max_length=100)
    estado = forms.CharField(label="Estado", max_length=2)
    numero_casa = forms.IntegerField(label="Numero da Casa", widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Exemplo: 175'
        }
    ))
    complemento = forms.CharField(label="Complemento", max_length=200, widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Exemplo: ap. 101'
        }
    ))



class DadosCartao(forms.Form):
    nome_cartao = forms.CharField(
        label="Nome do Cartão",
        max_length=40,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': "Exemplo: Joaquim da Silva",
                'required': True,
                'title': "Exemplo: Joaquim da Silva",
            },
        )
    )

    cpf = forms.CharField(
        label="CPF",
        max_length=11,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': "Apenas números",
                'required': True,
                'title': "Exemplo: 12345678945",
            },
        )
    )


    numero_cartao = forms.CharField(
        label="Número do Cartão",
        max_length=16,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'pattern': '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]',
                'placeholder': "Exemplo: 1234567811023456",
                'required': True,
                'title': "Exemplo: 1234567891023456",
            },
        )
    )

    cvv = forms.CharField(
        label="CVV",
        max_length=3,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'pattern': '[0-9][0-9][0-9]',
                'placeholder': "Exemplo: 123",
                'required': True,
                'title': "Exemplo: 123",
            },
        )
    )


    data_vencimento_cartao = forms.CharField(
        label="Data de Vencimento",
        widget=forms.TextInput(
            attrs={
                'placeholder': "MM/YYYY",
                'class': 'form-control',
                'required': True,
                'pattern': '[0-9]{2}/[0-9]{4}',
            },
        ),
    )

    opcao_pagamento = forms.ChoiceField(
        label="Opção:",
        choices=[[1, 'Crédito'], [0,'Débito']],
        widget=forms.Select(
            attrs={
                'id': 'id_opcao_pagamento',
                'class': 'form-control',
                'required': True
            },
        )
    )

    num_parcelas = forms.ChoiceField(
        label="N. Parcelas:",
        choices=[[1, '1x'], [2,'2x'],[3,'3x'],[4,'4x'],[5,'5x'],[6,'6x'],],
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'required': True
            },
        )
    )
