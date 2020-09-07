# CIFAR-10-Dataset-using-Flask-app
Implemented CIFAR-10 and achieved an accuracy of 90.7% on test scores and implemented a flask app to show the predictions.

CIFAR-10  is an established computer-vision dataset used for object recognition. It is a subset of the 80 million tiny images dataset and consists of 60,000 32x32 color images containing one of 10 object classes, with 6000 images per class. 

<h3>CONCEPTS INVOLVED:</h3>  


<b>DATA AUGMENTATION</b>: Data augmentation is a strategy that enables practitioners to significantly increase the diversity of data available for training models, without collecting new data. Data augmentation techniques such as cropping, padding, and horizontal flipping are commonly used to train large neural networks. 


<b>NEURAL NETWORKS</b>: Neural networks generally do not need to be programmed with specific rules that define what to expect from the input. The neural net learning algorithm instead learns from processing many labeled examples (i.e. data with "answers") that are supplied during training. Using this answer key to learn what characteristics of the input are needed to construct the correct output. Once enough examples have been processed, the neural network can begin to process new, unseen inputs and successfully return accurate results. The more examples and variety of inputs the network sees, the more accurate the results typically are provided as output because the it learns with experience. 


 <b>CONVOLUTIONS IN NEURAL NETWORK</b>: Convolution layers are the major building blocks used in convolutional neural networks. A convolution is the simple application of a filter to an input that results in an activation. Repeated application of the same filter to an input results in a map of activations called a feature map, indicating the locations and strength of a detected feature in an input, such as an image. The innovation of convolutional neural networks is the ability to automatically learn many features in parallel specific to a training dataset under the constraints of a specific predictive modeling problem, such as image classification. The result is highly specific features that can be detected anywhere on input images. 
 
 
<b>MAX POOLING</b>: A pooling layer is another building block of a CNN. Its function is to progressively reduce the spatial size of the representation to reduce the number of parameters and computation in the network. Pooling layer operates on each feature map independently. The most common approach used in pooling is max pooling. 


<b>BATCH-NORMALIZATION</b>: Batch normalization (also known as batch norm) is a technique for improving the speed, performance, and stability of artificial neural networks. It is used to normalize the input layer by re-centering and re-scaling. 


<b>DROPOUTS</b>: Dropout is a technique where randomly selected neurons are ignored during training. They are “dropped-out” randomly. This means that their contribution to the activation of downstream neurons is temporally removed on the forward pass and any weight updates are not applied to the neuron on the backward pass. 





<h3> DEEP LEARNING ARCHITECTURE </h3>

![Screenshot (344)](https://user-images.githubusercontent.com/45651397/92354104-4ac56a80-f0ff-11ea-8c3d-d5f574d4f47f.png)
