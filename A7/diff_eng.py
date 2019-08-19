import sys
import matplotlib.pyplot as plt

''' Python script to Simulate the Charles Babbage Difference Engine
    README file is included in the attachment.
    Author: Dubem Ezeh
'''

# take input of the number of rows to compute
n = int(sys.argv[1])

while(n<1 or n>100):
    n = int(raw_input("Supply number of rows you want the difference engine to compute: \n"))

x_list = []
y_list = []

# create a list of x values from 0 to n
for i in range(n+1):

    x_list.append(i)



arr = []

temp = []

'''t = raw_input("Supply computed first row elements, separated by a space, starting with value for y and ending with the/"
                       " constant, e.g. 1 2 3: \n")
                       
                       '''
#supply the first row elements as numbers separated by commas only, no spaces.
#The example below shows the script being used to compute 100 lines of difference values from -29375,5231,-284,6:

                #sudo python diff_eng.py 100 -29375,5231,-284,6

t = sys.argv[2]
t = t.split(",")
for i in range(t.__len__()):
    temp.append(int(t[i]))

length = temp.__len__()

arr.append(temp)

yy = []    # for plotting
yy.append(temp[0])

for i in range(1, n+1):
    temp = []
    for j in range(length):
        if (j == (length-1)):
            temp.append(arr[0][j])
        else:
            temp.append(arr[i-1][j] + arr[i-1][j+1])
    arr.append(temp)
    yy.append(temp[0])

# to generate the output in a readable manner

y1 = "X\tY\t\t1st Diff\t"
y2 = y1 + "2nd Diff\t"
y3 = y2+"3rd Diff\t"
y4 = y3 + "4th Diff\t"
y5 = y4 + "5th Diff\t"
y6 = y5 + "6th Diff\t"

#dictionary to store the different column names

dict = {1:y1, 2:y2, 3:y3, 4:y4, 5:y5, 6:y6}

#if statement to check whether a readable output can be generated

if(length in dict):
    print "\n" + dict[length - 1]
else:
    print 'out of compute capability'

#output generation

for i in range(n+1):
    print("%d\t")%(x_list[i]),
    for j in range(length):
        print ("%d\t\t")%(arr[i][j]),

    print "\n"

#plot generation

plt.plot(x_list, yy)

plt.show()


