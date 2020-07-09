fname = input('Enter file name: ')
fh = open(fname)
sum1 = 0
count = 0
for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        count +=1
        pos = line.find(':')
        num = line[pos+1:]
        num = float(num)
        sum1 += num

print('Average spam confidence:',sum1/count)
    
