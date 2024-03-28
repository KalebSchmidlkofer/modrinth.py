#!/usr/bin/env python3
# -*- coding: utf8 -*-
'''
Developed by Kaleb Schmidlkofer <kaleb@ashbyte.com>
An Unofficial modrinth api wrapper for python
'''

import requests

__version__ = '0.0.1'

class modrinth:
  async def __init__(self, apiServer:str='https://api.modrinth.com/v2/'):
    self.apiServer=apiServer
    
  async def modData(self, ):
    data = requests.get(f'{self.apiServer}')
    self.apiServer





