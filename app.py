from flask import Flask,request,render_template #for initializing flask & render the html templates
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline

application=Flask(__name__)

app=application

@app.route('/')
def home_page():
    return render_template('index.html') 

@app.route("/predict", methods = ["GET", "POST"])
def predict_datapoint(): 
    if request.method == "GET":
        return render_template("form.html") 
    
    else:

        data = CustomData(
            engine_no = request.form.get("engine_no"),
            cycle_no = request.form.get("cycle_no"),
            lpc_outlet_temperature = request.form.get("lpc_outlet_temperature"),
            hpc_outlet_temperature = request.form.get("hpc_outlet_temperature"),
            lpt_outlet_temperature = request.form.get("lpt_outlet_temperature"),
            hpc_outlet_pressure = request.form.get("hpc_outlet_pressure"),
            physical_fan_speed = request.form.get("physical_fan_speed"),
            physical_core_speed = request.form.get("physical_core_speed"),
            hpc_outlet_static_pressure = request.form.get("hpc_outlet_static_pressure"),
            fuel_flow_ratio = request.form.get("fuel_flow_ratio"),
            fan_speed = request.form.get("fan_speed"),
            bypass_ratio = request.form.get("bypass_ratio"),
            bleed_enthalpy = request.form.get("bleed_enthalpy"),
            high_pressure_cool_air_flow = request.form.get("high_pressure_cool_air_flow"),
            low_pressure_cool_air_flow  = request.form.get("low_pressure_cool_air_flow")       
        )
        
        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_new_data) #to predict the final output
        
        #To change this
        # if pred == 0: #For edible
        #     results = "Edible"
        #     return render_template("edible.html", final_result = results) #to render edible template, if result is edible

#to initalize the app when run
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)