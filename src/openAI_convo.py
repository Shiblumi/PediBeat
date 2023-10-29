import openai

class OpenAIConvo:
    def __init__(self, user_content='', system_content='', assistant_content=''):
        self.user_content = user_content
        self.system_content = system_content
        self.assistant_content = assistant_content
        
    def run_convo(self):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.system_content},
                {"role": "user", "content": self.user_content},
                {"role": "assistant", "content": self.assistant_content}
            ]
        )
        self.assistant_content = response['choices'][0]['message']['content']
        return self.assistant_content
    
    def add_user_content(self, user_content):
        self.user_content = user_content
        
    def add_system_content(self, system_content):
        self.system_content = system_content
        
    def add_assistant_content(self, assistant_content):
        self.assistant_content = assistant_content