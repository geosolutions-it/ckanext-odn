import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

import ckan.lib.base as base

import ckanext.odn.helpers as helpers


class OdnThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IRoutes, inherit=True)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'odn')

    # ITemplateHelpers
    def get_helpers(self):
        return {'recent_updates': helpers.recent_updates,
                'group_list': helpers.group_list,
                'get_odn_config': helpers.get_odn_config}

    # IRoutes
    def before_map(self, map):
        map.connect('istruzioni', '/istruzioni', controller='ckanext.odn.plugin_theme:ODNController', action='istruzioni')
        map.connect('opendata', '/opendata', controller='ckanext.odn.plugin_theme:ODNController', action='opendata')

        return map


class ODNController(base.BaseController):

    def istruzioni(self):
        return base.render('home/odn_istruzioni.html')

    def opendata(self):
        return base.render('home/odn_opendata.html')
