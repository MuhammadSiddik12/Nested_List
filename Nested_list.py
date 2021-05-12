Nested_lists=int(input("How many Nested Lists You Want:"))
Final_list=[]
for i in range(Nested_lists):
    How_Many_Elements=int(input(f"How Many Elements You Want To Put On Index No {i}:"))
    Temporary_list=[]
    for i in range(How_Many_Elements):
        Last_Elements=input("Enter Elements:")
        Temporary_list.append(Last_Elements)
    Final_list.append(Temporary_list)
print(Final_list)

