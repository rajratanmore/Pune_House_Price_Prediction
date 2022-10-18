import pickle
import pandas 
import json 
import config 
import numpy as np

class HousePrice():
    def __init__(self, bath, balcony):
        self.bath = bath
        self.balcony = balcony 
    

    def load_model(self):
        with open(config.model_path, 'rb') as f:
            self.model = pickle.load(f)
    
    def get_predicted_price(self):
        self.load_model()

        array = np.zeros(len(self.json_data['columns']))
        array[0]= self.bath 
        array[1]=self.balcony 

        print('test array --> \n', array)
        predicted_charges = self.model.predict([array])[0]
        reutnr np.around(predicted_charges, 2)

