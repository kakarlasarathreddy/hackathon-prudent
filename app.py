import streamlit as st
import joblib
import numpy as np

# Load the trained model
with open(r'C:\Users\HOME\Downloads\sentiment_analysis_ hotelreviews\naive_bayes.pkl', 'rb') as file:
    model = joblib.load(file)

# Define your Streamlit application
def app():
    st.image(r'C:\Users\HOME\Downloads\1_fDnVCDLv3a8tyxuZEWIS3w.png')
    st.title("Sentiment Analysis on Customer Reviews📝")

    # Collect user input for the features
    text = st.text_input('Enter your text here')
    
    # Add custom CSS to style the text only
    st.markdown("""
    <style>
    .result-text {
        font-size: 20px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    # Make predictions using the loaded model
    if st.button("Detect"):
        prediction = model.predict([text])[0]  # Get the single prediction
        
        # Map the numerical prediction to sentiment label
        if prediction == 0:
            Result = "Negative Review😡"
        elif prediction == 1:
            Result = "Positive Review😇"
        else:
            Result = "Neutral Review🤔"

        # Display the results with larger and bold text
        st.markdown(f"<div class='result-text'>{Result}</div>", unsafe_allow_html=True)

# Run the Streamlit application
if __name__ == "__main__":
    app()