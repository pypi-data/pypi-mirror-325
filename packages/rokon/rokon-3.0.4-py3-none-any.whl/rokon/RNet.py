import tensorflow as tf
from tensorflow.keras import layers, models

def RNet1(input_shape, num_classes, activation="relu"): 
    model = models.Sequential([ 
        layers.Conv2D(16, (3,3), activation=activation, input_shape=input_shape), 
        layers.MaxPooling2D(2,2), 
        layers.Conv2D(32, (3,3), activation=activation), 
        layers.MaxPooling2D(2,2), 
        layers.Flatten(), 
        layers.Dense(128, activation=activation), 
        layers.Dense(num_classes, activation='softmax')  # Output layer stays softmax
    ]) 
    return model 

def RNet2(input_shape, num_classes, activation="relu"): 
    model = models.Sequential([ 
        layers.Conv2D(32, (3,3), activation=activation, input_shape=input_shape), 
        layers.Conv2D(32, (3,3), activation=activation), 
        layers.MaxPooling2D(2,2), 
        layers.Conv2D(64, (3,3), activation=activation), 
        layers.MaxPooling2D(2,2), 
        layers.Flatten(), 
        layers.Dense(256, activation=activation), 
        layers.Dense(num_classes, activation='softmax')
    ]) 
    return model 

def RNet3(input_shape, num_classes, activation="relu"):
    model = models.Sequential([
        layers.Conv2D(16, (3,3), activation=activation, input_shape=input_shape),
        layers.MaxPooling2D(2,2),
        layers.Conv2D(16, (3,3), activation=activation),
        layers.MaxPooling2D(2,2),
        layers.Flatten(),
        layers.Dense(64, activation=activation),
        layers.Dense(num_classes, activation='softmax')
    ])
    return model

def RNet4(input_shape, num_classes, activation="relu"):
    model = models.Sequential([
        layers.Conv2D(32, (3,3), activation=activation, input_shape=input_shape),
        layers.Conv2D(32, (1,1), activation=activation),
        layers.MaxPooling2D(2,2),
        layers.Conv2D(64, (3,3), activation=activation),
        layers.Conv2D(64, (1,1), activation=activation),
        layers.MaxPooling2D(2,2),
        layers.Flatten(),
        layers.Dense(128, activation=activation),
        layers.Dense(num_classes, activation='softmax')
    ])
    return model

def RNet5(input_shape, num_classes, activation="relu"):
    model = models.Sequential([
        layers.DepthwiseConv2D((3, 3), activation=activation, input_shape=input_shape),
        layers.Conv2D(32, (1, 1), activation=activation),
        layers.MaxPooling2D(2, 2),
        layers.DepthwiseConv2D((3, 3), activation=activation),
        layers.Conv2D(64, (1, 1), activation=activation),
        layers.MaxPooling2D(2, 2),
        layers.Flatten(),
        layers.Dense(128, activation=activation),
        layers.Dense(num_classes, activation='softmax')
    ])
    return model

def RNet6(input_shape, num_classes, activation="relu"):
    model = models.Sequential([
        layers.DepthwiseConv2D((3, 3), activation=activation, input_shape=input_shape),
        layers.Conv2D(32, (1, 1), activation=activation),
        layers.MaxPooling2D(2, 2),
        layers.DepthwiseConv2D((3, 3), activation=activation),
        layers.Flatten(),
        layers.Dense(128, activation=activation),
        layers.Dense(num_classes, activation='softmax')
    ])
    return model
def RNet7(input_shape, num_classes, activation="relu"):
    model = models.Sequential([
        layers.Conv2D(64, (3, 3), activation=activation, input_shape=input_shape),
        layers.MaxPooling2D(2, 2),
        layers.Flatten(),
        layers.Dense(128, activation=activation),
        layers.Dense(num_classes, activation='softmax')
    ])
    return model

def RNet8(input_shape, num_classes, activation="relu"):
    model = models.Sequential([
        layers.Conv2D(64, (3, 3), activation=activation, input_shape=input_shape),
        layers.MaxPooling2D(2, 2),
        layers.Flatten(),
        layers.Conv2D(64, (3,3), activation=activation),
        layers.Conv2D(64, (1,1), activation=activation),
        layers.Dense(128, activation=activation),
        layers.Dense(num_classes, activation='softmax')
    ])
    return model

# Add this at the END of the file to allow wildcard imports
__all__ = ["RNet1", "RNet2", "RNet3", "RNet4", "RNet5", "RNet6", "RNet7", "RNet8"]
