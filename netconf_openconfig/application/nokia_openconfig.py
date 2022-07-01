from netconf_openconfig.consumer.netconf_client import NetconfClient
from netconf_openconfig.models.config_params import ConfigParams
from netconf_openconfig.service.service_api import ServiceOC


# TODO : check params before calling service class
#  TODO : aggregagte service calls if needed in method (for example; check if capabilities exists,
#   call service and filter result ...)
class ClientNetconfConfig:
    def __init__(self, params: ConfigParams):
        self._netconf_client = NetconfClient(params.host, params.port, params.login, params.password)
        self._service = ServiceOC(self._netconf_client)

    def get_capabilities(self):
        return self._service.capabilities()

    def config(self, target_config):
        return self._service.config(target_config)

    def get_system(self):
        return self._service.get_system()

    def get_all_components(self):
        return self._service.get_all_components()

    def get_all_terminal_device_logical_channel(self):
        return self._service.get_all_terminal_device_logical_channel()

    def set_client_port_mode(self):
        return self._service.set_client_port_mode()

    def add_logical_board(self, board_name):
        return self._service.add_logical_board(board_name)

        # DISCOVERY OF COMPONENTS AND TYPE OF COMPONENTS

    def get_component_filtered_by_name(self):
        return self._service.get_component_filtered_by_name()

    def get_component_filtered_by_optical_port(self):
        return self._service.get_component_filtered_by_optical_port()

    def get_nokia_user_label(self):
        return self._service.get_nokia_user_label()

    def get_all_component_by_type(self):
        return self._service.get_all_component_by_type()

    def get_component_type_by_compo_name(self):
        return self._service.get_component_type_by_compo_name()

    def get_subcomponent_card(self):
        return self._service.get_subcomponent_card()

    def get_subcomponent_port(self):
        return self._service.get_subcomponent_port()

    def get_port_type(self):
        return self._service.get_port_type()

    def get_subcomponent_port2(self):
        return self._service.get_subcomponent_port2()

    def get_all_subcomponent_port_type(self):
        return self._service.get_all_subcomponent_port_type()

    def get_subcomponent_optical_port_type(self):
        return self._service.get_subcomponent_optical_port_type()

    def get_subcomponent_optical_port_type2(self):
        return self._service.get_subcomponent_optical_port_type2()

    def get_all_operational_mode(self):
        return self._service.get_all_operational_mode()

    def get_operational_mode_51(self):
        return self._service.get_operational_mode_51()

    def get_all_admin_state_of_port(self):
        return self._service.get_all_admin_state_of_port()

    def get_admin_state_of_port(self):
        return self._service.get_admin_state_of_port()

        # DISCOVERY OF ADMIN STATUS OF INTERFACE

    def get_oc_interface(self):
        return self._service.get_oc_interface()

        # DISCOVERY OF OF CLIENT PORT CAPABILITIES (PROTOCOL_TYPE, RATE AND MAPPING).

    def get_terminal_device_ingress_channel(self):
        return self._service.get_terminal_device_ingress_channel()

    def get_terminal_device_transceiver_state(self):
        return self._service.get_terminal_device_transceiver_state()

    def get_logical_channel_capability_by_index(self):
        return self._service.get_logical_channel_capability_by_index()

        # DISCOVERY OF LINE PORT CAPABILITIES (PROTOCOL_TYPE, RATE GRANULARITY AND ALLOCATION).

    def get_logical_channel_line_capability_by_index(self):
        return self._service.get_logical_channel_line_capability_by_index()

        # DISCOVERY OF FREQUENCY AND OPERATIONAL MODE CONFIGURED IN A LINE PORT.

    def get_och_details(self):
        return self._service.get_och_details()

        # DISCOVERY OF TYPE OF LOGICAL CHANNEL ASSIGNMENTS (FLEX OR PRESET).

    def get_type_logical_channel_assignt(self):
        return self._service.get_type_logical_channel_assignt()

        # DISCOVERY OF LOGICAL CHANNEL ASSIGNMENT

    def get_all_channel_index(self):
        return self._service.get_all_channel_index()

        # DISCOVERY OF LOCATION OF A COMPONENT.

    def get_component_location(self):
        return self._service.get_component_location()

        # RETRIEVAL OF GLOBAL STRUCTURE OF HW INVENTORY.

    def get_all_subcomponents_chassis(self):
        return self._service.get_all_subcomponents_chassis()

        # RETRIEVAL OF INFORMATION OF EACH COMPONENT.

    def get_component_state(self):
        return self._service.get_component_state()

        # RETRIEVAL OF SLOT IDENTIFIERS (SLOT-ID) INFORMATION.

    def get_component_slot_id(self):
        return self._service.get_component_slot_id()

        # RETRIEVAL OF Q-VALUE OF OPTICAL CHANNEL(S)

    def get_logical_channel_q_value(self):
        return self._service.get_logical_channel_q_value()

    def get_fec_ber_q_value(self):
        return self._service.get_fec_ber_q_value()

        # SERVICE PROVISIONING OPERATIONS AND PROVISIONING OF PORT TYPE ON CLIENT PORT

    def get_port_type_on_client_port(self, port_name):
        return self._service.get_port_type_on_client_port(port_name)

    def set_port_type_on_client_port(self, port_name, device_port_value):
        return self._service.set_port_type_on_client_port(port_name, device_port_value)

        # PROVISIONING OF PORT STATE ON CLIENT PORT.

    def get_admin_state_port(self, device_port_name):
        return self._service.get_admin_state_port(device_port_name)

    def set_admin_state_port(self, device_port_name, device_port_state):
        return self._service.set_admin_state_port(device_port_name, device_port_state)

    def get_d5_logical_channels(self):
        return self._service.get_d5_logical_channels()

    def modify_assignement_logical_channel_in_another_logical_channel(self, index1, index2, atype, slot, action):
        return self._service.modify_assignement_logical_channel_in_another_logical_channel(index1, index2, atype, slot,
                                                                                           action)


