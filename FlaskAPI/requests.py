# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 23:26:32 2020

@author: mosto
"""

import requests
from data_input import data_in


URL = 'http://127.0.0.1:5000/preddict'
headers = {'Content-Type': 'application/json'}
data = {"input":data_in}

r = requests.get(URL,headers=headers,json=data)

r.json()