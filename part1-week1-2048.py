"""
Merge function for 2048 game.
"""
#Iterate over the list created in the previous step and create another new list in which pairs of tiles in the first list are replaced with a tile of twice the value and a zero tile.
def shift_line(line):
    """
    this function shift all the number to the left of the list
    """
    num = len(line)
    shifted_line=[]
    iter1 = 0
    while (num):
        if ((iter1 < len(line)) and (line[iter1] != 0)):
            shifted_line.append(line[iter1])
            iter1 += 1
            num -= 1
        elif (iter1 >= len(line)):
            shifted_line.append(0)
            num -= 1
        else:
            iter1+=1
    return shifted_line

#Iterate over the input and create an output list that has all of the non-zero tiles slid over to the beginning of the list with the appropriate number of zeroes at the end of the list.
def merge_line(line):
    """
    this function merge the number if adjacent number are the same
    """
    #print line
    length = len(line)
    if (length == 2):
         if (line[0] == line[1]):
                line[0] = 2*line[0]
                line[1] = 0
    for xx1 in range(length-1):
        if ( (line[xx1] == line[xx1+1]) and (line[xx1] != 0) ):
            line[xx1] = line[xx1]+line[xx1+1]
            line[xx1+1] = 0
    #print line
    return line

def merge(line):
    """
    shift number to the left, merge the numbers if the same, shift the numbers again
    """
    if (len(line)<1):
        return line
    shifted_line =  shift_line(line)
    #print shifted_line
    merged = merge_line(shifted_line)
    result = shift_line(merged)
    print result
    return result
