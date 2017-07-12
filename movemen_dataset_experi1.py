# coding: utf-8
import random
import sys




#data_pos = open("test_140.txt", 'r')
#data_sp_n = open("incall_sp_sn.txt", 'r')
#data_sn_p = open("dataset_20.txt", 'r')


data_pos = open("/home/ubuntu/dig_indicator/data/movement_data/movement_pos.txt", 'r')
data_sp_n = open("/home/ubuntu/dig_indicator/data/movement_data/movement_sp_n.txt", 'r')
data_sn_p = open("/home/ubuntu/dig_indicator/data/movement_data/movement_sn_p.txt", 'r')



dataset = []
for line in data_pos:
    dataset.append('__label__TRUE'+' '+line)
for line in data_sp_n:
    dataset.append('__label__TRUE'+' '+line)

print "Positive:",len(dataset)

for line in data_sn_p:
    dataset.append('__label__FALSE'+' '+line)

data_pos.close()
data_sp_n.close()
data_sn_p.close()


total_data_f = open("/home/ubuntu/dig_indicator/data/movement_data/movement_experiment/dataset_experi1.txt", 'w')

dataset.append(('__label__FALSE'+' '+myline).strip()+'\n')
lst = []
k = 0
for i in range(40000):
    neg_lines = open('/home/ubuntu/dig_indicator/data/movement_data/movement_neg.txt').read().splitlines()
    myline = random.choice(neg_lines)
    if myline not in lst:
        dataset.append(('__label__FALSE'+' '+myline).strip()+'\n')
        k += 1
        lst.append(myline)
        print "k:",k
        print "i:",i
        if k ==7000:
            break

random.shuffle(dataset)
print "Positive + Neagtive:", len(dataset)

for i in dataset:
    total_data_f.write("%s" % i)
print "Positive + Neagtive:", len(dataset)
total_data_f.close()

