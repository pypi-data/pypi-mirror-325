from . import BaseAgent
import os
from pathlib import Path

class FrontendAgent(BaseAgent):
    def __init__(self):
        super().__init__(os.getenv("OLLAMA_MODEL_STARCODER"))
        self.template_dir = Path(__file__).parent.parent / "templates/react"
        
    def create_component(self, task: str) -> dict:
        prompt = f"""EXACT REACT/TYPESCRIPT/Tailwind CODE FOR:
        {task}
        
        REQUIREMENTS:
        1. Use functional components
        2. Add PropTypes/TypeScript interfaces
        3. Implement proper error handling
        4. Include full Tailwind styling
        5. Add detailed JSDoc comments
        """
        return self.generate_code(prompt)