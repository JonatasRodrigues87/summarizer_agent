from langchain_google_genai import ChatGoogleGenerativeAI
import logging
logging.basicConfig(level=logging.INFO)
from template_agent import TemplateAgent


class Agent:
    
    def __init__(self, model="gemini-2.0-flash", temperature=0.2, max_output_tokens=300):
            self.llm = ChatGoogleGenerativeAI(model= model, temperature=temperature, max_tokens=max_output_tokens)           
            self.logger = logging.getLogger(__name__)
        

    def sumarize_text(self, text):
        templateAgent = TemplateAgent()
        template = templateAgent.get_template_prompt(text)
        messages = [ ("system", template), ("human", text)]
        response = self.llm.invoke(messages)
       
        return response.content