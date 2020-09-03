from datetime import  datetime,date
from contants import *

def compute_price1(d1,d2):
    # assert d2>=d1
    # assert isinstance(d1, datetime)
    # assert isinstance(d2, datetime)
    if not d2>=d1:
        raise ValueError('d2 must be superior to d1')

    if not isinstance(d1, date) or not isinstance(d2, date):
        raise TypeError('dates must be a date type.')

    return (d2-d1).days

def compute_price2(d1,d2,tp):
    '''
    computes renting price according to delta time and type of book
    :param d1: date on take
    :param d2: date on return
    :param tp: type  of book ('ficcao', 'romance', 'normal')
    :return:
    '''
    # assert d2>=d1
    # assert isinstance(d1, datetime)
    # assert isinstance(d2, datetime)
    if not d2>=d1:
        raise ValueError('d2 must be superior to d1')

    if not isinstance(d1, date) or not isinstance(d2, date):
        raise TypeError('dates must be a date type.')

    if not isinstance(tp, str) :
        raise TypeError('book type must be a string')

    if tp not in BOOK_TYPES :
        raise ValueError('Invalid book type')

    if tp == BOOK_TYPE_FICCAO:
        return float( (d2-d1).days * 3)
    else:
        return float ( (d2-d1).days * 1.5)


#small test
if __name__ == '__main__':
    d1 = date(2020, 5, 17)
    d_after = date(2020, 5, 25)

    print(compute_price1(d1, d_after))
    print(compute_price2(d1, d_after,'ficcao'))

