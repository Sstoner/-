from abc  import ABC,abstractclassmethod,ABCMeta
from  collections import  namedtuple

Customer =namedtuple("Customer","name fidelity")

class LineItem:

    def __init__(self,product,quantity,price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, "__total"):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)    #传入self
        return self.total() - discount

    def __repr__(self):
        fmt = "<Order total: {:.2f} due: {:.2f}>"
        return fmt.format(self.total(),self.due())

#优雅的写法
class Promotion(metaclass=ABCMeta):
    #__metaclass__ = ABCMeta
    @abstractclassmethod
    def discount(self,order):
        """返回折扣金额"""

class FidelityPromo(object):
    """为积分为1000或以上的顾客提供5%折扣"""
    def discount(self,order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0

class BulkItemPromo(object):
    """为单个商品为20个或以上时提供10%折扣"""
    def discount(self,order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount

class LargeOrderPromo(object):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    def discount(self,order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0

Promotion.register(FidelityPromo)
Promotion.register(BulkItemPromo)
Promotion.register(LargeOrderPromo)

#print(issubclass(FidelityPromo,Promotion))

'''
class Promotion(ABC):

    @abstractclassmethod
    def discount(self,order):
        """返回折扣金额"""

class FidelityPromo(Promotion):
    """为积分为1000或以上的顾客提供5%折扣"""
    def discount(self,order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    """为单个商品为20个或以上时提供10%折扣"""
    def discount(self,order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount

class LargeOrderPromo(Promotion):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    def discount(self,order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0
'''

vance = Customer("Vance Li",0)
ariel = Customer("Ariel Zeng",1100)
cart = [LineItem('apple',20,5),
        LineItem('peal',15,3),
        LineItem('orange',30,10)]

#get best discount
promos = [FidelityPromo,BulkItemPromo,LargeOrderPromo]
def best_promo(order):
    #for promo in promos:
    #    Order(vance,cart,promo)
    return max(promo().discount(order) for promo in promos)

print(best_promo(Order(vance,cart)))
