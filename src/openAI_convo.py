import openai

API_KEY = open("C:/Users/wilso/OneDrive/Documents/Code/keys/key_openAI_cal-hacks", "r").read()
openai.api_key = API_KEY

system_content = (f"You are an assistant for a doctor, analyzing a patient's vitals. I need you \
    to give me a diagnosis of the patient's condition based on this data. The data is in the form \
    of a csv file.")
user_content = "What is the third planet from the sun?"
assistant_content = ''


# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": system_content},
#         {"role": "user", "content": "PUT YOUR STR VAR HERE"},
#         {"role": "assistant", "content": "PUT YOUR STR VAR HERE"},
#     ]
# )

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": user_content},
    ]
)

response1 = response['choices'][0]['message']['content']
print(response1)

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Now, what's the planet next to it?"},
        {"role": "assistant", "content": response1},
    ]
)

response2 = response['choices'][0]['message']['content']
print(response2)
