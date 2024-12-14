def wrap(string, max_width):
    counter = 0
    mylist = []
    extra = len(string) % max_width
    extraString = string[len(string)-extra:len(string)+extra]
    final = []
    for k in range(0, len(string)):
        
        if counter == max_width:
            final.append(''.join(mylist))
            counter = 0
            mylist = []
        
        mylist.append(string[k])
        counter += 1
    final.append(extraString)
    return "\n".join(final)

wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4)