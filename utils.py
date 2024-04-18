from langchain_openai import AzureChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate
import os


os.environ["AZURE_OPENAI_API_KEY"] = "8ed4711d892f43ea9e5888928d5dbd20"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://eval-test-openai.openai.azure.com/"


llm = AzureChatOpenAI(
        openai_api_version="2024-02-15-preview",
        azure_deployment="gpt35-turbo",
        temperature=0.0)

def assistant_chain(
        system_message,
        human_template="{question}",
        llm=llm,
        output_parser=StrOutputParser()
):
    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", system_message),
        ("human", human_template),
    ])
        
    return chat_prompt | llm | output_parser


def eval_expected_words(
    system_message,
    question,
    expected_words,
    human_template="{question}",
    llm=llm,
    output_parser=StrOutputParser()
):
        
    assistant = assistant_chain(
            system_message,
            human_template,
            llm,
            output_parser)
    
    answer = assistant.invoke({"question": question})

    print(answer)

    assert any(word in answer.lower() for word in expected_words), \
        "Expected the assistant questions to include " \
        "'{}' but it did not".format(expected_words)


def evaluate_refusal(
    system_message,
    question,
    decline_response,
    human_template="{question}", 
    llm=llm,
    output_parser=StrOutputParser()
):
    
    assistant = assistant_chain(system_message, human_template, llm, output_parser)
  
    answer = assistant.invoke({"question": question})
    
    print(answer)
  
    assert decline_response.lower() in answer.lower(), \
        f"Expected the bot to decline with \
        '{decline_response}' got {answer}"
  
