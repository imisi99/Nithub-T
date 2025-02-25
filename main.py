from fastapi import FastAPI
import numpy as np
from pydantic import BaseModel
import onnxruntime as ort
import locale

try:
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
except locale.Error:
    locale.setlocale(locale.LC_ALL, "C")
app = FastAPI()


class InputText(BaseModel):
    text: str

model = "svm_model.onnx"
onnx_session = ort.InferenceSession(model)
@app.get("/")
async def landing_page():
    return {"message": "The Api is running"}

@app.get("/label")
async def label(text: InputText):
    input_x = np.array([text], dtype=str)

    output = onnx_session.run(None, {"input": input_x})
    return {"sentiment": output[0][0]}