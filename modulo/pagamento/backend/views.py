# -*- coding: utf-8 -*-

from django.shortcuts import render
from datetime import *
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import *
from django.core.exceptions import ObjectDoesNotExist
import urllib2
import json
import base64
from model_forms import *

url_clientes = "ec2-18-231-28-232.sa-east-1.compute.amazonaws.com:3002/"

#Renderiza a pagina inicial do site
def home(request):
    # Pega o usuário caso exista
    usuario = request.session.get('usuario', False)

    return render(request, 'backend/home.html', {'usuario': usuario})


def recuperar(request):
    return render(request, 'backend/recuperar.html')


'''---------------------------------------------------------------------------------------------------------'''
'''---------------------------------------------API DE ENDERECO---------------------------------------------'''
'''---------------------------------------------------------------------------------------------------------'''

#Renderiza a pagina que ira enviar o cep do endereco a ser pesquisado na api de enderecos
def endereco_cliente(request):
    # Pega o usuário caso exista
    usuario = request.session.get('usuario', False)

    # Recupera do forms enviado pelo html o cep
    endereco = DadosEndereco()

    # Passa o forms como contexto para ser utilizado para obtencao de dados no html
    context = {
        'endereco': endereco,
        'usuario': usuario
    }

    return render(request=request, template_name='backend/endereco_cep.html', context=context)


#Funcao que ira requisitar a api de enderecos, os dados de uma busca de endereco por cep
def endereco_cep(request):
    # Pega o usuário caso exista
    usuario = request.session.get('usuario', False)

    #URL com o endereco da api para fazer a requisicao
    url = 'http://wsendereco.tk/api/enderecos/cep/'

    endereco = DadosEndereco(data=request.POST)

    url = url + endereco['cep'].value()

    request2 = urllib2.Request(url=url, headers={'Content-Type': 'application/json'})

    try:
        # serializade_data = urllib2.urlopen(request2, data=json.dumps(data))
        serializade_data = urllib2.urlopen(request2).read()
        resposta = json.loads(serializade_data)

        context = {
            'bairro': resposta['Endereco'][0]['bairro'],
            'cidade': resposta['Endereco'][0]['cidade'],
            'inicio': resposta['Endereco'][0]['inicio'],
            'logradouro': resposta['Endereco'][0]['logradouro'],
            'longitude': resposta['Endereco'][0]['longitude'],
            'cep': resposta['Endereco'][0]['cep'],
            'latitude': resposta['Endereco'][0]['latitude'],
            'estado': resposta['Endereco'][0]['estado'],
            'fim': resposta['Endereco'][0]['fim'],
            'usuario': usuario
        }
        # return JsonResponse(resposta)
        return render(
            request=request,
            template_name="backend/confirma_endereco.html",
            context=context
        )

    except Exception as e:

        return JsonResponse({'error': e.code})


'''---------------------------------------------------------------------------------------------------------'''
'''---------------------------------------------API DE CLIENTES---------------------------------------------'''
'''---------------------------------------------------------------------------------------------------------'''


#Renderiza pagina que ira receber os dados do cliente para cadastrar na api de clientes
def dados_cliente(request):
    # Pega o usuário caso exista
    usuario = request.session.get('usuario', False)

    cliente = DadosCliente()

    # Passa o forms como contexto para ser utilizado para obtencao de dados no html
    context = {
        'cliente': cliente,
        'usuario': usuario
    }

    return render(
        request=request,
        template_name='backend/cadastro_cliente.html',
        context=context
    )


#Cadastra um cliente no modulo de clientes
def cadastra_cliente(request):

    #Recupera do forms enviado pelo html, os dados do cliente
    form_cliente = DadosCliente(data=request.POST)

    url = 'http://ec2-18-231-28-232.sa-east-1.compute.amazonaws.com:3002/register'

    data = {
        "email": form_cliente['email'].value(),
        "senha": form_cliente['senha'].value(),
        "cpf": form_cliente['cpf'].value(),
        "nome": form_cliente['nome_cliente'].value(),
        "dataDeNascimento": form_cliente['data_nascimento'].value(),
        "telefone": form_cliente['telefone'].value(),
        "idGrupo": 5
    }

    data = json.dumps(data)

    request2 = urllib2.Request(url=url, data=data, headers={'Content-Type': 'application/json'})

    try:
        # Pega o usuário caso exista
        usuario = request.session.get('usuario', False)

        serializade_data = urllib2.urlopen(request2).read()
        resposta = json.loads(serializade_data)

        context = {
            'registerToken': resposta['registerToken'],
            'usuario': usuario
        }

        # return JsonResponse(resposta)
        return render(request=request, template_name='backend/confirma_cadastro.html', context=context)

    except Exception as e:

        return JsonResponse({'error': e.code})


