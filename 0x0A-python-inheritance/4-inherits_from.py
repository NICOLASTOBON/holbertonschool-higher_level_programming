#!/usr/bin/python3


def inherits_from(obj, a_class):
    """ the object is an instance of a class """
    return isinstance(obj, a_class) and type(obj) != a_class
