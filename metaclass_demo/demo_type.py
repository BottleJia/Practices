
# https://realpython.com/python-metaclasses/
"""
Example 1
通过 type() 定义类
"""

Foo = type('Foo', (), {})
x = Foo()
print(x)  # <__main__.Foo object at 0x000001706EB56668>


class Foo:
    pass


x = Foo()
print(x)  # <__main__.Foo object at 0x0000016C4EFC19E8>

"""
Example 2
通过 type() 定义类并指定继承的父类
"""

Bar = type('Bar', (Foo,), dict(attr=100))
x = Bar()
print(x.attr)  # 100


class Bar(Foo):
    attr = 100


x = Bar()
print(x.attr)  # 100
print(x.__class__)  # <class '__main__.Bar'>
print(x.__class__.__bases__)  # (<class '__main__.Foo'>,)

"""
Example 3
通过 type() 定义类并添加类属性和类方法(通过lambda简单定义的函数)
"""
Foo = type('Foo', (), {'attr': 100, 'attr_val': lambda y: y.attr})
x = Foo()
print(x.attr)  # 100
print(x.attr_val())  # 100


class Foo:
    attr = 100

    def attr_val(self):
        return self.attr


x = Foo()
print(x.attr)  # 100
print(x.attr_val())  # 100

"""
Example 4
通过 type() 定义类并添加类属性和类方法, 
并且类方法是一个外部定义的稍微复杂一些的函数，然后命名空间字典中通过名称f赋值给attr_val
"""


def f(obj):
    print('attr =', obj.attr)


Foo = type('Foo', (), {'attr': 100, 'attr_val': f})
x = Foo()
x.attr_val()  # attr = 100
print(x.attr)  # 1


class Foo:
    attr = 100
    attr_val = f


x = Foo()
x.attr_val()  # attr = 100
print(x.attr)  # 100

