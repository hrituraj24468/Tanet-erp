def values():
    try:
        value=['JS pets']
        file=open("party.txt","r")
        z=len(file.readlines())
        file.close()
        file=open("party.txt","r")
        for i in range(0,z):
            a=file.readline()
            b,c=a.split(sep="^")
            value.append(b) 
        file.close()
        return value
    except:
        value=['JS pets']
        return value
