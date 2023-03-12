from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        data = super().generate(products)
        company = Counter(row['nome_da_empresa'] for row in products)
        stock = ''
        for key, value in company.items():
            stock += f'- {key}: {value}\n'
        return (data + '\n' + 'Produtos estocados por empresa:\n{}'
                ).format(stock)
