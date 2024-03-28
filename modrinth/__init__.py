#!/usr/bin/env python3
# -*- coding: utf8 -*-
'''
Developed by Kaleb Schmidlkofer <kaleb@ashbyte.com>
An Unofficial modrinth api wrapper for python
'''

import requests
from requests.exceptions import HTTPError
import asyncio
from loguru import logger
import sys
from urllib.parse import urlparse, urlsplit
import os
def debug_init(trace, debug):
    logger.remove()
    if debug:
        logger.add(sys.stderr, level='DEBUG')
    elif trace:
        logger.add(sys.stderr, level='TRACE')
    else:
        logger.add(sys.stderr, level='INFO')
        pass
    pass

debug_init(False, False)

__version__ = '2.0.0-alpha'
headers = {'User-Agent': f'KalebSchmidlkofer/modrinth.py/{__version__} (kaleb@ashbyte.com)'}



class Users:
  pass



statusEnum=["approved", "archived", "rejected", "draft", "unlisted", "processing", "withheld", "scheduled", "private", "unknown"]
class modrinthProjects:
  def __init__(self, modid):
    self.modid = modid
    self.data = self._Data()
    # self.utils = self._Utils()
  
  async def request_data(self):
    await self.data.request(self.modid)
    
  
  
  
  
  class _Data:
    
    def __init__(self, apiRoute:str='https://api.modrinth.com/v2/project/'):
      self.apiRoute=apiRoute
    
    async def _requestData(self):
      parsed_url=urlparse(self.modID)
      parsed_url=os.path.basename(parsed_url.path)
      r = requests.get(f'{self.apiRoute}{parsed_url}', headers=headers)
      if r.status_code == 200:
        return r.json()
      else:
        logger.error(f'Error: An error occured and no project was found! status Code:{r.status_code}')
        raise HTTPError('Got a 404 or something similar when trying to access url')
      
    async def _parseData(self) -> None:
      data = await self._requestData()
      self.clientSide = data['client_side']
      self.serverSide = data['server_side']
      self.gameVersions = data['game_versions']
      self.id = data['id']
      self.slug = data['slug']
      self.projectType = data['project_type']
      self.team = data['team']
      self.organization = data['organization']
      self.title = data['title']
      self.description = data['description']
      self.body = data['body']
      self.published = data['published']
      self.updated = data['updated']
      self.approved = data['approved']
      self.queued = data['queued']
      self.status = data['status']
      self.requestedStatus = data['requested_status']
      self.moderatorMessage = data['moderator_message']
      self.license = data['license']
      self.downloads = data['downloads']
      self.followers = data['followers']
      self.categories = data['categories']
      self.additionalCategories = data['additional_categories']
      self.loaders = data['loaders']
      self.versions = data['versions']
      self.icon_url = data['icon_url']
      self.issues_url = data['issues_url']
      self.source_url = data['source_url']
      self.wiki_url = data['wiki_url']
      self.discord_url = data['discord_url']
      self.donation_urls = data['donation_urls']
      self.gallery = data['gallery']
      self.color = data['color']
      self.threadId = data['thread_id']
      self.monetizationStatus = data['monetization_status']
    
    async def get_client_side(self) -> str:
      '''Returns "required", "optional" or "unsupported'''
      return self.clientSide
    async def get_server_side(self) -> str:
      '''Returns "required", "optional" or "unsupported'''
      return self.serverSide
    async def get_game_versions(self) -> list:
      return self.gameVersions
    async def get_id(self) -> str:
      return self.id
    async def get_slug(self) -> str:
      return self.slug
    async def get_project_type(self) -> str:
      return self.projectType
    async def get_team(self) -> str:
      return self.team
    async def get_organization(self) -> str:
      return self.organization
    async def get_title(self) -> str:
      return self.title
    async def get_description(self) -> str:
      return self.description
    async def get_body(self) -> str:
      return self.body
    async def get_published(self) -> str:
      return self.published
    async def get_updated(self) -> str:
      return self.updated
    async def get_approved(self) -> str:
      return self.approved
    async def get_queued(self):
      return self.queued
    async def get_status(self):
      if self.status in statusEnum:
        return self.status
      else:
        logger.warning(f'Error: self.status is not correct, it returned {self.status} instead of an allowed value')
        return self.status
    async def get_requested_status(self):
      return self.requestedStatus
    async def get_moderator_message(self):
      return self.moderatorMessage
    async def get_license(self):
      return self.license
    async def get_downloads(self):
      return self.downloads
    async def get_followers(self):
      return self.followers
    async def get_categories(self) -> list:
      return self.categories
    async def get_additional_categories(self) -> list:
      return self.additionalCategories
    async def get_loaders(self) -> list:
      return self.loaders
    async def get_versions(self) -> list:
      return self.versions
    async def get_icon_url(self):
      return self.icon_url
    async def get_issues_url(self):
      return self.issues_url
    async def get_source_url(self):
      return self.source_url
    async def get_wiki_url(self):
      return self.wiki_url
    async def get_discord_url(self):
      return self.discord_url
    async def get_donation_urls(self):
      return self.donation_urls
    async def get_gallery(self):
      return self.gallery
    async def get_color(self):
      return self.color
    async def get_threadId(self):
      return self.threadId
    async def get_monetization_status(self):
      return self.monetizationStatus

    async def request(self, modID:str):
      """Make a request to modrinth api for all data revolving a mod

      Args:
          modID (str): mod id/url of the mod your looking at
      """
      self.modID = modID
      await self._parseData()
      

  # class _Utils:
    # def __init__(self):
      # 
    # async def version(self, loader:list[str], mc_version:list[str], featured:bool=False):
      # params = {'loaders': loader, 'game_versions': mc_version}
# 
      # r=requests.get(url=f'{self.apiRoute}{self.modid}/version', headers=headers)
      # print(r.json())




class modrinthVersion:
  class versions:
    def __init__(self, modid):
      self.project = modrinthProjects(modid)



    



