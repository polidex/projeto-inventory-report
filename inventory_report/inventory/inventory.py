import json
import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():
    def import_data(path, type):
        if (path.__contains__('csv')):
            with open(path) as file:
                list = [item for item in csv.DictReader(file)]
        elif (path.__contains__('json')):
            with open(path) as file:
                list = json.load(file)

        if type == 'simples':
            return SimpleReport.generate(list)

        if type == 'completo':
            return CompleteReport.generate(list)
