from api.domain.enums.centro_custo_enum import CentroCustoEnum


class CentroCustoSwitch:
    def convert_from_sheet(self, var):
        var_normalized = str(var).lower()
        
        return {
            'familiar': int(CentroCustoEnum.FAMILIAR),
            'pede mais': int(CentroCustoEnum.PEDE_MAIS)
        }.get(var_normalized, False)
