def countWords():
    x=input("ENTER AN INPUT:")
    s=open("data.txt", "a+")
    p=s.read()
    xo=len(p.split("\n"))
    g=len(p)
    hp="\n"
    hp+=x
    s.write(hp)
    s.seek(g)
    v=s.readlines(xo+1)
    h=v[0].split()
    return len(h)
print(countWords())
