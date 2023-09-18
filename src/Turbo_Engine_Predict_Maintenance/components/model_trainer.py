import os
import sys
from dataclasses import dataclass

from src.Turbo_Engine_Predict_Maintenance.logger import logging
from src.Turbo_Engine_Predict_Maintenance.exception import CustomException
from src.Turbo_Engine_Predict_Maintenance.utils import save_object, evaluate_models

from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor

@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self, train_array, test_array):
        try:
            logging.info("Splitting training and test data inputs")
            X_train, y_train, X_test, y_test = (
                                                train_array[:, :-1],
                                                train_array[:, -1],
                                                test_array[:, :-1],
                                                test_array[:, -1]
                                            )

            models = {
                "Random Forest": RandomForestRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "XGBRegressor": XGBRegressor(),
                'SupportVectorMachine': SVR(C=5.0, epsilon=0.2,
                                            kernel='rbf',
                                            degree=3,
                                            gamma='auto',
                                            coef0=0.0,
                                            shrinking=True,
                                            tol=0.001,
                                            cache_size=500,
                                            verbose=False,
                                            max_iter=-1),
            }

            model_report = evaluate_models(X_train, y_train, X_test, y_test, models)

            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]

            if best_model_score < 0.6:
                print("No best model found")
            logging.info("No best model found")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted = best_model.predict(X_test)

            r2_square = r2_score(y_test, predicted)
            logging.info(f"Best found model is {best_model}, R2 Score : {r2_square}")
            print(f'Best Model Found , Model Name : {best_model} , R2 Score : {r2_square}')
            return r2_square

        except Exception as e:
            raise CustomException(e, sys)
