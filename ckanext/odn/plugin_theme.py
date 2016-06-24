import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

import ckanext.odn.helpers as helpers


class OdnThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    
    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'odn')


    # ITemplateHelpers
    def get_helpers(self):
        return {'recent_updates': helpers.recent_updates,
                'group_list': helpers.group_list}




