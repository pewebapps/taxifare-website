import datetime
import requests
import streamlit as st

url = 'https://taxifare.lewagon.ai/predict'


st.title("TAXI FARE PREDICTION")

with st.form("my_form"):
    d = st.date_input("Date")
    st.write("Date is:", d)

    t = st.time_input("Time")
    st.write("Time is", t)

    pickup_lat = st.number_input("Pickup Latitude")
    st.write("The latitude is", pickup_lat)

    pickup_lon = st.number_input("Pickup Longitude")
    st.write("The longitude is", pickup_lon)

    dropff_lat = st.number_input("Dropoff Latitude")
    st.write("The latitude is", dropff_lat)

    dropoff_lon = st.number_input("Dropoff Longitude")
    st.write("The longitude is", dropoff_lon)

    option = st.selectbox(
        "Total Passengers?",
        (1, 2, 3, 4, 5, 6),
        index=None,
        placeholder="",
    )
    st.write("You selected:", option)

    # Combine date and time
    combined_datetime = datetime.datetime.combine(d, t)
    formatted_datetime = combined_datetime.strftime("%Y-%m-%d %H:%M:%S")

    params = {
        "pickup_datetime": formatted_datetime,
        "pickup_latitude": pickup_lat,
        "pickup_longitude": pickup_lon,
        "dropoff_longitude": dropoff_lon,
        "dropoff_latitude": dropff_lat,
        "passenger_count": option
    }


    submitted = st.form_submit_button("Submit")
    if submitted:
        response = requests.get(url=url, params=params).json()
        if response:
            st.subheader("Response:")
            st.json(response)

    # submitted = st.form_submit_button("Submit")
    #     if submitted:
    #         st.write("slider", slider_val, "checkbox", checkbox_val)
