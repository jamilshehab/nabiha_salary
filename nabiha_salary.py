number_of_month=int(input("enter the user below :"))
for i in range(number_of_month):
#Create a user inputs
      nabiha_salary_of_the_month=int(input("Nabiha enter your salary of the month : "))
      month_name=input("enter your month name to store your salary for : ")
      your_saving_nabiha=int(input("Nabiha enter your saving  : "))
      your_rent_nabiha=int(input("Nabiha enter your rent : "))
      your_electricity_consumption=int(input("Nabiha enter your electricity consumption : "))
      additional_amount=150
#calculate the percentage of saving , rating and electricity
      nabiha_total_saving=your_saving_nabiha / nabiha_salary_of_the_month * 100 
      nabiha_total_rent=your_rent_nabiha / nabiha_salary_of_the_month * 100 
      nabiha_total_electricity_consumption=your_electricity_consumption / nabiha_salary_of_the_month * 100 
 
      total_amount=nabiha_total_saving + nabiha_total_rent + nabiha_total_electricity_consumption

      remainder_salary=nabiha_salary_of_the_month % total_amount

      total_yearly_rent=nabiha_total_rent + nabiha_total_electricity_consumption * 12

#nabiha total salary of the month times 2 just for fun
      nabiha_double_total_salary=nabiha_salary_of_the_month ** 2
      
      total_result=[]
      total_result.append({"Nabiha Salary" : nabiha_salary_of_the_month})
      total_result.append({"The Month Name" : month_name})
      total_result.append({"Nabiha Total Saving " : nabiha_total_saving})
      total_result.append({"Nabiha Total Rent " : nabiha_total_rent})
      total_result.append({"Nabiha Total Electricity Consumption" : nabiha_total_electricity_consumption})
      total_result.append({"Nabiha Total Amount is" : nabiha_total_electricity_consumption})
      total_result.append({"Nabiha Remainder Salary" : nabiha_total_electricity_consumption})
      total_result.append({"Nabiha Total Yearly Rent is " : nabiha_total_electricity_consumption})
      total_result.append({"Nabiha Double Total Salary" : nabiha_double_total_salary})
for key,value in total_result:
    if key == month_name and key == nabiha_salary_of_the_month:
       print("Hi")
# print(total_result)

 

