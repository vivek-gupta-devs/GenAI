from main import client

# Chat Completion Model
chat_completion_response = client.chat.completions.create(
    model="gpt-5-nano",
    messages= [
        {"role":"user", "content":"Hey, my name is Vivek Gupta"},
        {"role":"assistant", "content":"Hi Vivek! Nice to meet you. How can I help today?"},
        {"role":"user", "content":"What is my name?"},
        {"role":"assistant", "content":"Your name is Vivek Gupta.How can I assist you today?"},
        {"role":"user", "content":"Tell me about game theory techniques?"}
    ]
)

print(chat_completion_response.choices[0].message.content)
