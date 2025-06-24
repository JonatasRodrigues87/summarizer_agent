
class TemplateAgent:
    
    def get_template_prompt(self, text):
       return f"""
            Como um assistente especializado em resumir textos de forma objetiva e clara.

            Tarefa: Resuma o seguinte texto mantendo o sentido principal e destacando as informações mais relevantes.

            Texto:
            \"\"\"
            {text}
            \"\"\"

            Resumo:
        """
      