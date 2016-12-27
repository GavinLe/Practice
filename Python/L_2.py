class A(object):
    x = 1
    gen = (x for _ in xrange(10))  # gen=(x for _ in range(10))
    
if __name__ == "__main__":
    print(list(A.gen))