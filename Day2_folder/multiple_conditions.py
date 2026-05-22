#make multiple conditions to check grade by percentage
#taking marks of subject maths,science and english
math=int(input("enter marks of maths : "))
science=int(input("enter marks of science : "))
english=int(input("enter marks of english : "))

#;ets find the percentage
if math and science and english in range(1,101):
      percentage=(math+english+science)/3
      print(f"your percentage is {percentage}")
      

#lets give the Grade
if percentage >= 90:
    print("Grade A")
elif percentage >=80:
    print("Grade B")
elif percentage >=70 :
    print("Grade c")
elif percentage >=40 :
    print("Grade D")
else :
    print("you are fail")
    