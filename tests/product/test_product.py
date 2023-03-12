from inventory_report.inventory.product import Product


def test_cria_produto():
    productMock = Product(
        1,
        'CADEIRA',
        'Forces of Nature',
        '2022-04-04',
        '2023-02-09',
        'FR48',
        'Conservar em local fresco'
    )

    assert productMock.id == 1
    assert productMock.nome_do_produto == 'CADEIRA'
    assert productMock.nome_da_empresa == 'Forces of Nature'
    assert productMock.data_de_fabricacao == '2022-04-04'
    assert productMock.data_de_validade == '2023-02-09'
    assert productMock.numero_de_serie == 'FR48'
    assert productMock.instrucoes_de_armazenamento == 'Local fresco'
