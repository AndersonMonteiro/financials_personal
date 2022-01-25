import gspread
from oauth2client.service_account import ServiceAccountCredentials


class MovimentacaoSheetProvider:
    def __init__(self):
        file_name = 'creds.json'

        scope = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file']

        creds = ServiceAccountCredentials.from_json_keyfile_name(file_name, scope)

        client = gspread.authorize(creds)
        self.sheet = client.open('Controle Financeiro Familiar').get_worksheet(0)

    def consulta_movimentacoes(self):
        sheet_records = self.sheet.get_all_records()

        return sheet_records

    def atualiza_movimentacao_sheet(self, movimentacao_id, movimentacao):
        # consulta localização da celula

        self.sheet.update_cell(3, 3, 'N')
        pass

    def cadastra_movimentacao_sheet(self, movimentacao):
        row = ''
        self.sheet.insert_row(row, "i")
        pass
