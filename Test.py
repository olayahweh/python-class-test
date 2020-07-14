#Extraction of the colors from the html file provided
import os
import re


file = open('python_class_test.html', 'r')
stuff = file.read()


colors = re.findall(r'<td>((\w+,\s){18})(\w+)</td>', stuff)

color_1 = re.findall(r'<td>((\w+,\s){18})(\w+),</td>', stuff)

my_colors = (colors + color_1)

print(my_colors)

list(my_colors)

my_def = {}
def myfreq(my_list, bok):
    for tup in my_list:
        for my_colors in tup:
            if my_colors in bok:
                bok[my_colors] += 1
            else:
                bok[my_colors] = 1

    print(bok)

myfreq(my_colors, my_def)
    
#mean


print(numpy.array([my_def[k] for k in my_def]).mean())

#mostly worn

most_frequent = max(my_def, key=my_def.get)  
print(most_frequent, my_def[most_frequent])


# def CountFrequency(my_list): 
#   frek = {} 
#     for colors in my_colors:
#         if (colors in frek): 
#             frek[colors] += 1
#         else: 
#             frek[colors] = 1

#     for key, value in frek.items(): 
#         print ("% s : % d"%(key, value)) 

# if __name__ == "__main__":  
# #driver

# CountFrequency(my_colors) 

#variance
  
sum_total = (sum(my_def.values()))

vari = my_def.values()


mean = (sum(vari)) / len(vari)

x = []
for num in val:
     x.append((num - mean)** 2)

x = sum(x)
variance = x / sum_total
print(variance)

#Recursive searching algorithm

My_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

y = int(input("Enter a search number: "))
def SearchListAlgorithm(list, start, end, y):
    if end >= start:
        mid = start + (end - start) // 2
        
        if list[mid] == y:
            return mid
        elif list[mid] > y:
            return SearchedAlgorithm(list, start, mid - 1, y)
        else:
            return SearchedAlgorithm(list, mid + 1, end, y)
    
    else:
        return - 2
        
result = SearchedAlgorithm(My_numbers, 0, len(My_numbers) - 1, x)
if result != -2:
    print("searched is present at index " + str(result))
else:
    print("Searched is not present in list. ")

















