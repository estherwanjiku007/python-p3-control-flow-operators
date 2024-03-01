def admin_login(user_name,password):
    if user_name=="ADMIN" or user_name=="admin" and password==[1,2,3,4,5]:
       # print("Access granted")
        return "Access granted"
    else:
       # print("Access denied")
        return ("Access denied")
result=admin_login("ADMIN",[1,2,3,4,5])
print(result) 
def calc(operator,num1,num2):
    if operator=="+":
        return num1+num2
    elif operator=="-":
        return num1-num2
    elif operator=="x":
        return num1*num2
    elif operator=="/":
        return num1/num2
    else:
        return "You must provide an operation"
my_result=calc("/",5,7)
print(my_result)
def calc_avg(a,b,c):
    result=(a+b+c)/3
    print(result)
    return result

scoreKoalas=calc_avg(98,99,89)
scoreDolphins=calc_avg(49,30,38)
def check_winner(scoreDolphins,scoreKoalas):
    if scoreKoalas>=2*scoreDolphins:
        result=f"Koalas wins : {scoreKoalas} vs {scoreDolphins}"
        print(result)
        return result
    elif scoreDolphins>=2*scoreKoalas:
         result=f"Dolphins win :{scoreDolphins} vs {scoreKoalas}"
         print(result)
         return result
    else:print("No team wins")
check_winner(scoreDolphins,scoreKoalas)
#def fruit_processer(apples,oranges):
def calc_age(birthyr):
    age=2024-birthyr
    return age
the_result=calc_age(1980)
print(the_result)
    
