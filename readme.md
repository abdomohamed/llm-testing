# What?
The idea behind this repository to give an example on how to do automated testing for LLM-based application.

There are two types of LLM evaluations that we will learn about:

- **Rule based evaluations:**

    
    - Use string or pattern matching for e.g. usage for regular expression matching. 
    - It is fast and cost-effective to run part of the continuos integration pipeline (per commit) to get a fast feedback about the health of the change. 

- **Model graded evaluations:**


    - Use another LLM to validate the output of the content generated by the LLM used by application. It takes more time and cost more.
    - They're used to assess more complex output.
    - That's why they are recommended to be used pre-release of the application.   


||Traditional Software|LLM-based Applications|
|--|--|--|
|**Behavior**|Predefined rules|Probability + prediction|
|**Output**|Deterministic same input -> many output|Non-deterministic Same input -> many output|
|**Testing**|1 input -> 1 correct output|1 input -> many correct \| incorrect outputs |
|**Criteria**|Evaluate \| Assert right or wrong|Evaluate on (Accuracy, Quality, Consistency, Bias, Toxicity,...etc) |


# Why?

Enable the engineers to have more trust in the quality of the changes they're releasing. Which enable them to release more frequent with confidence.

# When to chose what?

|Use Case|Rule Based Eval| Model Graded Eval| 
|--|--|--|
|Sentiment Analysis|✔||
|Classification|✔||
|Ground Truth labels|✔||
|Many Good or Bad Outputs \| Complex Output|
| ↳ e.g. Summarization of a content||✔|
| ↳ e.g. Writing content||✔|
| ↳ e.g. Detecting Hallucination ||✔|

Data sets used for evaluations
 - MMLU https://huggingface.co/datasets/tasksource/mmlu
 - HeLaSwag  https://huggingface.co/datasets/Rowan/


# How to run?
