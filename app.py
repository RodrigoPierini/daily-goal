import streamlit as st

# Create a sidebar for navigation between pages
page = st.sidebar.selectbox("Select a Page", ["Goal Calculator", "Settings"])

# Set default values for session state (if not already set)
if 'ftw_units_hour' not in st.session_state:
    st.session_state.ftw_units_hour = 140
if 'ftw_binned_units_hour' not in st.session_state:
    st.session_state.ftw_binned_units_hour = 400
if 'app_units_hour' not in st.session_state:
    st.session_state.app_units_hour = 90

# Function to convert hours and minutes to decimal time
def convert_to_decimal_time(time_str):
    try:
        if ':' not in time_str:
            time_str += ':00'
        hours, minutes = map(int, time_str.split(':'))
        decimal_time = hours + minutes / 60
        return decimal_time
    except ValueError:
        st.error("Invalid time format. Please enter time in the format hours:minutes.")
        return None

# Function to convert decimal time to hours and minutes with leading zero for minutes
def convert_to_hours_minutes(decimal_time):
    hours = int(decimal_time)
    minutes = int((decimal_time - hours) * 60)
    return hours, f'{minutes:02d}'  # Format minutes with leading zero

# Page 1: Goal Calculator
if page == "Goal Calculator":
    st.title('Daily BOH Goal Calculator')

    # Input for total time for the day
    time_input = st.text_input('Total Time for the Day (format: hours: minutes):', '8:00')

    # Input for units of FTW to be processed for the day
    units_ftw = st.number_input('Units of FTW to be Processed for the Day:', min_value=0, value=0)

    # Input for units of FTW to be binned
    units_ftw_binned = st.number_input('Units of FTW to be binned:', min_value=0, value=0)

    if st.button('Calculate'):
        # Processing total time
        total_time = convert_to_decimal_time(time_input)
        if total_time is not None:
            st.write(f'Total time (in decimal): {total_time}')
            hours_total, minutes_total = convert_to_hours_minutes(total_time)
            st.write(f'⏳ Total time: {hours_total}:{minutes_total}')

            # Time to process FTW
            time_ftw = units_ftw / st.session_state.ftw_units_hour
            hours_ftw, minutes_ftw = convert_to_hours_minutes(time_ftw)
            st.write(f'⏳👟 Time to process FTW: {hours_ftw}:{minutes_ftw}')

            # Time to bin FTW
            time_ftw_binned = units_ftw_binned / st.session_state.ftw_binned_units_hour
            hours_ftw_binned, minutes_ftw_binned = convert_to_hours_minutes(time_ftw_binned)
            st.write(f'⏳👟 Time to bin FTW: {hours_ftw_binned}:{minutes_ftw_binned}')

            # Remaining time to process APP
            time_app = total_time - time_ftw - time_ftw_binned
            hours_app, minutes_app = convert_to_hours_minutes(time_app)
            st.write(f'⏳👕 Remaining time to process APP: {hours_app}:{minutes_app}')

            # Goal for APP
            goal_app = st.session_state.app_units_hour * time_app
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

# Page 2: Settings
elif page == "Settings":
    st.title('Settings')
    st.write("Here you can customize the units per hour.")

    # Input fields for settings
    st.session_state.ftw_units_hour = st.number_input('FTW Units per Hour:', min_value=1, value=st.session_state.ftw_units_hour)
    st.session_state.ftw_binned_units_hour = st.number_input('FTW Binned Units per Hour:', min_value=1, value=st.session_state.ftw_binned_units_hour)
    st.session_state.app_units_hour = st.number_input('APP Units per Hour:', min_value=1, value=st.session_state.app_units_hour)

    st.success("Settings updated!")
