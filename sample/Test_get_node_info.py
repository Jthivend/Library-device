from netconf_client.connect import connect_ssh
from netconf_client.ncclient import Manager
from xml.etree import ElementTree
from netconf_openconfig.service.service_api import *
from netconf_openconfig.service.filters.filtres import *


with connect_ssh('127.0.0.1', 17841, 'changeit', 'changeit', ) as sessions:
    e = Manager(sessions, timeout=120)
    config = NetconfClient('127.0.0.1', 17841, 'changeit', 'changeit')
    oc = ServiceOC(config)
    # Récupérer le node_id
    print(e.get_config("running", filtre_id).data_xml)
    # Récupérer le node_number
    print(e.get_config("running", filtre_number).data_xml)
    # Récupérer le node_type
    print(e.get_config("running", filtre_type).data_xml)
    # Récupérer le clli
    # print(e.get_config("running", filtre_clli).data_xml)
    # Récupérer le vendor
    # print(e.get_config("running", filtre_vendor).data_xml)
    # Récupérer le model
    # print(e.get_config("running", filtre_model).data_xml)
    # Récupérer le serial_id
    # print(e.get_config("running", filtre_serial_id).data_xml)
    # Récupérer l'adresse ip
    print(e.get_config("running", filtre_ip_address).data_xml)
    # Récupérer le prefix_length
    print(e.get_config("running", filtre_prefix_length).data_xml)
    # Récupérer la passerelle par défaut
    print(e.get_config("running", filtre_defaultgateway).data_xml)
    # Récupérer la source
    # print(e.get_config("running", filtre_source).data_xml)
    # Récupérer l'adresse ip courante
    # print(e.get_config("running", filtre_current_ip_address).data_xml)
    # Récupérer le prefix length courante
    # print(e.get_config("running", filtre_current_prefix_length).data_xml)
    # Récupérer la passerelle par défaut courante
    # print(e.get_config("running", filtre_current_default_gateway).data_xml)
    # Récupérer l'adresse mac
    # print(e.get_config("running", filtre_macAddress).data_xml)
    # Récupérer la version du logiciel
    # print(e.get_config("running", filtre_softwareVersion).data_xml)
    # Récupérer la version de openroadm
    # print(e.get_config("running", filtre_openroadm_version).data_xml)
    # Récupérer le template
    print(e.get_config("running", filtre_template).data_xml)
    # Récupérer la date courante
    # print(e.get_config("running", filtre_current_dateTime).data_xml)
    # Récupérer la position par latitude et longitude
    print(e.get_config("running", filtre_geoLocation).data_xml)
    # Récupérer le degré max que la machine peut endurer
    # print(e.get_config("running", filtre_max_degrees).data_xml)
    # print(e.get_config("running", filtre_max_srgs).data_xml)
    # print(e.get_config("running", filtre_max_num_bin_15min_historical_pm).data_xml)
    # print(e.get_config("running", filtre_max_num_bin_24hour_historical_pm).data_xml)
    # Récupérer les infos concernant l'interface
    print(e.get_config("running", filtre_interface).data_xml)
    # Récupérer le name, password et group du node  dans la branche user
    print(e.get_config("running", filtre_name).data_xml)
    print(e.get_config("running", filtre_password).data_xml)
    print(e.get_config("running", filtre_group).data_xml)
    # Récupérer le nom de la connexion
    print(e.get_config("running", filtre_connexion_name).data_xml)


