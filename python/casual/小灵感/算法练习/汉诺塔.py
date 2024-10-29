def move(n,From,buffer,to):
    if n==1:
        print(From,'—>',to)
        return
    move(n-1,From,to,buffer)
    move(1,From,buffer,to)
    move(n-1,buffer,From,to)

move(4, "T1", "T2", "T3", 0)