#!/usr/bin/python
import lutin.module as module
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

/usr/bin/perl ../util/mkbuildinf.pl "gcc -Iopenssl/crypto -Iopenssl -Iopenssl/include -DOPENSSL_THREADS -D_REENTRANT -DDSO_DLFCN -DHAVE_DLFCN_H -Wa,--noexecstack -m64 -DL_ENDIAN -O3 -Wall -DOPENSSL_IA32_SSE2 -DOPENSSL_BN_ASM_MONT -DOPENSSL_BN_ASM_MONT5 -DOPENSSL_BN_ASM_GF2m -DSHA1_ASM -DSHA256_ASM -DSHA512_ASM -DMD5_ASM -DAES_ASM -DVPAES_ASM -DBSAES_ASM -DWHIRLPOOL_ASM -DGHASH_ASM" "linux-x86_64" >buildinf.h
-Iopenssl/crypto -Iopenssl -Iopenssl/include -DOPENSSL_THREADS -D_REENTRANT -DDSO_DLFCN -DHAVE_DLFCN_H -Wa,--noexecstack -m64 -DL_ENDIAN -O3 -Wall -DOPENSSL_IA32_SSE2 -DOPENSSL_BN_ASM_MONT -DOPENSSL_BN_ASM_MONT5 -DOPENSSL_BN_ASM_GF2m -DSHA1_ASM -DSHA256_ASM -DSHA512_ASM -DMD5_ASM -DAES_ASM -DVPAES_ASM -DBSAES_ASM -DWHIRLPOOL_ASM -DGHASH_ASM -c -o 

def generate_x86_64cpuid.s

def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	
	my_module.add_prebuild_action(
	    src="openssl/crypto/x86_64cpuid.pl",
	    dst=
	
	my_module.add_src_file([
	    'openssl/crypto/cryptlib.c',
	    'openssl/crypto/mem.c',
	    'openssl/crypto/mem_dbg.c',
	    'openssl/crypto/cversion.c',
	    'openssl/crypto/ex_data.c',
	    'openssl/crypto/cpt_err.c',
	    'openssl/crypto/ebcdic.c',
	    'openssl/crypto/uid.c',
	    'openssl/crypto/o_time.c',
	    'openssl/crypto/o_str.c',
	    'openssl/crypto/o_dir.c',
	    'openssl/crypto/o_fips.c',
	    'openssl/crypto/o_init.c',
	    'openssl/crypto/fips_ers.c',
/usr/bin/perl openssl/crypto/x86_64cpuid.pl elf > x86_64cpuid.s
	    'x86_64cpuid.s',
	    ])
	my_module.compile_flags('c', [
	    '-Dlibcurl_EXPORTS',
	    '-DBUILDING_LIBCURL',
	    '-DHAVE_CONFIG_H',
	    ])
	my_module.compile_version("c", 1989, gnu=True)
	my_module.add_module_depend('z')
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "curl", "lib"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "curl", "include"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "curl", "include", "curl"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "generate"))
	my_module.add_header_file([
	    'curl/include/curl/mprintf.h',
	    'curl/include/curl/curlver.h',
	    'curl/include/curl/multi.h',
	    'curl/include/curl/curl.h',
	    'curl/include/curl/curlrules.h',
	    'curl/include/curl/typecheck-gcc.h',
	    'curl/include/curl/easy.h',
	    'curl/lib/curl_setup.h',
	    'generate/curlbuild.h',
	    ],
	    destination_path="curl")
	return my_module
