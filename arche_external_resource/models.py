from __future__ import unicode_literals

from arche.api import Base
from arche.interfaces import IIndexedContent
from arche.security import get_acl_registry, ROLE_ADMIN
from repoze.lru import LRUCache
from zope.interface import implementer
import requests

from arche_external_resource.interfaces import IExternalResource
from arche_external_resource import _


#FIXME: This might not be the best way to handle this
_remote_cache = LRUCache(200)


@implementer(IExternalResource, IIndexedContent)
class ExternalResource(Base):
    description = ""
    type_name = "ExternalResource"
    type_title = _("External Resource")
    type_description = _("Some kind of external resource.")
    add_permission = "Add %s" % type_name
    target = ""
    icon = "film"
    nav_visible = False
    listing_visible = True
    search_visible = True
    show_byline = True

    @property
    def content_data(self):
        if self.target:
            data = _remote_cache.get(self.target, None)
            if data is not None:
                return data
            response = requests.get(self.target, verify = False)
            if response.ok:
                data = response.json()
                _remote_cache.put(self.target, data)
                return data
        return {}

    @property
    def title(self):
        return self.content_data.get('title', u'')


def includeme(config):
    config.add_content_factory(ExternalResource)
    config.add_addable_content('ExternalResource', ('Root', 'Document'))
    aclreg = get_acl_registry(config.registry)
    aclreg['public'].add(ROLE_ADMIN, ExternalResource.add_permission)
