# 装饰器实现
def singleton(cls):
    instances = {}
    def w(*args,**kwargs):
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)
        return instances[cls]
    return w
@singleton
class A:
    pass

# __new__方法实现
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance = super(Singleton,cls).__new__(cls,*args,**kwargs)
        return cls._instance

o1 = Singleton()
o2 = Singleton()
print(o1 == o2 )


# 元类实现
class SingletonType(type):
    def __init__(self,*args,**kwargs):
        self._instance = None
        super().__init__(*args,**kwargs)

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__(*args,**kwargs)
        return self._instance

class T(metaclass=SingletonType):
    pass
t1 = T()
t2 = T()
print(t1 == t2)
