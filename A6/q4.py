import sys


def main():
    '''This script takes entries from the file supplied and sorts th ID. If no file is supplied, it uses standard input to take entries from the user.
Input: the input will be the the filename supplied by user, or entries from standard input.
Output: 2 columns will be printed with the id and names sorted by ID'''
    if len(sys.argv)<2:
        print 'Using stdin. Press Ctrl-D when done!\n'
    
        f = sys.stdin
    else:
        print 'Using %s\n'%sys.argv[1]
        fileName = sys.argv[1]
        f = open(fileName,'r')
    l = f.readlines()
    d = dict()
    print "\n"
    print "ID\tName"
    
    for i in l:
        
        i = i.split(' ')
        i[0] = int(i[0])
        d[i[0]] = ''
        

        for j in range(1,len(i)):
            d[i[0]] = d[i[0]] + i[j] + ' '
    
    for k in sorted(d.keys()):
        print k,'\t',d[k]
        

if __name__ == '__main__':
    main()
