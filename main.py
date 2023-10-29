import sys
import openai
sys.path.append('src/')
from data_stream import DataStream
from openAI_convo import OpenAIConvo
from speech_recognition import SpeechRecognition


if __name__ == '__main__':
    # SpeechRecognition Test
    sr = SpeechRecognition("C:/Users/wilso/OneDrive/Documents/Code/CalHacks/data/TQBFJOTLD.wav")
    speech_to_text = sr.run()
    print(speech_to_text)
    
    # DataStream Test
    d_stream = DataStream(5, 10, 15)
    d_stream.initialize_csv('col1', 'col2', 'col3')
    for i in range(50):
        d_stream.feed_buffers(i, i, i)
    # d_stream.display()
    d_stream.flush_buffers_to_csv()
    
    
    # print(d_stream.get_last_n_from_csv(5))
    
    # # OpenAIConvo Test
    # # Set up OpenAI API key
    # API_KEY = open("C:/Users/wilso/OneDrive/Documents/Code/keys/key_openAI_cal-hacks", "r").read()
    # openai.api_key = API_KEY
    
    # chatGPT = OpenAIConvo()
    # chatGPT.add_user_content("What is the largest planet in our solar system?")
    # response = chatGPT.run_convo()
    # print(response)
    
    # chatGPT.add_assistant_content(response)
    # chatGPT.add_user_content("In one sentence, what is the second largest?")
    # response = chatGPT.run_convo()
    # print(response)o