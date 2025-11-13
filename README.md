# Financial Chatbot – Analisador de Balanços Financeiros

**Status:** Projeto em desenvolvimento – atualmente implementando o módulo de análise de balanços e o sistema de chat.

---

## Visão Geral

Este projeto consiste em um chatbot web desenvolvido com Flask e integrado à API Gemini, capaz de ler e interpretar balanços financeiros em PDF enviados pelo usuário. O objetivo é permitir que o usuário converse com seus próprios documentos financeiros, obtendo respostas claras e contextuais sobre o conteúdo.

O objetivo futuro é integrar o sistema em uma plataforma web, onde o usuário poderá:
- Tomar decisões de investimento de forma mais informada;
- Comparar indicadores entre empresas e setores;
- Receber resumos automáticos dos principais dados financeiros.

---

## Funcionalidades (planejadas e em desenvolvimento)

- Upload de arquivos PDF contendo balanços financeiros;
- Extração automática do texto contido nos PDFs (via PyPDF2);
- Envio de perguntas relacionadas ao documento;
- Geração de respostas contextuais utilizando Google Gemini;
- Armazenamento do histórico de conversas durante a sessão.

---

## Tecnologias e Conceitos Envolvidos

- Python 3.10+
- Flask – para o servidor web e rotas HTTP
- PyPDF2 – extração de texto de arquivos PDF
- Google Generative AI (Gemini API) – processamento e análise semântica do conteúdo
- HTML/CSS/JS – interface simples de interação

---

## Aprendizados até o momento

- Estruturação de sistemas em módulos independentes;  
- Criação de lógica condicional para análise financeira;  
- Entendimento de indicadores contábeis;  
- Planejamento de integração com IA e web;

---

## Roadmap

- Criar base de dados de indicadores setoriais;  
- Integrar API de cotações e dados de mercado;  
- Integrar a capacidade de comparação de empresas por setor e avaliar preços dos ativos e definir se a ação está com preço baixo ou alto comparado ao segmento.
- Projeção de valorização da ação com base em análises de mercado feitas pela IA.
- Dashboard do usuário com valor investido, dividendos recebidos, valorização da carteira, etc

---

## Autor
**Elton Lopes**  
Estudante autodidata e entusiasta em automação, IA e fintechs
[LinkedIn](https://www.linkedin.com/in/elton-lopes-832a75110/)

[Outros projetos no GitHub](https://github.com/Japa-arch?tab=repositories)

