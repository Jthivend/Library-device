import logging
import sys
from logging import Logger

from netconf_client.connect import connect_ssh
from netconf_client.ncclient import Manager

from netconf_openconfig.service.filters.filtres import *

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger: Logger = logging.getLogger(__name__)

with connect_ssh('127.0.0.1', 17841, 'changeit', 'changeit', ) as sessions:
    e = Manager(sessions, timeout=120)

    # get node_id
    logger.info(e.get_config("running", filtre_id).data_xml)

    # get node_number
    logger.info(e.get_config("running", filtre_number).data_xml)

    # get  node_type
    logger.info(e.get_config("running", filtre_type).data_xml)

    # get clli
    # logger.info(e.get_config("running", filtre_clli).data_xml)

    # get vendor
    # logger.info(e.get_config("running", filtre_vendor).data_xml)

    # get model
    # logger.info(e.get_config("running", filtre_model).data_xml)

    # get serial_id
    # logger.info(e.get_config("running", filtre_serial_id).data_xml)

    # get address ip
    logger.info(e.get_config("running", filtre_ip_address).data_xml)

    # get prefix_length
    logger.info(e.get_config("running", filtre_prefix_length).data_xml)

    # get defaultgateway
    logger.info(e.get_config("running", filtre_defaultgateway).data_xml)

    # get macAddress
    # logger.info(e.get_config("running", filtre_macAddress).data_xml)

    # get softwareVersion
    # logger.info(e.get_config("running", filtre_softwareVersion).data_xml)

    # get openroadm_version
    # logger.info(e.get_config("running", filtre_openroadm_version).data_xml)

    # get  template
    logger.info(e.get_config("running", filtre_template).data_xml)

    # get  current_datetime
    # logger.info(e.get_config("running", filtre_current_dateTime).data_xml)

    # get  geolocation
    logger.info(e.get_config("running", filtre_geoLocation).data_xml)

    # get  max_degrees
    # logger.info(e.get_config("running", filtre_max_degrees).data_xml)

    # get max_srgs
    # logger.info(e.get_config("running", filtre_max_srgs).data_xml)

    # get max_num_bin_15min_historical_pm
    # logger.info(e.get_config("running", filtre_max_num_bin_15min_historical_pm).data_xml)
