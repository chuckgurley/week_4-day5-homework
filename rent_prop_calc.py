# """
  
#     Group 1
# -Manja Wilson
# -Abdelkader Elhamri
# -Chuck Gurley
    
    
#     First section -INCOME-
    
#     inputs - 
#         rental income _2000____
#         laundry income___0___
#         storage income__0___
#         misc income__0____
        
#     total monthly property income------>___show output__2000___<------ important value month_income
    
        
#     Second section -annual-
    
#     inputs-
#         taxes - 150
#         insurance- 100
#         
#             electric-0
#             water-0
#             sewer-0
#             garbage-0
#             gas-0
#         HOA fees-0
#         lawn service-0
#         vacancy- 100
#         repairs-100
#         capital expenses(roof appliances)-100
#         property management-200
#         mortgage-860
        
#     total monthly property expenses------>_____show output__1610_______<------ important value month_expenses
    
    
    
#     Third Section  -CASH FLOW-
    
#     inputs- 
#       (month_income) -  (month_expenses) = cash_flow   (2000 - 1610 = 390)
      
#       ------------>___show output_300__<------------- important value cash_flow 
      
    
    
#     Fourth Section Cash on Cash Return on Investment
    
#     create inputs -    
#         Down Payment ___40000_______    
#         Closing Cost___3000______      
#         Repair or Rehab___7000_____       
#         misc ___0___                                                                                  
        
#             add together =  ---> total investment 50000 (total_invest) 
                                                                                    
#        cash_flow x 12 = --->_____show output__4680____<--------- annual_cash_flow
       
#        annual_cash_flow( 4680) / total_investment( 50000) = cash_on_cash_roi x 100 and turned into %
       
       
#         --------------->  actuall_COCROI 9.36<---------------
         
    
    
#     """

# Step 1: Get monthly income
rental_income = float(input("Enter rental income: "))
laundry_income = float(input("Enter laundry income: "))
storage_income = float(input("Enter storage income: "))
misc_income = float(input("Enter miscellaneous income: "))
monthly_income = rental_income + laundry_income + storage_income + misc_income

# Step 2: Get monthly expenses
taxes = float(input("Enter taxes: "))
insurance = float(input("Enter insurance: "))
electric = float(input("Enter electric bill: "))
water = float(input("Enter water bill: "))
sewer = float(input("Enter sewer bill: "))
garbage = float(input("Enter garbage bill: "))
gas = float(input("Enter gas bill: "))
hoa_fees = float(input("Enter HOA fees: "))
lawn_service = float(input("Enter lawn service cost: "))
vacancy = float(input("Enter vacancy cost: "))
repairs = float(input("Enter repairs cost: "))
capital_expenses = float(input("Enter capital expenses cost: "))
property_management = float(input("Enter property management cost: "))
mortgage = float(input("Enter mortgage payment: "))
monthly_expenses = taxes + insurance + electric + water + sewer + garbage + gas + hoa_fees + lawn_service + vacancy + repairs + capital_expenses + property_management + mortgage

# Step 3: Calculate monthly cash flow
monthly_cash_flow = monthly_income - monthly_expenses

# Step 4: Calculate total investment
down_payment = float(input("Enter down payment: "))
closing_cost = float(input("Enter closing cost: "))
repair_rehab = float(input("Enter repair or rehab cost: "))
misc = float(input("Enter miscellaneous cost: "))
total_investment = down_payment + closing_cost + repair_rehab + misc

# Step 5: Calculate annual cash flow and ROI
annual_cash_flow = monthly_cash_flow * 12
roi = annual_cash_flow / total_investment * 100

# Step 6: Print ROI
print("Cash on Cash Return on Investment: {:.2f}%".format(roi))