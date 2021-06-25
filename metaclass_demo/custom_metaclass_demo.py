class Foo:
    pass


def new(cls):
    x = object.__new__(cls)
    x.attr = 100
    return x


Foo.__new__ = new

f = Foo()
print(f.attr)  # 100

g = Foo()
print(g.attr)  # 100

"""
Object Factory
"""


class Foo:
    def __init__(self):
        self.attr = 100


x = Foo()
print(x.attr)  # 100
y = Foo()
print(y.attr)  # 100
z = Foo()
print(z.attr)  # 100

"""
class Factory
"""


class Meta(type):
    def __init__(cls, name, bases, dct):
        cls.attr = 100


class X(metaclass=Meta):
    pass


print(X.attr)  # 100


class Y(metaclass=Meta):
    pass


print(Y.attr)  # 100


class Z(metaclass=Meta):
    pass


print(Y.attr)  # 100

"""
简单的继承也可以实现上述的效果
"""


class Base:
    attr = 100


class X(Base):
    pass


print(X.attr)  # 100


class Y(Base):
    pass


print(Y.attr)  # 100


class Z(Base):
    pass


print(Y.attr)  # 100

"""
或者类的装饰器
"""


def decorator(cls):
    class NewClass(cls):
        attr = 100

    return NewClass


@decorator
class X:
    pass


print(X.attr)  # 100


@decorator
class Y:
    pass


print(Y.attr)  # 100


@decorator
class Z:
    pass


print(Y.attr)  # 100
