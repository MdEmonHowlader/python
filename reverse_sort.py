d=[23,1,23,32,3,4]
def reverse_sort(data):
    s=sorted(data)
    re=s[::-1]
    return re
print(reverse_sort(d))