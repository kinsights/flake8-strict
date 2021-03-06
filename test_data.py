def f1(a,  # S100
       b):  # S101
    pass


def f2(
    a,
    b  # S101
):
    pass


def f3(
    a,
    b,
):
    pass


# trailing comma after *args or **kwargs is a syntax error therefore
# we don't want to enforce it such situations


def f4(
    a,
    *args
):
    pass


def f5(
    b,
    **kwargs
):
    pass

def f6(
    *,
    d
):
    pass


f3(1,  # S100
   2)  # S101

f3(
    1,
    2)  # S101

f3(
    1,
    2  # S101
)

f3(
    1,
    2,
)

kwargs = {}

f5('-o',  # S100
   some_keyword_argument='./')  # S101

f5(
    b='something',
)

(
    ''.
    format())
