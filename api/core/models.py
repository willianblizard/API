# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'categoria'


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome_cli = models.CharField(max_length=200, blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    cli_telefone = models.CharField(max_length=200, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class FichaUsuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=14, blank=True, null=True)
    ddd = models.CharField(max_length=2, blank=True, null=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    senha = models.CharField(max_length=100, blank=True, null=True)
    tipo_pessoa = models.CharField(max_length=2, blank=True, null=True)
    nome_fantasia = models.CharField(max_length=100)
    nome = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ficha_usuario'


class Fornecedor(models.Model):
    id_fornecedor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    telefone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200)
    telefone_adicional = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'fornecedor'


class ProdCategoria(models.Model):
    categoria_id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='categoria_id_categoria')
    produto_id_produto = models.ForeignKey('Produto', models.DO_NOTHING, db_column='produto_id_produto')

    class Meta:
        managed = False
        db_table = 'prod_categoria'


class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)
    tamanho = models.CharField(max_length=20, blank=True, null=True)
    custo = models.TextField()  # This field type is a guess.
    preco = models.TextField()  # This field type is a guess.
    fornecedor_id_fornecedor = models.ForeignKey(Fornecedor, models.DO_NOTHING, db_column='fornecedor_id_fornecedor')

    class Meta:
        managed = False
        db_table = 'produto'


class Venda(models.Model):
    id_venda = models.AutoField(primary_key=True)
    data_venda = models.DateTimeField()
    valor_total = models.TextField()  # This field type is a guess.
    forma_pagamento = models.CharField(max_length=200)
    parc = models.SmallIntegerField(blank=True, null=True)
    valor_pago = models.TextField()  # This field type is a guess.
    desconto = models.TextField()  # This field type is a guess.
    cliente_id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_id_cliente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venda'


class VendaProduto(models.Model):
    qtd_prd = models.IntegerField()
    produto_id_produto = models.ForeignKey(Produto, models.DO_NOTHING, db_column='produto_id_produto')
    venda_id_venda = models.ForeignKey(Venda, models.DO_NOTHING, db_column='venda_id_venda')

    class Meta:
        managed = False
        db_table = 'venda_produto'
