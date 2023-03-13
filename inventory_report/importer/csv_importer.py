import csv
from importer import Importer


class ImportCSV(Importer):
    @classmethod
    def import_data(cls, path):
        type_csv = '.csv'
        if type_csv not in path:
            raise ValueError('Arquivo inválido')

        with open(path) as file:
            report = [i for i in csv.DictReader(file)]

        return report
