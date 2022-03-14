from api.models.models import (
    Moeda, TipoMovimentacao, FormaPagamento, StatusMovimentacao, Categoria,
    TipoConta, InstituicaoFinanceira, Bandeira, PrioridadeMovimentacao, Conta, Endereco,
    Movimentacao, Perfil, Comentario, Cartao, MetaFinanceira, Orcamento, GrupoAcesso,
    TipoGrupoAcesso, ParticipanteGrupoAcesso, Fatura
)
from rest_framework import serializers


class MoedaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Moeda
        fields = ('__all__')


class TipoMovimentacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoMovimentacao
        fields = ('__all__')


class FormaPagamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = FormaPagamento
        fields = ('__all__')


class StatusMovimentacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = StatusMovimentacao
        fields = ('__all__')


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ('__all__') 


class TipoContaSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoConta
        fields = ('__all__')


class InstituicaoFinanceiraSerializer(serializers.ModelSerializer):

    class Meta:
        model = InstituicaoFinanceira
        fields = ('__all__')


class BandeiraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bandeira
        fields = ('__all__')


class PrioridadeMovimentacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrioridadeMovimentacao
        fields = ('__all__')

class ContaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conta
        fields = ('__all__')

class EnderecoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Endereco
        fields = ('__all__')


class MovimentacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movimentacao
        fields = ('__all__')

class PerfilSerializer(serializers.ModelSerializer):

    class Meta:
        model = Perfil
        fields = ('__all__')


class ComentarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comentario
        fields = ('__all__')


class CartaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cartao
        fields = ('__all__')


class MetaFinanceiraSerializer(serializers.ModelSerializer):

    class Meta:
        model = MetaFinanceira
        fields = ('__all__')

class OrcamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orcamento
        fields = ('__all__')

class TipoGrupoAcessoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoGrupoAcesso
        fields = ('__all__')

class GrupoAcessoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GrupoAcesso
        fields = ('__all__')

class ParticipanteGrupoAcessoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ParticipanteGrupoAcesso
        fields = ('__all__')

class FaturaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Fatura
        fields = ('__all__')
