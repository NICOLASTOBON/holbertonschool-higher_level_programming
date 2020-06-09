#!/usr/bin/python3
""" Module """
import json


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ json to string """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file """
        if list_objs is None or list_objs == []:
            new_list = []
        else:
            new_list = [item.to_dictionary() for item in list_objs]
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as f:
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        "from json string"
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create """
        from models.rectangle import Rectangle

        new_class = cls(10, 10) if cls is Rectangle else cls(10)
        new_class.update(**dictionary)

        return new_class

    @classmethod
    def load_from_file(cls):
        """ Load from file """
        import os.path
        new_list = []
        file_name = cls.__name__ + ".json"
        if not os.path.isfile(file_name):
            return new_list
        with open(file_name, "r") as f:
            items = cls.from_json_string(f.read())
            for item in items:
                new_list.append(cls.create(**item))
        return new_list
