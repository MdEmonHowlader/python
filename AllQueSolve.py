k=[101,102,103,104]
v=["USA", "BD", "UK", "China"]
lst= dict(zip(k, v))
print(lst)

# def calculate_waiver(cgpa, fee):
#     if cgpa>3.50:
#         waiver=0.20
#     elif 3.00<=cgpa <=3.50:
#         waiver=0.10
#     else:
#         waiver=0.5
#     net_fee=fee-(fee*waiver)
#     return net_fee
# cgpa=float(input("Enter You CGPA: "))
# fee=float(input("Enter Your Fee: "))
# net_fee=calculate_waiver(cgpa, fee)
# # print(net_fee)

def odd_number():
    i = 1
    odd_list = []
    while i <= 100:
        if i % 2 != 0:
            odd_list.append(i)
        i += 1
    return odd_list

print(odd_number())

print("*\n")
list1=[1,2,3]
list2=[5,4,5]
common=list(set(list1)& set(list2))
if common:
    print("Common elements are: ", common)
else:
    print("No common element's")
    
    
print('\n')

lst=[2,3,4,5,6]
if len(lst)<3:
    print("Not possible")
else:
    print(lst[1:-1])
    
    

print("\n")
i = 1
while i <= 100:
    if i % 2 != 0:
        print(i)
    i += 1
