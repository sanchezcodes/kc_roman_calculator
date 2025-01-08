from django.db.migrations.operations.base import Operation


def test_create_calculos():
    calculo = Calculo(1, 2, Operation.ADD)
    assert calculo.num_1 == 1
    assert calculo.num_2 == 2
    assert calculo.operation == Operation.ADD
    assert calculo.result == 3

    calculo = Calculo(1, 2, Operation.SUB)
    assert calculo.num_1 == 1
    assert calculo.num_2 == 2
    assert calculo.operation == Operation.SUB
    assert calculo.result == -1