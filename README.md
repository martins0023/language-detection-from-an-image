# language-detection-from-an-image
A python model used to detect type of language from an image and accepts text as input in a graphical user interface for for type of language detection with bytes offset and number.

Introduction
Every Machine Learning enthusiast has a dream of building/working on a cool project, isn’t it? Mere understandings of the theory aren’t enough, you need to work on projects, try to deploy them, and learn from them. Moreover, working on specific domains like NLP gives you wide opportunities and problem statements to explore. Through this article, I wish to introduce you to an amazing project, the Language Detection model using Natural Language Processing. This will take you through a real-world example of ML(application to say). So, let’s not wait anymore.
 

About the langueges that can be detected, which contains text details for 17 different languages.

Languages are:

* English

* Portuguese
* French

* Greek

* Dutch

* Spanish

* Japanese

* Russian

* Danish

* Italian

* Turkish

* Swedish

* Arabic

* Malayalam

* Hindi

* Tamil

* Telugu

* Hebrews

* Swahili

* France

* Korea

* Russia

* Thailand

* Japan

Using the text we have to create a model which will be able to predict the given language. This is a solution for many artificial intelligence applications and computational linguists. These kinds of prediction systems are widely used in electronic devices such as mobiles, laptops, etc for machine translation, and also on robots. It helps in tracking and identifying multilingual documents too. The domain of NLP is still a lively area of researchers.

next, Separating Independent and Dependent features
Now we can separate the dependent and independent variables, here text data is the independent variable and the language name is the dependent variable.

## Label Encoding
Our output variable, the name of languages is a categorical variable. For training the model we should have to convert it into a numerical form, so we are performing label encoding on that output variable. For this process, we are importing LabelEncoder from sklearn.

## Text Preprocessing
This is a dataset created using scraping the Wikipedia, so it contains many unwanted symbols, numbers which will affect the quality of our model. So we should perform text preprocessing techniques.

Bag of Words
As we all know that, not only the output feature but also the input feature should be of the numerical form. So we are converting text into numerical form by creating a Bag of Words model using CountVectorizer.

## Train Test Splitting
We preprocessed our input and output variable. The next step is to create the training set, for training the model and test set, for evaluating the test set. For this process, we are using a train test split.

## Model Training and Prediction
The model creation part. We are using the naive_bayes algorithm for our model creation. Then training the model using the training set.

predict the output for the test set.

## Model Evaluation
evaluate the model

The accuracy of the model is 0.97 which is very good and our model is performing well. Now let’s plot the confusion matrix using the seaborn heatmap.

Predicting with some more data
Now let’s test the model prediction using text in different languages.

## What is an Epoch?
In terms of artificial neural networks, an epoch refers to one cycle through the full training dataset. Usually, training a neural network takes more than a few epochs. In other words, if we feed a neural network the training data for more than one epoch in different patterns, we hope for a better generalization when given a new "unseen" input (test data). An epoch is often mixed up with an iteration. Iterations is the number of batches or steps through partitioned packets of the training data, needed to complete one epoch.  Heuristically, one motivation is that (especially for large but finite training sets) it gives the network a chance to see the previous data to readjust the model parameters so that the model is not biased towards the last few data points during training.  


Be aware that there is no guarantee a network will converge or "get better" by letting it learn the data for multiple epochs. It is an art in machine learning to decide the number of epochs sufficient for a network.

In parallel, when we apply this to other areas of machine learning such as reinforcement learning, we see that an agent may not take the same route to complete the same task. This is because the agent is learning which decisions to make and trying to understand the consequences of such action(s). With a neural network, the goal of the model is generally to classify or generate material which is right or wrong. Thus, an epoch for an experimental agent performing many actions for a single task may vary from an epoch for an agent trying to perform a single action for many tasks of the same nature.  In reinforcement learning terminology, this is more typically referred to as an episode.

## Some Statistics
Given the complexity and variability of data in real world problems, it may take hundreds to thousands of epochs to get some sensible accuracy on test data. Also, the term epoch varies in definition according to the problem at hand.
Example
As a specific example of an epoch in reinforcement learning, let's consider traveling from point A to B in a city. Now, we can take multiple routes to reach B and the task is to drive from A to B a hundred times. Consider an epoch to be any route taken from a set of available routes. An iteration on the other hand describes the specifics of the route like which turns, how many stops, etc.  In the reinforcement learning terminology, an iteration is often called an action.

## Images

![project_interface](https://github.com/martins0023/language-detection-from-an-image/assets/69491293/601b7683-c436-4409-96dd-266faa3b449d)


## shell 

![shell_backgroung](https://github.com/martins0023/language-detection-from-an-image/assets/69491293/82eebce9-958d-4df8-963a-f8924b5d4f58)

