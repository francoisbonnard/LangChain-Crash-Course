# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o")

# Invoke the model with a message
result = model.invoke("What is 81 divided by 9?")
print("Full result:")
print(result)
# content='81 divided by 9 is 9.'
# response_metadata={'token_usage': {'completion_tokens': 9, 
#                                      'prompt_tokens': 16, 
#                                      'total_tokens': 25,
#                                      'prompt_tokens_details': {'cached_tokens': 0},
#                                      'completion_tokens_details': {'reasoning_tokens': 0}}, 
#                                      'model_name': 'gpt-4o', 
#                                      'system_fingerprint': 'fp_2f406b9113', 
#                                      'finish_reason': 'stop', 
#                                      'logprobs': None}
#  id='run-795b9fb4-0ac9-4de6-8362-3cbec4ecd54b-0'
#  usage_metadata={'input_tokens': 16, 'output_tokens': 9, 'total_tokens': 25}
print("Content only:")
print(result.content)
# 81 divided by 9 is 9. 
print(result.name)
# None
