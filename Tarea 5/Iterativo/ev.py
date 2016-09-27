# ( p | q )
def evalua(exp,e):
  data = exp.split()
  dicOBin = {'&':' and ','|':' or ','=>':''}
  dicOUna =  {'!':'not '}
  ops, val = [],[]
  for i in data:
    if i == '(':
      pass
    elif (i in dicOBin) or (i in dicOUna):
      ops.append(i)
    elif i == ')':
      op, va = ops.pop(), val.pop()
      if op in dicOUna:
        va = eval(dicOUna[op]+str(va))
      elif op == '=>':
        va = not val.pop() or va
      else:
        va = eval(str(val.pop())+dicOBin[op]+str(va))
      val.append(va)
    else:
      val.append(e[i])
  return val

def tdd(f,fp,e,r):
    return f(fp,e) == r

print('******************************* TDD')
print( tdd(evalua,'( p => q )',{'p':True,'q':False},[False]))
print( tdd(evalua,'( p => q )',{'p':True,'q':True},[True]))
