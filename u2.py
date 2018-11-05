#Knuth's "Algorithm U", from stackoverflow
# https://codereview.stackexchange.com/questions/1526/finding-all-k-subset-partitions

import utils

# altered to limit to min/max length, and require ordered lists. Feasible to run now!

def algorithm_u(ns, m):
    def check(lli):
      if lli == None:
        return False
      prev = lli[0][0] - 1
      for li in lli:
        if len(li) < 2 or len(li) > 6:
          return False
        for i in li:
          if i != prev + 1:
            return False
          prev = i
      return True

    def visit0(n, a):
        ps = [[] for i in range(m)]
        for j in range(0,n):
            ps[a[j + 1]].append(ns[j])
        return ps

    def visit1(n, a):
        ps = [[] for i in range(m)]
        for j in range(0,n):
            ps[a[j + 1]].append(ns[j])
        return ps

    def visit(n, a):
        ps = [[] for i in range(m)]
        for j in range(0,n):
            ps[a[j + 1]].append(ns[j])
        return ps

    def f(mu, nu, sigma, n, a):
        if mu == 2:
            out = visit(n, a)
            if check(out):
              yield(out)
        else:
            for v in f(mu - 1, nu - 1, (mu + sigma) % 2, n, a):
                if check(v):
                  yield v
        if nu == mu + 1:
            a[mu] = mu - 1
            out = visit(n, a)
            if check(out):
              yield out
            while a[nu] > 0:
                a[nu] = a[nu] - 1
                out = visit(n, a)
                if check(out):
                  yield out
        elif nu > mu + 1:
            if (mu + sigma) % 2 == 1:
                a[nu - 1] = mu - 1
            else:
                a[mu] = mu - 1
            if (a[nu] + sigma) % 2 == 1:
                for v in b(mu, nu - 1, 0, n, a):
                    if check(v):
                      yield v
            else:
                for v in f(mu, nu - 1, 0, n, a):
                    if check(v):
                      yield v
            while a[nu] > 0:
                a[nu] = a[nu] - 1
                if (a[nu] + sigma) % 2 == 1:
                    for v in b(mu, nu - 1, 0, n, a):
                        if check(v):
                          yield v
                else:
                    for v in f(mu, nu - 1, 0, n, a):
                        if check(v):
                          yield v

    def b(mu, nu, sigma, n, a):
        if nu == mu + 1:
            while a[nu] < mu - 1:
                out = visit(n, a)
                if check(out):
                  yield out
                a[nu] = a[nu] + 1
            out = visit(n, a)
            if check(out):
              yield out
            a[mu] = 0
        elif nu > mu + 1:
            if (a[nu] + sigma) % 2 == 1:
                for v in f(mu, nu - 1, 0, n, a):
                    if check(v):
                        yield v
            else:
                for v in b(mu, nu - 1, 0, n, a):
                    if check(v):
                        yield v
            while a[nu] < mu - 1:
                a[nu] = a[nu] + 1
                if (a[nu] + sigma) % 2 == 1:
                    for v in f(mu, nu - 1, 0, n, a):
                        if check(v):
                            yield v
                else:
                    for v in b(mu, nu - 1, 0, n, a):
                        if check(v):
                            yield v
            if (mu + sigma) % 2 == 1:
                a[nu - 1] = 0
            else:
                a[mu] = 0
        if mu == 2:
            out = visit(n, a)
            if check(out):
              yield out
        else:
            for v in b(mu - 1, nu - 1, (mu + sigma) % 2, n, a):
                if check(v):
                    yield v

    n = len(ns)
    a = [0] * (n + 1)
    for j in range(1, m + 1):
        a[n - m + j] = j - 1
    return f(m, n, 0, n, a)

def walk(s, n):
  out = []
  for l in algorithm_u(s, n):
    out.append(list(l))
  return out

def checkordered(l):
  val = -1
  for x in utils.flatten(l):
    if val + 1 == x:
      val = x
    else:
      return False
  return True

def checklength(lli, min, max):
  for li in lli:
    if not(len(li) >= min and len(li) <= max):
      return False
  return True
    
def walkordered0(s, n):
  out = []
  for l in algorithm_u(s, n):
    l = list(l)
    if checkordered(l) and checklength(l, 2, 6):
      out.append(l)
  return out

def walkordered(s, n):
  print('')
  out = []
  for l in algorithm_u(s, n):
    l = list(l)
    if checkordered(l) and checklength(l, 2, 6):
       print(l)

def visit(ns, a, n):
    ps = [[] for i in range(6)]
    for j in range(n):
        ps[a[j + 1]].append(ns[j])
    return ps

if __name__ == "__main__":
  print(walk([0,1,2,3],2))
  walkordered([0,1,2],2)
  #print(walkordered([0,1,2,3],3))
  #print(walkordered([0,1,2,3,4,5,6,7],2))
  walkordered(list(range(10)),4)
  walkordered(list(range(30)),6)
  walkordered(list(range(15)),4)
  #print(walkordered(list(range(15)),3))
  #print(walkordered(list(range(15)),4))
  #print(walkordered(list(range(15)),5))
  #print(walkordered(list(range(15)),6))
