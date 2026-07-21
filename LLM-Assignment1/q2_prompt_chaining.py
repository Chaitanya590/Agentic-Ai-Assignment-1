import argparse
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

parser = argparse.ArgumentParser(description="Run a prompt chaining workflow")
parser.add_argument("topic", nargs="?", help="The topic to summarize and question")
args = parser.parse_args()

api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("MODEL_NAME", "gpt-4o-mini")
user_query = (args.topic or "").strip() or input("Enter a topic: ").strip() or "Summarize the benefits of prompt chaining for LLM applications."

if not api_key or api_key == "your_openai_api_key_here":
    print("\nOpenAI API key not configured.")
    print("Please set OPENAI_API_KEY in the .env file to run the full LLM workflow.")
    print(f"\nFallback workflow for '{user_query}':")
    print("1. Summary: Prompt chaining helps break a task into smaller steps.")
    print("2. Key points: It improves clarity, control, and reliability.")
    print("3. Questions: What problem does the workflow solve? How does it improve quality? Why is it useful?")
else:
    client = OpenAI(api_key=api_key)

    try:
        step1 = client.responses.create(
            model=model_name,
            input=f"Create a short summary of this topic: {user_query}",
        )

        step2 = client.responses.create(
            model=model_name,
            input=f"Extract 3 key points from this summary:\n{step1.output_text}",
        )

        step3 = client.responses.create(
            model=model_name,
            input=f"Generate 3 useful questions based on this topic:\n{user_query}",
        )

        print("\nSummary:")
        print(step1.output_text)
        print("\nKey points:")
        print(step2.output_text)
        print("\nQuestions:")
        print(step3.output_text)
    except Exception as exc:
        print(f"\nLLM request failed: {exc}")
        print(f"\nFallback workflow for '{user_query}':")
        print("1. Summary: Prompt chaining helps break a task into smaller steps.")
        print("2. Key points: It improves clarity, control, and reliability.")
        print("3. Questions: What problem does the workflow solve? How does it improve quality? Why is it useful?")
