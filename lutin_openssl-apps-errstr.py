#!/usr/bin/python
import realog.debug as debug
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


def configure(target, my_module):
	my_module.add_src_file([
	    'openssl/apps/apps.c',
	    'openssl/apps/app_rand.c',
	    #'openssl/apps/genpkey.c',
	    'openssl/apps/errstr.c',
	    ])
	my_module.compile_version("c", 1989, gnu=True)
	my_module.add_depend('openssl')
	my_module.add_path("openssl/apps")
	my_module.add_path("openssl/crypto")
	my_module.add_path("openssl")
	return True
