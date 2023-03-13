from importer import Importer


class ImportJson(Importer):
    @classmethod
    def Import_data(cls, path):
        type_json = '.json'
        if type_json not in path:
            raise ValueError('Arquivo inválido')
