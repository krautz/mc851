from django import forms

class DadosCliente(forms.Form):
    nome_cliente = forms.CharField(label="Nome do Cliente", max_length=100, widget=forms.TextInput(
        attrs={
            'type': 'name',
            'class': 'form-control',
            'placeholder': "Nome"
        }
    ))
    email = forms.CharField(label="Email", max_length=100, widget=forms.TextInput(
        attrs={
            'type': 'email',
            'class': 'form-control',
            'placeholder': "Exemplo: email@email.com"
        }
    ))
    senha = forms.CharField(label="Senha", max_length=100, widget=forms.TextInput(
        attrs={
            'type': 'password',
            'class': 'form-control',
            'placeholder': "Senha"
        }
    ))
    cpf = forms.CharField(label="CPF", max_length=11, widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': "Exemplo: 12345678912"
        }
    ))
    data_nascimento = forms.CharField(label="Data de Nascimento", max_length=100, widget=forms.TextInput(
        attrs={
            'type': 'date',
            'class': 'form-control',
            'placeholder': "Exemplo: 01/01/2000"
        }
    ))
    telefone = forms.CharField(label="Telefone", max_length=9, widget=forms.TextInput(
        attrs={
            'type': 'tel',
            'class': 'form-control',
            'placeholder': "Exemplo: 123456789"
        }
    ))
    id_grupo = forms.CharField(label="Id do Grupo", max_length=100, widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': "Exemplo: 1"
        }
    ))

class DadosEndereco(forms.Form):
    id = forms.IntegerField(label="Id do Endereco")
    cep = forms.CharField(label="CEP", max_length=8)
    logradouro = forms.CharField(label="Logradouro", max_length=100)
    inicio = forms.CharField(label="Inicio", max_length=50)
    fim = forms.CharField(label="Fim", max_length=50)
    latitude = forms.CharField(label="Latitude", max_length=12)
    longitude = forms.CharField(label="Longitude", max_length=12)
    bairro = forms.CharField(label="Bairro", max_length=100)
    cidade = forms.CharField(label="Cidade", max_length=100)
    estado = forms.CharField(label="Estado", max_length=2)