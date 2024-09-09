class loan:
    def __init__(self, amount, term):
        # Initialize the loan with amount, term, and default values for total, loan type, and interest
        self.amount = amount
        self.term = term
        self.total = 0
        self.loan_type = ''
        self.interest = 0

    def calculate_simple_interest(self, rate):
        # Calculate simple interest and update total amount and interest
        # Formula for simple interest: Interest = Principal * Rate * Time
        i = self.amount * rate / 100 * self.term
        self.total = self.amount + i
        self.interest = i
        self.loan_type = 'Simple interest'
    
    def calculate_compound_interest(self, rate):
        # Calculate compound interest using the formula for compound interest
        # Formula for compound interest: A = P * (1 + r/n)^(nt)
        a = self.amount
        self.loan_type = 'Compound interest'
        for i in range(self.term):
            a += a * (rate / 100)  # Apply interest for each compounding period.
        self.total = a
        self.interest = a - self.amount
    
    def reciept(self):
        # Print a receipt showing the amount, type of loan, and the interest calculated.
        print(f'R {self.amount} {self.loan_type} loan taken ')
        print(f'{self.interest} ')

def main():
    # Main function to interact with the user and perform loan calculations
    print("Loan calculator")
    
    # Get loan amount and term from the user
    amount = float(input("Enter amount: "))
    term = int(input("Enter period: "))
    
    # Create a loan object with the provided amount and term.
    l = loan(amount, term)

    # Prompt the user to choose the type of interest calculation
    type = int(input("1 for simple interest, 2 for compound interest: "))

    # Perform the chosen interest calculation
    if type == 1:
        l.calculate_simple_interest(50)  # Example interest rate for simple interest.
    
    elif type == 2:
        l.calculate_compound_interest(30)  # Example interest rate for compound interest.

    else:
        # Handle invalid input
        print('Invalid Input: Enter a valid value')
    
    # Print the receipt
    l.reciept()

# Entry point of the script
if __name__ == "__main__":
    main()