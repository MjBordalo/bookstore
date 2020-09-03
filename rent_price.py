from datetime import  datetime,date
from contants import *



def compute_price(d1,d2,tp=BOOK_TYPE_FICCAO):
    '''
    FASE=1:  computes renting price according to delta time
    FASE=2 and 3: computes renting price according to delta time and type of book
    (see project definitions)
    :param d1: date on take
    :param d2: date on return
    :param tp: type  of book ('ficcao', 'romance', 'normal')
    :return:
    '''
    if not d2>=d1:
        raise ValueError('d2 must be superior to d1')

    if not isinstance(d1, date) or not isinstance(d2, date):
        raise TypeError('dates must be a date type.')

    if not isinstance(tp, str) :
        raise TypeError('book type must be a string')

    if tp not in BOOK_TYPES :
        raise ValueError('Invalid book type')

    #compute price according to fase of project
    if  FASE == 1:
        return (d2 - d1).days
    elif FASE == 2:
        if tp == BOOK_TYPE_FICCAO:
            return float((d2 - d1).days * 3)
        else:
            return float((d2 - d1).days * 1.5)
    elif FASE == 3:
        if tp == BOOK_TYPE_FICCAO:
            return float( (d2-d1).days * 3)
        else:
            #romance & normal
            price = 2 + max(0,(d2-d1).days -2 )*1.5 #durante os primeiros 2 dias, será cobrado 1 euro por dia e 1,5 euros depois disso.O valor mínimo será de 2 euros se
            return float ( price)
    else:
        raise ValueError('Invalid FASE.')


#small test
if __name__ == '__main__':
    d1 = date(2020, 5, 17)
    d_after = date(2020, 5, 25)

    print(compute_price(d1, d_after))
    print(compute_price(d1, d_after,'ficcao'))

