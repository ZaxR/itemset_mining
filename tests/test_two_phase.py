from itemset_mining.two_phase_huim import HUIRecord, TwoPhase


def test_two_phase():
    transactions = [
        [("Coke 12oz", 6), ("Chips", 2), ("Dip", 1)],
        [("Coke 12oz", 1)],
        [("Coke 12oz", 2), ("Chips", 1)],
        [("Chips", 1)],
        [("Chips", 2)],
        [("Coke 12oz", 6), ("Chips", 1)]
    ]

    external_utilities = {
        "Coke 12oz": 1.29,
        "Chips": 2.99,
        "Dip": 3.49
    }

    minutil = 20.00

    hui = TwoPhase(transactions, external_utilities, minutil)
    result = list(hui.get_hui())
    expected = [
        HUIRecord(items=frozenset({'Chips'}), itemset_utility=20.93),
        HUIRecord(items=frozenset({'Chips', 'Coke 12oz'}), itemset_utility=30.02)
    ]

    assert result == expected
