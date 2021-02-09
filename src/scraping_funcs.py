# Import Modules
import numpy as np
import copy
import pandas as pd
from itertools import count
import time
import lxml
import html
import json
import requests
import requests_html as reqHTML
import urllib.parse as urllib
from bs4 import BeautifulSoup
from pprint import pprint

    


def construct_sephora_req(search_term:str='moisturizer', page_num:int=1) -> dict:
    '''Given the category, page number and meta data, constructs page link for use with requests.get
        
        Use in conjunction with async scraping functions
        Default set to moisturizers
    '''
    res = {}
    # Construct link
    base_link = 'https://www.sephora.com/api/catalog/search?'
    payload = {
    'type' : 'keyword',
    'q' : search_term,
    'currentPage' : page_num
    }
    
    # Add results to res to use as kwarg
    res['url'] = base_link
    res['params'] = payload 

    return res


def get_api_json(req_params:dict, return_json:bool=True) -> dict:
    '''Given the 
    '''
    res = None
    # Check link
    if req_params:
        try:
            response = requests.get(**req_params)
            res = response.json() if return_json else response
        except requests.exceptions.RequestException as e:
            print(e)
        
    return res


async def get_page_html(page_link:str='', html_element:bool=True) -> lxml.html.Element:
    '''Given the URL of a JS rendered webpage, function will return the raw html from page in bytes format
    
        Must use 'await' command with function, setting html_element to True will return html.Element object, otherwise will return html page in bytes
    '''
    res = None
    # Check link
    if page_link:
        try:
            # Start Session
            asession = reqHTML.AsyncHTMLSession()
            # Request Page
            r = await asession.get(page_link, headers={'User-Agent': 'Mozilla/5.0'})
            await r.html.arender()
            res = lxml.html.fromstring(r.html.raw_html) if html_element else r
        except requests.exceptions.RequestException as e:
            print(e)
        
    return res

def get_pagnation_num(html_page:lxml.html.Element, pagnation_xpath:str=None) -> int:
    '''Given the html.Element object returned from get_page_html, returns max pagnation for product category'''
    res = None
    if not pagnation_xpath:
        # Set default pagnation xpath for sephora.com 
        pagnation_xpath = '/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/main/div[3]/div/div[3]/div[2]/nav/ul/li[6]/button'
    
    try:
        element_list = html_page.xpath(pagnation_xpath)
        if element_list:
            res = int(element_list[0].text)
    except:
        pass
    return res
    
    