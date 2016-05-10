#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os


def get_type():
	return "BINARY"

def get_sub_type():
	return "SAMPLE"

def get_desc():
	return "open SSL crypto library"

def get_licence():
	return "BSD like + notif"

def get_compagny_type():
	return "org"

def get_compagny_name():
	return "openssl"

def get_maintainer():
	return ["XXX XXX<rt@openssl.org>"]

def get_version():
	return [1,0,2]




def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	my_module.add_src_file([
	    'openssl/apps/apps.c',
	    'openssl/apps/app_rand.c',
	    'openssl/apps/dh.c',
	    ])
	my_module.compile_version("c", 1989, gnu=True)
	my_module.add_module_depend('openssl')
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "openssl", "apps"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "openssl/crypto"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "openssl"))
	return my_module
