from flask import *
import os
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from app import app



prediction_key = "696c08249fa941b5bb15aa3b3abd75a7"
publish_iteration_name = "classifyModel"
ENDPOINT = "https://uohpyday-prediction.cognitiveservices.azure.com/"
projectId = "a3f86974-e467-494a-8f7c-c988f092ae0f"
# prediction_key = "your-prediction key"
# publish_iteration_name = "classifyModel"
# ENDPOINT = "your-endpoint"
# projectId = "your project id"
