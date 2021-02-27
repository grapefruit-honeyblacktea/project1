def is_cheap_set(a,b,c,d,e):
    cheap1 = min(a,b,c)
    cheap2 = min(d,e)
    total = cheap1 + cheap2 - 50
    return total

if __name__ == '__main__':
    burger1 = int(input())
    burger2 = int(input())
    burger3 = int(input())
    drink1 = int(input())
    drink2 = int(input())

    print(is_cheap_set(burger1,burger2,burger3,drink1,drink2))