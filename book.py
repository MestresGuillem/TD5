# -*- coding: utf-8 -*-

"""
Created on Tue Mar 29 00:20:04 2022

@author: gmestres
"""
import pandas as pd

class Book:
    def __init__(self, order):
        self.order = order
        self.buy_orders = list()
        self.sell_orders = list()

    def __str__(self):
        res = "Book on " + self.order + "\n"

        for order in self.sell_orders:
            res += "\t" + str(order) + "\n"

        for order in self.buy_orders:
            res += "\t" + str(order) + "\n"

        return res

    def insert_buy(self, count, price):
        order = Order("BUY", count, price)
        self.buy_orders.append(order)
        self.buy_orders.sort(key=lambda o: int(o.price), reverse=True)

        print("--- Insert BUY " + str(count) + "@" + str(price) + " id=" + str(order.id) + " on " + self.order)

        self.process_orders()

        print(str(self))
        print("------------------------")

    def insert_sell(self, count, price):
        order = Order("SELL", count, price)
        self.sell_orders.append(order)
        self.sell_orders.sort(key=lambda o: int(o.price), reverse=True)

        print("--- Insert SELL " + str(count) + "@" + str(price) + " id=" + str(order.id) + " on " + self.order)

        self.process_orders()

        print(str(self))
        print("------------------------")

    def process_orders(self):
        if len(self.buy_orders) == 0 or len(self.sell_orders) == 0:
            return

        while self.buy_orders[0].price >= self.sell_orders[-1].price:
            sell_order = self.sell_orders[-1]
            buy_order = self.buy_orders[0]

            if sell_order.count == buy_order.count:
                print("Execute " + str(buy_order.count) + " at " + str(buy_order.price) + " on " + self.order)

                self.sell_orders.remove(sell_order)
                self.buy_orders.remove(buy_order)
            elif sell_order.count < buy_order.count:
                print("Execute " + str(sell_order.count) + " at " + str(buy_order.price) + " on " + self.order)

                self.sell_orders.remove(sell_order)

                buy_order.count -= sell_order.count
            else:
                print("Execute " + str(buy_order.count) + " at " + str(buy_order.price) + " on " + self.order)

                self.buy_orders.remove(buy_order)

                sell_order.count -= buy_order.count


class Order:
    i = 1

    def __init__(self, typ, count, price):
        self.typ = typ
        self.count = count
        self.price = price
        self.id = Order.i

        Order.i += 1

    def __str__(self):
        return self.typ + " " + str(self.count) + "@" + str(self.price) + " id=" + str(self.id)

