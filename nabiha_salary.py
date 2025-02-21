number_of_month=int(input("enter the user below :"))
total_result=[]
for i in range(0,number_of_month):
#Create a user inputs
      nabiha_salary_of_the_month=int(input("Nabiha enter your salary of the month : "))
      month_name=input("enter your month name to store your salary for : ")
      your_saving_nabiha=int(input("Nabiha enter your saving  : "))
      your_rent_nabiha=int(input("Nabiha enter your rent : "))
      your_electricity_consumption=int(input("Nabiha enter your electricity consumption : "))
      additional_amount=150
      is_additional=True
#calculate the percentage of saving , rating and electricity
      nabiha_total_saving=your_saving_nabiha / nabiha_salary_of_the_month * 100 
      nabiha_total_rent=your_rent_nabiha / nabiha_salary_of_the_month * 100 
      nabiha_total_electricity_consumption=your_electricity_consumption / nabiha_salary_of_the_month * 100 
      total_amount=nabiha_total_saving + nabiha_total_rent + nabiha_total_electricity_consumption
      remainder_salary=nabiha_salary_of_the_month - total_amount
      total_yearly_rent=nabiha_total_rent + nabiha_total_electricity_consumption * 12
#nabiha total salary of the month times 2 just for fun
      nabiha_double_total_salary=nabiha_salary_of_the_month ** 2
      total_result.append(f"Nabiha Salary {nabiha_salary_of_the_month} $")
      total_result.append(f"The Month Name {month_name}")
      total_result.append(f"Nabiha Total Saving {nabiha_total_saving} $")
      total_result.append(f"Nabiha Total Rent {nabiha_total_rent} $")
      total_result.append(f"Nabiha Total Electricity Consumption {nabiha_total_electricity_consumption} $")
      total_result.append(f"Nabiha Total Amount {total_amount} $")
      total_result.append(f"Nabiha Remainder Salary {remainder_salary} $")
      total_result.append(f"Nabiha Total Yearly Rent is {total_yearly_rent} $")
      total_result.append(f"Nabiha Double Total Salary {nabiha_double_total_salary} $")
      # if is_additional:
      #    nabiha_additional_amount=additional_amount / total_amount
      #    total_result.append(f"Nabiha Additional Amount is : {nabiha_additional_amount} $")
for item in range(len(total_result)):
   print(nabiha_salary_of_the_month==total_result[item])
 # print(total_result)
    
 
 
 

