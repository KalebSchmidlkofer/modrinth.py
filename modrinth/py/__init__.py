#!/usr/bin/env python3
# -*- coding: utf8 -*-
'''
Developed by Kaleb Schmidlkofer <kaleb@ashbyte.com>
An Unofficial modrinth api wrapper for python
'''

import requests
import asyncio
from loguru import logger
import sys

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

__version__ = '0.0.1'


modID='made-in-abyss-ost'

class Users:
  pass



statusEnum=["approved", "archived", "rejected", "draft", "unlisted", "processing", "withheld", "scheduled", "private", "unknown"]
class modrinthProjects:
  class Data:
    
    def __init__(self, apiRoute:str='https://api.modrinth.com/v2/project/'):
      self.apiRoute=apiRoute
    
    async def _requestData(self):
      r = requests.get(f'{self.apiRoute}{modID}')
      return r.json()
    
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


    async def request(self):
      await self._parseData()
      
projects=modrinthProjects.Data()
asyncio.run(projects.request())

