from datetime import  datetime,date


def compute_price1(d1,d2):
    # assert d2>=d1
    # assert isinstance(d1, datetime)
    # assert isinstance(d2, datetime)
    if not d2>=d1:
        raise ValueError('d2 must be superior to d1')

    if not isinstance(d1, date) or not isinstance(d2, date):
        raise TypeError('dates must be a date type.')

    return (d2-d1).days


#small test
if __name__ == '__main__':
    d1 = date(2020, 5, 17)
    d_after = date(2020, 5, 25)

    compute_price1(d1, d_after)