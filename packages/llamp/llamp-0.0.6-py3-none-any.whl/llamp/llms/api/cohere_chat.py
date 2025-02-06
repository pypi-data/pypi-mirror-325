import time
import os
import cohere

from llamp.llms.base_llm_system import BaseLLMSystem

# from tenacity import (
#     retry,
#     stop_after_attempt, # type: ignore
#     wait_random_exponential, # type: ignore
# )

class CohereChat(BaseLLMSystem):
    def __init__(self, system_name="CohereChat",save_path="game_logs", temperature = 0.0, model="command", stop_sequences=None):
        
        super().__init__(system_name, save_path, temperature=temperature)        
        self.base_prompt = [{
            "role" : "system",
            "content" : "You will interact with the environment to solve the given task. Think step by step "
        }]
        self.reset()
        API_KEY = os.environ['COHERE_API_KEY']
        self.co = cohere.Client(API_KEY)

        self.temperature = temperature
        self.model = model
        self.stop_sequences=stop_sequences

    
    def get_current_prompt_cohere(self):
        """Returns the current prompt and last message for Cohere's API"""
        out_list = []
        for messages in self.current_prompt:
            temp_dict = {}
            if messages["role"] == "assistant":
                cohere_role = "CHATBOT" 
            elif messages["role"] == "user":
                cohere_role = "USER"
            elif messages["role"] == "system":
                cohere_role = "SYSTEM"
            else:
                cohere_role = "user"
            temp_dict["role"] = cohere_role
            temp_dict["message"] = messages["content"]
            out_list.append(temp_dict)

        return out_list

    # @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6),reraise=True)
    def call_model(self, temperature=None):
        """Call OpenAI API"""

        current_prompt = self.get_current_prompt_cohere()

        message = current_prompt[-1]["message"]
        if len(current_prompt)>1:
            chat_history = current_prompt[:-1]

        response = self.co.chat(
            message = message,
            model=self.model,
            chat_history=chat_history,
            temperature=self.temperature,
            stop_sequences=self.stop_sequences
        )

        answer = response.text
        return answer


if __name__=="__main__":
    print("Nothing to run here.")



 