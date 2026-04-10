import gradio as gr
import joblib
import pandas as pd

model = joblib.load("model.pkl")

def predict(age, duration, city_tier):
    data = pd.DataFrame({
        "Age": [age],
        "DurationOfPitch": [duration],
        "CityTier": [city_tier]
    })

    prediction = model.predict(data)[0]

    return "Will Purchase" if prediction == 1 else "Will Not Purchase"

interface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Age"),
        gr.Number(label="Duration"),
        gr.Number(label="City Tier")
    ],
    outputs="text"
)

interface.launch()
