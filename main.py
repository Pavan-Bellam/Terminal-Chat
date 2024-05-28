from langchain_openai import ChatOpenAI
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Store for session histories
session_store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    """Retrieve or create chat message history for a given session."""
    if session_id not in session_store:
        session_store[session_id] = ChatMessageHistory()
    return session_store[session_id]

def create_chat_chain() -> RunnableWithMessageHistory:
    """Create and configure the chat chain with message history."""
    prompt = ChatPromptTemplate(
        input_variables=['content'],
        messages=[
            MessagesPlaceholder(variable_name="history"),
            HumanMessagePromptTemplate.from_template('{content}')
        ]
    )

    llm = ChatOpenAI(model='gpt-4o')
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    return RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="content",
        history_messages_key="history"
    )

def main():
    """Main function to handle the chat interaction."""
    chain_with_message_history = create_chat_chain()

    while True:
        content = input(">> ")
        result = []
        for chunk in chain_with_message_history.stream(
            {'content': content},
            config={'configurable': {'session_id': '1'}}
        ):
            print(chunk, end='')  # print chunk without adding a new line
            result.append(chunk)
        print('\n')
       

if __name__ == "__main__":
    main()
