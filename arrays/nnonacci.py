def nbonnaci(n,m):

     vals=[0 for i in range(n-1)]
     vals.append(1)
     vals.append(1)

     g=1
     for i in range(m):
          g=g-vals[i]+vals[-1]
          vals.append(g)
     print(vals)
nbonnaci(4,8)
