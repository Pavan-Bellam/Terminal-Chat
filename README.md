# Chat History Memory Project

This project demonstrates a chat application that remembers the conversation history. It is designed for studying purposes and utilizes the LangChain framework with OpenAI's GPT-4 model to maintain and interact with session-based chat histories.

## Features

- **Session-based Memory**: The application remembers the text and conversation history based on session IDs.
- **Streamed Responses**: Responses from the language model are streamed and displayed in real-time.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_name>
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```sh
    python main.py
    ```

2. Interact with the chat application:
    - Enter your text input after the `>>` prompt.
    - The application will display responses from the language model in real-time and remember the conversation history for the session.

## Example

```sh
>> My name is Pavan
Nice to meet you, Pavan!

>> Do you remember my name?
Yes, I remember your name is Pavan.
```

## Purpose

This project is created as part of a study exercise to understand and implement session-based memory in chat applications using modern language models.
