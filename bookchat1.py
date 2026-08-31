import gradio as gr
import requests


def chat(message, history):

    url = "http://localhost:11434/api/chat"

    # System instructions
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful chatbot for a small bookstore. "
                "The bookstore has programming, fiction, and history books. "
                "The bookstore opens at 9:00 AM. "
                "Answer customer questions briefly and clearly."
            )
        }
    ]

    # Add previous conversation
    for msg in history:
        messages.append({
            "role": msg["role"],
            "content": msg["content"]
        })

    # Add current question
    messages.append({
        "role": "user",
        "content": message
    })

    try:
        response = requests.post(
            url,
            json={
                "model": "llama3.2:1b",
                "messages": messages,
                "stream": False
            }
        )

        data = response.json()

        return data["message"]["content"]

    except Exception as e:
        return f"Error: {str(e)}"


gr.ChatInterface(
    fn=chat,
    title="Bookstore Chatbot"
).launch()