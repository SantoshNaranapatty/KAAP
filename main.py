from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import argparse

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--task", default="return a list of number")
parser.add_argument("--language", default="javascript")
args = parser.parse_args()
#dont forget to secure this key

llm = OpenAI()

code_prompt = PromptTemplate(
    template="Write a very short {language} function that will {task}",
    input_variables=["language", "task"]
)

code_prompt_2 = PromptTemplate(
    template="Please check if this {language} snippet is correct: {code}",
    input_variables=["language", "code"]
)

code_chain = LLMChain(
    llm = llm,
    prompt = code_prompt,
    output_key = 'code'
)

code_chain_2 = LLMChain(
    llm = llm,
    prompt = code_prompt_2,
    output_key = "test"
)

result = code_chain({"language":args.language,
"task":args.task})

print(result["code"])