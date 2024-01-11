f = open("creditcard.csv")

n_parts = 7

i=0
for line in f.readlines():
    ## print(line)
    ## input()
    i = i + 1

print(i)

f.close()

batch = int( i / n_parts )

print(batch)

f = open("creditcard.csv")

f_out1 = open("creditcard_part1.csv","w")
f_out2 = open("creditcard_part2.csv","w")
f_out3 = open("creditcard_part3.csv","w")
f_out4 = open("creditcard_part4.csv","w")
f_out5 = open("creditcard_part5.csv","w")
f_out6 = open("creditcard_part6.csv","w")
f_out7 = open("creditcard_part7.csv","w")

j = 0
for line in f.readlines():
    if j in range(0, batch):
        the_f = f_out1
    elif j in range(batch, 2*batch):
        the_f = f_out2
    elif j in range(2*batch, 3*batch):
        the_f = f_out3
    elif j in range(3*batch, 4*batch):
        the_f = f_out4
    elif j in range(4*batch, 5*batch):
        the_f = f_out5
    elif j in range(5*batch, 6*batch):
        the_f = f_out6
    elif j in range(6*batch, 7*batch):
        the_f = f_out7
    the_f.write(line)
    j = j + 1

f_out1.close()
f_out2.close()
f_out3.close()
f_out4.close()
f_out5.close()
f_out6.close()
f_out7.close()
