# deep-learning-chatbot
A deep learning based question answer chatbot which works on the basis of intent recognition.

⚪   how'd you exists?\
🟣   You created me?

### **Code and Resources used**

**Language**-python 3.9

**dataset**-[intent recoginition dataset kaggle](https://www.kaggle.com/datasets/elvinagammed/chatbots-intent-recognition-dataset)

**Pakages Used**- numpy, keras, nltk, pickle, pandas, sklearn

**model Used** - neural network 

### **Procedural steps**

**step1 data extraction** - first of all download the dataset from given link in code and resources section. create the word embedding of the given data of type bag of words so that it can be passed to the neural network.

**step2 (model creation & training)** - create a model creation function on the basis of number of layers and activation function. instead of making a direct model we created a function so that we can use grid search cv to optimize the model.

**step4 (create user interface for input)**-create a form type interface using html and css to take the input image file from the user.

**step5 (deploy with flask)**-connect the model to make predictions on user input data using the model.for the we need to connect our model using the flask framework.which in contained by the 'app.py'file in repositary.

