# Question_Answering_Web_App

A natural language processing (NLP) question-answering (QA) system is a computer program that uses AI to understand the meaning and context of questions and provide accurate answers. The goal is to create a system that can understand the context of a question, search for relevant information, and present an accurate answer. Here, I learned how to load a pre-trained language model for question-answering tasks in our system and dependencies like transformers and Pytorch using the NLP pipeline to configure and modify the model based on our requirements. Then I create a web app for it using Anvil, which allows me to build a free Python-based drag-and-drop web app and deploy it over the cloud. 


![Screenshot (199)](https://github.com/CoderNitu/Question_Answering_Web_App/assets/87817227/35e66140-2343-4460-be25-0907b033f5cd)

This is the public link to my web app: https://musty-frightened-shake.anvil.app. To use this app, you have to make a clone of my app on the Anvil website in your system, as the uplink key generated, which helps us to integrate or hook the Anvil server to our notebook, will be different for different people's systems. For the cloning procedure check: https://anvil.works/docs/editor/cloning


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

This model generates free text directly based on the context. Generating text is the task of producing new text. These models can, for example, fill in incomplete text or paraphrase(rewording or expressing the meaning of something written or spoken using different words, especially to achieve greater clarity). A popular variant of Text Generation models, also known as the Casual Language model(CLM) predicts the next word given a bunch of words. Word by word a longer text is formed that results in for example: Giving an incomplete sentence, completing it, continuing a story given the first sentences, and providing a code description, to generate the code.

![Screenshot (200)](https://github.com/CoderNitu/Question_Answering_Web_App/assets/87817227/af6ca4b0-aa60-4c3e-9b03-5362f391a0fc)

# (b) Closed Generative QA

In this case, no context is provided. A model completely generates the answer.


We can also differentiate QA models depending on whether they are open-domain or closed-domain. Open-domain models are not restricted to a specific domain, while closed-domain models are restricted to a specific domain (e.g. legal, medical documents). The main difference between a closed-domain and an open-domain QA system is the dataset on which it was trained.

# Transformer Models: The Future of Natural Language Processing

Transformer models are a type of deep learning model that is used for natural language processing (NLP) tasks. They are able to learn long-range dependencies(connections and relationships between words in a sentence), which makes them very powerful for tasks such as machine translation, text summarization, and question answering. Transformer models work by first encoding the input sentence into a sequence of vectors. This encoding is done using a self-attention mechanism, which allows the model to learn the relationships between the words in the sentence. Once the input sentence has been encoded, the model decodes it into a sequence of output tokens. This decoding is also done using a self-attention mechanism. The attention mechanism is what allows transformer models to learn long-range dependencies between words in a sentence. The attention mechanism works by focusing on the most relevant words in the input sentence when decoding the output tokens. Transformer models are very powerful, but they can be computationally expensive to train. However, they are constantly being improved, and they are becoming more efficient and powerful all the time.

![12](https://github.com/CoderNitu/Question_Answering_Web_App/assets/87817227/0efb847d-bce1-4bfc-bdf0-57142ad3e437)

![seq2seq](https://github.com/CoderNitu/Question_Answering_Web_App/assets/87817227/f9d33a0d-9522-4f2f-b0f9-3f7a9f5d3faf)

# Different Transformer Models 

![Screenshot (202)](https://github.com/CoderNitu/Question_Answering_Web_App/assets/87817227/b6da09eb-610c-42f2-aac3-65643ef6d77f)

All the Transformer models mentioned above (GPT, BERT, BART, T5, etc.) have been trained as language models. This means they have been trained on large amounts of raw text in a self-supervised fashion. Self-supervised learning is a type of training in which the objective is automatically computed from the inputs of the model. That means that humans do not need to label the data! This type of model develops a statistical understanding of the language it has been trained on, but it’s not very useful for specific practical tasks. Because of this, the general pre-trained model then goes through a process called transfer learning. During this process, the model is fine-tuned in a supervised way — that is, using human-annotated labels — on a given task.

# Pre-Trained Model Used

The pre-trained model I used is the "Roberta-base" model, which shares the same architecture as the BERT model with some modifications in hyperparameters and tiny embedding tweaks. It is trained using the SQuAD2.0 dataset and used for Extraction QA tasks. You can look further at the model on the Huggingface website: https://huggingface.co/deepset/roberta-base-squad2.

## Tensorflow vs Keras vs PyTorch:

These are the three most famous deep-learning Python framework use for learning, developing, and training neural networks. All of them have their own pros and cons.

# 1. Tensorflow 
TensorFlow is an end-to-end open-source deep learning framework developed by Google and released in 2015. It is known for documentation and training support, scalable production and deployment options, multiple abstraction levels, and support for different platforms, such as Android. TensorFlow is a symbolic math library used for neural networks and is best suited for dataflow programming across a range of tasks. It offers multiple abstraction levels for building and training models.

# 2. Keras
 
Keras is an effective high-level neural network Application Programming Interface (API) written in Python. This open-source neural network library is designed to provide fast experimentation with deep neural networks, and it can run on top of CNTK, TensorFlow, and Theano. Keras was adopted and integrated into TensorFlow in mid-2017. Users can access it via the tf.keras module. However, the Keras Library can still operate separately and independently.

# 3. PyTorch

PyTorch is a relatively new deep-learning framework based on Torch. Developed by Facebook’s AI research group and open-sourced on GitHub in 2017, it’s used for natural language processing applications. PyTorch has a reputation for simplicity, ease of use, flexibility, efficient memory usage, and dynamic computational graphs. It also feels native, making coding more manageable and increasing processing speed.









