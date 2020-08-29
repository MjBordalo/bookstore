from datetime import  datetime


def compute_price1(d1,d2):
    assert d2>=d1
    return (d2-d1).days