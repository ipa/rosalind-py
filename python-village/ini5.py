__author__ = 'paoliw'

f = open('input/ini5.txt', 'r')
fo = open('output/ini5.txt', 'w')

counter = 0
for line in f:
    counter += 1
    if counter % 2 == 0:
        fo.write(line)

f.close()
fo.close()