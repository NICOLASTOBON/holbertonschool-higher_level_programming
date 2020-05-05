#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_str = []
    tuple_str.append(len(sentence))
    if bool(sentence) is False:
        tuple_str.append(None)
        return tuple(tuple_str)
    else:
        tuple_str.append(sentence[0])
        return tuple(tuple_str)
