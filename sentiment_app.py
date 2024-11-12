import nltk
from textblob import TextBlob
import streamlit as st

# Download NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('brown')

def analyze_sentiment(text):
    """Analyzes the sentiment of a given text using TextBlob."""
    analysis = TextBlob(text)
    return analysis.sentiment.polarity, analysis.sentiment.subjectivity

def classify_sentiment(polarity):
    """Classifies the sentiment based on the polarity score."""
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Set up the app
st.set_page_config(page_title="Sentiment Analyzer", page_icon="😊")

# Create a container for the main content
container = st.container()

with container:
    # Add a title and description
    st.title("Sentiment Analyzer")
    st.write("Enter your text below and click 'Analyze' to get the sentiment.")

    # Create a text input field with a placeholder
    text_input = st.text_area("Your Text Here", height=200)

    # Add an analyze button
    if st.button("Analyze"):
        if text_input:
            polarity, subjectivity = analyze_sentiment(text_input)
            sentiment = classify_sentiment(polarity)

            # Display the results in a visually appealing way
            st.markdown(f"### Sentiment Analysis Results")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Polarity:** {polarity:.2f}")
                st.markdown(f"**Subjectivity:** {subjectivity:.2f}")
            with col2:
                st.markdown(f"**Overall Sentiment:**")
                if sentiment == "Positive":
                    st.markdown(f"<h1 style='color:green;'>{sentiment}</h1>", unsafe_allow_html=True)
                elif sentiment == "Negative":
                    st.markdown(f"<h1 style='color:red;'>{sentiment}</h1>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<h1 style='color:red;'>{sentiment}</h1>", unsafe_allow_html=True)
        else:
            st.warning("Please enter some text.")

# Add a background image and custom CSS
st.markdown(
    """
    <style>
        .stApp {
            background-image: url(https://wallpaperset.com/w/full/5/f/a/176039.jpg);
            background-size: cover;
        }
    </style>
    """,
    unsafe_allow_html=True
)