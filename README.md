# Question_Answering_Web_App

A natural language processing (NLP) question-answering (QA) system is a computer program that uses AI to understand the meaning and context of questions and provide accurate answers. The goal is to create a system that can understand the context of a question, search for relevant information, and present an accurate answer. Here, I learn how to load a pre-trained language model for question-answering tasks in our system along with dependencies like transformers and Pytorch using the NLP pipeline to configure. Then I create a web app for it using Anvil, which allows me to build a free Python-based drag-and-drop web app and deploy it over the cloud. 

![Screenshot (198)](https://github.com/CoderNitu/Question_Answering_Web_App/assets/87817227/bf3a72cd-6cfb-4718-bb90-da4bd3c99868)


## Question-Answering Model

Question-answering models can retrieve the answer to a question from a given text, which is useful for searching for an answer in a document. Some question-answering models can generate answers without context such as ChatGPT, Julias AI, etc. Context means passage(A paragraph from an article or blog)/corpus/snippets which we need to provide our model, ask questions from it, and get a result as an output, that plays an alternative to the process of Reading comprehension (the ability to read a piece of text(context) and then answer questions about it) which our model does for us.

![Screenshot (197)](https://github.com/CoderNitu/Question_Answer_Web_App/assets/87817227/9c0b57ca-5ec7-46c8-b3d5-6180387f2be1)

## Question Answering Model Variants

# 1. Extractive QA 

Extractive QA systems help us find answers to questions within our documents/context. The documents are processed by a reader model, which identifies the relevant answers. Unlike generative QA systems, extractive QA systems don't generate new text. Instead, they focus on extracting information from the documents we provide. Extractive QA systems are often more computationally efficient compared to generative QA systems. Extracting an answer is faster than generating it, and the models used in extractive QA are smaller than those used in generative QA. These systems are well-suited for handling and extracting answers from long documents, such as books or research papers. Extractive QA systems excel when providing answers that are similar to the text. They struggle with questions that require synthesizing information or generating answers not directly stated in the document text. The table format may be challenging for extractive QA, as it performs best on textual documents. The pre-trained model "RoBERTa-base-squad2" that I used can also be used for extractive, open book/domain QA tasks. The model takes a context and the question and extracts the answer from the given context. 




