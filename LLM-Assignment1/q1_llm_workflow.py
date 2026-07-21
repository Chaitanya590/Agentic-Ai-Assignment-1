import argparse
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

parser = argparse.ArgumentParser(description="Generate a response from an LLM")
parser.add_argument("prompt", nargs="?", help="The prompt to send to the model")
args = parser.parse_args()

api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("MODEL_NAME", "gpt-4o-mini")
prompt = (args.prompt or "").strip() or input("Enter your prompt: ").strip() or "Explain the basic workflow of an LLM application in 3 bullet points."

if not api_key or api_key == "your_openai_api_key_here":
    print("\nOpenAI API key not configured.")
    print("Please set OPENAI_API_KEY in the .env file to run the LLM version.")
    print(f"\nFallback response to your prompt:\n{prompt}")
else:
    client = OpenAI(api_key=api_key)

    try:
        response = client.responses.create(
            model=model_name,
            input=prompt,
        )
        print("\nLLM response:\n")
        print(response.output_text)
    except Exception as exc:
        print(f"\nLLM request failed: {exc}")
        print(f"\nFallback response to your prompt:\n{prompt}")
