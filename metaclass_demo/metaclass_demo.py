#!/usr/bin/python3
"""
使用metaclass自由的、动态的修改/增加/删除 类的或者实例中的方法或者属性
"""


def ma(cls):
    print("method a")


def mb(cls):
    print("method b")


method_dict = {
    "ma": ma,
    "mb": mb
}


class DynamicMethod(type):
    def __new__(cls, name, bases, dct):
        if name[:3] == 'Abc':
            dct.update(method_dict)
        return type.__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        super(DynamicMethod, cls).__init__(name, bases, dct)


class AbcTest(metaclass=DynamicMethod):

    def mc(self, x):
        print(x * 3)


class NotAbc(metaclass=DynamicMethod):

    def md(self, x):
        print(x * 4)


def main1():
    a = AbcTest()
    a.mc(3)
    a.ma()
    print(dir(a))

    b = NotAbc()
    print(dir(b))


"""
批量的对某些方法使用decorator
"""
from types import FunctionType


def login_required(func):
    print("login check logic here")
    return func


class LoginDecorator(type):
    def __new__(cls, name, bases, dct):
        for name, value in dct.items():
            if name not in ('__metaclass__', '__init__', '__module__') and type(value) == FunctionType:
                value = login_required(value)

            dct[name] = value
        return type.__new__(cls, name, bases, dct)


class Operation(metaclass=LoginDecorator):
    def delete(self, x):
        print("delete %s" % str(x))


def main2():
    op = Operation()
    op.delete('test')  # login check logic here  delete test


"""
当引入地第三方库的时候，如果该库某些类需要patch的时候可以使用metaclass
"""


def monkey_patch(name, bases, dct):
    """
    name : PatchA
    bases: <class '__main__.A'>
    dct： {
        "__module__":"__main__",
        "__qualanme__":"PathcA",
        "patcha_method":<function PatchA.patch_method at 0x00000002385724F268>
    }
    """
    assert len(bases) == 1
    base = bases[0]
    for name, value in dct.items():
        if name not in ('__module__', '__metaclass__'):
            setattr(base, name, value)
    return base


class A(object):
    def a(self):
        print('i am A object')


class PatchA(A, metaclass=monkey_patch):

    def patcha_method(self):
        print('this is a method patched for class A')


def main3():
    pa = PatchA()
    pa.patcha_method()
    pa.a()
    print(dir(pa))
    print(dir(PatchA))


if __name__ == '__main__':
    main3()
