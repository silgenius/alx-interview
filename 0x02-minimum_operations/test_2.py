def minop(n : int) -> int:
    noh = 1
    nop = 0
    result = []
    for i in range(2, int((n ** 0.5)) + 1):
        print(i)
        if n % i == 0:
            print('in')
            a = i # i is a factor of n
            b = n // a
            copy = noh
            nop += 1
            
            if noh != a:
                # Pasting
                noh *= a
                nop += (noh - 1)
            
            if n != noh: 
                copy = noh
                nop += 1
                # Paste what is in copy
                noh += copy * (b - 1)
                nop += (b - 1)
                result.append(nop)
    result = sorted(result)
    return result[0]
            
print('minop: ', minop(12))