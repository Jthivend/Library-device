from netconf_openconfig.service.service_api import *

netconfclient = NetconfClient('127.0.0.1', 17841, 'changeit', 'changeit')
oc = ServiceOC(netconfclient)

filter_edit_id = oc.modify_node_id('XPDR-B1')
netconfclient.mgr.edit_config(filter_edit_id, 'running')
netconfclient.mgr.commit(True)

# filter_edit_type = oc.modify_node_type('1')
# netconfclient.mgr.edit_config(filter_edit_type, 'running')
# netconfclient.mgr.commit(True)

# filter_edit_number = oc.modify_node_number('xpdr')
# netconfclient.mgr.edit_config(filter_edit_number, 'running')
# netconfclient.mgr.commit(True)

filter_edit_ipAddress = oc.modify_node_ipAddress('1.2.3.4')
netconfclient.mgr.edit_config(filter_edit_ipAddress, 'running')
netconfclient.mgr.commit(True)

filter_edit_prefixLength = oc.modify_node_prefixLength('24')
netconfclient.mgr.edit_config(filter_edit_prefixLength, 'running')
netconfclient.mgr.commit(True)

filter_edit_defaultGateway = oc.modify_node_defaultGateway('1.2.3.4')
netconfclient.mgr.edit_config(filter_edit_defaultGateway, 'running')
netconfclient.mgr.commit(True)

# filter_edit_template = oc.modify_node_template('template_TRANSPONDER')
# netconfclient.mgr.edit_config(filter_edit_template, 'running')
# netconfclient.mgr.commit(True)

# filter_edit_latitude = oc.modify_node_latitude('1.0000')
# netconfclient.mgr.edit_config(filter_edit_latitude, 'running')
# netconfclient.mgr.commit(True)

# filter_edit_longitude = oc.modify_node_longitude('2.0000')
# netconfclient.mgr.edit_config(filter_edit_longitude, 'running')
# netconfclient.mgr.commit(True)

filter_edit_interface = oc.modify_interface('XPDR2-NETWORK1-761:768', '1/0/0-PLUG-NET')
netconfclient.mgr.edit_config(filter_edit_interface, 'running')
netconfclient.mgr.commit(True)

# filter_edit_connexion_name = oc.modify_connexion_name('name')
# netconfclient.mgr.edit_config(filter_edit_connexion_name, 'running')
# netconfclient.mgr.commit(True)

filter_edit_user = oc.modify_user('openroadm', 'openroadm', 'sudo')
netconfclient.mgr.edit_config(filter_edit_user, 'running')
netconfclient.mgr.commit(True)
