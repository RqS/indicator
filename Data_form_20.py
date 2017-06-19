# coding: utf-8
import sys
import random



total_data_f = open("dataset_20.txt", 'w')

lst = []
k = 0
for i in range(200):
    neg_lines = open('/home/ubuntu/dig_indicator/data/incall_data/incall_neg.txt').read().splitlines()
    myline =random.choice(neg_lines)
    if line not in lst:
        total_data_f.write("%d.%s\n" %(i,myline))
        k += 1
        lst_1.append(myline)
        if k == 20:
            break

lst = []
k = 0
for i in range(200):
    neg_lines = open('/home/ubuntu/dig_indicator/data/incall_data/incall_sn_p.txt').read().splitlines()
    myline =random.choice(neg_lines)
    if line not in lst:
        total_data_f.write("%d.%s\n" %(i,myline))
        k += 1
        lst_1.append(myline)
        if k == 20:
            break

lst = []
k = 0
for i in range(200):
    neg_lines = open('/home/ubuntu/dig_indicator/data/incall_data/incall_pos.txt').read().splitlines()
    myline =random.choice(neg_lines)
    if line not in lst:
        total_data_f.write("%d.%s\n" %(i,myline))
        k += 1
        lst_1.append(myline)
        if k == 20:
            break



lst = []
k = 0
for i in range(200):
    neg_lines = open('/home/ubuntu/dig_indicator/data/incall_data/incall_sp_n.txt').read().splitlines()
    myline =random.choice(neg_lines)
    if line not in lst:
        total_data_f.write("%d.%s\n" %(i,myline))
        k += 1
        lst_1.append(myline)
        if k == 20:
            break

lst = []
k = 0
for i in range(200):
    neg_lines = open('/home/ubuntu/dig_indicator/data/incall_data/incall_p_n.txt').read().splitlines()
    myline =random.choice(neg_lines)
    if line not in lst:
        total_data_f.write("%d.%s\n" %(i,myline))
        k += 1
        lst_1.append(myline)
        if k == 20:
            break

    
lst = []
k = 0
for i in range(200):
    neg_lines = open('/home/ubuntu/dig_indicator/data/incall_data/incall_sp_sn.txt').read().splitlines()
    myline =random.choice(neg_lines)
    if line not in lst:
        total_data_f.write("%d.%s\n" %(i,myline))
        k += 1
        lst_1.append(myline)
        if k == 20:
            break


lst = []
k = 0
for i in range(200):
    neg_lines = open('/home/ubuntu/dig_indicator/data/incall_data/incall_ne.txt').read().splitlines()
    myline =random.choice(neg_lines)
    if line not in lst:
        total_data_f.write("%d.%s\n" %(i,myline))
        k += 1
        lst_1.append(myline)
        if k == 20:
            break

total_data_f.close()

