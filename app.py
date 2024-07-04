# import streamlit as st
# from openai import OpenAI

# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


# st.sidebar.header("Sbet parameters")
# sys_Mesaage=st.sidebar.text_input("System message:", value="You are helpful assistant")
# model_TEM=st.sidebar.slider(label="Temp", step=0.01, min_value=0.0,max_value=2.0,value=1.0)
# number = st.sidebar.number_input("Insert a number", value=None, placeholder="Type a number...")
# # st.write("The current number is ", number)

# def get_gym_program(weight, tall):
#   response = client.chat.completions.create(
#       model="gpt-3.5-turbo",
#       temperature=1.7,
#       messages=[
#           {"role": "system", "content": f"{sys_Mesaage}"},
#           {"role": "user", "content": f">>Bio stats: {weight}, {tall}"},
#       ]
#     )
#   return response.choices[0].message.content

# st.title("Real title")
# st.markdown("**Day1 : Upper Body**")
# st.write(sys_Mesaage)



# import streamlit as st
# from openai import OpenAI

# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


# def get_gym_program(system_message, weight, tall, goal):
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         temperature=0.7,
#         messages=[
#             {"role": "system", "content": f"{system_message}"},
#             {"role": "user", "content": f">>Bio stats: {weight}, {tall}\n\n>>Objective: {goal}"},
#         ]
#     )
#     return response.choices[0].message.content


# # User inputs and model parameters
# st.sidebar.header("Sbet parameters")
# system_message = st.sidebar.text_input("System message:",
#                                        value="You are helpful assistant")
# model_temp = st.sidebar.slider("Temp", step=0.01, min_value=0.0,
#                                max_value=2.0,
#                                value=1.0)
# max_token = st.sidebar.slider("Max Token", step=100, min_value=200,
#                               max_value=4000,
#                               value=512)

# goal = st.sidebar.text_input("User objective:",
#                              value="General fitness")
# weight = st.sidebar.number_input(
#     "Insert your weight", value=70, placeholder="Your weight in KG")
# tall = st.sidebar.number_input(
#     "How tall are you:", value=165, placeholder="Your length in CM")


# # Main page components
# st.title("🥗 Sbet the nutritionist")
# get_gym_program(system_message, weight, tall, goal)


# st.markdown("*Day 1: Upper Body*")


# import streamlit as st
# from openai import OpenAI

# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


# def get_gym_program(system_message, weight, tall, goal):
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         temperature=0.7,
#         messages=[
#             {"role": "system", "content": f"{system_message}"},
#             {"role": "user", "content": f">>Bio stats: {weight}, {tall}\n\n>>Objective: {goal}"},
#         ]
#     )
#     return response.choices[0].message.content


# # User inputs and model parameters
# st.sidebar.header("Sbet parameters")
# prompt_message = "You are Sbet my GYM Trainer. \
#                     Based on my objective and my \
#                     Bio stats give me one week program. \
#                     Then add to it nutritionist advise for \
#                     the type of food and calories I need to consume."

# system_message = st.sidebar.text_area("System message:",
#                                       value=prompt_message)
# model_temp = st.sidebar.slider("Temp", step=0.01, min_value=0.0,
#                                max_value=2.0,
#                                value=1.0)
# max_token = st.sidebar.slider("Max Token", step=100, min_value=200,
#                               max_value=4000,
#                               value=512)

# st.sidebar.header("User based input:")
# goal = st.sidebar.text_input("User objective:",
#                              value="General fitness")
# weight = st.sidebar.number_input(
#     "Insert your weight", value=70, placeholder="Your weight in KG")
# tall = st.sidebar.number_input(
#     "How tall are you:", value=165, placeholder="Your length in CM")


# # Main page components
# st.title("🥗 Sbet the nutritionist")
# response = get_gym_program(system_message, weight, tall, goal)


# st.markdown(response)


import streamlit as st
import openai
import folium
from streamlit_folium import folium_static
# st.set_config('browser.uiDirection', 'RTL')
st.set_page_config('Travale assites',page_icon='.\Vector.png',)

# إعدادات OpenAI
openai.api_key = st.secrets["OPENAI_API_KEY"]

# وظائف مساعدة
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
    print(response.choices[0].message.content)
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

# اختيار اللغة
language = st.sidebar.selectbox("اختر اللغة | Choose Language", ["English", "العربية"])
lang_code = 'en' if language == "English" else 'ar'



# واجهة المستخدم باستخدام Streamlit
st.title(translations[lang_code]['title'])

# إدخال تفضيلات المستخدم
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
            st.markdown(body=destinations,unsafe_allow_html=True
)

        # destination_list = [line.strip() for line in destinations.split('\n') if line.strip()]

        # destination = st.selectbox(translations[lang_code]['choose_destination'], destination_list)
        

            # عرض الخريطة التفاعلية
            # st.subheader(translations[lang_code]['map'])
            
            # # تعيين إحداثيات افتراضية (على سبيل المثال، وسط المدينة)
            # coordinates = [25.276987, 55.296249]  # إحداثيات افتراضية لدبي، يمكنك تغييرها حسب الحاجة

            # map_center = coordinates
            # m = folium.Map(location=map_center, zoom_start=13)
            # folium.Marker(location=map_center, popup=destination).add_to(m)
            # folium_static(m)
    else:
        st.error(translations[lang_code]['error_details'])

