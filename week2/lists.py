number_a = [1, 2, 3, 4, 5]
list_b = [6, "Backdoor", 8, "Monday", 10]
list_c = ["Skinny jeans", "T-shirt", "Hoodie", "Sneakers", "Backpack"]
number_d = [11, 12 , 13, 14, 15]
list_e = []

#list_b[1] = "Frontdoor"
#print(list_b)
list_c.insert(len(list_c),5)
list_e.append(1)

numbers = [number_a + number_d for numer in range(1, 6)]

print(numbers)

#for item in list_b:
   # print(item)