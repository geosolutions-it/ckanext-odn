import logging
import operator

from pylons import config

import ckan
import ckan.model as model
import ckan.plugins as p
import ckan.lib.search as search
import ckan.lib.helpers as h

NUM_MOST_VIEWED_DATASETS = 10

log = logging.getLogger(__file__)


def recent_updates(n):
    '''
    Return a list of the n most recently updated datasets.
    '''
    context = {'model': model,
               'session': model.Session,
               'user': p.toolkit.c.user or p.toolkit.c.author}
    data = {'rows': n,
            'sort': u'metadata_modified desc',
            'facet': u'false'}
    try:
        search_results = p.toolkit.get_action('package_search')(context, data)
    except search.SearchError:
        log.error('Error searching for recently updated datasets')
        log.error(e)
        search_results = {}

#    log.error('Found %d recent updates ' % len(search_results))
#    log.error('Updates:  %r ' % search_results)
    return search_results.get('results', [])

def group_list(count=1):
    
    def get_group(id):
        context = {'ignore_auth': True,
                   'limits': {'packages': 2},
                   'for_view': True}
        data_dict = {'id': id,
                     'include_datasets': False}

        try:
            out = p.toolkit.get_action('group_show')(context, data_dict)
        except logic.NotFound:
            return None
        return out

    groups_ret = []

    list_data_dict = {'limit': count, 'sort': 'package_count'}
    glist = p.toolkit.get_action('group_list')({}, list_data_dict)

    for group_name in glist:
        group = get_group(group_name)
        groups_ret.append(group)

    return groups_ret


def get_odn_config():
    '''
        Returns a dict with all configuration options related to ODN,
        that is those starting with 'odn.')
    '''
    namespace = 'odn.'
    return dict([(k.replace(namespace, ''), v) for k, v in config.iteritems()
                 if k.startswith(namespace)])