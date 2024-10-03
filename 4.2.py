def insertion_sort(list1): 
        for i in range(1, len(list1)): 
 
            value = list1[i] 
            j = i - 1 
            while j >= 0 and value < list1[j]: 
                list1[j + 1] = list1[j] 
                j -= 1 
            list1[j + 1] = value 
        return list1 
 
list1 = [180, 11, 3000, 5, 62] 
print("Неотсортированный массив", list1) 
 
print("Отсортированный массив", insertion_sort(list1)) 
