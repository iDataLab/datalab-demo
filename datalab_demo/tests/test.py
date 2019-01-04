#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is the test module.

"""

#:Demo variable
demoVar = "Hello World!"

def demo_add_func(num1, num2):
    """
    This function is to add 2 numbers and return the result
    :param num1: Number 1
    :param num2: Number 2
    :return: Result of the input 2 numbers
    """
    return num1+num2


class DemoPersonClass(object):
    """
    This Class is a demo class which describe a Person class.
    """

    def __init__(self, name=None, age=25):
        """
        This is the constructure fucntion used to create the object by passing necessary parameters.

        :param name: Person name
        :param age:  Person age
        """
        self.name = name
        self.age = age

    def show_name(self):
        """
        Show person name.
        :return: No returned
        """
        print(self.name)

    def show_age(self):
        """
        Show person age.
        :return: No returned
        """
        print(self.age)

if __name__=="__main__":
    per = DemoPersonClass(name="David", age=28)
    per.show_name()
    per.show_age()