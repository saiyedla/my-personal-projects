def calculate_compound_interest(initial_amount, annual_interest_rate, term_years, contribution_amount=0, contribution_frequency='yearly'):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    
    total_periods = term_years * 12 if contribution_frequency == 'monthly' else term_years
    
    total_amount = initial_amount
    
    for period in range(total_periods):
        if contribution_frequency == 'monthly' or (contribution_frequency == 'yearly' and period % 12 == 0):
            total_amount += contribution_amount
        
        total_amount *= (1 + monthly_interest_rate)
    
    interest_earned = total_amount - initial_amount - (contribution_amount * total_periods)
    
    print("\nTotal amount after compound interest :", round(total_amount, 2))
    print("\nInterest earned :", round(interest_earned, 2))
    
initial_amount = float(input("Enter initial amount: "))
annual_interest_rate = float(input("Enter annual interest rate (%): "))
term_years = int(input("Enter term in years: "))
contribution_option = input("Do you want to make contributions? (yes/no): ").lower()
contribution_frequency = input("Enter contribution frequency (monthly/yearly): ").lower()

if contribution_option == 'yes':
    contribution_amount = float(input("Enter contribution amount: "))
else:
    contribution_amount = 0
    contribution_frequency = 'yearly'

# Calculate compound interest and directly print the output
calculate_compound_interest(initial_amount, annual_interest_rate, term_years, contribution_amount, contribution_frequency)
