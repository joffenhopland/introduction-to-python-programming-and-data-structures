def main():  
    # Enter yearly interest rate
    annualInterestRate = float(input("Enter yearly interest rate, for example 8.25: "))

    # Enter number of years
    numberOfYears = int(input("Enter number of years as an integer, for example 5: "))
    # Enter loan amount
    loanAmount = float(input("Enter loan amount, for example 120000.95: "))

    # Display results
    print("The monthly payment is $", end = '')
    print(format(getMonthlyPayment(annualInterestRate, numberOfYears, loanAmount), ".2f"))
    print("The total payment is $", end = '')
    print(format(getTotalPayment(annualInterestRate, numberOfYears, loanAmount), ".2f"))
  
def getMonthlyPayment(annualInterestRate, numberOfYears, loanAmount):
    # Obtain monthly interest rate
    monthlyInterestRate = annualInterestRate / 1200

    # Calculate payment
    monthlyPayment = loanAmount * monthlyInterestRate / (1
      - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))

    return monthlyPayment
  
def getTotalPayment(annualInterestRate, numberOfYears, loanAmount):
    return getMonthlyPayment(annualInterestRate, numberOfYears, 
      loanAmount) * numberOfYears * 12;        

main()
