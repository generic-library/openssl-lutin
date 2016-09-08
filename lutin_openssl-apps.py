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
	    'openssl/apps/speed.c',
	    ])
	"""
	    'openssl/apps/s_client.c',
	    'openssl/apps/speed.c',
	    'openssl/apps/apps.c',
	    'openssl/apps/version.c',
	    'openssl/apps/sess_id.c',
	    'openssl/apps/ciphers.c',
	    'openssl/apps/nseq.c',
	    'openssl/apps/pkcs12.c',
	    'openssl/apps/pkcs8.c',
	    'openssl/apps/pkey.c',
	    'openssl/apps/pkeyparam.c',
	    'openssl/apps/pkeyutl.c',
	    'openssl/apps/spkac.c',
	    'openssl/apps/smime.c',
	    'openssl/apps/cms.c',
	    'openssl/apps/rand.c',
	    'openssl/apps/engine.c',
	    'openssl/apps/ocsp.c',
	    'openssl/apps/prime.c',
	    'openssl/apps/ts.c',
	    'openssl/apps/srp.c',
	    'openssl/apps/openssl.c'
	"""
	my_module.compile_version("c", 1989, gnu=True)
	my_module.add_depend('openssl')
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "openssl", "apps"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "openssl/crypto"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "openssl"))
	return my_module
