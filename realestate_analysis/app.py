"""Real estate Analysis"""
import os

from tp_common import print_header


def load_file(filename):
    return []


def query_data(data):
    return []


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
