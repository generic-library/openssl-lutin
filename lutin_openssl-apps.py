#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os


def get_type():
	return "BINARY"

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
	"""
	my_module.add_prebuild_action(
	    src="openssl/crypto/x86_64cpuid.pl",
	    dst=
	"""
	
	#line(---) = gcc -DMONOLITH -I.. -I../include -DOPENSSL_THREADS -D_REENTRANT -DDSO_DLFCN -DHAVE_DLFCN_H -Wa,--noexecstack -m64 -DL_ENDIAN -O3 -Wall -DOPENSSL_IA32_SSE2 -DOPENSSL_BN_ASM_MONT -DOPENSSL_BN_ASM_MONT5 -DOPENSSL_BN_ASM_GF2m -DSHA1_ASM -DSHA256_ASM -DSHA512_ASM -DMD5_ASM -DAES_ASM -DVPAES_ASM -DBSAES_ASM -DWHIRLPOOL_ASM -DGHASH_ASM -c -o
	my_module.add_src_file([
	    'openssl/apps/apps.c',
	    'openssl/apps/verify.c',
	    ])
	my_module.compile_flags('c', [
	    '-DOPENSSL_NO_ASM',
	    ])
	my_module.compile_flags('link', [
	    '-ldl',
	    ])
	"""
	    'openssl/apps/asn1pars.c',
	    'openssl/apps/req.c',
	    'openssl/apps/dgst.c',
	    'openssl/apps/dh.c',
	    'openssl/apps/dhparam.c',
	    'openssl/apps/enc.c',
	    'openssl/apps/passwd.c',
	    'openssl/apps/gendh.c',
	    'openssl/apps/errstr.c',
	    'openssl/apps/ca.c',
	    'openssl/apps/pkcs7.c',
	    'openssl/apps/crl2p7.c',
	    'openssl/apps/crl.c',
	    'openssl/apps/rsa.c',
	    'openssl/apps/rsautl.c',
	    'openssl/apps/dsa.c',
	    'openssl/apps/dsaparam.c',
	    'openssl/apps/ec.c',
	    'openssl/apps/ecparam.c',
	    'openssl/apps/x509.c',
	    'openssl/apps/genrsa.c',
	    'openssl/apps/gendsa.c',
	    'openssl/apps/genpkey.c',
	    'openssl/apps/s_server.c',
	    'openssl/apps/s_client.c',
	    'openssl/apps/speed.c',
	    'openssl/apps/s_time.c',
	    'openssl/apps/apps.c',
	    'openssl/apps/s_cb.c',
	    'openssl/apps/s_socket.c',
	    'openssl/apps/app_rand.c',
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
	my_module.add_module_depend('openssl')
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "openssl", "apps"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "openssl/crypto"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "openssl"))
	"""
	rm -f openssl
	shlib_target=; if [ -n "" ]; then \
		shlib_target="linux-shared"; \
	elif [ -n "" ]; then \
	 FIPSLD_CC="gcc"; CC=/usr/local/ssl/fips-2.0/bin/fipsld; export CC FIPSLD_CC; \
	fi; \
	LIBRARIES="-L.. -lssl -L.. -lcrypto" ; \
	make -f ../Makefile.shared -e \
		APPNAME=openssl OBJECTS="openssl.o verify.o asn1pars.o req.o dgst.o dh.o dhparam.o enc.o passwd.o gendh.o errstr.o ca.o pkcs7.o crl2p7.o crl.o rsa.o rsautl.o dsa.o dsaparam.o ec.o ecparam.o x509.o genrsa.o gendsa.o genpkey.o s_server.o s_client.o speed.o s_time.o apps.o s_cb.o s_socket.o app_rand.o version.o sess_id.o ciphers.o nseq.o pkcs12.o pkcs8.o pkey.o pkeyparam.o pkeyutl.o spkac.o smime.o cms.o rand.o engine.o ocsp.o prime.o ts.o srp.o" \
		LIBDEPS=" $LIBRARIES -ldl" \
		link_app.${shlib_target}
	make[2]: Entering directory '/home/heero/dev/perso/framework/openssl-lutin/openssl/apps'
	( :; LIBDEPS="${LIBDEPS:--L.. -lssl -L.. -lcrypto -ldl}"; LDCMD="${LDCMD:-gcc}"; LDFLAGS="${LDFLAGS:--DOPENSSL_THREADS -D_REENTRANT -DDSO_DLFCN -DHAVE_DLFCN_H -Wa,--noexecstack -m64 -DL_ENDIAN -O3 -Wall -DOPENSSL_IA32_SSE2 -DOPENSSL_BN_ASM_MONT -DOPENSSL_BN_ASM_MONT5 -DOPENSSL_BN_ASM_GF2m -DSHA1_ASM -DSHA256_ASM -DSHA512_ASM -DMD5_ASM -DAES_ASM -DVPAES_ASM -DBSAES_ASM -DWHIRLPOOL_ASM -DGHASH_ASM}"; LIBPATH=`for x in $LIBDEPS; do echo $x; done | sed -e 's/^ *-L//;t' -e d | uniq`; LIBPATH=`echo $LIBPATH | sed -e 's/ /:/g'`; LD_LIBRARY_PATH=$LIBPATH:$LD_LIBRARY_PATH ${LDCMD} ${LDFLAGS} -o ${APPNAME:=openssl} openssl.o verify.o asn1pars.o req.o dgst.o dh.o dhparam.o enc.o passwd.o gendh.o errstr.o ca.o pkcs7.o crl2p7.o crl.o rsa.o rsautl.o dsa.o dsaparam.o ec.o ecparam.o x509.o genrsa.o gendsa.o genpkey.o s_server.o s_client.o speed.o s_time.o apps.o s_cb.o s_socket.o app_rand.o version.o sess_id.o ciphers.o nseq.o pkcs12.o pkcs8.o pkey.o pkeyparam.o pkeyutl.o spkac.o smime.o cms.o rand.o engine.o ocsp.o prime.o ts.o srp.o ${LIBDEPS} )
	make[2]: Leaving directory '/home/heero/dev/perso/framework/openssl-lutin/openssl/apps'
	make[2]: Entering directory '/home/heero/dev/perso/framework/openssl-lutin/openssl'
	Doing certs/demo
	pca-cert.pem => e83ef475.0
	ca-cert.pem => 3f77a2b5.0
	dsa-ca.pem => cbdbd8bc.0
	dsa-pca.pem => de4fa23b.0
	make[2]: Leaving directory '/home/heero/dev/perso/framework/openssl-lutin/openssl'
	make[1]: Leaving directory '/home/heero/dev/perso/framework/openssl-lutin/openssl/apps'
	"""

	return my_module
