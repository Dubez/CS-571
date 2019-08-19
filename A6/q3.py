import sys


def main():
    '''This script takes the entries in the file, sorting them out by id.
Input: the input will be the 'ids' file
Output: 2 columns will be printed: ID and names, sorted by ID number'''
    fileName = sys.argv[1]
    f = open(fileName,'r')
    l = f.readlines()
    d = dict()
    print "ID\tName"
    for i in l:
        
        i = i.strip('\n')
        i = i.split(' ')
        i[0] = int(i[0])
        d[i[0]] = ''
        

        for j in range(1,len(i)):
            d[i[0]] = d[i[0]] + i[j] + ' '
            
    for k in sorted(d.keys()):
        print k,'\t',d[k]
        



if __name__ == '__main__':
    main()
