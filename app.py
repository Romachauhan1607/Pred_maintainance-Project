from flask import Flask, request, render_template
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline

application = Flask(__name__)
app = application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict_datapoints():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        data = CustomData(
            Engine_no = request.form.get("Engine_no"),
            Cycle_no = request.form.get("Cycle_no"),
            LPC_outlet_temperature = request.form.get("LPC_outlet_temperature"),
            HPC_outlet_temperature = request.form.get("HPC_outlet_temperature"),
            LPT_outlet_temperature = request.form.get("LPT_outlet_temperature"),
            HPT_outlet_pressure = request.form.get("HPT_outlet_pressure"),
            Physical_fan_speed = request.form.get("Physical_fan_speed"),
            Physical_core_speed = request.form.get("Physical_core_speed"),
            HPC_outlet_static_pressure = request.form.get("HPC_outlet_static_pressure"),
            Fuel_flow_ratio = request.form.get("Fuel_flow_ratio"),
            Fan_speed = request.form.get("Fan_speed"),
            Bypass_ratio = request.form.get("Bypass_ratio"),
            Bleed_enthalpy = request.form.get("Bleed_enthalpy"),
            High_pressure_cool_air_flow = request.form.get("High_pressure_cool_air_flow"),
            Low_pressure_cool_air_flow  = request.form.get("Low_pressure_cool_air_flow")       
            )
        
        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_new_data)

        results=round(pred[0])

        return render_template('results.html',final_result=results)


if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True,port=5001)