import joblib
import pandas as pd
import gradio as gr

MODEL_PATH = "insurance_best_pipeline.joblib"
model = joblib.load(MODEL_PATH)

def predict_charges(age, sex, bmi, children, smoker, region):
    row = pd.DataFrame([{
        "age": age,
        "sex": str(sex).strip().lower(),
        "bmi": bmi,
        "children": children,
        "smoker": str(smoker).strip().lower(),
        "region": str(region).strip().lower(),
    }])

    
    def bmi_group_local(b):
        if b < 18.5: return "underweight"
        if b < 25:   return "normal"
        if b < 30:   return "overweight"
        return "obese"

    row["bmi_group"] = row["bmi"].apply(bmi_group_local)
    row["age_squared"] = row["age"] ** 2
    row["bmi_x_smoker"] = row["bmi"] * (row["smoker"] == "yes").astype(float)

    pred = model.predict(row)[0]
    return float(pred)

demo = gr.Interface(
    fn=predict_charges,
    inputs=[
        gr.Number(label="Age", value=30),
        gr.Dropdown(["female","male"], label="Sex", value="male"),
        gr.Number(label="BMI", value=26.0),
        gr.Number(label="Children", value=0),
        gr.Dropdown(["yes","no"], label="Smoker", value="no"),
        gr.Dropdown(["northeast","northwest","southeast","southwest"], label="Region", value="southeast"),
    ],
    outputs=gr.Number(label="Predicted Insurance Charges"),
    title="Medical Insurance Cost Prediction",
)

demo.launch()
