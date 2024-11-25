string = str(input("Введите строку для поиска: "))   
text = []   
count = 0 
with open("text.txt", "r", encoding = "utf-8") as file:   
    for lines in file:  
        if string in lines:   
            text.append(string)  
            count += 1  
sort = sorted(text, key = len)  
for line in text: 
    print(line)   
print("Количество строк: ", count) 