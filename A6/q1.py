import sys


def main():
    '''This script computes entries in the file supplied
Input: the input will be the 'students' file
Output: 2 columns will be printed containing the students' names and averages'''
    fileName = sys.argv[1]
    f = open(fileName,'r')
    l = f.readlines()
    print "Student\tAverage"
    
    for i in l:
        i = i.strip('\n')
        i = i.split(' ')
        sum = 0
        for j in range(1,(len(i))):
            sum = sum + float(i[j])
        avg = sum/(len(i)-1)
        print "%s\t%.2f"%(i[0],avg)




if __name__ == '__main__':
    main()
