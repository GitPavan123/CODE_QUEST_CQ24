
I.	PROBLEM STATEMENT
In today's digital age, the lack of internet access creates significant barriers for rural children's education. Without online resources, kids in rural areas miss out on important tools they need to learn and develop skills. This section examines how the proposed solution affects rural education in a positive way. It also looks at the difficulties in implementing effective educational strategies in rural communities. Addressing these issues is crucial to ensure that all children, regardless of where they live, have equal access to quality education. Additionally, innovative solutions leveraging offline resources can play a pivotal role in enhancing learning opportunities for rural children. Ultimately, prioritizing equitable access to education is fundamental to fostering inclusive growth and development in rural communities.

II.	SOLUTION
A.	Open source offline code generation bot:
1)	In order to resolve this particular barrier of rural children from having a knowledge regarding the current tech, it becomes mandatory to develop a chat bot that requires no active internet connection for generating appropriate coding related answers for the prompted questions. The bot is designed in such a way that it can be accessed on a custom web application as well as in the native command line interface itself. 

B.	Technological stakes:
1)	We can achieve this by making use of some existing open source LLM (Large Language Model) which has the potential to serve the purpose. An LLM in general is an AI model that is pretrained with billions or even trillions of parameters (Vocabulary or Word count). Through such training the model is capable of learning new things in less time and data. With such trained model, by utlizing the concept of transfer learning we can be able to fine tune the model to our specific needs. 
      
2)	In our case we are using llama 2, an open source LLM, trained and published by META, which has various models including llama2 7B, llama2 13B and llama2 70B (“B” refers to billion). Each model varies with the number of parameters used for training. We are using the 7B variation since it is comparitively a light weight model, which can run on a system with less hardware configuration. The model is fine tuned with appropriate word2vec embeddings in such a way that, it has build the logical insights about solving a coding related question. 

C.	Deployment and Implementation:
1)	Model loading: The model llama2-7B is initially downloaded from the official page of llama by META or can also be cloned from the official repository of hugging face API. Then a local environment is created for the model in the system itself.

2)	Deployment Framework: An appropriate framework for deploying the model as a web application is chosen (Eg: Flask, Django, Streamlit, Gradio, etc…). In this project we are using Gradio for deployment.

3)	UI design: A simple web application is created with the help of stremlit library in python. UI components such as Generate, Stop or Interrupt are added into the UI for seamless experience. 


 
