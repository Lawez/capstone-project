import streamlit as st
import pickle
import pandas as pd

# Load the pickled model
with open('kitale_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Define the expected feature set used during model training
expected_features = ['Calories to Burn (Kcal)', 'Dream Weight', 'Actual Weight', 'Age', 'Duration',
                     'maximum Heart Rate', 'Height', 'Weather Conditions', 'Gender']
# Define the mapping of categories to numerical values for ordinal encoding
weather_mapping = {'Sunny': 0, 'Cloudy': 1, 'Rainy': 2}
gender_mapping = {'Male': 0, 'Female': 1}

# Define a dictionary of intensity levels and descriptions
exercise_intensity_descriptions = {
    1: 'Very low intensity: Suitable for individuals with minimal physical activity, such as walking at a leisurely pace, stretching or yoga, and gentle swimming. However, please note that your preference is prioritized.',
    2: 'Low intensity: Suitable for beginners or individuals with limited physical activity, such as light jogging or running, cycling at a relaxed pace, and beginner\'s aerobics. However, please remember that your preference takes priority.',
    3: 'Moderate intensity: Suitable for individuals who engage in regular physical activity, including brisk walking, dancing, and water aerobics. However, please keep in mind that your preference is given priority.',
    4: 'Medium intensity: Suitable for individuals with moderate fitness and physical activity, such as power walking, cycling at a moderate pace, and Zumba. However, please remember that your preference is given priority.',
    5: 'Moderate to high intensity: Suitable for individuals with moderate to high fitness levels, including jogging or running at a moderate pace, high-intensity interval training (HIIT), and kickboxing. However, please note that your preference is given priority.',
    6: 'High intensity: Suitable for individuals with a high level of fitness and physical activity, such as running at a fast pace, circuit training, and CrossFit. However, please keep in mind that your preference is given priority.',
    7: 'High intensity: Suitable for individuals with a high level of fitness and physical activity, such as advanced HIIT workouts, competitive sports (e.g., soccer, basketball), and spinning or indoor cycling classes. However, please remember that your preference is given priority.',
    8: 'Very high intensity: Suitable for individuals with very high fitness and physical activity, including sprinting or interval sprints, plyometric exercises, and heavy weightlifting. However, please keep in mind that your preference is given priority.',
    9: 'Very higher intensity: Suitable for individuals with very high fitness and physical activity, such as advanced CrossFit workouts, box jumps, and Olympic weightlifting. However, please note that your preference is given priority.',
    10: 'Extremely high intensity: Suitable for athletes or individuals with exceptional fitness levels, including professional sports training, marathon running, and elite-level strength and conditioning programs. However, please remember that your preference is given priority.'
}


def main():
    # Add custom CSS to set the background color and adjust the title position
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("../static/workout.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center center;
            background-color: grey;
        }
        .stApp h1 {
            margin-top: 10px;
            margin-bottom: 30px;
            color: white;
        }
        .stApp label {
            color: white;
        }
        .stApp .predicted-intensity {
            background-color: black;
            padding: 10px;
            border-radius: 10px;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title('Exercise Intensity Recommender')

    # Add spacing between title and input text boxes
    st.markdown("<br>", unsafe_allow_html=True)

    # Add input fields to the first column
    col1, col2 = st.columns(2)
    with col1:
        calorie_range = st.selectbox('Select Calories Range to Burn', ['100 and Below', '101 to 200', '201 to 300', '301 to 400',
                                                      '401 to 500', '501 to 600', '601 to 700', '701 to 800',
                                                      '801 and Above'])
        dream_weight = st.number_input('Dream Weight', step=1, format="%d")
        actual_weight = st.number_input('Actual Weight', step=1, format="%d")
        age = st.number_input('Age', step=1, format="%d")

    # Calculate maximum heart rate
    max_heart_rate = 220 - age

    # Add input fields to the second column
    with col2:
        duration = st.number_input('Duration in minutes', step=1, format="%d")
        height = st.number_input('Height in meters', step=0.01, format="%.2f")
        weather_conditions = st.selectbox('Weather Conditions', ['Sunny', 'Cloudy', 'Rainy'])
        gender = st.selectbox('Gender', ['Male', 'Female'])

    # Prepare user input as a DataFrame
    user_input = pd.DataFrame({
        'Calories to Burn (Kcal)': [0.0],  # Placeholder value
        'Dream Weight': [dream_weight],
        'Actual Weight': [actual_weight],
        'Age': [age],
        'Duration': [duration],
        'maximum Heart Rate': [max_heart_rate],
        'Height': [height],
        'Weather Conditions': [weather_conditions],
        'Gender': [gender]
    })

    # Perform ordinal encoding for categorical features
    user_input_encoded = user_input.copy()
    user_input_encoded['Weather Conditions'] = user_input_encoded['Weather Conditions'].map(weather_mapping)
    user_input_encoded['Gender'] = user_input_encoded['Gender'].map(gender_mapping)

    # Reorder the columns to match the expected feature set
    user_input_encoded = user_input_encoded.reindex(columns=expected_features)

    # Replace the 'Calories to Burn (Kcal)' value based on the selected range
    if calorie_range == '100 and Below':
        user_input_encoded.loc[0, 'Calories to Burn (Kcal)'] = -1
    elif calorie_range == '101 to 200':
        user_input_encoded.loc[0, 'Calories to Burn (Kcal)'] = -0.5
    elif calorie_range == '201 to 300':
        user_input_encoded.loc[0, 'Calories to Burn (Kcal)'] = 0.1
    elif calorie_range == '301 to 400':
        user_input_encoded.loc[0, 'Calories to Burn (Kcal)'] = 0.3
    elif calorie_range == '401 to 500':
        user_input_encoded.loc[0, 'Calories to Burn (Kcal)'] = 0.8
    elif calorie_range == '501 to 600':
        user_input_encoded.loc[0, 'Calories to Burn (Kcal)'] = 1.3
    elif calorie_range == '601 to 700':
        user_input_encoded.loc[0, 'Calories to Burn (Kcal)'] = 1.6
    elif calorie_range == '701 to 800':
        user_input_encoded.loc[0, 'Calories to Burn (Kcal)'] = 1.9
    elif calorie_range == '801 and Above':
        user_input_encoded.loc[0, 'Calories to Burn (Kcal)'] = 3.7

    # Make prediction using the loaded model
    predicted_intensity = loaded_model.predict(user_input_encoded)

    # Round off predicted intensity to the nearest whole number
    rounded_intensity = round(predicted_intensity[0])

    # Get exercise intensity description based on predicted intensity level
    intensity_description = exercise_intensity_descriptions.get(rounded_intensity, 'No description available')

    # Display the rounded intensity, intensity description, and original predicted intensity
    st.subheader('Predicted Exercise Intensity')
    prediction_style = f"predicted-intensity"
    st.markdown(f'<p class="{prediction_style}">{rounded_intensity}</p>', unsafe_allow_html=True)

    st.subheader('Exercise Intensity Description')
    st.write(intensity_description)

    # Show maximum Heart rate
    st.subheader('maximum Heart Rate at that Intensity')
    st.write(max_heart_rate)


if __name__ == '__main__':
    main()
