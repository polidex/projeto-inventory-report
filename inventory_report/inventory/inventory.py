import json
import csv
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryValidations:
    def get_data(type, list):
        if type == 'simples':
            return SimpleReport.generate(list)

        if type == 'completo':
            return CompleteReport.generate(list)

    def get_archive(path):
        if (path.__contains__('csv')):
            with open(path) as file:
                response = [i for i in csv.DictReader(file)]
                return response
        elif (path.__contains__('json')):
            with open(path) as file:
                response = json.load(file)
                return response
        else:
            tree = ET.parse(path)
            root = tree.getroot()

            response = []
            for child in root:
                product = {}
                for i in child:
                    product[i.tag] = i.text

                response.append(product)
            return response


class Inventory(InventoryValidations):
    def import_data(path, type):
        list = InventoryValidations.get_archive(path)
        report = InventoryValidations.get_data(type, list)
        return report
