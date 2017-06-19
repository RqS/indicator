# coding: utf-8
import sys
import random



total_data_f = open("dataset_20.txt", 'w')


for i in range(20):
    neg_lines = open('/data/incall_data/incall_neg.txt').read().splitlines()
    myline =random.choice(neg_lines)
    total_data_f.write("%s\n" % myline)


for i in range(20):
    neg_lines = open('/data/incall_data/incall_sn_p.txt').read().splitlines()
    myline =random.choice(neg_lines)
    total_data_f.write("%s\n" % myline)

for i in range(20):
    neg_lines = open('/data/incall_data/incall_pos.txt').read().splitlines()
    myline =random.choice(neg_lines)
    total_data_f.write("%s\n" % myline)

for i in range(20):
    neg_lines = open('/data/incall_data/incall_sp_n.txt').read().splitlines()
    myline =random.choice(neg_lines)
    total_data_f.write("%s\n" % myline)

for i in range(20):
    neg_lines = open('/data/incall_data/incall_p_n.txt').read().splitlines()
    myline =random.choice(neg_lines)
    total_data_f.write("%s\n" % myline)

for i in range(20):
    neg_lines = open('/data/incall_data/incall_sp_sn.txt').read().splitlines()
    myline =random.choice(neg_lines)
    total_data_f.write("%s\n" % myline)

for i in range(20):
    neg_lines = open('/data/incall_data/incall_ne.txt').read().splitlines()
    myline =random.choice(neg_lines)
    total_data_f.write("%s\n" % myline)

total_data_f.close()

