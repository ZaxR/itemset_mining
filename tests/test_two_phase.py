import pytest
from pytest_cases import fixture_ref, parametrize_plus

from itemset_mining.two_phase_huim import HUIRecord, TwoPhase


@pytest.fixture(scope='module')
def transactions_list():
    return [
        [("Coke 12oz", 6), ("Chips", 2), ("Dip", 1)],
        [("Coke 12oz", 1)],
        [("Coke 12oz", 2), ("Chips", 1)],
        [("Chips", 1)],
        [("Chips", 2)],
        [("Coke 12oz", 6), ("Chips", 1)]
    ]


@pytest.yield_fixture(scope='module')
def transactions_generator(transactions_list):
    return (t for t in transactions_list)


@pytest.fixture(scope='module')
def external_utilities():
    return {
        "Coke 12oz": 1.29,
        "Chips": 2.99,
        "Dip": 3.49
    }


@parametrize_plus("transactions, ext_utilities",
                  [
                      (fixture_ref(transactions_list), fixture_ref(external_utilities)),
                      (fixture_ref(transactions_generator), fixture_ref(external_utilities))
                  ]
                  )
def test_two_phase(transactions, ext_utilities):

    minutil = 20.00

    hui = TwoPhase(transactions, ext_utilities, minutil)
    result = list(hui.get_hui())
    expected = [
        HUIRecord(items=('Chips',), itemset_utility=20.93),
        HUIRecord(items=('Chips', 'Coke 12oz'), itemset_utility=30.02)
    ]

    assert result == expected
