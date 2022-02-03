i = int(input()); l=[]
for _ in range(i):
  s = input()
  c, *v = s.split(); v=map(int,v)
  if c == 'insert': l.insert(*v)
  elif c == 'remove': l.remove(*v)
  elif c == 'append': l.append(*v)
  elif c == 'sort': l.sort()
  elif c == 'reverse': l.reverse()
  elif c == 'pop': l.pop(*v)
  elif c == 'print': print(l)
  else: raise RuntimeError("invalid command")