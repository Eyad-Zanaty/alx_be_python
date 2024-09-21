monthly_income = eval(input("please input your monthly income: "))
monthly_expenses = eval(input("please input your monthly expenses: "))
monthly_saving = monthly_income - monthly_expenses
annually_saving = monthly_saving * 12 + (monthly_saving * 12 * 0.05)
print("Your monthly saving is:", monthly_saving)
print("your annually saving is:", annually_saving)