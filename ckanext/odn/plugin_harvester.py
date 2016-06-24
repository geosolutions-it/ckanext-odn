from datetime import datetime
import logging

import ckan.plugins as plugins

import ckanext.spatial.model.harvested_metadata as s
from ckanext.spatial.interfaces import ISpatialHarvester

log = logging.getLogger(__name__)


class OdnHarvesterPlugin(plugins.SingletonPlugin):

    plugins.implements(ISpatialHarvester, inherit=True)

    # GN usa questo substitutiongroup nelle online resource
    log.info('init: Adding ISO mapping to gmx:MimeFileType')
    for element in s.ISOResourceLocator.elements:
        if element.name == 'name':
            element.search_paths.append('gmd:name/gmx:MimeFileType/text()')
            break;

    # GN inserisce il tipo di risorsa in questo attributo
    log.info('init: Adding ISO mapping to gmx:MimeFileType/@type')
    s.ISOResourceLocator.elements.append(
            s.ISOElement(
            name="mimetype",
            search_paths=["gmd:name/gmx:MimeFileType/@type"],
            multiplicity="0..1",))

    log.info('init: Replacing ISO mapping to metadata PoC')
    for element in s.ISODocument.elements:
        if element.name == 'metadata-point-of-contact':
            log.info('init: Metadata PoC mapping found')
            element.search_paths = ["gmd:contact/gmd:CI_ResponsibleParty"]
            break;

    # ISpatialHarvester method
    def get_package_dict(self, context, data_dict):

        package_dict = data_dict['package_dict']
        iso_values = data_dict['iso_values']

        ind, org, mail = self._find_responsible(iso_values['metadata-point-of-contact'], 'pointOfContact')

        if ind or org:
            # log.info('Updating PoC: %s - %s', ind, org )
            package_dict['author'] = ind + " - " + org

        if mail:
            package_dict['author_email'] = mail

        if iso_values['dataset-reference-date'] and len(iso_values['dataset-reference-date']):
            package_dict['version'] = "{} - {}".format(
                iso_values['dataset-reference-date'][0]['type'],
                iso_values['dataset-reference-date'][0]['value'])

        resource_locators = iso_values.get('resource-locator', [])
        self._update_resources(package_dict['resources'], resource_locators, package_dict)

        return package_dict


    def _update_resources(self, resources, locators, package_dict):
        # @type resources: list
        # @type locators: list
        
        # l'harvester originale include anche onlineResource esterni a Distribution, che vanno eliminati
        resources_to_delete = []

        for resource in resources:
            locator = self._get_locator_by_url(resource, locators)
            if not locator:
                resources_to_delete.append(resource)
                continue

            if not resource['format']:
                self._guess_format(resource, locator, package_dict)

        for delendum in resources_to_delete:
            log.info('Removing resource %s', delendum['url'])
            resources.remove(delendum)


    def _get_locator_by_url(self, resource, locators):
        for locator in locators:
            if resource['url'] == locator.get('url', '').strip():
                return locator

        return None

    def _guess_format(self, resource, resource_locator, package_dict):
        #
        resource_type = None
        resource_format = None

        # resource = {}
#        if package_dict['extras']['resource-type'] == 'service':
#            # Check if the service is a view service
#            test_url = url.split('?')[0] if '?' in url else url
#            if self._is_wms(test_url):
#                resource['verified'] = True
#                resource['verified_date'] = datetime.now().isoformat()
#                resource_format = 'WMS'

        # GN customization for CERCO
        if resource_locator.get('protocol','') == 'TOLOMEO:preset':
            resource_type = 'TOLOMEO:preset'
            resource['verified'] = True
            resource['verified_date'] = datetime.now().isoformat()
            # resource_format = 'mappa'
        # GN specific WMS type
        elif resource_locator.get('protocol','') == 'OGC:WMS-1.3.0-http-get-map' or \
             resource_locator.get('protocol','') == 'OGC:WMS-1.1.1-http-get-map' :
                 
            resource_type='WMS'
            resource_format = 'WMS'
            resource['verified'] = True
            resource['verified_date'] = datetime.now().isoformat()
        # GN link to page
        elif resource_locator.get('protocol','') == 'WWW:LINK-1.0-http--link' :
            resource['verified'] = True
            resource_type = 'link'
        #    resource_format = 'WMS'
        # GN downloadable resource
        elif resource_locator.get('protocol','') == 'WWW:DOWNLOAD-1.0-http--download':
            resource['verified'] = True # ??
            resource['verified_date'] = datetime.now().isoformat() # ??
            if resource_locator.get('mimetype','') == 'application/x-compressed':
                 # this is a ZIP file
                 resource_type = 'download'
                 resource_format = 'ZIP'
            if resource_locator.get('mimetype','') == 'application/gnutar':
                 # this is a TGZ file
                 resource_type = 'download'
                 resource_format = 'TGZ'

        resource.update(
            {
                'resource_type': resource_type,
                'format': resource_format or None,
            })

    def _find_responsible(self, responsible_parties , role):
        '''Find the first responsible info for the given role.

        :param responsible_organisations: list of dicts, each with keys
                      includeing 'organisation-name' and 'role'
        :returns: individual,organization,mail
        '''

        # log.info('Checking %s', responsible_parties)

        if responsible_parties:
            for rparty in responsible_parties:
                if rparty['role'] == role:
                    return rparty['individual-name'], \
                           rparty['organisation-name'], \
                           rparty['contact-info']['email']

        return None, None, None