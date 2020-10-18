def main():
    print("This program helps you calculate a property's return on investment."\
        + "\nor ROI.")
    my_building = buildingBuilder()

class building():
    def __init__(self):
        self.house = True

    def incomeBuild(self, rental, laundry, storage, misc):
        self.income = [rental, laundry, storage, misc]

        self.totIncome = sum(self.income)

    def expensesBuild(self, taxes, insurance, hoa, lawn, vacancy, repairs,\
            capex, propManage, mortgage, water = 0, garbage = 0, electric = 0, gas = 0):
        self.expenses = [taxes, insurance, hoa, lawn, vacancy, repairs,\
            capex, propManage, mortgage]
        self.totExpenses = sum(self.expenses)
    
    def cashFlow(self):
        self.totCashFlow = self.totIncome - self.totExpenses
        return self.totCashFlow
    
    def investmentBuild(self, downPay, closing, rehab, misc):
        self.investments = [downPay, closing, rehab, misc]
        self.totInvestments = sum(self.investments)
        
    def roiBuild(self):
        self.roi = self.totCashFlow * 12 / self.totInvestments * 100
        return self.roi

def buildingBuilder():
    abuilding = building()
    # Income
    print("Let's calculate the total income of the property.")
    print("Upon prompts, enter the expected monthly values for the property")
    print("If you don't know a value, just press enter to use the average typical value")
    rental_in = printer('rental income', 2000)
    laundry_in = printer('laundry income', 0)
    storage_in = printer("storage income", 0)
    misc_in = printer("miscellaneous income", 0)
    abuilding.incomeBuild(rental_in, laundry_in, storage_in, misc_in)
    print(f"This property's total monthtly income is {abuilding.totIncome}")
    print()

    # Expenses
    print("Let's calculate the property's total expenses!")
    taxes = printer('property taxes', 150)
    insurance = printer('insurance payments', 100)
    hoa = printer('HOA fees', 0)
    lawn = printer('lawn/snow fees', 0)
    vacancy = printer('savings in case of vacancy', 100)
    repairs = printer('property repairs', 100)
    capex = printer('capital expenses', 100)
    propManage = printer('property management', 200)
    mortgage = printer('mortgage payments', 860)   
    utility = input('Will the tenents pay for the utilites?(y/n)')
    if utility.lower not in ['n', 'no']:
        water = printer("water/sewer payments", 30)
        garbage = printer("garbage cost", 30)
        electric = printer('electric cost', 30)
        gas = printer("gas cost", 30)
        abuilding.expensesBuild(taxes, insurance, hoa, lawn, vacancy, repairs,\
            capex, propManage, mortgage, water, garbage, electric, gas)
    else:
        abuilding.expensesBuild(taxes, insurance, hoa, lawn, vacancy, repairs,\
            capex, propManage, mortgage)
    print(f"This property's total monthly expensive is {abuilding.totExpenses}")
    print()

    # Cash flow
    print("Let's find the cash flow for the property!")
    print(f"The property's monthly cashflow is {abuilding.cashFlow()}.")
    print()

    # Cash on Cash Return
    print("Let's calculate the property's Cash on Cash Return on Investment!")
    # Calculating investments
    downPay = printer('down payment', 40000, start = 'Property')
    closing = printer('closing costs', 3000, start = 'Property')
    rehab = printer('rehab budget', 7000, start = 'Property')
    misc = printer('miscellenous ownership costs', 0, start = 'Property')
    abuilding.investmentBuild(downPay, closing, rehab, misc)
    print(f"The property's investment cost is {abuilding.totInvestments}.")
    print()
    # getting ROI
    print("The property's Cash on Cash Return on Investment is "\
        + f"{abuilding.roiBuild()}%.")

    return abuilding

def printer(category, default, start = 'Monthly'):
    value =  input(f'{start} {category}: ')
    try:
        return int(value)
    except:
        print(f'Using default value: {default}')
        return default

main()