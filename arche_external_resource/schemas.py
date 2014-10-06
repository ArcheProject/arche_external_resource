from __future__ import unicode_literals

from arche.schemas import BaseSchema
from deform.widget import TextInputWidget
import colander
import requests


class EmbedWidget(TextInputWidget):
    template = 'widgets/embed_textinput'
    #readonly?


class JSONURL(object):
    """ Validator """

    def __init__(self):
        pass

    def __call__(self, node, value):
        colander.url(node, value)
        try:
            response = requests.get(value, verify = False) #FIXME: SSL problem here too
        except requests.exceptions.RequestException as e:
            raise colander.Invalid(node, str(e))
        if 'application/json' not in response.headers.get('content-type'):
            raise colander.Invalid(node, _(u"URL didn't return information on a shared object. (Must be a json response)"))


class ExternalResourceSchema(BaseSchema):
    target = colander.SchemaNode(colander.String(),
                                 validator = JSONURL(),
                                 widget = EmbedWidget())


def includeme(config):
    config.add_content_schema('ExternalResource', ExternalResourceSchema, 'add')
    config.add_content_schema('ExternalResource', ExternalResourceSchema, 'edit')
