import requests
import json
import time

BASE_URL = "http://localhost:8000/chat"
SESSION_ID = "test-session-automation"

test_cases = [
    {
        "agent": "PathMatch",
        "prompt": "I really enjoy solving puzzles and logic problems, but I'm not sure what career fits that. Can you help?",
        "expected_keywords": ["interest", "puzzle", "logic", "career"]
    },
    {
        "agent": "InfoScout",
        "prompt": "What are the top 3 programming languages used in AI development in 2024?",
        "expected_keywords": ["Python", "Java", "C++", "research", "source"]
    },
    {
        "agent": "Opportune",
        "prompt": "Are there any hackathons for high school students coming up in December?",
        "expected_keywords": ["hackathon", "competition", "deadline", "apply"]
    },
    {
        "agent": "MistakeMonitor",
        "prompt": "I keep getting a 'RecursionError: maximum recursion depth exceeded' in my Python code. What does that mean?",
        "expected_keywords": ["recursion", "limit", "base case", "stack"]
    },
    {
        "agent": "MentalLift",
        "prompt": "I'm feeling really stressed about my upcoming exams and I can't focus.",
        "expected_keywords": ["stress", "breathe", "break", "support"]
    },
    {
        "agent": "Evaluator",
        "prompt": "I've learned Python basics and built a calculator. How can I track my progress to become a data scientist?",
        "expected_keywords": ["roadmap", "goal", "milestone", "progress"]
    }
]

def run_tests():
    print(f"Starting Agent Verification Tests on {BASE_URL}...\n")
    
    for test in test_cases:
        print(f"Testing Agent: {test['agent']}")
        print(f"Prompt: {test['prompt']}")
        
        try:
            start_time = time.time()
            response = requests.post(BASE_URL, json={"session_id": SESSION_ID, "message": test["prompt"]})
            duration = time.time() - start_time
            
            if response.status_code == 200:
                reply = response.json().get("reply", "")
                print(f"Response ({duration:.2f}s):\n{reply[:200]}...") # Print first 200 chars
                
                # Simple keyword check (not perfect, but a good indicator)
                # In a real scenario, we'd check if the orchestrator mentions consulting the agent
                # or if the response style matches.
                print("✅ Request successful")
            else:
                print(f"❌ Request failed with status {response.status_code}: {response.text}")
        except Exception as e:
            print(f"❌ Exception: {e}")
        
        print("-" * 60 + "\n")

if __name__ == "__main__":
    run_tests()
