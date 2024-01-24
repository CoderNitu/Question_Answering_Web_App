# Question_Answering_Web_App

A natural language processing (NLP) question-answering (QA) system is a computer program that uses AI to understand the meaning and context of questions and provide accurate answers. The goal is to create a system that can understand the context of a question, search for relevant information, and present an accurate answer. Here, I learn how to load a pre-trained language model for question-answering tasks in our system along with dependencies like transformers and Pytorch using the NLP pipeline to configure. Then I create a web app for it using Anvil, which allows me to build a free Python-based drag-and-drop web app and deploy it over the cloud. 


![Screenshot (199)](https://github.com/CoderNitu/Question_Answering_Web_App/assets/87817227/35e66140-2343-4460-be25-0907b033f5cd)


## Question-Answering Model

Question-answering models can retrieve the answer to a question from a given text, which is useful for searching for an answer in a document. Some question-answering models can generate answers without context such as ChatGPT, Julias AI, etc. Context means passage(A paragraph from an article or blog)/corpus/snippets which we need to provide our model, ask questions from it, and get a result as an output, that plays an alternative to the process of Reading comprehension (the ability to read a piece of text(context) and then answer questions about it) which our model does for us.

![Screenshot (197)](https://github.com/CoderNitu/Question_Answer_Web_App/assets/87817227/9c0b57ca-5ec7-46c8-b3d5-6180387f2be1)

## Question Answering Model Variants

Question answering (QA) in natural language processing (NLP) can be approached using various techniques, and different types of language models can be employed for this task. Two common approaches for QA involve extractive and generative methods

# 1. Extractive QA 

Extractive QA systems help us find answers to questions within our documents/context. The documents are processed by a reader model, which identifies the relevant answers. Unlike generative QA systems, extractive QA systems don't generate new text. Instead, they focus on extracting information from the documents we provide. Extractive QA systems are often more computationally efficient compared to generative QA systems. Extracting an answer is faster than generating it, and the models used in extractive QA are smaller than those used in generative QA. These systems are well-suited for handling and extracting answers from long documents, such as books or research papers. Extractive QA systems excel when providing answers that are similar to the text. They struggle with questions that require synthesizing information or generating answers not directly stated in the document text. The table format may be challenging for extractive QA, as it performs best on textual documents. Extractive QA often utilizes pre-trained language models such as BERT (Bidirectional Encoder Representations from Transformers), RoBERTa (Robustly optimized BERT approach), or other transformer-based models. These models are fine-tuned for extractive QA tasks. The pre-trained model "RoBERTa-base-squad2" that I used can also be used for extractive, open book/domain QA tasks. The model takes a context and the question and extracts the answer from the given context. 


![question_answering_11 (1)](https://github.com/CoderNitu/Question_Answering_Web_App/assets/87817227/1d0bf9f4-ad12-4ab5-b943-0494f0c2f3a6)

# 2. Generative QA

Generative QA uses large language models to generate human-like responses to user queries in question-answering apps. Instead of simply extracting answers from existing documents, generative systems create a new text based on instructions provided in the prompt. A prompt is a specific instruction given to the model in natural language to help it understand the task and generate an appropriate response. To build a basic generative QA system, we need a large language model (LLM), like GPT(Generative Pre-trained Transformer), and a simple prompt, such as a user query. LLMs are trained to predict the next word in a sequence and generate answers token by token. Based on the prompt, the model generates an answer.

![2a5a22a-Generative_QA](https://github.com/CoderNitu/Question_Answering_Web_App/assets/87817227/2b444ea3-87b8-4a4d-924a-336cfff420d1)

# (a) Open Generative QA

The model generates free text directly based on the context. Generating text is the task of producing new text. These models can, for example, fill in incomplete text or paraphrase(rewarding or expressing the meaning of something written or spoken using different words.).

![Screenshot (200)](https://github.com/CoderNitu/Question_Answering_Web_App/assets/87817227/992165d8-fb5a-49ed-bf24-0cc0fd0fb20e)




