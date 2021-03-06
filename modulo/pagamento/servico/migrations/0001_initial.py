# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-09-12 21:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boleto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco', models.CharField(max_length=50)),
                ('num_boleto', models.CharField(max_length=100)),
                ('data_vencimento', models.DateField()),
                ('nome_empresa', models.CharField(max_length=100)),
                ('endereco_empresa', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_cartao', models.CharField(max_length=15)),
                ('cvv', models.CharField(max_length=5)),
                ('nome_cartao', models.CharField(max_length=50)),
                ('data_vencimento_cartao', models.DateField()),
                ('credito', models.BooleanField()),
                ('debito', models.BooleanField()),
                ('num_parcelas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf_cliente', models.IntegerField()),
                ('valor', models.FloatField()),
                ('data_emissao', models.DateField()),
                ('cnpj_empresa', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='cartao',
            name='pedido',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='servico.Pedido'),
        ),
        migrations.AddField(
            model_name='boleto',
            name='pedido',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='servico.Pedido'),
        ),
    ]
