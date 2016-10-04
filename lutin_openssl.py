#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os


def get_type():
	return "LIBRARY"

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
	    'openssl/ssl/s2_meth.c',
	    'openssl/ssl/s2_srvr.c',
	    'openssl/ssl/s2_clnt.c',
	    'openssl/ssl/s2_lib.c',
	    'openssl/ssl/s2_enc.c',
	    'openssl/ssl/s2_pkt.c',
	    'openssl/ssl/s3_meth.c',
	    'openssl/ssl/s3_srvr.c',
	    'openssl/ssl/s3_clnt.c',
	    'openssl/ssl/s3_lib.c',
	    'openssl/ssl/s3_enc.c',
	    'openssl/ssl/s3_pkt.c',
	    'openssl/ssl/s3_both.c',
	    'openssl/ssl/s3_cbc.c',
	    'openssl/ssl/s23_meth.c',
	    'openssl/ssl/s23_srvr.c',
	    'openssl/ssl/s23_clnt.c',
	    'openssl/ssl/s23_lib.c',
	    'openssl/ssl/s23_pkt.c',
	    'openssl/ssl/t1_meth.c',
	    'openssl/ssl/t1_srvr.c',
	    'openssl/ssl/t1_clnt.c',
	    'openssl/ssl/t1_lib.c',
	    'openssl/ssl/t1_enc.c',
	    'openssl/ssl/d1_meth.c',
	    'openssl/ssl/d1_srvr.c',
	    'openssl/ssl/d1_clnt.c',
	    'openssl/ssl/d1_lib.c',
	    'openssl/ssl/d1_pkt.c',
	    'openssl/ssl/d1_both.c',
	    'openssl/ssl/d1_enc.c',
	    'openssl/ssl/d1_srtp.c',
	    'openssl/ssl/ssl_lib.c',
	    'openssl/ssl/ssl_err2.c',
	    'openssl/ssl/ssl_cert.c',
	    'openssl/ssl/ssl_sess.c',
	    'openssl/ssl/ssl_ciph.c',
	    'openssl/ssl/ssl_stat.c',
	    'openssl/ssl/ssl_rsa.c',
	    'openssl/ssl/ssl_asn1.c',
	    'openssl/ssl/ssl_txt.c',
	    'openssl/ssl/ssl_algs.c',
	    'openssl/ssl/bio_ssl.c',
	    'openssl/ssl/ssl_err.c',
	    'openssl/ssl/kssl.c',
	    'openssl/ssl/tls_srp.c',
	    'openssl/ssl/t1_reneg.c',
	    'openssl/ssl/ssl_utst.c'
	    ])
	
	my_module.add_header_file([
	    'openssl/ssl/dtls1.h',
	    'openssl/ssl/kssl.h',
	    'openssl/ssl/srtp.h',
	    'openssl/ssl/ssl.h',
	    'openssl/ssl/ssl2.h',
	    'openssl/ssl/ssl23.h',
	    'openssl/ssl/ssl3.h',
	    'openssl/ssl/tls1.h',
	    ],
	    destination_path="openssl")
	
	my_module.compile_version("c", 1989, gnu=True)
	my_module.add_depend('crypto')
	my_module.add_path("openssl/apps")
	my_module.add_path("openssl/crypto")
	my_module.add_path("openssl")
	
	return True
