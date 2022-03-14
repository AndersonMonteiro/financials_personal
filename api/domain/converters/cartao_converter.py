class CartaoSwitch:

    def convert_from_sheet(self, var):
        var_normalized = str(var).lower()

        return {
            'nubank master - anderson': 1,
            'santander master - maellidda': 2,
            'inter master - anderson': 3,
            'nubank master - maellidda': 4,
            'pan - anderson': 5,
            'inter pf - maellidda': 6,
            'inter pj - maellidda': 7,
            'inter pj - anderson': 8,
            'c6 anderson': 9
        }.get(var_normalized, False)
