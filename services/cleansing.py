import pandas as pd
from collections import Counter
from libs.nlp import preprocessing
from services import AppServiceProject

class CleansingServices(AppServiceProject):
    async def split_word(self, text):
        try:
            preprocess = preprocessing(text)
            
            data = {
                "data": preprocess
            }
            
            return self.success_response(data)
        except Exception as e:
            return self.error_response(e)