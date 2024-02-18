import streamlit as st
import requests

# Streamlit app header
def news():
    st.title("Your News")

    # Function to fetch health news from the News API
    def get_health_news(api_key,countries,category,language,start,end):
        NEWS_API_ENDPOINT = "https://newsapi.org/v2/top-headlines"
        params = {
            "apiKey": api_key,
            "country": countries,
            "category": category,
            "languge":language,
            "from":start,
            "to":end
        }

        response = requests.get(NEWS_API_ENDPOINT, params=params)

        if response.status_code == 200:
            news_data = response.json()
            articles = news_data.get("articles", [])
            return articles
        else:
            st.error("Error fetching news data.")
            return []

    # Input field for the News API key
    api_key = "d60a3309a20c4386bd73eb16d7b3c992"

    # Fetch health news
    try:
        if api_key:
            countries=st.selectbox(label="Choose Your Country",options=['In','Us','at','au','bg','cn','de','eg','fr','gd','gr','il','it','jp','kr','no','nz','ru','sg','ua','za'])
            category=st.selectbox(label="Category ",options=['health','business','entertainment','science','general','sports','technology'])
            languages=st.selectbox(label="language ",options=['en','ar','de','es','fr','he','it','no','nl','pt','ru','sv','ud','zh'])
            start=st.date_input("Enter Start date:")
            end=st.date_input("Enter end date")
            health_news = get_health_news(api_key,countries,category,languages,start,end)

            # Display news articles with imagesend=
            for index, article in enumerate(health_news, start=1):
                st.subheader(f"{index}. {article['title']}")
                st.image(article['urlToImage'], caption='Image', use_column_width=True)
                st.write(article['description'])
                st.text(f"Source: {article['source']['name']}")
                st.text(f"Published at: {article['publishedAt']}")
                st.divider()
    except:
        st.success("Done")