# Confirma o cadastro de um cliente
def confirma_cadastro(request):

    # Url da api de clientes para confirmar o cadastramento do usuario
    url = 'http://ec2-18-231-28-232.sa-east-1.compute.amazonaws.com:3002/confirm'

    # Obtem da request, o token de sessao
    register_token = request.POST.get('registerToken')

    # Monta o JSON com o registerToken para que a API de clientes confirme o cadastramento do usuario
    data = {
        'registerToken': register_token
    }

    data = json.dumps(data)

    request2 = urllib2.Request(url=url, data=data, headers={'Content-Type': 'application/json'})

    try:
        serializade_data = urllib2.urlopen(request2).read()
        resposta = json.loads(serializade_data)

        return render(request=request, template_name='backend/cadastro_cliente_confirmado.html')

    except Exception as e:

        return JsonResponse({'error': e})


#Renderiza a pagina de login
def login(request):
    # Pega o usuário caso exista
    usuario = request.session.get('usuario', False)

    # Instancia um forms para os dados do cliente
    cliente = DadosCliente()

    # Passa o forms como contexto para ser utilizado para obtencao de dados no html
    context = {
        'cliente': cliente,
        'usuario': usuario
    }

    return render(request=request, template_name='backend/login.html', context=context)

#Realiza o login na api de clientes
def resultado_login(request):

    #Recupera do forms enviado pelo html, os dados do cliente
    form_cliente = DadosCliente(data=request.POST)

    url ='http://ec2-18-231-28-232.sa-east-1.compute.amazonaws.com:3002/login'

    data = {
        "email": form_cliente['email'].value(),
        "senha": form_cliente['senha'].value(),
    }

    data = json.dumps(data)

    request2 = urllib2.Request(
        url=url,
        data=data,
        headers={'Content-Type': 'application/json'}
    )

    try:
        serializade_data = urllib2.urlopen(request2).read()
        resposta = json.loads(serializade_data)

        # Trocar para nome do cliente
        request.session['usuario'] = form_cliente['email'].value().split("@")[0]

        context = {
            'sessionToken': resposta['sessionToken']
        }

        return render(request=request, template_name='backend/login_confirmado.html')

    except Exception as e:

        return JsonResponse({'error': e})

def logout(request):
    request.session['usuario'] = ''

    return render(request=request, template_name='backend/home.html')


def minha_conta(request):
    # Pega o usuário caso exista
    usuario = request.session.get('usuario', False)

    context = {
            'usuario': usuario
        }

    return render(request=request, template_name='backend/minha_conta.html', context=context)

'''---------------------------------------------------------------------------------------------------------'''
'''---------------------------------------------API DE PRODUTOS---------------------------------------------'''
'''---------------------------------------------------------------------------------------------------------'''

def produtos_eletrodomesticos(request, pagina):

    return att_produto(request, pagina, "eletrodomestico")
    #return get_produtos (request, pagina, "eletromestico")
    # return HttpResponse("eletro" + str(pagina))
    #produtos (request, pagina, "eletromestico")
    # Pega o usuário caso exista
    # usuario = request.session.get('usuario', False)
    #
    # return render(request=request, template_name='backend/produtos.html', context={'usuario': usuario})

def produtos_computadores(request, pagina):
    #produtos (request, pagina, "computador")
    return HttpResponse("comp" + str(pagina))

def produtos_celulares(request, pagina):
    #produtos (request, pagina, "celular")
    return HttpResponse("celulares" + str(pagina))

#Funcao que realiza um request para a api de produtos para pegar a lista de produtos
def get_produtos(request, pagina, categoria):

    url = 'http://ec2-18-218-218-216.us-east-2.compute.amazonaws.com:8080/api/products?page=' + pagina + '&itemsPerPage=10'

    request2 = urllib2.Request(url=url)

    #Adiciona ao request o login de autorizacao
    basic_auth = base64.b64encode('%s:%s' % ('pagamento', 'LjKDBeqw'))
    request2.add_header("Authorization", "Basic %s" % basic_auth)

    try:

        # Pega o usuário caso exista
        usuario = request.session.get('usuario', False)

        # Realiza o request e obtem os dados retornados
        serializade_data = urllib2.urlopen(request2).read()
        resposta = json.loads(serializade_data)

        #Lista com os produtos retornados
        produtos = resposta['content']

        #Adiciona os ids dos produtos no banco de dados
        for i in range(0, len(produtos)):

            if(Produtos.objects.filter(id_produto=resposta['content'][i]['id']) == False):

                p = Produtos()
                p.id_produto = resposta['content'][i]['id']
                p.save()

        #JSON com a lista de produtos que sera retornado
        context = {
            'produtos': produtos,
            'registerToken': resposta['registerToken'],
            'usuario': usuario

        }

        return JsonResponse(context)

    except Exception as e:

        return JsonResponse({'error': e})

