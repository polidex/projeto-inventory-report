import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():
    def import_data(path, type):
        with open(path) as file:
            list = [item for item in csv.DictReader(file)]

        if type == 'simples':
            return SimpleReport.generate(list)

        if type == 'completo':
            return CompleteReport.generate(list)
