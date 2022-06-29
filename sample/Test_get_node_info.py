from netconf_openconfig.service.filters.filtres import *

netconfclient = NetconfClient('127.0.0.1', 17841, 'changeit', 'changeit')
oc = ServiceOC(netconfclient)
# Récupérer le node_id
print(netconfclient.mgr.get_config("running", filtre_id).data_xml)
# Récupérer le node_number
print(netconfclient.mgr.get_config("running", filtre_number).data_xml)
# Récupérer le node_type
print(netconfclient.mgr.get_config("running", filtre_type).data_xml)
# Récupérer le clli
# print(netconfclient.mgr.get_config("running", filtre_clli).data_xml)
# Récupérer le vendor
# print(netconfclient.mgr.get_config("running", filtre_vendor).data_xml)
# Récupérer le model
# print(netconfclient.mgr.get_config("running", filtre_model).data_xml)
# Récupérer le serial_id
# print(netconfclient.mgr.get_config("running", filtre_serial_id).data_xml)
# Récupérer l'adresse ip
print(netconfclient.mgr.get_config("running", filtre_ip_address).data_xml)
# Récupérer le prefix_length
print(netconfclient.mgr.get_config("running", filtre_prefix_length).data_xml)
# Récupérer la passerelle par défaut
print(netconfclient.mgr.get_config("running", filtre_defaultgateway).data_xml)
# Récupérer la source
# print(netconfclient.mgr.get_config("running", filtre_source).data_xml)
# Récupérer l'adresse ip courante
# print(netconfclient.mgr.get_config("running", filtre_current_ip_address).data_xml)
# Récupérer le prefix length courante
# print(netconfclient.mgr.get_config("running", filtre_current_prefix_length).data_xml)
# Récupérer la passerelle par défaut courante
# print(netconfclient.mgr.get_config("running", filtre_current_default_gateway).data_xml)
# Récupérer l'adresse mac
# print(netconfclient.mgr.get_config("running", filtre_macAddress).data_xml)
# Récupérer la version du logiciel
# print(netconfclient.mgr.get_config("running", filtre_softwareVersion).data_xml)
# Récupérer la version de openroadm
# print(netconfclient.mgr.get_config("running", filtre_openroadm_version).data_xml)
# Récupérer le template
print(netconfclient.mgr.get_config("running", filtre_template).data_xml)
# Récupérer la date courante
# print(netconfclient.mgr.get_config("running", filtre_current_dateTime).data_xml)
# Récupérer la position par latitude et longitude
print(netconfclient.mgr.get_config("running", filtre_geoLocation).data_xml)
# Récupérer le degré max que la machine peut endurer
# print(netconfclient.mgr.get_config("running", filtre_max_degrees).data_xml)
# print(netconfclient.mgr.get_config("running", filtre_max_srgs).data_xml)
# print(netconfclient.mgr.get_config("running", filtre_max_num_bin_15min_historical_pm).data_xml)
# print(netconfclient.mgr.get_config("running", filtre_max_num_bin_24hour_historical_pm).data_xml)
# Récupérer les infos concernant l'interface
print(netconfclient.mgr.get_config("running", filtre_interface).data_xml)
# Récupérer le name, password et group du node  dans la branche user
print(netconfclient.mgr.get_config("running", filtre_name).data_xml)
print(netconfclient.mgr.get_config("running", filtre_password).data_xml)
print(netconfclient.mgr.get_config("running", filtre_group).data_xml)
# Récupérer le nom de la connexion
print(netconfclient.mgr.get_config("running", filtre_connexion_name).data_xml)
