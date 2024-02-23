import streamlit as st
import pandas as pd
from pycaret.classification import load_model, predict_model
from pathlib import Path


st.title('Mushroom Prediction')

def predict_mushroom(model, df):
    
    predictions_data = predict_model(estimator = model, data = df)
    return predictions_data['prediction_label'][0]

mr_model = load_model(Path(__file__).parents[2] / 'models' / 'mushroom_pipeline')


def get_user_input():
    st.write("Please fill in the required information to get your prediction")

    cap_shapes = ['convex', 'bell', 'sunken', 'flat', 'knobbed', 'conical']
    cap_shape = st.selectbox("Cap Shape", cap_shapes)

    cap_surfaces = ['smooth', 'scaly', 'fibrous', 'grooves']
    cap_surface = st.selectbox("Cap Surface", cap_surfaces)

    cap_colors = ['brown', 'yellow', 'white', 'gray', 'red', 'pink', 'buff', 'purple', 'cinnamon', 'green']
    cap_color = st.selectbox("Color of Cap", cap_colors)

    bruise = ['bruises', 'no']
    bruises = st.selectbox("Bruises", bruise)

    odors = ['pungent', 'almond', 'anise', 'none', 'foul', 'creosote', 'fishy', 'spicy', 'musty']
    odor = st.selectbox("Odor", odors)
    
    gill_attach = ['free', 'attached']
    gill_attachment = st.selectbox("Gill Attachment", gill_attach)

    gill_space = ['close', 'crowded']
    gill_spacing = st.selectbox("Gill Spacing", gill_space)

    gill_sizes = ['narrow', 'broad']
    gill_size = st.selectbox("Gill Size", gill_sizes)

    gill_colors = ['black', 'brown', 'gray', 'pink', 'white', 'chocolate', 'purple', 
                   'red', 'buff', 'green', 'yellow', 'orange']
    gill_color = st.selectbox("Gill Color", gill_colors)
    
    stalk_shapes = ['enlarging', 'tapering']
    stalk_shape = st.selectbox("Stalk Shape", stalk_shapes)

    stalk_roots = ['equal', 'club', 'bulbous', 'rooted']
    stalk_root = st.selectbox("Stalk Root", stalk_roots)

    stalk_surface_ar = ['smooth', 'fibrous', 'silky', 'scaly']
    stalk_surface_above_ring = st.selectbox("Stalk Surface Above Ring", stalk_surface_ar)

    stalk_surface_br = ['smooth', 'fibrous', 'scaly', 'silky']
    stalk_surface_below_ring = st.selectbox("Stalk Surface Below Ring", stalk_surface_br)

    stalk_color_ar = ['white', 'gray', 'pink', 'brown', 'buff', 'red', 'orange', 
                      'cinnamon', 'yellow']
    stalk_color_above_ring = st.selectbox("Stalk Color Above Ring", stalk_color_ar)
    
    stalk_color_br = ['white', 'pink', 'gray', 'buff', 'brown', 'red', 'yellow', 
                      'orange', 'cinnamon']
    stalk_color_below_ring = st.selectbox("Stalk Color Below Ring", stalk_color_br)
    
    veil_colors = ['white', 'brown', 'orange', 'yellow']
    veil_color = st.selectbox("Veil Color",veil_colors)

    ring_numbers = ['one', 'two', 'none']
    ring_number = st.selectbox("Rings on the Stem", ring_numbers)

    ring_types = ['pendant', 'evanescent', 'large', 'flaring', 'none']
    ring_type = st.selectbox( "Type of Rings", ring_types)

    spore_print_colors = ['black', 'brown', 'purple', 'chocolate', 'white', 'green', 
                          'orange', 'yellow', 'buff']
    spore_print_color = st.selectbox("Spore Print Color",spore_print_colors)
    
    pop = ['scattered', 'numerous', 'abundant', 'several', 'solitary', 
                  'clustered']
    population = st.selectbox("Population", pop)
    
    habitats = ['urban', 'grasses', 'meadows', 'woods', 'path', 'leaves']
    habitat = st.selectbox("Habitat", habitats)



    user_input = {
        "cap-shape": cap_shape,
        "cap-surface": cap_surface,
        "cap-color": cap_color,
        "bruises": bruises,
        "odor": odor,
        "gill-attachment": gill_attachment,
        "gill-spacing": gill_spacing,
        "gill-size": gill_size,
        "gill-color": gill_color,
        "stalk-shape": stalk_shape,
        "stalk-root": stalk_root,
        "stalk-surface-above-ring": stalk_surface_above_ring,
        "stalk-surface-below-ring": stalk_surface_below_ring,
        "stalk-color-above-ring": stalk_color_above_ring,
        "stalk-color-below-ring": stalk_color_below_ring,
        "veil-color": veil_color,
        "ring-number": ring_number,
        "ring-type": ring_type,
        "spore-print-color": spore_print_color,
        "population": population,
        "habitat": habitat,
    }


    features_df = pd.DataFrame([user_input])
    # prediction = predict_quality(model, features_df)
    # st.write(prediction)
    return features_df, user_input



if __name__ == "__main__":
    st.markdown("""
        <style>
            .stColumn > div:first-child { 
                position: sticky;
                top: 10px;
                z-index: 1000;
            }
        </style>
        """, 
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([3, 1, 2])
    with col1:
        df, user_input = get_user_input()
    with col3:
        prediction = predict_mushroom(model, df)
        st.subheader('Predicted Output')
        if prediction == 'poisonous':
            st.markdown("<h1 style='color: red;'>‼️ OH NO ‼️</h1>", unsafe_allow_html=True)
            st.write(f':red_circle[Based on feature values, you are likely to have cardiovascular issues]')
        if prediction == 'edible':
            st.markdown("<h1 style='color: green;'>YAY 😀</h1>", unsafe_allow_html=True)
            st.write(f':green_circle[Based on feature values, you are normal. Unlikely to have cardiovascular issues]')