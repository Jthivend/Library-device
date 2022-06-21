import os.path
from pathlib import Path

from ncclient.operations import RPCError

from netconf_openconfig.consumer.netconf_client import NetconfClient
from netconf_openconfig.service import logger
from netconf_openconfig.utils.jinja_utile import instanciate_template_jinja


def read_filter(filename):
    resp_file = Path(__file__).parent / "filters" / filename
    with resp_file.open() as file:
        return file.read()


class ServiceOC:
    def __init__(self, client: NetconfClient):
        self.filter_directory = os.path.join(os.path.dirname(__file__), 'filters')
        self._client = client

    def capabilities(self):
        return self._client.get_capabilities()

    def config(self, target_config):
        """
        :param target_config:
        :return:
        """
        return self._client.get_config(target_config)
+

    def modify_node_id(self, node_id):
        template = instanciate_template_jinja(self.filter_directory, "filter_edit_node_id.xml")
        output = template.render(node_id=node_id)
        return output

    def modify_node_type(self, node_type):
        template = instanciate_template_jinja(self.filter_directory, "filter_edit_node_type.xml")
        output = template.render(node_type=node_type)
        return output

    def modify_node_number(self, node_number):
        template = instanciate_template_jinja(self.filter_directory, "filter_edit_node_number.xml")
        output = template.render(node_number=node_number)
        return output

    def modify_node_clli(self, clli):
        template = instanciate_template_jinja(self.filter_directory, "filter_edit_clli.xml")
        output = template.render(clli=clli)
        return output

    def modify_node_ipAddress(self, ipAddress):
        template = instanciate_template_jinja(self.filter_directory, "filter_edit_ipAddress.xml")
        output = template.render(ipAddress=ipAddress)
        return output

    def modify_node_prefixLength(self, prefixLength):
        template = instanciate_template_jinja(self.filter_directory, "filter_edit_prefixLength.xml")
        output = template.render(prefixLength=prefixLength)
        return output

    def modify_node_defaultGateway(self, defaultGateway):
        template = instanciate_template_jinja(self.filter_directory, "filter_edit_defaultGateway.xml")
        output = template.render(defaultGateway=defaultGateway)
        return output

    def modify_node_template(self, template):
        template = instanciate_template_jinja(self.filter_directory, "filter_edit_template.xml")
        output = template.render(template=template)
        return output

    def modify_node_latitude(self, latitude):
        template = instanciate_template_jinja(self.filter_directory, "filter_edit_geoLocation.xml")
        output = template.render(latitude=latitude)
        return output

    def modify_node_longitude(self, longitude):
        template = instanciate_template_jinja(self.filter_directory, "filter_edit_geoLocation.xml")
        output = template.render(longitude=longitude)
        return output
