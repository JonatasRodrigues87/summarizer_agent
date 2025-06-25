# Agente sumarizador de artigos com LangChain, Gemini e Streamlit
Uma aplicação de Inteligência Artificial aplicada a linguagem natural, desenvolvida com fins didáticos para demonstrar o uso prático de LLMs (Large language Models) com LangChain e Streamlit.

# Objetivo
Criar um agente inteligente capaz de resumir textos e arquivos de forma clara e objetiva, utilizando um modelo da API Gemini (Google).

# Tecnologias Utilizadas

- [**Streamlit**] -> Interface web para entrada e saída de dados.
- [**LangChain**] -> Faz a orquestração do fluxo: recebe o input, monta o prompt com o contexto e o texto.
- [**Gemini API (LLM)**] -> Modelo de linguagem utilizado para receber o prompt e gerar as respostas.
- [**Python 3.11.8**] -> Linguagem principal para o desenvolvimento.

# Pré-requisito
- Conta e chave de API do Gemini  

# Instalação
Clone o repositório:
```bash
git clone https://github.com/JonatasRodrigues87/summarizer_agent.git
cd repositorio_local
```
Crie um ambiente virtual e ative:
```
python -m venv virtual_env
source virtual_env/bin/activate # ou virtual_env/Scripts/activate no Windows
```
Instale as dependências:
```
pip install -r requirements.txt
```
Configuração da API Gemini:
```
setx GOOGLE_API_KEY "SUA_API_KEY" #cria uma variável de ambiente chamada GOOGLE_API_KEY com o valor da chave passada com parâmetro
```

#Como executar:
```
streamlit run app.py
```

