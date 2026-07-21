import argparse
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

parser = argparse.ArgumentParser(description="Run a basic RAG-based QA workflow")
parser.add_argument("question", nargs="?", help="The question to answer from the document")
args = parser.parse_args()

api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("MODEL_NAME", "gpt-4o-mini")

base_dir = Path(__file__).resolve().parent
context_path = base_dir / "sample_document.txt"

with context_path.open("r", encoding="utf-8") as f:
    context = f.read()

question = (args.question or "").strip() or input("Enter your question: ").strip() or "What are the main customer concerns mentioned in the document?"

if not api_key or api_key == "your_openai_api_key_here":
    print("\nOpenAI API key not configured.")
    print("Please set OPENAI_API_KEY in the .env file to run the full RAG workflow.")
    print(f"\nFallback answer for '{question}':")
    print("The document mentions login troubleshooting, billing questions, and delayed onboarding emails as common support issues.")
else:
    client = OpenAI(api_key=api_key)

    try:
        response = client.responses.create(
            model=model_name,
            input=(
                "Use the provided context to answer the question.\n\n"
                f"Context:\n{context}\n\nQuestion:\n{question}"
            ),
        )

        print("\nRAG answer:\n")
        print(response.output_text)
    except Exception as exc:
        print(f"\nLLM request failed: {exc}")
        print(f"\nFallback answer for '{question}':")
        print("The document mentions login troubleshooting, billing questions, and delayed onboarding emails as common support issues.")
