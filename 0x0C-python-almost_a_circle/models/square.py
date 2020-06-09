#!/usr/bin/python3
""" Modules """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ initial """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ property """
        return self.width

    @size.setter
    def size(self, size):
        """ setter """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ Update """
        if args:
            attr = ["id", "size", "x", "y"]
            for idx, value in enumerate(args):
                setattr(self, attr[idx], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """ dictionary """
        new_dict = {}
        for key, value in vars(self).items():

            if key == "_Rectangle__width":
                new_dict["size"] = value
            elif key == "_Rectangle__height":
                continue
            else:
                new_dict[key.split('_')[-1]] = value
        return new_dict

    def __str__(self):
        """ str """
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
        )