#Funcao que renderiza a pagina para o admin que ira atualizar os dados de um produto
def render_att_produtos(request):

    # Instancia um forms para os dados do Produto
    produto = DadosProduto()

    # Passa o forms como contexto para ser utilizado para obtencao de dados no html
    context = {
        'produto': produto,
    }

    return render(request=request, template_name='backend/admin_dados_produto.html', context=context)


#Funcao que atualiza as informacoes de um produto
def att_produto(request):

    #Recebe o id do produto por post
    form_Produto = DadosProduto(data=request.POST)
    id_produto = form_Produto['id_produto'].value()

    #PROCURA O PRODUTO NA API DE PRODUTOS, PARA QUE SEUS DADOS SEJAM ATUALIZADOS

    #Url da requisicao
    url = 'http://ec2-18-218-218-216.us-east-2.compute.amazonaws.com:8080/api/products/' + id_produto

    request2 = urllib2.Request(url=url)

    # Adiciona ao request o login de autorizacao
    basic_auth = base64.b64encode('%s:%s' % ('pagamento', 'LjKDBeqw'))
    request2.add_header("Authorization", "Basic %s" % basic_auth)

    #Realiza uma requisicao ao modulo de produtos para obter os dados do produto
    try:
        serializade_data = urllib2.urlopen(request2).read()
        dados_produto = json.loads(serializade_data)

    except Exception as e:

        return JsonResponse({'error': e})

    #Atualiza os dados que o admin quer que sejam atualizados
    for key in form_Produto.fields:

        if(form_Produto[key].data):
            dados_produto[key] = form_Produto[key].data


    #ATUALIZA OS DADOS DO PRODUTO

    # Url da requisicao
    url = 'http://ec2-18-218-218-216.us-east-2.compute.amazonaws.com:8080/api/products/' + id_produto

    data = json.dumps(dados_produto)
    request2 = urllib2.Request(url=url, data=data, headers={'Content-Type': 'application/json'})
    request2.get_method = lambda: 'PATCH'

    basic_auth = base64.b64encode('%s:%s' % ('pagamento', 'LjKDBeqw'))
    request2.add_header("Authorization", "Basic %s" % basic_auth)

    #Envia a requsicao ao modulo
    try:
        serializade_data = urllib2.urlopen(request2).read()
        resposta = json.loads(serializade_data)

        return JsonResponse(resposta)

    except Exception as e:

        return JsonResponse({'error': e})


def produtos (request, pagina, categoria):

    # url = 'http://ec2-18-218-218-216.us-east-2.compute.amazonaws.com:8080/api/products?page=0&itemsPerPage=10'
    url = 'http://ec2-18-218-218-216.us-east-2.compute.amazonaws.com:8080/api/products/f47eaf47-0669-40d2-8b13-d983c871e0ba'

    data = {
            "id": "f47eaf47-0669-40d2-8b13-d983c871e0ba",
            "name": "TESTE2",
            "description": "Geladeira Brastemp Frost Free Duplex 500 litros cor Inox com Turbo Control",
            "weight": 82,
            "category": "ELETRODOMESTICO",
            "type": "Geladeira",
            "manufacturer": "Brastemp",
            "quantityInStock": 10,
            "value": 3499.99,
            "promotionalValue": 10,
            "availableToSell": True,
            "onSale": False,
            "ownerGroup": "pagamento",
            "images": [],
            "creationDate": "2018-10-10",
            "updateDate": "2018-10-10",
            "lastModifiedBy": "pagamento"
            }

    data = json.dumps(data)
    request2 = urllib2.Request(url=url, data=data, headers={'Content-Type': 'application/json'})
    request2.get_method = lambda: 'PATCH'

    basic_auth = base64.b64encode('%s:%s' % ('pagamento', 'LjKDBeqw'))
    request2.add_header("Authorization", "Basic %s" % basic_auth)

    try:
        serializade_data = urllib2.urlopen(request2).read()
        resposta = json.loads(serializade_data)


        return JsonResponse(resposta)
        # return render(request=request, template_name='backend/confirma_cadastro.html', context=context)

    except Exception as e:

        return JsonResponse({'error': e})


def meu_carrinho(request):
    # Pega o usuário caso exista
    usuario = request.session.get('usuario', False)

    context = {
            'usuario': usuario
        }
    return render(request=request, template_name='backend/meu_carrinho.html', context=context)

