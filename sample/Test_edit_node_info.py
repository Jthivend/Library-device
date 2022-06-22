from netconf_client.connect import connect_ssh
from netconf_client.ncclient import Manager
from xml.etree import ElementTree
from netconf_openconfig.service.service_api import *

with connect_ssh('127.0.0.1', 17841, 'changeit', 'changeit', ) as sessions:
    e = Manager(sessions, timeout=120)
    config = NetconfClient('127.0.0.1', 17841, 'changeit', 'changeit')
    oc = ServiceOC(config)

    filter_edit_id = oc.modify_node_id('XPDR-B1')
    e.edit_config(filter_edit_id, 'running')
    e.commit(True)

    # filter_edit_type = oc.modify_node_type('1')
    # e.edit_config(filter_edit_type, 'running')
    # e.commit(True)

    # filter_edit_number = oc.modify_node_number('xpdr')
    # e.edit_config(filter_edit_number, 'running')
    # e.commit(True)

    # filter_edit_clli = oc.modify_node_clli('node')
    # e.edit_config(filter_edit_clli, 'running')
    # e.commit(True)

    filter_edit_ipAddress = oc.modify_node_ipAddress('1.2.3.4')
    e.edit_config(filter_edit_ipAddress, 'running')
    e.commit(True)

    filter_edit_prefixLength = oc.modify_node_prefixLength('24')
    e.edit_config(filter_edit_prefixLength, 'running')
    e.commit(True)

    filter_edit_defaultGateway = oc.modify_node_defaultGateway('1.2.3.4')
    e.edit_config(filter_edit_defaultGateway, 'running')
    e.commit(True)

    # filter_edit_template = oc.modify_node_template('template_TRANSPONDER')
    # e.edit_config(filter_edit_template, 'running')
    # e.commit(True)

    # filter_edit_latitude = oc.modify_node_latitude('1.0000')
    # e.edit_config(filter_edit_latitude, 'running')
    # e.commit(True)

    # filter_edit_longitude = oc.modify_node_longitude('2.0000')
    # e.edit_config(filter_edit_longitude, 'running')
    # e.commit(True)

    filter_edit_interface = oc.modify_interface('XPDR2-NETWORK1-761:768', '1/0/0-PLUG-NET')
    e.edit_config(filter_edit_interface, 'running')
    e.commit(True)

    filter_edit_connexion_name = oc.modify_connexion_name('name')
    e.edit_config(filter_edit_connexion_name, 'running')
    e.commit(True)
