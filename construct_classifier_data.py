import sys
import random

from shutil import copyfile

pos_line = 7454
neg_line = 16651219
p = pos_line / float(neg_line)

pos_file = sys.argv[1]
neg_file = sys.argv[2]

train_data = sys.argv[3]

negative_f = open(neg_file, 'r')

copyfile(positive_f, train_data)
train_f = open(train_data, 'w')

for line in negative_f:
	r = random.random()
	if r <= p:
		train_f.write("%s\n" % line)
