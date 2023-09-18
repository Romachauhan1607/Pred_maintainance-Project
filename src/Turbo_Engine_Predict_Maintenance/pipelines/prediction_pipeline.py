import sys
import os
import pandas as pd
from src.Turbo_Engine_Predict_Maintenance.logger import logging
from src.Turbo_Engine_Predict_Maintenance.exception import CustomException
from src.Turbo_Engine_Predict_Maintenance.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            print("Before Loading")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds

        except Exception as e:
            raise CustomException(e, sys)
					

class CustomData:
    def __init__(self,
                 engine_number: float,
                 time_cycles: float,
                 sensor_measurement2: float,
                 sensor_measurement3: float,
                 sensor_measurement4: float,
                 sensor_measurement7: float,
                 sensor_measurement8: float,
                 sensor_measurement9: float, 
                 sensor_measurement11: float,
                 sensor_measurement12: float,
                 sensor_measurement13: float,
                 sensor_measurement15: float,
                 sensor_measurement17: float,
                 sensor_measurement20: float,
                 sensor_measurement21: float
                 ):
        
        self.engine_number = engine_number
        self.time_cycles = time_cycles
        self.sensor_measurement2 = sensor_measurement2
        self.sensor_measurement3 = sensor_measurement3
        self.sensor_measurement4 = sensor_measurement4
        self.sensor_measurement7 = sensor_measurement7
        self.sensor_measurement8 = sensor_measurement8
        self.sensor_measurement9 = sensor_measurement9
        self.sensor_measurement11 = sensor_measurement11
        self.sensor_measurement12 = sensor_measurement12
        self.sensor_measurement13 = sensor_measurement13
        self.sensor_measurement15 = sensor_measurement15
        self.sensor_measurement17 = sensor_measurement17
        self.sensor_measurement20 = sensor_measurement20
        self.sensor_measurement21 = sensor_measurement21
    

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                     "engine_number" : [self.engine_number],
                     "time_cycles" : [self.time_cycles],
                     "sensor_measurement2"  : [self.sensor_measurement2], 
                     "sensor_measurement3"  : [self.sensor_measurement3], 
                     "sensor_measurement4"  : [self.sensor_measurement4], 
                     "sensor_measurement7"  : [self.sensor_measurement7], 
                     "sensor_measurement8"  : [self.sensor_measurement8], 
                     "sensor_measurement9"  : [self.sensor_measurement9], 
                     "sensor_measurement11" : [self.sensor_measurement11], 
                     "sensor_measurement12" : [self.sensor_measurement12], 
                     "sensor_measurement13" : [self.sensor_measurement13], 
                     "sensor_measurement15" : [self.sensor_measurement15], 
                     "sensor_measurement17" : [self.sensor_measurement17], 
                     "sensor_measurement20" : [self.sensor_measurement20], 
                     "sensor_measurement21" : [self.sensor_measurement21], 

                    }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)