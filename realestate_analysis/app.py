"""Real estate Analysis"""
import csv
import os

try:
    import statistics
except ImportError:
    import realestate_analysis.statistics_standin_py2 as statistics

from realestate_analysis.data_types import Purchase
from tp_common import print_header


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        purchases = []
        reader = csv.DictReader(fin)

        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

    return purchases


# def load_file_simple(filename):
#     with open(filename, 'r', encoding='utf-8') as fin:
#         header = fin.readline().strip()
#         print('header: ' + header)
#
#         lines = []
#         for line in fin:
#             line_data = line.strip().split(',')
#             lines.append(line_data)
#
#         print(lines[:5])


def announce(item, msg):
    print("Pulling item {} for {}".format(item, msg))
    return item


def query_data(data):
    # Sort by price
    data.sort(key=lambda p: p.price)

    high_purchase = data[-1]
    print("The most expensive house is ${:,} with {} beds and {} baths".format(
        high_purchase.price, high_purchase.beds, high_purchase.baths
    ))

    low_purchase = data[0]
    print("The least expensive house is ${:,} with {} beds and {} baths".format(
        low_purchase.price, low_purchase.beds, low_purchase.baths
    ))

    # Average price house?
    prices = []
    [prices.append(pur.price) for pur in data]

    avg_price = statistics.mean(prices)
    print("The average price for a home is ${:,}".format(int(avg_price)))

    # Average price of 2 bedroom homes
    # List comprehension
    # two_bed_homes = [
    #     pur  # projection or items
    #     for pur in data  # the set to process
    #     if pur.beds == 2  # test /condition
    # ]

    # Generator expression
    two_bed_homes = (
        pur  # projection or items
        for pur in data  # the set to process
        if announce(pur, '2-bedrooms, found {}'.format(pur.beds)) and
           pur.beds == 2  # test /condition
    )

    # avg_price = statistics.mean(p.price, for p in two_bed_homes)
    # avg_baths = statistics.mean(p.baths for p in two_bed_homes)
    # avg_sqft = statistics.mean(p.sq__ft for p in two_bed_homes)

    homes = []

    for h in two_bed_homes:
        if len(homes) > 5:
            break
        homes.append(h)

    avg_price = statistics.mean((announce(p.price, 'price') for p in homes))
    avg_baths = statistics.mean((p.baths for p in homes))
    avg_sqft = statistics.mean((p.sq__ft for p in homes))

    print("The average 2 bedroom-home is ${:,}, baths={}, sq ft={:,}".format(
        int(avg_price), round(avg_baths, 1), round(avg_sqft, 1)))


def main():
    print_header('Real Estate Data Miner')
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data',
                        'SacramentoRealEstateTransactions2008.csv')


if __name__ == '__main__':
    main()
