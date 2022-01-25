from api.domain.enums.categoria_enum import CategoriaEnum


class CategoriaSwitch:

    def convert_from_sheet(self, var):
        return {
            'Alimentação': int(CategoriaEnum.ALIMENTACAO),
            'Educação': int(CategoriaEnum.EDUCACAO),
            'Lazer': int(CategoriaEnum.LAZER),
            'Transporte': int(CategoriaEnum.TRANSPORTE),
            'Moradia': int(CategoriaEnum.MORADIA),
            'Pets': int(CategoriaEnum.PETS),
            'Saúde': int(CategoriaEnum.SAUDE),
            'Serviços Digitais': int(CategoriaEnum.SERVICOS_DIGITAIS),
            'Investimento': int(CategoriaEnum.INVESTIMENTOS),
            'Impostos': int(CategoriaEnum.IMPOSTOS),
            'Roupas': int(CategoriaEnum.ROUPAS),
            'Salário': int(CategoriaEnum.SALARIO),
            'Bens de consumo': int(CategoriaEnum.BENS_CONSUMO),
            'Serviços financeiros': int(CategoriaEnum.SERVICO_FINANCEIRO),
            'Outros': int(CategoriaEnum.OUTROS),
            'Beleza': int(CategoriaEnum.BELEZA),
            'Comunicação': int(CategoriaEnum.COMUNICACAO),
            'Presente': int(CategoriaEnum.PRESENTE),
            'Doação': int(CategoriaEnum.DOACAO),
            'Lanches e refeições': int(CategoriaEnum.LANCHES_REFEICAO),
            'Utilitários': int(CategoriaEnum.BENS_CONSUMO)
        }.get(var, False)
