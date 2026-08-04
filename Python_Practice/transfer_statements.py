# Transfer statements - break
students = ["Anil","Prasad","Sumanth"]
for i in students:
    if i=="Kiran":
        print(f"Student found")
        break
else:
    print(f"Student not found")

# Manufacturing products status
products_status = ["ok","ok","defect","ok","ok","defect"]
for i in products_status:
    if i == "defect":
        continue
    print (i)


for i in range(10):
    if i == 3:
        pass
print (f"last iteration {i}")

empty_list = []
for i in range(1,12):
    result = i ** 2 
    empty_list.append(result)
print (empty_list)


