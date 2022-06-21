#!/usr/bin/env python
# encoding: utf-8

import yaml


def get_paramerters_from_yaml(yml_file):
    """Serialization of yaml files.

         The function serialize all files contained in a given directory if nom_fichier is empty
         Each yaml file (a team sheet) is serialized and added to the end of a list

         :param nom_fichier: (str) name of yaml file to serialize
         :return dict_serialize: (dict) name of the dictionnary resulting from the serialization
         :example: get_paramerters_from_yaml("config.yml")

     """

    with open(yml_file, encoding='utf-8') as file_id:
        dict_serialize = yaml.load(file_id, Loader=yaml.FullLoader)
        file_id.close()

    return dict_serialize

# dico = get_paramerters_from_yaml("config_tests.yml")
# print(dico)
# print(dico.get("host"))
