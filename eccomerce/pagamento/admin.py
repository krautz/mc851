from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Cartao)
admin.site.register(Boleto)
admin.site.register(Pagamento)
