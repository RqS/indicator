# coding: utf-8
import random
import sys




#data_pos = open("test_140.txt", 'r')
#data_sp_n = open("incall_sp_sn.txt", 'r')
#data_sn_p = open("dataset_20.txt", 'r')


data_pos = open("/home/ubuntu/dig_indicator/data/incall_data/incall_pos.txt", 'r')
data_sp_n = open("/home/ubuntu/dig_indicator/data/incall_data/incall_sp_n.txt", 'r')
data_sn_p = open("/home/ubuntu/dig_indicator/data/incall_data/incall_sn_p.txt", 'r')



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


total_data_f = open("/home/ubuntu/dig_indicator/data/incall_data/dataset_neg.txt", 'w')


lst = []
k = 0
for i in range(80000):
    neg_lines = open('test_140.txt').read().splitlines()
    myline = random.choice(neg_lines)
    if myline not in lst:
        dataset.append('__label__FALSE'+' '+myline)
        k += 1
        lst.append(myline)
        if k ==70000:
            break

random.shuffle(dataset)

for i in dataset:
    total_data_f.write("%s" % i)

total_data_f.close()

