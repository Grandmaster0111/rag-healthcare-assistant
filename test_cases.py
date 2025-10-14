from main import answer_question  # Make sure `answer_question` returns {'answer': ..., 'sources': [...]}

test_questions = [
    "What are the symptoms of diabetes?",
    "How is hypertension diagnosed?",
    "What causes migraine headaches?",
    "What is keratoderma with woolly hair?",
    "How is asthma treated?",
    "What precautions should a person with heart disease follow?",
    "What is the difference between Type 1 and Type 2 diabetes?",
    "Explain the mechanism of action of insulin.",
    "What does autoimmune disease mean?",
    "Why is vitamin D important for bone health?",
    "What are the side effects of metformin?",
    "When is a CT scan recommended?",
    "What should I know before a laparoscopic surgery?",
    "How can I manage my blood pressure naturally?",
    "What diet is best for someone with chronic kidney disease?",
    "Is intermittent fasting safe for diabetics?",
    "What are the long-term effects of COVID-19?",
    "Are mRNA vaccines safe?",
    "What is telemedicine, and how does it help rural healthcare?",
    "What is Wilson’s disease?",
    "How do you treat Kawasaki disease in children?",
    "What is the role of AI in medical diagnosis?",
    "What sources back up the answer about type 2 diabetes?",
    "Can you show the citations for the information about hypertension?",
]

def run_pipeline(question):
    print("=====================================")
    print(f"Question: {question}")
    try:
        result = answer_question(question)
        answer = result.get('answer', '').strip()
        print(f"Answer: {answer}\n")
        print("Sources:")
        for src in result.get("sources", []):
            print(f"- {src}")
        print("")
        return bool(answer)
    except Exception as e:
        print(f"Error processing question: {e}\n")
        return False

if __name__ == "__main__":
    passed = 0
    failed = 0

    for q in test_questions:
        if run_pipeline(q):
            print("Result: PASSED\n")
            passed += 1
        else:
            print("Result: FAILED\n")
            failed += 1

    print("=====================================")
    print(f"Total test cases: {len(test_questions)}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
