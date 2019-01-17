
def mean(data):
    """
    Simple method to calculate the mean of a collection
    :param data: Collection to work on
    """
    total = 0
    count = 0

    for x in data:
        count += 1
        total += x

    return total / max(1, count)