def likes(names):
    result=""
    listlen=len(names)
    if listlen==0:
        result = "no one likes this"
    if listlen==1:
        result = names[0]+" likes this"
    if listlen==2:
        result = names[0]+" and "+names[1]+" like this"
    if listlen==3:
        result = names[0]+", "+names[1]+" and "+names[2]+" like this"
    if listlen>3:
        result = names[0]+", "+names[1]+" and " + \
            str(listlen-2)+" others like this"
    return result
