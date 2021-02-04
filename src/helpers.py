import re


def strip_unicode(string:str) -> str:
    '''Given a string contaning unicode characters, removes all instances of unicode'''
    res = re.sub(r'[^\x00-\x7F]+','', string)
    return res