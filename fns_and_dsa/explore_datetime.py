from datetime import now, today

def display_current_datetime():
    current_date = now()
    print(f'Current date and time: {current_date}')
    
    
def calculate_future_date():
    number_of_days = int(input('Enter the number of days to add to the current date: '))
    future_date = today() + timedelta(days=number_of_days)
    print(f'Future date: {future_date}')