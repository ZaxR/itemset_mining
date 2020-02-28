# High-Utility Itemset Mining
Implements high-utility itemset mining algorithms.

## Currently implemented algorithms:
- Two-Phase  
  Liu Y., Liao W., Choudhary A. (2005) A Two-Phase Algorithm for Fast Discovery of High Utility Itemsets. In: Ho T.B., Cheung D., Liu H. (eds) Advances in Knowledge Discovery and Data Mining. PAKDD 2005. Lecture Notes in Computer Science, vol 3518. Springer, Berlin, Heidelberg  
  Link: http://cucis.ece.northwestern.edu/publications/pdf/LiuLia05A.pdf

## Roadmap (high to low priority):
- **Address low-correlation HUIs with one of bond, all-confidence, or affinity.** Itemsets that are high utility, but where the items aren't correlated can be misleading for making marketing decisions. E.g. if an itemset of a TV and a pen is a HUI, it's likely just because the TV is expensive, not because it's an interesting pattern.
- **Add *average* utility measure support**, for easier, more intuitive minutil
- **Support discount strategies** via a discount strategy table and upgraded external utilities table.
- **Add top-k HUI support.**
- **Support identifying periodic high utility itemsets.** This allows detection of purchase patterns among high-utility itemsets to allow cross-promotions to customers who buy sets of items periodically.
- **Support items' on-shelf time.** Ignmoring on-shelf time will biat toward items that have more shelf time, since they have more chance to generate higher utility.
- **Allow incremental transaction updates** without rerunning everything.
- **Support concise HUI itemsets, specifically closed form.** This allows the algorithm to be more efficient, only showing longer itemsets, which may be the most interesting ones (correlation issues aside).


### Example:

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
