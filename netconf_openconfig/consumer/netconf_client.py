#!/usr/bin/env python
# encoding: utf-8
import atexit

from ncclient import manager


class NetconfClient:

    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

        self.mgr = manager.connect(host=self.host,
                                   port=self.port,
                                   username=self.username,
                                   password=self.password,
                                   look_for_keys=False,
                                   hostkey_verify=False)

        atexit.register(self.disconnect)

    def disconnect(self):
        self.mgr.close_session()

    def get_capabilities(self):
        return self.mgr.server_capabilities

    def list_schema(self, schema):
        sch = self.mgr.get_schema(schema)
        print(sch)

    def get(self):
        return self.mgr.get()

    def get_config(self, target_config):
        return self.mgr.get_config(source=target_config)

    def filter_config(self, target_config, filter_cfg):
        return self.mgr.get_config(target_config, filter_cfg)

    def edit_config(self, xml_body, target_config):
        return self.mgr.edit_config(xml_body, target=target_config, default_operation="merge")