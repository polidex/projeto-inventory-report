from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(products):
        data_de_fabricacao = min([p['data_de_fabricacao'] for p in products])
        data_atual = datetime.now().date()
        data_de_validade = min([p['data_de_validade'] for p in products
                                if datetime
                                .fromisoformat(p['data_de_validade'])
                                .date() >= data_atual])
        empresas = {}
        for p in products:
            if p['nome_da_empresa'] in empresas:
                empresas[p['nome_da_empresa']] += 1
            else:
                empresas[p['nome_da_empresa']] = 1
            empresa_com_mais_produtos = max(empresas, key=empresas.get)

        return (
            'Data de fabricação mais antiga: {}\n'
            'Data de validade mais próxima: {}\n'
            'Empresa com mais produtos: {}'
        ).format(data_de_fabricacao, data_de_validade,
                 empresa_com_mais_produtos)
