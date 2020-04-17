#!/usr/local/bin/python3
# encoding:utf-8
import execjs
from other_tools.n_javascrpit import JS_GET_SIGN

def get_sign(key:str):
    """Get the keyValue : sign for BaiduTranslation
    
    Arguments:
        key {str} -- The keyWord you want to translate
    
    Returns:
        str -- the signVale
    """
    js = execjs.compile(JS_GET_SIGN)
    sign = js.call("e",key)  
    return sign




