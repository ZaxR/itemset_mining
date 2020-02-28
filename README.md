Implements high-utility itemset mining algorithms.

Currently implemented algorithms:
- Two-Phase  
  Liu Y., Liao W., Choudhary A. (2005) A Two-Phase Algorithm for Fast Discovery of High Utility Itemsets. In: Ho T.B., Cheung D., Liu H. (eds) Advances in Knowledge Discovery and Data Mining. PAKDD 2005. Lecture Notes in Computer Science, vol 3518. Springer, Berlin, Heidelberg  
  Link: http://cucis.ece.northwestern.edu/publications/pdf/LiuLia05A.pdf

Example:

```python
    >>> from operator import attrgetter

    >>> transactions = [
            [("Coke 12oz", 6), ("Chips", 2), ("Dip", 1)],
            [("Coke 12oz", 1)],
            [("Coke 12oz", 2), ("Chips", 1)],
            [("Chips", 1)],
            [("Chips", 2)],
            [("Coke 12oz", 6), ("Chips", 1)]
        ]

    >>> # ARP for each item
    >>> external_utilities = {
            "Coke 12oz": 1.29,
            "Chips": 2.99,
            "Dip": 3.49
        }

    >>> # Minimum dollar value generated by an itemset we care about across all transactions
    >>> minutil = 20.00

    >>> hui = TwoPhase(transactions, external_utilities, minutil)
    >>> result = hui.get_hui()
    >>> # Default order of results is Alphabetically by length ascending for the itemset.
    >>> # However, it may be more desirable to rank based on utility descending, as below
    >>> sorted(result, key=attrgetter('twu'), reverse=True)
    [HUIRecord(items=frozenset({'Chips'}), twu=42.480000000000004),
     HUIRecord(items=frozenset({'Coke 12oz'}), twu=34.8),
     HUIRecord(items=frozenset({'Chips', 'Coke 12oz'}), twu=33.510000000000005)]

```
