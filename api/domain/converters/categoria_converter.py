from api.domain.enums.categoria_enum import CategoriaEnum


class CategoriaSwitch:

    def convert_from_sheet(self, var):
        var_normalized = str(var).lower()
        return {
            'alimentação': int(CategoriaEnum.ALIMENTACAO),
            'educação': int(CategoriaEnum.EDUCACAO),
            'lazer': int(CategoriaEnum.LAZER),
            'transporte': int(CategoriaEnum.TRANSPORTE),
            'moradia': int(CategoriaEnum.MORADIA),
            'pets': int(CategoriaEnum.PETS),
            'saúde': int(CategoriaEnum.SAUDE),
            'serviços digitais': int(CategoriaEnum.SERVICOS_DIGITAIS),
            'investimento': int(CategoriaEnum.INVESTIMENTOS),
            'impostos': int(CategoriaEnum.IMPOSTOS),
            'roupas': int(CategoriaEnum.ROUPAS),
            'salário': int(CategoriaEnum.SALARIO),
            'bens de consumo': int(CategoriaEnum.BENS_CONSUMO),
            'serviços financeiros': int(CategoriaEnum.SERVICO_FINANCEIRO),
            'outros': int(CategoriaEnum.OUTROS),
            'beleza': int(CategoriaEnum.BELEZA),
            'comunicação': int(CategoriaEnum.COMUNICACAO),
            'presente': int(CategoriaEnum.PRESENTE),
            'doação': int(CategoriaEnum.DOACAO),
            'lanches e refeições': int(CategoriaEnum.LANCHES_REFEICAO),
            'utilitários': int(CategoriaEnum.BENS_CONSUMO)
        }.get(var_normalized, False)
