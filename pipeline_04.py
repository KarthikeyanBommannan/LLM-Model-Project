import os
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

template ="Answer the question: {question}"
prompt = PromptTemplate(template= template, input_variables = ["question"])

llm_chain = LLMChain(prompt = prompt, llm = HuggingFaceHub(model_kwargs={"temperature":0,"max_length":64}))

question = input()
print(llm_chain.run(question))