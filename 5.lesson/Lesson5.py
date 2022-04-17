def k(a,b,c):
    return (a + b + c)/3

result = k(int(input("Enter Number: ")),int(input("Enter Number: ")),int(input("Enter Number: ")))
print(result)

def month(f):
    if f == 1:
        return "Січень"
    elif f == 2:
        return "Лютий"
    elif f == 3:
        return "Березень"
    elif f == 4:
        return "Квітень"
    elif f == 5:
        return "Травень"
    elif f == 6:
        return "Червень"
    elif f == 7:
        return "Липень"
    elif f == 8:
        return "Серпень"
    elif f == 9:
        return "Вересень"
    elif f == 10:
        return "Жовтень"
    elif f == 11:
        return "Листопад"
    elif f == 12:
        return "Грудень"
    else:
        return "Введіть число від 1 до 12"
result = month(int(input("Місяць: ")))
print(result)

def c(a,b):
    if a < b:
        return b
    elif a > b:
        return b

result = c(int(input("Enter Number: ")),int(input("Enter Number: ")))
print(result)