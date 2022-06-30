from netconf_openconfig.consumer.netconf_client import NetconfClient
from netconf_openconfig.models.config_params import ConfigParams
from netconf_openconfig.service.service_api import ServiceOC


# TODO : check params before calling service class
#  TODO : aggregagte service calls if needed in method (for example; check if capabilities exists,
#   call service and filter result ...)
class NetconfConfig:
    def __init__(self, params: ConfigParams):
        self._netconf_client = NetconfClient(params.host, params.port, params.login, params.password)
        self._service = ServiceOC(self._netconf_client)


