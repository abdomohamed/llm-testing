from utils import eval_expected_words, evaluate_refusal
from common import system_message 

"""
  The below are test cases for the rule-based system. The way the tests are structured is as follows:
  
  1. The send the user question to the LLM (gpt3.5 turbo)
  2. Then the output from the system is checked to see if it contains the expected words.
  3. The test would be considered successful if the output from the system contains any of the expected words.
  4. Otherwise the test would fail.

"""

"""
Expected response: The system should generate 3 questions with this format: Question N:{delimiter} <question N>
Assert: Will check if the output contains the expected from the science subject.
"""


def test_science_quiz():
    question = "Generate a quiz about science."
    expected_subjects = ["davinci", "telescope", "physics", "curie"]
    eval_expected_words(
        system_message,
        question,
        expected_subjects)


"""
Expected response: The system should generate 3 questions with this format: Question N:{delimiter} <question N>
Assert: Will check if the output contains the expected from the  geography subject.
"""


def test_geography_quiz():
    question = "Generate a quiz about geography."
    expected_subjects = ["paris", "france", "louvre"]
    eval_expected_words(
      system_message,
      question,
      expected_subjects)


"""
Expected refusal response: "I'm sorry I do not have information about that"
"""


def test_refusal_rome():
    question = "Help me create a quiz about Rome"
    decline_response = "I'm sorry"
    evaluate_refusal(
        system_message,
        question,
        decline_response)