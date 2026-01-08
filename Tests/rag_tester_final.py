"""
STRICT RAG AUTOMATIC TEST RUNNER
For Sigma Web Development Course (Transcript-Grounded RAG)
"""

import subprocess
import sys
import time

# Path to your main RAG entry file
RAG_SCRIPT = "process_incoming.py"
PYTHON_EXEC = sys.executable  


#creating test cases to check the rag system
TEST_CASES = [
    
    ("what is html", "definition"),
    ("define seo", "definition"),
    ("what is css", "definition"),
    ("what are semantic tags", "definition"),

    ("explain core web vitals", "mentioned_not_explained"),
    ("what is mongodb", "out_of_scope_or_mentioned"),

    ("where is paragraphs and links explained", "location"),
    ("which tag is used for images", "which"),
    ("in which video are forms explained", "location"),

    ("how does website work", "how_no_steps"),
    ("how to add image in html", "how_steps"),
    ("how to create a form in html", "how_steps"),

    ("difference between inline css and internal css", "difference"),
    ("difference between div and span", "difference"),
    ("difference between id and class", "difference"),

    ("html", "vague"),
    ("css", "vague"),
    ("forms", "vague"),

    ("teach me the whole course", "edge"),
    ("explain everything about html", "edge"),

    ("what is capital of india", "out_of_scope"),
    ("what is react native", "out_of_scope"),
    ("what is python programming", "out_of_scope"),
]

#Runner function
def run_test(question, qtype):
    print("\n" + "=" * 70)
    print(f"QUESTION: {question}")
    print(f"TYPE: {qtype}")
    print("-" * 70)

    process = subprocess.Popen(
        [PYTHON_EXEC, RAG_SCRIPT],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    stdout, stderr = process.communicate(
        input=question + "\n"
    )

    if stderr:
        print("ERROR:")
        print(stderr)
    else:
        print("RESPONSE:")
        print(stdout.strip())


if __name__ == "__main__":
    print("\n STRICT RAG AUTOMATED TEST RUNNER")
    print("=" * 70)

    for q, qt in TEST_CASES:
        run_test(q, qt)
        time.sleep(1)

    print("\n Test run completed.")
