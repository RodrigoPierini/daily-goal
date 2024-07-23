import streamlit as st

# Function to convert hours and minutes to decimal time
def convert_to_decimal_time(time_str):
    hours, minutes = map(int, time_str.split(':'))
    decimal_time = hours + minutes / 60
    return decimal_time

# Function to convert decimal time to hours and minutes
def convert_to_hours_minutes(decimal_time):
    hours = int(decimal_time)
    minutes = int((decimal_time - hours) * 60)
    return hours, minutes

# Streamlit app
st.title('Daily BOH Goal Calculator')

# Input for total time for the day
time_input = st.text_input('Total Time for the Day (format: hours: minutes):', '8:00')

# Input for units of FTW to be processed for the day
units_ftw = st.number_input('Units of FTW to be Processed for the Day:', min_value=0, value=0)

if st.button('Calculate'):
    # Processing total time
    total_time = convert_to_decimal_time(time_input)
    st.write(f'Total time (in decimal): {total_time}')
    hours_total, minutes_total = convert_to_hours_minutes(total_time)
    st.write(f'⏳ Total time: {hours_total}:{minutes_total}')

    # Time to process FTW
    time_ftw = units_ftw / 140
    hours_ftw, minutes_ftw = convert_to_hours_minutes(time_ftw)
    st.write(f'⏳👟 Time to process FTW: {hours_ftw}:{minutes_ftw}')

    # Remaining time to process APP
    time_app = total_time - time_ftw
    hours_app, minutes_app = convert_to_hours_minutes(time_app)
    st.write(f'⏳👕 Remaining time to process APP: {hours_app}:{minutes_app}')

    # Goal for APP
    goal_app = 90 * time_app
    goal_app_round = round(goal_app)
    st.write(f'👕 Goal for APP: {goal_app_round}')

    # Time to Pricing APP
    time_pricing = time_app * 0.3
    hours_pricing, minutes_pricing = convert_to_hours_minutes(time_pricing)
    st.write(f'🏷️ Time to Pricing APP: {hours_pricing}:{minutes_pricing}')

    # Time to Hanging APP
    time_hanging = time_app * 0.7
    hours_hanging, minutes_hanging = convert_to_hours_minutes(time_hanging)
    st.write(f'〰️ Time to Hanging APP: {hours_hanging}:{minutes_hanging}')
