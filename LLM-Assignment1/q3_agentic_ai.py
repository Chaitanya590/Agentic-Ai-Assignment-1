import argparse
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

parser = argparse.ArgumentParser(description="Run a simple agentic AI workflow")
parser.add_argument("task", nargs="?", help="The task for the agent")
args = parser.parse_args()

api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("MODEL_NAME", "gpt-4o-mini")
user_task = (args.task or "").strip() or input("Enter a task for the agent: ").strip() or "Plan a small agentic AI workflow for customer support."

if not api_key or api_key == "your_openai_api_key_here":
    print("\nOpenAI API key not configured.")
    print("Please set OPENAI_API_KEY in the .env file to run the full agent flow.")
    print(f"\nFallback plan for '{user_task}':")
    print("1. Understand the goal")
    print("2. Break the task into smaller steps")
    print("3. Execute each step")
    print("4. Review and present the result")
else:
    client = OpenAI(api_key=api_key)

    try:
        response = client.responses.create(
            model=model_name,
            input=(
                "You are a helpful AI agent. "
                f"Create a step-by-step plan, execute it, and present the final output for this task: {user_task}"
            ),
        )

        print("\nAgent output:\n")
        print(response.output_text)
    except Exception as exc:
        print(f"\nLLM request failed: {exc}")
        print(f"\nFallback plan for '{user_task}':")
        print("1. Understand the goal")
        print("2. Break the task into smaller steps")
        print("3. Execute each step")
        print("4. Review and present the result")
