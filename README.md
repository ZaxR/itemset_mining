# Itemset Mining
<a href="https://pypi.org/project/itemset-mining/"><img src="https://img.shields.io/pypi/dm/itemset-mining?style=for-the-badge" alt="downloads" /></a>  

<a href="https://pypi.org/project/itemset-mining/"><img src="https://img.shields.io/pypi/v/itemset-mining?style=for-the-badge" alt="latest release" /></a>
<a href="https://pypi.org/project/itemset-mining/"><img src="https://img.shields.io/pypi/pyversions/itemset-mining?style=for-the-badge" alt="supported python versions" /></a>
<a href="https://pypi.org/project/itemset-mining/"><img src="https://img.shields.io/pypi/status/itemset-mining?style=for-the-badge" alt="package status" /></a>
<a href="https://github.com/ZaxR/itemset-mining/blob/master/LICENSE"><img src="https://img.shields.io/pypi/l/itemset-mining?style=for-the-badge" alt="license" /></a>

<a href="https://travis-ci.com/ZaxR/itemset_mining"><img src="https://img.shields.io/travis/com/ZaxR/itemset_mining?style=for-the-badge" alt="travis build status" /></a>
<a href="https://itemset_mining.readthedocs.io/en/latest/"><img src="https://img.shields.io/readthedocs/itemset_mining/latest?style=for-the-badge" alt="docs build status" /></a>
<a href="https://codecov.io/gh/ZaxR/itemset_mining"><img src="https://img.shields.io/codecov/c/github/zaxr/itemset_mining?style=for-the-badge" alt="coverage status" /></a>

Implements itemset mining algorithms.

## Algorithms

### High-utility itemset mining (HUIM)
HUIM generalizes the problem of frequent itemset mining (FIM) by considering item values and weights. A popular application of HUIM is to discover all sets of items purchased together by customers that yield a high profit for the retailer. In such a case, item values would show not just that a load of bread is in a basket, but how many there are; and weights would include the profit from a loaf of bread.

More technically, HUIM requires transactions in the transactions "database" to have internal utilities (i.e. item values) associated with each item in each transaction and a "database" of external utilities for each item (i.e. weights).

| Algorithm        | Class                                  | How to Cite |
|------------------|----------------------------------------|-------------|
| [Two-Phase\*][1] | itemset_mining.two_phase_huim.TwoPhase | [Link][2]   |

\* Includes max length support<br>

[1]: <http://cucis.ece.northwestern.edu/publications/pdf/LiuLia05A.pdf> "Two-Phase (2005)"
[2]: <https://link.springer.com/chapter/10.1007/11430919_79#citeas> "Get citation text"

## Roadmap (high to low priority):
- **Address low-correlation HUIs with one of bond, all-confidence, or affinity.** Itemsets that are high utility, but where the items aren't correlated can be misleading for making marketing decisions. E.g. if an itemset of a TV and a pen is a HUI, it's likely just because the TV is expensive, not because it's an interesting pattern.
- **Add *average* utility measure support**, for easier, more intuitive minutil
- **Support discount strategies** via a discount strategy table and upgraded external utilities table.
- **Add top-k HUI support.**
- **Support identifying periodic high utility itemsets.** This allows detection of purchase patterns among high-utility itemsets to allow cross-promotions to customers who buy sets of items periodically.
- **Support items' on-shelf time.** Ignmoring on-shelf time will biat toward items that have more shelf time, since they have more chance to generate higher utility.
- **Allow incremental transaction updates** without rerunning everything.
- **Support concise HUI itemsets, specifically closed form.** This allows the algorithm to be more efficient, only showing longer itemsets, which may be the most interesting ones (correlation issues aside).

### Installation:
```bash
pip install itemset-mining
```

### Example:

```python
    >>> from operator import attrgetter
    >>> from itemset_mining.two_phase_huim import TwoPhase
    >>> transactions = [
    ...     [("Coke 12oz", 6), ("Chips", 2), ("Dip", 1)],
    ...     [("Coke 12oz", 1)],
    ...     [("Coke 12oz", 2), ("Chips", 1), ("Filet Mignon 1lb", 1],
    ...     [("Chips", 1)],
    ...     [("Chips", 2)],
    ...     [("Coke 12oz", 6), ("Chips", 1)]
    ... ]
    >>> # ARP for each item
    >>> external_utilities = {
    ...     "Coke 12oz": 1.29,
    ...     "Chips": 2.99,
    ...     "Dip": 3.49,
    ...     "Filet Mignon 1lb": 22.99
    ... }
    >>> # Minimum dollar value generated by an itemset we care about across all transactions
    >>> minutil = 20.00

    >>> hui = TwoPhase(transactions, external_utilities, minutil)
    >>> result = hui.get_hui()
    >>> sorted(result, key=attrgetter('itemset_utility'), reverse=True)
    ... # doctest: +NORMALIZE_WHITESPACE
    [HUIRecord(items=('Chips', 'Coke 12oz'), itemset_utility=30.02),
     HUIRecord(items=('Chips', 'Coke 12oz', 'Filet Mignon 1lb'), itemset_utility=28.56),
     HUIRecord(items=('Chips', 'Filet Mignon 1lb'), itemset_utility=25.979999999999997),
     HUIRecord(items=('Coke 12oz', 'Filet Mignon 1lb'), itemset_utility=25.57),
     HUIRecord(items=('Filet Mignon 1lb',), itemset_utility=22.99),
     HUIRecord(items=('Chips',), itemset_utility=20.93)]

```
