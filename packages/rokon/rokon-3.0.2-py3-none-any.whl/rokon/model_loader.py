import tensorflow as tf 
from rokon.RNet import RNet1, RNet2 
 
model_dict = { 
    "RNet1": RNet1, 
    "RNet2": RNet2, 
} 
 
def get_rokon_model(model_name, input_shape=(256, 256, 3), num_classes=10): 
    if model_name in model_dict: 
        return model_dict[model_name](input_shape=input_shape, num_classes=num_classes) 
    else: 
        raise ValueError(f"Model {model_name} not found in rokon!") 
