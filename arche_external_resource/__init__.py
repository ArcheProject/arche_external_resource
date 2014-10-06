from pyramid.i18n import TranslationStringFactory
from pyramid_deform import configure_zpt_renderer


_ = TranslationStringFactory('arche_external_resource')

_default_settings = {'arche_external_resource.deform_search_path': 'arche_external_resource:/templates/deform'}


def includeme(config):
    config.include('.models')
    config.include('.schemas')
    config.include('.views')
    settings = config.registry.settings
    if 'arche_external_resource.deform_search_path' not in settings:
        settings['arche_external_resource.deform_search_path'] = _default_settings['arche_external_resource.deform_search_path']
    configure_zpt_renderer(search_path = settings['arche_external_resource.deform_search_path'].split())
