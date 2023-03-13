from importer import Importer


class ImportXml(Importer):
    @classmethod
    def Import_data(cls, path):
        type_xml = '.xml'
        if type_xml not in path:
            raise ValueError('Arquivo inválido')
