import streamlit as st
import pandas as pd
import pycaret
from pycaret.regression import load_model as load_model_regression, predict_model as predict_model_regression
from pathlib import Path

st.title('Home Price Prediction')

def predict_homes(model, df):
    predictions = predict_model_regression(estimator=model, data =df)
    
    return predictions['prediction_label'][0]

homes = load_model_regression(Path(__file__).parents[2] / 'models' / 'homely_resort')

def get_user_inputs():
    st.write("Fill in the following fields to get a rough estimate of the price!")
    
    accomodates = st.slider("Accomodates (pax)", 1, 16, step = 1)
    
    availability = st.slider("Whats the availability (per month)", 1,30, step=1)
    
    bathrooms = st.slider("How many bathrooms do you have?", 0.0, 7.0, step=0.5)
    
    bed_types = ['Airbed','Couch','Futon','Pull-out Sofa','Real Bed']
    bed_type = st.selectbox("Bed Type", bed_types)
    
    bedrooms = st.slider('How many beds in the rental?', 0.0,10.0, step=1.0)
    
    beds = st.slider('How many beds?',1.0,16.0, step=1.0)
    
    calculated = st.slider('How many available listings?',1,20, step = 1)
    
    cancellation_policy = ['flexible','moderate','no_refunds','strict','super_strict_30']
    cancellation = st.selectbox("Cancellation_policy", cancellation_policy)
    
    guest = st.slider('How many extra guests?',0,15, step=1)
    
    hosts = ['t','f']
    host = st.selectbox("Is host a superhost?", hosts)
    
    listings = st.slider('How many total listings?', 1.0,21.0,step =1.0)
    
    bookables = ['t','f']
    bookable = st.selectbox('Is listing available now?',bookables)
    
    nights = st.slider('Maximum Nights of stay',1,365)
    
    reviews = st.slider('How many reviews does this listing have?',1, 500, step=1)
    
    properties = ['Apartment','Bed & Breakfast','Boat','Bungalow','Cabin','Camper/RV',
                  'Condominium','House','Loft','Other','Tent','Townhouse','Villa']
    property = st.selectbox("Type of property", properties)
    
    checkin = st.slider("Rate check-in",1.0,10.0,step=1.0)
    
    communication = st.slider("Rate communication",1.0,10.0,step=1.0)
    
    location = st.slider("Rate location",1.0,10.0,step=1.0)
    
    rating = st.slider("Overall Rating",1.0,100.0,step = 1.0)
    
    value = st.slider("Rate value for money",1.0,10.0,step=1.0)
    
    rooms = ['Entire home/apt','Private room','Shared room']
    room = st.selectbox('What are you renting?', rooms)
    
    user_input ={
        "accommodates" : accomodates,
        "availability_30": availability,
        "bathrooms": bathrooms,
        "bed_type": bed_type,
        "bedrooms": bedrooms,
        "beds": beds,
        "calculated_host_listings_count": calculated,
        "cancellation_policy": cancellation,
        "guests_included": guest,
        "host_is_superhost": host,
        "host_listings_count": listings,
        "instant_bookable": bookable,
        "maximum_nights": nights,
        "number_of_reviews": reviews,
        "property_type": property,
        "review_scores_checkin":checkin,
        "review_scores_communication": communication,
        "review_scores_location": location,
        "review_scores_rating": rating,
        "review_scores_value": value,
        "room_type":room,
    }
    
    features_df = pd.DataFrame([user_input])
    features_df['host_is_superhost'] = features_df['host_is_superhost'].replace({'t': 1, 'f': 0})
    features_df['instant_bookable'] = features_df['instant_bookable'].replace({'t': 1, 'f': 0})
    
    return features_df, user_input

if __name__ == "__main__":
    col1, col2, col3 = st.columns([3,1,2])
    
    with col1:
        df, user_input = get_user_inputs()
    with col3:
        prediction = predict_homes(homes, df)
        output = round(prediction)
        st.subheader("Predicted Price")
        st.write('The predicted rental of the listing is: ')
        st.write(f"<h1 style='color:green;'> ${output}</h1>", unsafe_allow_html=True)

    