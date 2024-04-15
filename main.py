import instructor

from openai import OpenAI
from pydantic import BaseModel


class Dates(BaseModel):
    passed_date: str
    effective_date: str


client = instructor.from_openai(
    OpenAI(
        base_url = "http://localhost:11434/v1",
        api_key = "ollama", # required, but unused
    ),
    mode = instructor.Mode.JSON,
)

response = client.chat.completions.create(
  model = "tinyllama:chat",
  messages = [
      {
          "role": "user", 
          "content": "Bank Standard Resolution passed on 20/12/24 effective 21/12/24. Extract passed date and effective date"
      }],
  response_model = Dates,
)

print(response) 

# Findings
# 1) instructor only works well for specific models, does not work well for other models where the prompts used in instructor are not engineered to fit them
# 2) instructor performs poorly for tinyllama:chat but works reasonably well for llama2:chat.