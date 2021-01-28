# Import Modules
import numpy as np
import copy
import pandas as pd
from lxml import html, etree
import json
import requests
import requests_html as reqHTML
from bs4 import BeautifulSoup
from pprint import pprint


def get_pagnation(category:str) -> int:
    '''Given a category for a product on sephora.com, will return the number of pages relavent to the products'''
    res = None
    base_link = f'https://www.sephora.com/shop/{category}'    
    pagnation_xpath = '/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/main/div[3]/div/div[3]/div[2]/nav'
    
    return res
    


def get_product_links(category:str, page_num:int, return_str:bool=True) -> dict:
    '''Given a category for a product catalog, function will collect relavent links for each product. Designed specifically for use on sephora.com. Will return response object return_str set to False'''
    # Construct link
    base_link = f'https://www.sephora.com/shop/{category}'    
    cur_page = f'?currentPage={page_num}' if page_num > 1 else ''
    full_link = f'{base_link}{cur_page}'
    # Start Session
    session = reqHTML.AsyncHTMLSession()
    # Request Page
    r = session.get(full_link)
    # Render Content
    page = r.html.render()
    
    
    return html.fromstring(page.content) if return_str else page