# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-21 15:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrinho', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backend.Carrinho')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='backend.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Produtos_no_Carrinho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('carrinho', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='backend.Carrinho')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='backend.Produtos')),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='carrinho',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Carrinho'),
        ),
    ]
