#!/usr/bin/env python
# encoding: utf-8

from jinja2 import Environment, FileSystemLoader


def instanciate_template_jinja(dir_template, template_file):
    env = Environment(loader=FileSystemLoader(dir_template))
    template = env.get_template(template_file)
    return template
