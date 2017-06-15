import sys
import random

from shutil import copyfile

pos_line = 8778
neg_line = 23089366
p = pos_line / float(neg_line)

pos_file = sys.argv[1]
neg_file = sys.argv[2]

train_data = sys.argv[3]

negative_f = open(neg_file, 'r')

copyfile(pos_file, train_data)
train_f = open(train_data, 'a')
train_f.write("\n")
for line in negative_f:
	r = random.random()
	if r <= p:
		train_f.write("%s" % line)
