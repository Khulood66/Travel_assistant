
import streamlit as st
import openai
st.set_page_config('Travale assites',page_icon='.\Vector.png',)

openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_destination_suggestions(preferences, budget,lan):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.1,
        messages=[
            {"role": "system", "content": f"You are a helpful travel planning assistant and speak in {lan} language."},
            {"role": "user", "content": f"Based on the preferences: {preferences} and a budget of {budget}, suggest travel destinations with brief descriptions and Suggest popular tourist activities and places to visit and hotels or accommodations at least 5 suggestion and keep to be defferent from one to anther."}
        ]
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content

def get_activity_hotels_suggestions(destination,lan):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.1,
        messages=[
            {"role": "system", "content": f"You are a helpful travel planning assistantand speak in {lan} language."},
            {"role": "user", "content": f"Suggest popular tourist activities and places to visit in {destination} for a budget of {budget} and can you give some pictures to thes places."}
        ]
    )
    return response.choices[0].message.content

def get_accommodation_suggestions(destination, budget,lan):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.1,
        messages=[
            {"role": "system", "content": f"You are a helpful travel planning assistant and speak in {lan} language."},
            {"role": "user", "content": f"Suggest hotels or accommodations in {destination} for a budget of {budget}."}
        ]
    )
    return response.choices[0].message.content

def get_plan_suggestion(destination,lan,interval):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.1,
        messages=[
            {"role": "system", "content": f"You are a helpful travel planning assistant and speak in {lan} language."},
            {"role": "user", "content": f"Suggest plan for {interval} days that includes interactive activities in {destination} and specify the time."}
        ]
    )
    return response.choices[0].message.content

# إعداد الترجمات
translations = {
    'en': {
        'title': "Travel Planning Assistant",
        'preferences': "Enter your travel preferences (e.g., beaches, shopping, adventure):",
        'budget': "Enter your travel budget (in USD):",
        'days': "Enter the days you expect to stay at your destination:",
        'destination': "Enter your destination:",
        'suggest_destinations': "Suggest Destinations",
        'destination_suggestions': "Destination Suggestions:",
        'choose_destination': "Choose a destination for more details:",
        'activities': "Tourist activities in {destination}:",
        'accommodations': "Accommodations in {destination}:",
        'plan': "Suggest plan for {inteval} in {destination}:",
        'map': "Destination Map:",
        'error_details': "Please enter all details.",
        'error_coordinates': "No coordinates found for this destination."
    },
    'ar': {
        'title': "مساعد تخطيط السفر",
        'preferences': "أدخل تفضيلاتك للسفر (مثلاً: شواطئ، تسوق، مغامرات):",
        'budget': "أدخل ميزانيتك للسفر (بالدولار):",
        'days': "ادخل الايام المتوقع جلوسها في وجهتك :",
        'destination': "أدخل المنطقة التي تحب ان تزورها:",
        'suggest_destinations': "اقتراح وجهات",
        'destination_suggestions': "اقتراحات اخرى :",
        'choose_destination': "اختر وجهة للحصول على تفاصيل أكثر:",
        'activities': "أنشطة سياحية في {destination}:",
        'accommodations': "أماكن الإقامة في {destination}:",
        'plan': "خطة مقترحة لمدة {inteval} في {destination}:",
        'map': "خريطة الوجهة:",
        'error_details': "يرجى إدخال جميع التفاصيل.",
        'error_coordinates': "لم يتم العثور على إحداثيات لهذه الوجهة."
    }
}

# Choose language
language = st.sidebar.selectbox("اختر اللغة | Choose Language", ["English", "العربية"])
lang_code = 'en' if language == "English" else 'ar'

st.title(translations[lang_code]['title'])

# inputs from users
preferences = st.sidebar.text_area(translations[lang_code]['preferences'])
budget = st.sidebar.number_input(translations[lang_code]['budget'], min_value=0)
destination = st.sidebar.text_input(translations[lang_code]['destination'])
inteval = st.sidebar.number_input(translations[lang_code]['days'], min_value=10)

if st.sidebar.button(translations[lang_code]['suggest_destinations']):
    if preferences and budget:
            activities = get_activity_hotels_suggestions(destination,language)
            accommodations = get_accommodation_suggestions(destination, budget,language)
            plan=get_plan_suggestion(destination,language,inteval)
            
            st.subheader(translations[lang_code]['activities'].format(destination=destination))
            st.write(activities)
            
            st.subheader(translations[lang_code]['accommodations'].format(destination=destination))
            st.write(accommodations)

            st.subheader(translations[lang_code]['plan'].format(inteval=inteval,destination=destination))
            st.write(plan)
            destinations = get_destination_suggestions(preferences, budget,language)
            st.subheader(translations[lang_code]['destination_suggestions'])
            st.markdown(body=destinations,unsafe_allow_html=True)

    else:
        st.error(translations[lang_code]['error_details'])

