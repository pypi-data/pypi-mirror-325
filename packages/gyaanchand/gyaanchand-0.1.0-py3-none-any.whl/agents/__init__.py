import ollama  
import os  
from typing import Dict, Any  
import logging  
from ..utils.logger import setup_logger  

setup_logger()  

class BaseAgent:  
    def __init__(self, model: str):  
        self.model = model  
        self.base_prompt = """  
        You are GyaanChand - a professional code generation AI.  
        Follow these rules:  
        1. Generate production-ready code  
        2. Include error handling  
        3. Use industry best practices  
        4. Add detailed comments  
        """  

    def generate_code(self, prompt: str) -> Dict[str, Any]:  
        try:  
            response = ollama.generate(  
                model=self.model,  
                prompt=f"{self.base_prompt}\nUser Task: {prompt}",  
                options={'num_ctx': 4096, 'temperature': 0}  
            )  
            return {  
                'code': response['response'],  
                'metadata': {  
                    'model': self.model,  
                    'tokens_used': response.get('eval_count', 0)  
                }  
            }  
        except Exception as e:  
            logging.error(f"Generation failed: {str(e)}")  
            raise  