from api.domain.enums.prioridade_enum import PrioridadeEnum
from django.db import models
import uuid
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User


class Perfil(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False, blank=True)
    sobrenome = models.CharField(max_length=50, null=False, blank=True)
    data_nascimento = models.DateField(null=False, blank=True)
    status_ativo = models.BooleanField(default=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_atualizacao = models.DateTimeField(null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    grupo_acesso = models.ForeignKey('GrupoAcesso', on_delete=models.PROTECT, null=True, blank=False)

    class Meta:
        db_table = 'perfil'
        ordering = ('data_cadastro',)

class TipoGrupoAcesso(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=30, unique=True, null=False)    

    class Meta:
        db_table = 'tipo_grupo_acesso'

class GrupoAcesso(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=30, unique=True, null=False)
    tipo_grupo_acesso = models.ForeignKey(TipoGrupoAcesso, on_delete=models.PROTECT)
    perfil_responsavel = models.ForeignKey(Perfil, on_delete=models.PROTECT, null=False, related_name='responsavel_grupo_acesso')
    data_cadastro = models.DateTimeField(blank=False, null=True)
    data_atualizacao = models.DateTimeField(blank=False, null=True)

    class Meta:
        db_table = 'grupo_acesso'
        ordering = ('data_cadastro', )

class ParticipanteGrupoAcesso(models.Model):
    id = models.AutoField(primary_key=True)
    perfil_participante = models.ForeignKey(Perfil, on_delete=models.PROTECT, null=True, related_name='responsavel_participante')
    grupo_acesso = models.ForeignKey(GrupoAcesso, on_delete=models.PROTECT)
    edicao_ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(blank=False, null=True)
    data_atualizacao = models.DateTimeField(blank=False, null=True)

    class Meta:
        db_table = 'participante_grupo_acesso'
        ordering = ('data_cadastro', )

class Moeda(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=20, unique=True, null=False)
    simbolo = models.CharField(max_length=5, unique=True, null=True)

    class Meta:
        db_table = 'moeda'
        ordering = ('descricao', )

class TipoMovimentacao(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50, unique=True, null=False)

    class Meta:
        db_table = 'tipo_movimentacao'
        ordering = ('descricao', )

class FormaPagamento(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50, unique=True, null=False)

    class Meta:
        db_table = 'forma_pagamento'
        ordering = ('descricao', )

class StatusMovimentacao(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=30, unique=True, null=False)

    class Meta:
        db_table = 'status_movimentacao'
        ordering = ('descricao', )

class PrioridadeMovimentacao(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=30, unique=True, null=False)

    class Meta:
        db_table = 'prioridade_movimentacao'
        ordering = ('descricao', )

class TipoConta(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50, unique=True, null=False)

    class Meta:
        db_table = 'tipo_conta'
        ordering = ('descricao', )

class InstituicaoFinanceira(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100, unique=True, null=False)
    codigo = models.CharField(max_length=10, null=True)
    nome_completo = models.CharField(max_length=300, unique=True, null=False)
    data_inicio_operacao = models.DateField(null=True)

    class Meta:
        db_table = 'instituicao_financeira'
        ordering = ('descricao', )

class UF(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100, null=False)
    sigla = models.CharField(max_length=10, null=False)

    class Meta:
        db_table = 'uf'

class Endereco(models.Model):
    id = models.AutoField(primary_key=True)
    logradouro = models.CharField(max_length=200, null=True, blank=True)
    numero = models.CharField(max_length=15, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    cep = models.CharField(max_length=20, null=True, blank=True)
    pais = models.CharField(max_length=50, null=True, blank=True)
    lat = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    lon = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    data_cadastro = models.DateTimeField(null=False, blank=True)
    data_atualizacao = models.DateTimeField(null=True, blank=True)
    status_ativo = models.BooleanField(default=True, null=False, blank=True)
    uf = models.ForeignKey(UF, on_delete=models.PROTECT, blank=True)

    class Meta:
        db_table = 'endereco'

class Conta(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_conta = models.CharField(max_length=20, null=True)
    digito_conta = models.CharField(max_length=1, null=True)
    codigo_agencia = models.CharField(max_length=10, null=True)
    saldo = models.FloatField(null=False, default=0, blank=True)
    status_ativo = models.BooleanField(default=True, null=False, blank=True)
    tipo_conta = models.ForeignKey(TipoConta, on_delete=models.PROTECT)
    instituicao_financeira = models.ForeignKey(InstituicaoFinanceira, on_delete=models.PROTECT, null=True)
    descricao = models.CharField(max_length=200, null=True)
    data_cadastro = models.DateTimeField(null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)
    perfil_responsavel = models.ForeignKey(Perfil, on_delete=models.PROTECT, null=True)
    grupo_acesso = models.ForeignKey(GrupoAcesso, on_delete=models.PROTECT, null=True, blank=False)

    class Meta:
        db_table = 'conta'
        ordering = ('data_cadastro', )

class TipoCartao(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50, unique=True, null=False)

    class Meta:
        db_table = 'tipo_cartao'
        ordering = ('descricao', )

class Bandeira(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50, unique=True, null=False)

    class Meta:
        db_table = 'bandeira'
        ordering = ('descricao', )

class Cartao(models.Model):
    id = models.AutoField(primary_key=True)
    valor_limite = models.FloatField(null=True, blank=False)
    status_ativo = models.BooleanField(default=True, null=False, blank=True)
    dia_vencimento = models.IntegerField(null=True, blank=False)
    dia_fechamento = models.IntegerField(null=True, blank=False)
    data_cadastro = models.DateTimeField(blank=False, null=True)
    data_atualizacao = models.DateTimeField(blank=False, null=True)
    bandeira = models.ForeignKey(Bandeira, on_delete=models.PROTECT)
    tipo_cartao = models.ForeignKey(TipoCartao, on_delete=models.PROTECT)
    conta = models.ForeignKey(Conta, on_delete=models.PROTECT, null=True)

    class Meta:
        db_table = 'cartao'
        ordering = ('data_cadastro', )

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50, unique=True, null=False)

    class Meta:
        db_table = 'categoria'
        ordering = ('descricao', )

class Movimentacao(models.Model):
    id = models.AutoField(primary_key=True)
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    descricao = models.CharField(max_length=300, null=False)
    data_realizacao = models.DateField(blank=True, null=True)
    data_vencimento = models.DateField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    data_atualizacao = models.DateTimeField(auto_now=True, blank=True, null=True)
    data_pagamento = models.DateField(blank=True, null=True)
    data_previsao = models.DateField(blank=True, null=True)
    parcela_atual = models.IntegerField(blank=True, null=True)
    parcela_total = models.IntegerField(blank=True, null=True)
    status_ativo = models.BooleanField(default=True, blank=True)
    valor_pago = models.FloatField(null=True)
    valor_previsao = models.FloatField(null=False)
    tipo_movimentacao = models.ForeignKey(TipoMovimentacao, on_delete=models.PROTECT, null=False)
    status_movimentacao = models.ForeignKey(StatusMovimentacao, on_delete=models.PROTECT, blank=True)
    endereco_despesa = models.ForeignKey(Endereco, on_delete=models.PROTECT, blank=True, null=True)
    prioridade = models.ForeignKey(PrioridadeMovimentacao, on_delete=models.PROTECT, blank=True, default=int(PrioridadeEnum.NORMAL))
    categoria = models.ForeignKey(Categoria, blank=True, on_delete=models.PROTECT)
    perfil_responsavel = models.ForeignKey(Perfil, on_delete=models.PROTECT, null=True, related_name='responsavel_movimentacao')
    perfil_destinatario = models.ForeignKey(Perfil, on_delete=models.PROTECT, null=True, related_name='destinatario_pagamento')
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.PROTECT, null=True, blank=True)
    conta_origem = models.ForeignKey(Conta, on_delete=models.PROTECT, related_name='conta_origem', blank=True, null=True)
    conta_destino = models.ForeignKey(Conta, on_delete=models.PROTECT, related_name='conta_destino', blank=True, null=True)
    cartao = models.ForeignKey(Cartao, on_delete=models.PROTECT, blank=True, null=True)
    moeda = models.ForeignKey(Moeda, on_delete=models.PROTECT)
    history = HistoricalRecords(custom_model_name='historical_movimentacao')
    grupo_acesso = models.ForeignKey(GrupoAcesso, on_delete=models.PROTECT, null=True, blank=False)
    movimentacao_sheet_id = models.UUIDField(null=True)

    class Meta:
        db_table = 'movimentacao'
        ordering = ('data_atualizacao', )

class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.CharField(max_length=500, null=False)
    data_cadastro = models.DateTimeField(blank=False, null=True)
    data_atualizacao = models.DateTimeField(blank=False, null=True)
    movimentacao = models.ForeignKey(Movimentacao, on_delete=models.PROTECT)
    perfil_responsavel = models.ForeignKey(Perfil, on_delete=models.PROTECT, null=True, related_name='responsavel_comentario')
    history = HistoricalRecords(
        custom_model_name='historical_comentario'
    )

    class Meta:
        db_table = 'comentario'
        ordering = ('data_cadastro', )

class MetaFinanceira(models.Model):
    id = models.AutoField(primary_key=True)
    models.CharField(max_length=500, null=False)
    data_cadastro = models.DateTimeField(blank=False, null=True)
    data_atualizacao = models.DateTimeField(blank=False, null=True)
    data_final = models.DateField(blank=False, null=True)
    valor = models.FloatField(null=True, blank=False)
    perfil_responsavel = models.ForeignKey(Perfil, on_delete=models.PROTECT, null=True, related_name='responsavel_meta')
    categoria = models.ForeignKey(Categoria, blank=True, on_delete=models.PROTECT)

    class Meta:
        db_table = 'meta_financeira'
        ordering = ('data_cadastro', )

class Orcamento(models.Model):
    id = models.AutoField(primary_key=True)
    models.CharField(max_length=500, null=False)
    data_cadastro = models.DateTimeField(blank=False, null=True)
    data_atualizacao = models.DateTimeField(blank=False, null=True)
    data_final = models.DateField(blank=False, null=True)
    valor = models.FloatField(null=True, blank=False)
    perfil_responsavel = models.ForeignKey(Perfil, on_delete=models.PROTECT, null=True, related_name='responsavel_orcamento')
    categoria = models.ForeignKey(Categoria, blank=True, on_delete=models.PROTECT)

    class Meta:
        db_table = 'orcamento'
        ordering = ('data_cadastro', )

class Pagamento(models.Model):
    id = models.AutoField(primary_key=True)
    data_cadastro = models.DateTimeField(blank=False, null=True)
    data_atualizacao = models.DateTimeField(blank=False, null=True)
    conta_origem = models.ForeignKey(Conta, on_delete=models.PROTECT, related_name='conta_origem_pagamento', blank=True, null=True)
    conta_destino = models.ForeignKey(Conta, on_delete=models.PROTECT, related_name='conta_destino_pagamento', blank=True, null=True)
    perfil_responsavel = models.ForeignKey(Perfil, on_delete=models.PROTECT, null=True, related_name='responsavel_pagamento')
    valor_pagamento = models.FloatField(null=True, blank=False)

    class Meta:
        db_table = 'pagamento'
        ordering = ('data_cadastro', )
