#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

#Windows build : CROSS_COMPILE="x86_64-w64-mingw32-" ./Configure mingw64 no-asm shared --prefix=/opt/mingw6

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
	"""
	my_module.add_prebuild_action(
	    src="openssl/crypto/x86_64cpuid.pl",
	    dst=
	"""
	
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
	    'openssl/crypto/mem_clr.c',
	    ])
	#/usr/bin/perl openssl/crypto/x86_64cpuid.pl elf > x86_64cpuid.s
	my_module.add_src_file([
	    'openssl/crypto/objects/o_names.c',
	    'openssl/crypto/objects/obj_dat.c',
	    'openssl/crypto/objects/obj_lib.c',
	    'openssl/crypto/objects/obj_err.c',
	    'openssl/crypto/objects/obj_xref.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/md4/md4_dgst.c',
	    'openssl/crypto/md4/md4_one.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/md5/md5_dgst.c',
	    'openssl/crypto/md5/md5_one.c',
	    ])
	#/usr/bin/perl openssl/crypto/md5/asm/md5-x86_64.pl elf > md5-x86_64.s
	my_module.add_src_file([
	    'openssl/crypto/sha/sha_dgst.c',
	    'openssl/crypto/sha/sha1dgst.c',
	    'openssl/crypto/sha/sha_one.c',
	    'openssl/crypto/sha/sha1_one.c',
	    'openssl/crypto/sha/sha256.c',
	    'openssl/crypto/sha/sha512.c',
	    ])
	#/usr/bin/perl openssl/crypto/sha/asm/sha1-x86_64.pl elf > sha1-x86_64.s
	#/usr/bin/perl openssl/crypto/sha/asm/sha512-x86_64.pl elf sha256-x86_64.s
	#/usr/bin/perl openssl/crypto/sha/asm/sha512-x86_64.pl elf sha512-x86_64.s
	my_module.add_src_file([
	    'openssl/crypto/mdc2/mdc2dgst.c',
	    'openssl/crypto/mdc2/mdc2_one.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/hmac/hmac.c',
	    'openssl/crypto/hmac/hm_ameth.c',
	    'openssl/crypto/hmac/hm_pmeth.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/ripemd/rmd_dgst.c',
	    'openssl/crypto/ripemd/rmd_one.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/whrlpool/wp_dgst.c',
	    'openssl/crypto/whrlpool/wp_block.c',# add if no asm
	    ])
	#/usr/bin/perl openssl/crypto/whrlpool/asm/wp-x86_64.pl elf > wp-x86_64.s
	my_module.add_src_file([
	    'openssl/crypto/des/set_key.c',
	    'openssl/crypto/des/ecb_enc.c',
	    'openssl/crypto/des/cbc_enc.c',
	    'openssl/crypto/des/ecb3_enc.c',
	    'openssl/crypto/des/cfb64enc.c',
	    'openssl/crypto/des/cfb64ede.c',
	    'openssl/crypto/des/cfb_enc.c',
	    'openssl/crypto/des/ofb64ede.c',
	    'openssl/crypto/des/enc_read.c',
	    'openssl/crypto/des/enc_writ.c',
	    'openssl/crypto/des/ofb64enc.c',
	    'openssl/crypto/des/ofb_enc.c',
	    'openssl/crypto/des/str2key.c',
	    'openssl/crypto/des/pcbc_enc.c',
	    'openssl/crypto/des/qud_cksm.c',
	    'openssl/crypto/des/rand_key.c',
	    'openssl/crypto/des/des_enc.c',
	    'openssl/crypto/des/fcrypt_b.c',
	    'openssl/crypto/des/fcrypt.c',
	    'openssl/crypto/des/xcbc_enc.c',
	    'openssl/crypto/des/rpc_enc.c',
	    'openssl/crypto/des/cbc_cksm.c',
	    'openssl/crypto/des/ede_cbcm_enc.c',
	    'openssl/crypto/des/des_old.c',
	    'openssl/crypto/des/des_old2.c',
	    'openssl/crypto/des/read2pwd.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/aes/aes_core.c', # add if no asm
	    'openssl/crypto/aes/aes_cbc.c', # add if no asm
	    'openssl/crypto/aes/aes_misc.c',
	    'openssl/crypto/aes/aes_ecb.c',
	    'openssl/crypto/aes/aes_cfb.c',
	    'openssl/crypto/aes/aes_ofb.c',
	    'openssl/crypto/aes/aes_ctr.c',
	    'openssl/crypto/aes/aes_ige.c',
	    'openssl/crypto/aes/aes_wrap.c',
	    ])
	#/usr/bin/perl openssl/crypto/aes/asm/aes-x86_64.pl elf > aes-x86_64.s
	#/usr/bin/perl openssl/crypto/aes/asm/vpaes-x86_64.pl elf > vpaes-x86_64.s
	#/usr/bin/perl openssl/crypto/aes/asm/bsaes-x86_64.pl elf > bsaes-x86_64.s
	#/usr/bin/perl openssl/crypto/aes/asm/aesni-x86_64.pl elf > aesni-x86_64.s
	#/usr/bin/perl openssl/crypto/aes/asm/aesni-sha1-x86_64.pl elf > aesni-sha1-x86_64.s
	my_module.add_src_file([
	    'openssl/crypto/rc2/rc2_ecb.c',
	    'openssl/crypto/rc2/rc2_skey.c',
	    'openssl/crypto/rc2/rc2_cbc.c',
	    'openssl/crypto/rc2/rc2cfb64.c',
	    'openssl/crypto/rc2/rc2ofb64.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/rc4/rc4_utl.c',
	    'openssl/crypto/rc4/rc4_skey.c', # add if no asm
	    'openssl/crypto/rc4/rc4_enc.c', # add if no asm
	    ])
	#/usr/bin/perl openssl/crypto/rc4/asm/rc4-x86_64.pl elf > rc4-x86_64.s
	#/usr/bin/perl openssl/crypto/rc4/asm/rc4-md5-x86_64.pl elf > rc4-md5-x86_64.s
	my_module.add_src_file([
	    'openssl/crypto/idea/i_cbc.c',
	    'openssl/crypto/idea/i_cfb64.c',
	    'openssl/crypto/idea/i_ofb64.c',
	    'openssl/crypto/idea/i_ecb.c',
	    'openssl/crypto/idea/i_skey.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/bf/bf_skey.c',
	    'openssl/crypto/bf/bf_ecb.c',
	    'openssl/crypto/bf/bf_enc.c',
	    'openssl/crypto/bf/bf_cfb64.c',
	    'openssl/crypto/bf/bf_ofb64.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/cast/c_skey.c',
	    'openssl/crypto/cast/c_ecb.c',
	    'openssl/crypto/cast/c_enc.c',
	    'openssl/crypto/cast/c_cfb64.c',
	    'openssl/crypto/cast/c_ofb64.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/camellia/camellia.c', # add if no asm
	    'openssl/crypto/camellia/cmll_cbc.c', # add if no asm
	    'openssl/crypto/camellia/cmll_ecb.c',
	    'openssl/crypto/camellia/cmll_ofb.c',
	    'openssl/crypto/camellia/cmll_cfb.c',
	    'openssl/crypto/camellia/cmll_ctr.c',
	    'openssl/crypto/camellia/cmll_utl.c',
	    'openssl/crypto/camellia/cmll_misc.c',
	    ])
	#/usr/bin/perl openssl/crypto/camellia/asm/cmll-x86_64.pl elf > cmll-x86_64.s
	my_module.add_src_file([
	    'openssl/crypto/seed/seed.c',
	    'openssl/crypto/seed/seed_ecb.c',
	    'openssl/crypto/seed/seed_cbc.c',
	    'openssl/crypto/seed/seed_cfb.c',
	    'openssl/crypto/seed/seed_ofb.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/modes/cbc128.c',
	    'openssl/crypto/modes/ctr128.c',
	    'openssl/crypto/modes/cts128.c',
	    'openssl/crypto/modes/cfb128.c',
	    'openssl/crypto/modes/ofb128.c',
	    'openssl/crypto/modes/gcm128.c',
	    'openssl/crypto/modes/ccm128.c',
	    'openssl/crypto/modes/xts128.c',
	    ])
	#/usr/bin/perl openssl/crypto/modes/asm/ghash-x86_64.pl elf > ghash-x86_64.s
	my_module.add_src_file([
	    'openssl/crypto/bn/bn_add.c',
	    'openssl/crypto/bn/bn_div.c',
	    'openssl/crypto/bn/bn_exp.c',
	    'openssl/crypto/bn/bn_lib.c',
	    'openssl/crypto/bn/bn_ctx.c',
	    'openssl/crypto/bn/bn_mul.c',
	    'openssl/crypto/bn/bn_mod.c',
	    'openssl/crypto/bn/bn_print.c',
	    'openssl/crypto/bn/bn_rand.c',
	    'openssl/crypto/bn/bn_shift.c',
	    'openssl/crypto/bn/bn_word.c',
	    'openssl/crypto/bn/bn_blind.c',
	    'openssl/crypto/bn/bn_kron.c',
	    'openssl/crypto/bn/bn_sqrt.c',
	    'openssl/crypto/bn/bn_gcd.c',
	    'openssl/crypto/bn/bn_prime.c',
	    'openssl/crypto/bn/bn_err.c',
	    'openssl/crypto/bn/bn_sqr.c',
	    'openssl/crypto/bn/bn_asm.c', # or for x86 'openssl/crypto/bn/asm/x86_64-gcc.c', # I do not understand why ...
	    'openssl/crypto/bn/bn_recp.c',
	    'openssl/crypto/bn/bn_mont.c',
	    'openssl/crypto/bn/bn_mpi.c',
	    'openssl/crypto/bn/bn_exp2.c',
	    'openssl/crypto/bn/bn_gf2m.c',
	    'openssl/crypto/bn/bn_nist.c',
	    'openssl/crypto/bn/bn_depr.c',
	    'openssl/crypto/bn/bn_const.c',
	    'openssl/crypto/bn/bn_x931p.c',
	    ])
	#/usr/bin/perl openssl/crypto/bn/asm/x86_64-mont.pl elf > x86_64-mont.s
	#/usr/bin/perl openssl/crypto/bn/asm/x86_64-mont5.pl elf > x86_64-mont5.s
	#/usr/bin/perl openssl/crypto/bn/asm/x86_64-gf2m.pl elf > x86_64-gf2m.s
	#/usr/bin/perl openssl/crypto/bn/asm/modexp512-x86_64.pl elf > modexp512-x86_64.s
	my_module.add_src_file([
	    'openssl/crypto/ec/ec_lib.c',
	    'openssl/crypto/ec/ecp_smpl.c',
	    'openssl/crypto/ec/ecp_mont.c',
	    'openssl/crypto/ec/ecp_nist.c',
	    'openssl/crypto/ec/ec_cvt.c',
	    'openssl/crypto/ec/ec_mult.c',
	    'openssl/crypto/ec/ec_err.c',
	    'openssl/crypto/ec/ec_curve.c',
	    'openssl/crypto/ec/ec_check.c',
	    'openssl/crypto/ec/ec_print.c',
	    'openssl/crypto/ec/ec_asn1.c',
	    'openssl/crypto/ec/ec_key.c',
	    'openssl/crypto/ec/ec2_smpl.c',
	    'openssl/crypto/ec/ec2_mult.c',
	    'openssl/crypto/ec/ec_ameth.c',
	    'openssl/crypto/ec/ec_pmeth.c',
	    'openssl/crypto/ec/eck_prn.c',
	    'openssl/crypto/ec/ecp_nistp224.c',
	    'openssl/crypto/ec/ecp_nistp256.c',
	    'openssl/crypto/ec/ecp_nistp521.c',
	    'openssl/crypto/ec/ecp_nistputil.c',
	    'openssl/crypto/ec/ecp_oct.c',
	    'openssl/crypto/ec/ec2_oct.c',
	    'openssl/crypto/ec/ec_oct.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/rsa/rsa_eay.c',
	    'openssl/crypto/rsa/rsa_gen.c',
	    'openssl/crypto/rsa/rsa_lib.c',
	    'openssl/crypto/rsa/rsa_sign.c',
	    'openssl/crypto/rsa/rsa_saos.c',
	    'openssl/crypto/rsa/rsa_err.c',
	    'openssl/crypto/rsa/rsa_pk1.c',
	    'openssl/crypto/rsa/rsa_ssl.c',
	    'openssl/crypto/rsa/rsa_none.c',
	    'openssl/crypto/rsa/rsa_oaep.c',
	    'openssl/crypto/rsa/rsa_chk.c',
	    'openssl/crypto/rsa/rsa_null.c',
	    'openssl/crypto/rsa/rsa_pss.c',
	    'openssl/crypto/rsa/rsa_x931.c',
	    'openssl/crypto/rsa/rsa_asn1.c',
	    'openssl/crypto/rsa/rsa_depr.c',
	    'openssl/crypto/rsa/rsa_ameth.c',
	    'openssl/crypto/rsa/rsa_prn.c',
	    'openssl/crypto/rsa/rsa_pmeth.c',
	    'openssl/crypto/rsa/rsa_crpt.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/dsa/dsa_gen.c',
	    'openssl/crypto/dsa/dsa_key.c',
	    'openssl/crypto/dsa/dsa_lib.c',
	    'openssl/crypto/dsa/dsa_asn1.c',
	    'openssl/crypto/dsa/dsa_vrf.c',
	    'openssl/crypto/dsa/dsa_sign.c',
	    'openssl/crypto/dsa/dsa_err.c',
	    'openssl/crypto/dsa/dsa_ossl.c',
	    'openssl/crypto/dsa/dsa_depr.c',
	    'openssl/crypto/dsa/dsa_ameth.c',
	    'openssl/crypto/dsa/dsa_pmeth.c',
	    'openssl/crypto/dsa/dsa_prn.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/ecdsa/ecs_lib.c',
	    'openssl/crypto/ecdsa/ecs_asn1.c',
	    'openssl/crypto/ecdsa/ecs_ossl.c',
	    'openssl/crypto/ecdsa/ecs_sign.c',
	    'openssl/crypto/ecdsa/ecs_vrf.c',
	    'openssl/crypto/ecdsa/ecs_err.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/dh/dh_asn1.c',
	    'openssl/crypto/dh/dh_gen.c',
	    'openssl/crypto/dh/dh_key.c',
	    'openssl/crypto/dh/dh_lib.c',
	    'openssl/crypto/dh/dh_check.c',
	    'openssl/crypto/dh/dh_err.c',
	    'openssl/crypto/dh/dh_depr.c',
	    'openssl/crypto/dh/dh_ameth.c',
	    'openssl/crypto/dh/dh_pmeth.c',
	    'openssl/crypto/dh/dh_prn.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/ecdh/ech_lib.c',
	    'openssl/crypto/ecdh/ech_ossl.c',
	    'openssl/crypto/ecdh/ech_key.c',
	    'openssl/crypto/ecdh/ech_err.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/dso/dso_dl.c',
	    'openssl/crypto/dso/dso_dlfcn.c',
	    'openssl/crypto/dso/dso_err.c',
	    'openssl/crypto/dso/dso_lib.c',
	    'openssl/crypto/dso/dso_null.c',
	    'openssl/crypto/dso/dso_openssl.c',
	    'openssl/crypto/dso/dso_win32.c',
	    'openssl/crypto/dso/dso_vms.c',
	    'openssl/crypto/dso/dso_beos.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/engine/eng_err.c',
	    'openssl/crypto/engine/eng_lib.c',
	    'openssl/crypto/engine/eng_list.c',
	    'openssl/crypto/engine/eng_init.c',
	    'openssl/crypto/engine/eng_ctrl.c',
	    'openssl/crypto/engine/eng_table.c',
	    'openssl/crypto/engine/eng_pkey.c',
	    'openssl/crypto/engine/eng_fat.c',
	    'openssl/crypto/engine/eng_all.c',
	    'openssl/crypto/engine/tb_rsa.c',
	    'openssl/crypto/engine/tb_dsa.c',
	    'openssl/crypto/engine/tb_ecdsa.c',
	    'openssl/crypto/engine/tb_dh.c',
	    'openssl/crypto/engine/tb_ecdh.c',
	    'openssl/crypto/engine/tb_rand.c',
	    'openssl/crypto/engine/tb_store.c',
	    'openssl/crypto/engine/tb_cipher.c',
	    'openssl/crypto/engine/tb_digest.c',
	    'openssl/crypto/engine/tb_pkmeth.c',
	    'openssl/crypto/engine/tb_asnmth.c',
	    'openssl/crypto/engine/eng_openssl.c',
	    'openssl/crypto/engine/eng_cnf.c',
	    'openssl/crypto/engine/eng_dyn.c',
	    'openssl/crypto/engine/eng_cryptodev.c',
	    'openssl/crypto/engine/eng_rsax.c',
	    'openssl/crypto/engine/eng_rdrand.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/buffer/buffer.c',
	    'openssl/crypto/buffer/buf_str.c',
	    'openssl/crypto/buffer/buf_err.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/bio/bio_lib.c',
	    'openssl/crypto/bio/bio_cb.c',
	    'openssl/crypto/bio/bio_err.c',
	    'openssl/crypto/bio/bss_mem.c',
	    'openssl/crypto/bio/bss_null.c',
	    'openssl/crypto/bio/bss_fd.c',
	    'openssl/crypto/bio/bss_file.c',
	    'openssl/crypto/bio/bss_sock.c',
	    'openssl/crypto/bio/bss_conn.c',
	    'openssl/crypto/bio/bf_null.c',
	    'openssl/crypto/bio/bf_buff.c',
	    'openssl/crypto/bio/b_print.c',
	    'openssl/crypto/bio/b_dump.c',
	    'openssl/crypto/bio/b_sock.c',
	    'openssl/crypto/bio/bss_acpt.c',
	    'openssl/crypto/bio/bf_nbio.c',
	    'openssl/crypto/bio/bss_log.c',
	    'openssl/crypto/bio/bss_bio.c',
	    'openssl/crypto/bio/bss_dgram.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/stack/stack.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/lhash/lhash.c',
	    'openssl/crypto/lhash/lh_stats.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/rand/md_rand.c',
	    'openssl/crypto/rand/randfile.c',
	    'openssl/crypto/rand/rand_lib.c',
	    'openssl/crypto/rand/rand_err.c',
	    'openssl/crypto/rand/rand_egd.c',
	    'openssl/crypto/rand/rand_win.c',
	    'openssl/crypto/rand/rand_unix.c',
	    'openssl/crypto/rand/rand_os2.c',
	    'openssl/crypto/rand/rand_nw.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/err/err.c',
	    'openssl/crypto/err/err_all.c',
	    'openssl/crypto/err/err_prn.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/evp/encode.c',
	    'openssl/crypto/evp/digest.c',
	    'openssl/crypto/evp/evp_enc.c',
	    'openssl/crypto/evp/evp_key.c',
	    'openssl/crypto/evp/evp_acnf.c',
	    'openssl/crypto/evp/evp_cnf.c',
	    'openssl/crypto/evp/e_des.c',
	    'openssl/crypto/evp/e_bf.c',
	    'openssl/crypto/evp/e_idea.c',
	    'openssl/crypto/evp/e_des3.c',
	    'openssl/crypto/evp/e_camellia.c',
	    'openssl/crypto/evp/e_rc4.c',
	    'openssl/crypto/evp/e_aes.c',
	    'openssl/crypto/evp/names.c',
	    'openssl/crypto/evp/e_seed.c',
	    'openssl/crypto/evp/e_xcbc_d.c',
	    'openssl/crypto/evp/e_rc2.c',
	    'openssl/crypto/evp/e_cast.c',
	    'openssl/crypto/evp/e_rc5.c',
	    'openssl/crypto/evp/m_null.c',
	    'openssl/crypto/evp/m_md2.c',
	    'openssl/crypto/evp/m_md4.c',
	    'openssl/crypto/evp/m_md5.c',
	    'openssl/crypto/evp/m_sha.c',
	    'openssl/crypto/evp/m_sha1.c',
	    'openssl/crypto/evp/m_wp.c',
	    'openssl/crypto/evp/m_dss.c',
	    'openssl/crypto/evp/m_dss1.c',
	    'openssl/crypto/evp/m_mdc2.c',
	    'openssl/crypto/evp/m_ripemd.c',
	    'openssl/crypto/evp/m_ecdsa.c',
	    'openssl/crypto/evp/p_open.c',
	    'openssl/crypto/evp/p_seal.c',
	    'openssl/crypto/evp/p_sign.c',
	    'openssl/crypto/evp/p_verify.c',
	    'openssl/crypto/evp/p_lib.c',
	    'openssl/crypto/evp/p_enc.c',
	    'openssl/crypto/evp/p_dec.c',
	    'openssl/crypto/evp/bio_md.c',
	    'openssl/crypto/evp/bio_b64.c',
	    'openssl/crypto/evp/bio_enc.c',
	    'openssl/crypto/evp/evp_err.c',
	    'openssl/crypto/evp/e_null.c',
	    'openssl/crypto/evp/c_all.c',
	    'openssl/crypto/evp/c_allc.c',
	    'openssl/crypto/evp/c_alld.c',
	    'openssl/crypto/evp/evp_lib.c',
	    'openssl/crypto/evp/bio_ok.c',
	    'openssl/crypto/evp/evp_pkey.c',
	    'openssl/crypto/evp/evp_pbe.c',
	    'openssl/crypto/evp/p5_crpt.c',
	    'openssl/crypto/evp/p5_crpt2.c',
	    'openssl/crypto/evp/e_old.c',
	    'openssl/crypto/evp/pmeth_lib.c',
	    'openssl/crypto/evp/pmeth_fn.c',
	    'openssl/crypto/evp/pmeth_gn.c',
	    'openssl/crypto/evp/m_sigver.c',
	    'openssl/crypto/evp/evp_fips.c',
	    'openssl/crypto/evp/e_aes_cbc_hmac_sha1.c',
	    'openssl/crypto/evp/e_rc4_hmac_md5.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/asn1/a_object.c',
	    'openssl/crypto/asn1/a_bitstr.c',
	    'openssl/crypto/asn1/a_utctm.c',
	    'openssl/crypto/asn1/a_gentm.c',
	    'openssl/crypto/asn1/a_time.c',
	    'openssl/crypto/asn1/a_int.c',
	    'openssl/crypto/asn1/a_octet.c',
	    'openssl/crypto/asn1/a_print.c',
	    'openssl/crypto/asn1/a_type.c',
	    'openssl/crypto/asn1/a_set.c',
	    'openssl/crypto/asn1/a_dup.c',
	    'openssl/crypto/asn1/a_d2i_fp.c',
	    'openssl/crypto/asn1/a_i2d_fp.c',
	    'openssl/crypto/asn1/a_enum.c',
	    'openssl/crypto/asn1/a_utf8.c',
	    'openssl/crypto/asn1/a_sign.c',
	    'openssl/crypto/asn1/a_digest.c',
	    'openssl/crypto/asn1/a_verify.c',
	    'openssl/crypto/asn1/a_mbstr.c',
	    'openssl/crypto/asn1/a_strex.c',
	    'openssl/crypto/asn1/x_algor.c',
	    'openssl/crypto/asn1/x_val.c',
	    'openssl/crypto/asn1/x_pubkey.c',
	    'openssl/crypto/asn1/x_sig.c',
	    'openssl/crypto/asn1/x_req.c',
	    'openssl/crypto/asn1/x_attrib.c',
	    'openssl/crypto/asn1/x_bignum.c',
	    'openssl/crypto/asn1/x_long.c',
	    'openssl/crypto/asn1/x_name.c',
	    'openssl/crypto/asn1/x_x509.c',
	    'openssl/crypto/asn1/x_x509a.c',
	    'openssl/crypto/asn1/x_crl.c',
	    'openssl/crypto/asn1/x_info.c',
	    'openssl/crypto/asn1/x_spki.c',
	    'openssl/crypto/asn1/nsseq.c',
	    'openssl/crypto/asn1/x_nx509.c',
	    'openssl/crypto/asn1/d2i_pu.c',
	    'openssl/crypto/asn1/d2i_pr.c',
	    'openssl/crypto/asn1/i2d_pu.c',
	    'openssl/crypto/asn1/i2d_pr.c',
	    'openssl/crypto/asn1/t_req.c',
	    'openssl/crypto/asn1/t_x509.c',
	    'openssl/crypto/asn1/t_x509a.c',
	    'openssl/crypto/asn1/t_crl.c',
	    'openssl/crypto/asn1/t_pkey.c',
	    'openssl/crypto/asn1/t_spki.c',
	    'openssl/crypto/asn1/t_bitst.c',
	    'openssl/crypto/asn1/tasn_new.c',
	    'openssl/crypto/asn1/tasn_fre.c',
	    'openssl/crypto/asn1/tasn_enc.c',
	    'openssl/crypto/asn1/tasn_dec.c',
	    'openssl/crypto/asn1/tasn_utl.c',
	    'openssl/crypto/asn1/tasn_typ.c',
	    'openssl/crypto/asn1/tasn_prn.c',
	    'openssl/crypto/asn1/ameth_lib.c',
	    'openssl/crypto/asn1/f_int.c',
	    'openssl/crypto/asn1/f_string.c',
	    'openssl/crypto/asn1/n_pkey.c',
	    'openssl/crypto/asn1/f_enum.c',
	    'openssl/crypto/asn1/x_pkey.c',
	    'openssl/crypto/asn1/a_bool.c',
	    'openssl/crypto/asn1/x_exten.c',
	    'openssl/crypto/asn1/bio_asn1.c',
	    'openssl/crypto/asn1/bio_ndef.c',
	    'openssl/crypto/asn1/asn_mime.c',
	    'openssl/crypto/asn1/asn1_gen.c',
	    'openssl/crypto/asn1/asn1_par.c',
	    'openssl/crypto/asn1/asn1_lib.c',
	    'openssl/crypto/asn1/asn1_err.c',
	    'openssl/crypto/asn1/a_bytes.c',
	    'openssl/crypto/asn1/a_strnid.c',
	    'openssl/crypto/asn1/evp_asn1.c',
	    'openssl/crypto/asn1/asn_pack.c',
	    'openssl/crypto/asn1/p5_pbe.c',
	    'openssl/crypto/asn1/p5_pbev2.c',
	    'openssl/crypto/asn1/p8_pkey.c',
	    'openssl/crypto/asn1/asn_moid.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/pem/pem_sign.c',
	    'openssl/crypto/pem/pem_seal.c',
	    'openssl/crypto/pem/pem_info.c',
	    'openssl/crypto/pem/pem_lib.c',
	    'openssl/crypto/pem/pem_all.c',
	    'openssl/crypto/pem/pem_err.c',
	    'openssl/crypto/pem/pem_x509.c',
	    'openssl/crypto/pem/pem_xaux.c',
	    'openssl/crypto/pem/pem_oth.c',
	    'openssl/crypto/pem/pem_pk8.c',
	    'openssl/crypto/pem/pem_pkey.c',
	    'openssl/crypto/pem/pvkfmt.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/x509/x509_def.c',
	    'openssl/crypto/x509/x509_d2.c',
	    'openssl/crypto/x509/x509_r2x.c',
	    'openssl/crypto/x509/x509_cmp.c',
	    'openssl/crypto/x509/x509_obj.c',
	    'openssl/crypto/x509/x509_req.c',
	    'openssl/crypto/x509/x509spki.c',
	    'openssl/crypto/x509/x509_vfy.c',
	    'openssl/crypto/x509/x509_set.c',
	    'openssl/crypto/x509/x509cset.c',
	    'openssl/crypto/x509/x509rset.c',
	    'openssl/crypto/x509/x509_err.c',
	    'openssl/crypto/x509/x509name.c',
	    'openssl/crypto/x509/x509_v3.c',
	    'openssl/crypto/x509/x509_ext.c',
	    'openssl/crypto/x509/x509_att.c',
	    'openssl/crypto/x509/x509type.c',
	    'openssl/crypto/x509/x509_lu.c',
	    'openssl/crypto/x509/x_all.c',
	    'openssl/crypto/x509/x509_txt.c',
	    'openssl/crypto/x509/x509_trs.c',
	    'openssl/crypto/x509/by_file.c',
	    'openssl/crypto/x509/by_dir.c',
	    'openssl/crypto/x509/x509_vpm.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/x509v3/v3_bcons.c',
	    'openssl/crypto/x509v3/v3_bitst.c',
	    'openssl/crypto/x509v3/v3_conf.c',
	    'openssl/crypto/x509v3/v3_extku.c',
	    'openssl/crypto/x509v3/v3_ia5.c',
	    'openssl/crypto/x509v3/v3_lib.c',
	    'openssl/crypto/x509v3/v3_prn.c',
	    'openssl/crypto/x509v3/v3_utl.c',
	    'openssl/crypto/x509v3/v3err.c',
	    'openssl/crypto/x509v3/v3_genn.c',
	    'openssl/crypto/x509v3/v3_alt.c',
	    'openssl/crypto/x509v3/v3_skey.c',
	    'openssl/crypto/x509v3/v3_akey.c',
	    'openssl/crypto/x509v3/v3_pku.c',
	    'openssl/crypto/x509v3/v3_int.c',
	    'openssl/crypto/x509v3/v3_enum.c',
	    'openssl/crypto/x509v3/v3_sxnet.c',
	    'openssl/crypto/x509v3/v3_cpols.c',
	    'openssl/crypto/x509v3/v3_crld.c',
	    'openssl/crypto/x509v3/v3_purp.c',
	    'openssl/crypto/x509v3/v3_info.c',
	    'openssl/crypto/x509v3/v3_ocsp.c',
	    'openssl/crypto/x509v3/v3_akeya.c',
	    'openssl/crypto/x509v3/v3_pmaps.c',
	    'openssl/crypto/x509v3/v3_pcons.c',
	    'openssl/crypto/x509v3/v3_ncons.c',
	    'openssl/crypto/x509v3/v3_pcia.c',
	    'openssl/crypto/x509v3/v3_pci.c',
	    'openssl/crypto/x509v3/pcy_cache.c',
	    'openssl/crypto/x509v3/pcy_node.c',
	    'openssl/crypto/x509v3/pcy_data.c',
	    'openssl/crypto/x509v3/pcy_map.c',
	    'openssl/crypto/x509v3/pcy_tree.c',
	    'openssl/crypto/x509v3/pcy_lib.c',
	    'openssl/crypto/x509v3/v3_asid.c',
	    'openssl/crypto/x509v3/v3_addr.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/conf/conf_err.c',
	    'openssl/crypto/conf/conf_lib.c',
	    'openssl/crypto/conf/conf_api.c',
	    'openssl/crypto/conf/conf_def.c',
	    'openssl/crypto/conf/conf_mod.c',
	    'openssl/crypto/conf/conf_mall.c',
	    'openssl/crypto/conf/conf_sap.c',
	    'openssl/crypto/txt_db/txt_db.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/pkcs7/pk7_asn1.c',
	    'openssl/crypto/pkcs7/pk7_lib.c',
	    'openssl/crypto/pkcs7/pkcs7err.c',
	    'openssl/crypto/pkcs7/pk7_doit.c',
	    'openssl/crypto/pkcs7/pk7_smime.c',
	    'openssl/crypto/pkcs7/pk7_attr.c',
	    'openssl/crypto/pkcs7/pk7_mime.c',
	    'openssl/crypto/pkcs7/bio_pk7.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/pkcs12/p12_add.c',
	    'openssl/crypto/pkcs12/p12_asn.c',
	    'openssl/crypto/pkcs12/p12_attr.c',
	    'openssl/crypto/pkcs12/p12_crpt.c',
	    'openssl/crypto/pkcs12/p12_crt.c',
	    'openssl/crypto/pkcs12/p12_decr.c',
	    'openssl/crypto/pkcs12/p12_init.c',
	    'openssl/crypto/pkcs12/p12_key.c',
	    'openssl/crypto/pkcs12/p12_kiss.c',
	    'openssl/crypto/pkcs12/p12_mutl.c',
	    'openssl/crypto/pkcs12/p12_utl.c',
	    'openssl/crypto/pkcs12/p12_npas.c',
	    'openssl/crypto/pkcs12/pk12err.c',
	    'openssl/crypto/pkcs12/p12_p8d.c',
	    'openssl/crypto/pkcs12/p12_p8e.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/comp/comp_lib.c',
	    'openssl/crypto/comp/comp_err.c',
	    'openssl/crypto/comp/c_rle.c',
	    'openssl/crypto/comp/c_zlib.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/ocsp/ocsp_asn.c',
	    'openssl/crypto/ocsp/ocsp_ext.c',
	    'openssl/crypto/ocsp/ocsp_ht.c',
	    'openssl/crypto/ocsp/ocsp_lib.c',
	    'openssl/crypto/ocsp/ocsp_cl.c',
	    'openssl/crypto/ocsp/ocsp_srv.c',
	    'openssl/crypto/ocsp/ocsp_prn.c',
	    'openssl/crypto/ocsp/ocsp_vfy.c',
	    'openssl/crypto/ocsp/ocsp_err.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/ui/ui_err.c',
	    'openssl/crypto/ui/ui_lib.c',
	    'openssl/crypto/ui/ui_openssl.c',
	    'openssl/crypto/ui/ui_util.c',
	    'openssl/crypto/ui/ui_compat.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/krb5/krb5_asn.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/cms/cms_lib.c',
	    'openssl/crypto/cms/cms_asn1.c',
	    'openssl/crypto/cms/cms_att.c',
	    'openssl/crypto/cms/cms_io.c',
	    'openssl/crypto/cms/cms_smime.c',
	    'openssl/crypto/cms/cms_err.c',
	    'openssl/crypto/cms/cms_sd.c',
	    'openssl/crypto/cms/cms_dd.c',
	    'openssl/crypto/cms/cms_cd.c',
	    'openssl/crypto/cms/cms_env.c',
	    'openssl/crypto/cms/cms_enc.c',
	    'openssl/crypto/cms/cms_ess.c',
	    'openssl/crypto/cms/cms_pwri.c',
	    'openssl/crypto/pqueue/pqueue.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/ts/ts_err.c',
	    'openssl/crypto/ts/ts_req_utils.c',
	    'openssl/crypto/ts/ts_req_print.c',
	    'openssl/crypto/ts/ts_rsp_utils.c',
	    'openssl/crypto/ts/ts_rsp_print.c',
	    'openssl/crypto/ts/ts_rsp_sign.c',
	    'openssl/crypto/ts/ts_rsp_verify.c',
	    'openssl/crypto/ts/ts_verify_ctx.c',
	    'openssl/crypto/ts/ts_lib.c',
	    'openssl/crypto/ts/ts_conf.c',
	    'openssl/crypto/ts/ts_asn1.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/srp/srp_lib.c',
	    'openssl/crypto/srp/srp_vfy.c',
	    ])
	my_module.add_src_file([
	    'openssl/crypto/cmac/cmac.c',
	    'openssl/crypto/cmac/cm_ameth.c',
	    'openssl/crypto/cmac/cm_pmeth.c',
	    ])
	#line(---)= gcc -I../include -DOPENSSL_THREADS -D_REENTRANT -DDSO_DLFCN -DHAVE_DLFCN_H -Wa,--noexecstack -m64 -DL_ENDIAN -O3 -Wall -DOPENSSL_IA32_SSE2 -DOPENSSL_BN_ASM_MONT -DOPENSSL_BN_ASM_MONT5 -DOPENSSL_BN_ASM_GF2m -DSHA1_ASM -DSHA256_ASM -DSHA512_ASM -DMD5_ASM -DAES_ASM -DVPAES_ASM -DBSAES_ASM -DWHIRLPOOL_ASM -DGHASH_ASM -c -o
	if "Windows" not in target.get_type():
		my_module.add_src_file([
		    'openssl/engines/e_4758cca.c',
		    'openssl/engines/e_aep.c',
		    'openssl/engines/e_atalla.c',
		    'openssl/engines/e_cswift.c',
		    'openssl/engines/e_gmp.c',
		    'openssl/engines/e_chil.c',
		    'openssl/engines/e_nuron.c',
		    'openssl/engines/e_sureware.c',
		    'openssl/engines/e_ubsec.c',
		    'openssl/engines/e_padlock.c',
		    'openssl/engines/e_capi.c',
		    ])
	#line(---) = gcc -I../../include -DOPENSSL_THREADS -D_REENTRANT -DDSO_DLFCN -DHAVE_DLFCN_H -Wa,--noexecstack -m64 -DL_ENDIAN -O3 -Wall -DOPENSSL_IA32_SSE2 -DOPENSSL_BN_ASM_MONT -DOPENSSL_BN_ASM_MONT5 -DOPENSSL_BN_ASM_GF2m -DSHA1_ASM -DSHA256_ASM -DSHA512_ASM -DMD5_ASM -DAES_ASM -DVPAES_ASM -DBSAES_ASM -DWHIRLPOOL_ASM -DGHASH_ASM -c -o
	my_module.add_src_file([
	    'openssl/engines/ccgost/e_gost_err.c',
	    'openssl/engines/ccgost/gost2001_keyx.c',
	    'openssl/engines/ccgost/gost2001.c',
	    'openssl/engines/ccgost/gost89.c',
	    'openssl/engines/ccgost/gost94_keyx.c',
	    'openssl/engines/ccgost/gost_ameth.c',
	    'openssl/engines/ccgost/gost_asn1.c',
	    'openssl/engines/ccgost/gost_crypt.c',
	    'openssl/engines/ccgost/gost_ctl.c',
	    'openssl/engines/ccgost/gost_eng.c',
	    'openssl/engines/ccgost/gosthash.c',
	    'openssl/engines/ccgost/gost_keywrap.c',
	    'openssl/engines/ccgost/gost_md.c',
	    'openssl/engines/ccgost/gost_params.c',
	    'openssl/engines/ccgost/gost_pmeth.c',
	    'openssl/engines/ccgost/gost_sign.c',
	    ])
	my_module.add_flag('c', [
	    '-DOPENSSL_THREADS',
	    '-DL_ENDIAN',
	    '-D_REENTRANT',
	    ],
	    export=True)
	
	if "Windows" not in target.get_type():
		my_module.add_flag('c', [
		    '-Wa,--noexecstack',
		    '-DHAVE_DLFCN_H',
		    '-DDSO_DLFCN',
		    ])
	else:
		my_module.add_flag('c', [
		    "-D_WINDLL",
		    "-DOPENSSL_PIC",
		    "-D_MT",
		    "-DDSO_WIN32",
		    "-DWIN32_LEAN_AND_MEAN",
		    "-DUNICODE",
		    "-D_UNICODE"
		    ],
		    export=True)
	if "RPI3" in target.get_type():
		my_module.add_flag('c', [
		    '-m64',
		    ])
	my_module.add_flag('c', [
	    '-DOPENSSL_NO_ASM',
	    ],
	    export=True)
	if "Windows" in target.get_type():
		my_module.add_depend([
		    "gdi"
		    ])
	my_module.compile_version("c", 1989, gnu=True)
	my_module.add_depend('z')
	my_module.add_path("openssl")
	my_module.add_path("openssl/crypto")
	my_module.add_path("openssl/crypto/modes")
	my_module.add_path("openssl/crypto/asn1")
	my_module.add_path("openssl/crypto/evp")
	my_module.add_path("generate")
	my_module.add_header_file([
	    'openssl/crypto/aes/aes.h',
	    'openssl/crypto/asn1/asn1.h',
	    'openssl/crypto/asn1/asn1_mac.h',
	    'openssl/crypto/asn1/asn1t.h',
	    'openssl/crypto/bio/bio.h',
	    'openssl/crypto/bf/blowfish.h',
	    'openssl/crypto/bn/bn.h',
	    'openssl/crypto/buffer/buffer.h',
	    'openssl/crypto/camellia/camellia.h',
	    'openssl/crypto/cast/cast.h',
	    'openssl/crypto/cmac/cmac.h',
	    'openssl/crypto/cms/cms.h',
	    'openssl/crypto/comp/comp.h',
	    'openssl/crypto/conf/conf.h',
	    'openssl/crypto/conf/conf_api.h',
	    'openssl/crypto/crypto.h',
	    'openssl/crypto/des/des.h',
	    'openssl/crypto/des/des_old.h',
	    'openssl/crypto/dh/dh.h',
	    'openssl/crypto/dsa/dsa.h',
	    'openssl/crypto/dso/dso.h',
	    'openssl/e_os2.h',
	    'openssl/crypto/ebcdic.h',
	    'openssl/crypto/ec/ec.h',
	    'openssl/crypto/ecdh/ecdh.h',
	    'openssl/crypto/ecdsa/ecdsa.h',
	    'openssl/crypto/engine/engine.h',
	    'openssl/crypto/err/err.h',
	    'openssl/crypto/evp/evp.h',
	    'openssl/crypto/hmac/hmac.h',
	    'openssl/crypto/idea/idea.h',
	    'openssl/crypto/krb5/krb5_asn.h',
	    'openssl/crypto/lhash/lhash.h',
	    'openssl/crypto/md4/md4.h',
	    'openssl/crypto/md5/md5.h',
	    'openssl/crypto/mdc2/mdc2.h',
	    'openssl/crypto/modes/modes.h',
	    'openssl/crypto/objects/obj_mac.h',
	    'openssl/crypto/objects/objects.h',
	    'openssl/crypto/ocsp/ocsp.h',
	    'openssl/crypto/opensslv.h',
	    'openssl/crypto/ossl_typ.h',
	    'openssl/crypto/pem/pem.h',
	    'openssl/crypto/pem/pem2.h',
	    'openssl/crypto/pkcs12/pkcs12.h',
	    'openssl/crypto/pkcs7/pkcs7.h',
	    'openssl/crypto/pqueue/pqueue.h',
	    'openssl/crypto/rand/rand.h',
	    'openssl/crypto/rc2/rc2.h',
	    'openssl/crypto/rc4/rc4.h',
	    'openssl/crypto/ripemd/ripemd.h',
	    'openssl/crypto/rsa/rsa.h',
	    'openssl/crypto/stack/safestack.h',
	    'openssl/crypto/seed/seed.h',
	    'openssl/crypto/sha/sha.h',
	    'openssl/crypto/srp/srp.h',
	    'openssl/crypto/stack/stack.h',
	    'openssl/crypto/symhacks.h',
	    'openssl/crypto/ts/ts.h',
	    'openssl/crypto/txt_db/txt_db.h',
	    'openssl/crypto/ui/ui.h',
	    'openssl/crypto/ui/ui_compat.h',
	    'openssl/crypto/whrlpool/whrlpool.h',
	    'openssl/crypto/x509/x509.h',
	    'openssl/crypto/x509/x509_vfy.h',
	    'openssl/crypto/x509v3/x509v3.h',
	    ],
	    destination_path="openssl")
	
	my_module.add_header_file([
	    'generate/' + target.get_name() + '/opensslconf.h',
	    ],
	    destination_path="openssl")
	# normaly generate with : /usr/bin/perl util/mkbuildinf.pl "gcc -Iopenssl/crypto -Iopenssl -Iopenssl/include -DOPENSSL_THREADS -D_REENTRANT -DDSO_DLFCN -DHAVE_DLFCN_H -Wa,--noexecstack -m64 -DL_ENDIAN -O3 -Wall -DOPENSSL_IA32_SSE2 -DOPENSSL_BN_ASM_MONT -DOPENSSL_BN_ASM_MONT5 -DOPENSSL_BN_ASM_GF2m -DSHA1_ASM -DSHA256_ASM -DSHA512_ASM -DMD5_ASM -DAES_ASM -DVPAES_ASM -DBSAES_ASM -DWHIRLPOOL_ASM -DGHASH_ASM" "linux-x86_64" >buildinf.h
	# but I do not understand the utility (global build of the application
	my_module.add_header_file([
	    'generate/buildinf.h',
	    ],
	    destination_path="openssl")
	my_module.add_depend([
	    'c',
	    'm'
	    ])
	if "Linux" in target.get_type():
		my_module.add_depend([
		    'rpc',
		    'arpa',
		    ])
	return True
