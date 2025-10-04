if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new = sorted(list(set(arr)))
    if (len(new) >= 2):
        print(new[-2])
    else:
        print(new[-1])