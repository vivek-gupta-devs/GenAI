import tiktoken 

# To get the tokeniser corresponding to a specific model in the OpenAI API:
enc = tiktoken.encoding_for_model("gpt-4o")

text = "With one change in fruit intake from orange to guava, you are leveraging a better vitamin C vitamin without needing a complex regimen of supplements."

tokens = enc.encode(text)
print("Encoded tokens from text: ",tokens)

decode_text = enc.decode(tokens)
print("Decoded text from tokens: ",decode_text)



