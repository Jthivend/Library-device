import argparse
import logging
import sys
from logging import Logger
from netconf_openconfig.application.nokia_openconfig import ClientNetconfConfig
from netconf_openconfig.service.service_api import *
from netconf_openconfig.models.config_params import ConfigParams

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger: Logger = logging.getLogger(__name__)


def main():
    args = check_parameters()
    config_params = ConfigParams(args.host, 17841, args.login, args.password)
    nokia_openconfig = ClientNetconfConfig(config_params)
    capabilities = nokia_openconfig.get_capabilities()
    logger.info('Get capabilities %s', list(capabilities))
    logger.info(
        'Capabilities urn:ietf:params:xml:ns:yang:ietf-inet-types?module=ietf-inet-types&revision=2013-07-15:'
        ' module %s',
        capabilities[
            'urn:ietf:params:xml:ns:yang:ietf-inet-types?module=ietf-inet-typeig_paramss&revision=2013-07-15'].parameters.get(
            'module'))


def check_parameters():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, required=True, help='netconf host IP address')
    parser.add_argument('--login', type=str, required=True, help='netconf login')
    parser.add_argument('--password', type=str, required=True, help='netconf password')
    return parser.parse_args()


if __name__ == '__main__':
    main()
