# coding: utf-8
import random
import sys




#data_pos = open("test_140.txt", 'r')
#data_sp_n = open("incall_sp_sn.txt", 'r')
#data_sn_p = open("dataset_20.txt", 'r')


data_pos = open("/home/ubuntu/dig_indicator/data/incall_data/incall_pos.txt", 'r')
data_sp_n = open("/home/ubuntu/dig_indicator/data/incall_data/incall_sp_n.txt", 'r')
data_sn_p = open("/home/ubuntu/dig_indicator/data/incall_data/incall_sn_p.txt", 'r')
data_ne = open("/home/ubuntu/dig_indicator/data/incall_data/incall_ne.txt", 'r')


dataset = []
for line in data_pos:
    dataset.append('__label__TRUE'+' '+line)
for line in data_sp_n:
    dataset.append('__label__TRUE'+' '+line)

print "Negative:",len(dataset)

for line in data_sn_p:
    dataset.append('__label__FALSE'+' '+line)

data_pos.close()
data_sp_n.close()
data_sn_p.close()


total_data_f = open("form_dataset_expri2.txt", 'w')


for i in range(50000):
    neg_lines = open('/home/ubuntu/dig_indicator/data/incall_data/incall_neg.txt').read().splitlines()
    myline = random.choice(neg_lines)
    dataset.append(('__label__FALSE'+' '+myline).strip()+'\n')
    print i

open('/home/ubuntu/dig_indicator/data/incall_data/incall_neg.txt').close()

for i in range(20000):
    ne_lines = open('/home/ubuntu/dig_indicator/data/incall_data/incall_ne.txt').read().splitlines()
    myline = random.choice(neg_lines)
    dataset.append(('__label__FALSE' + ' ' + myline).strip() + '\n')
    print i
open('/home/ubuntu/dig_indicator/data/incall_data/incall_ne.txt').close()

random.shuffle(dataset)

for i in dataset:
    total_data_f.write("%s" % i)


total_data_f.close()

