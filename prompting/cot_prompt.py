from main import client
import json

# Chain Of Thought: The model is encouraged to break down reasoning step by step before arriving to any solution.

SYSTEM_PROMPT = '''
    You are an helpfull AI assistant who is specialized in resolving user query.
    For the given user input, analyse the input and breakdown the problem step by step.
    The steps as follow, you get an user input, analyse it, think it, think it again and think for serval time. Then return the response with explanation.

    Follow the step "analyse","think","output", "validate" then finally return the "result"

    Rules: 
    1: Strictly return output in json format.
    2: Carefully review user query.
    3: Properly validate the output.
    4: Always perform one step at a time and for next step wait for user input.
    5: Available coin denominations (1, 2, 5, 10, 20)

    Output Format:
    { "step": string, "output": string }

    Example:
    User: How many 20 rupees coins need to make 100 rupees?
    Output: {"step":"analyse", "output":"Seems, like user wanted to know about some calculation about money"}
    Output: {"step":"think", "output":"This looks like 100 rupees can be make from 20 rupees coins"}
    Output: {"step":"output", "output":"5 coins"}
    Output: {"step":"validate", "output":"estimated calculation looks 100/20=5 coins"}
    Output: {"step":"result", "output":"Total 5 coins needed of 20 rupees each to make 100 rupees."}
'''

'''
response = client.chat.completions.create(
    model="gpt-5-nano",
    messages= [
        {"role":"system", "content": SYSTEM_PROMPT},
        {"role":"user", "content":"How many coins needed of rupee 1,2,5 and 10 to make 87 rupees?"},
        {"role":"assistant", "content": json.dumps({"step":"analyse","output":"User asks for a combination of 1, 2, 5, and 10 rupee coins that sum to 87. Multiple solutions exist; I will aim for a valid solution with the minimal number of coins by using the largest denominations first (greedy approach) and then fill the remainder with smaller denominations."})},
        {"role":"assistant", "content": json.dumps({"step":"think","output":"Approach: maximize 10-rupee coins to minimize coin count. 87 divided by 10 gives 8 tens (80), remainder 7. Make 7 with 5 and 2 (best 5+2). So solution: 8 x 10-rupee coins, 1 x 5-rupee coin, 1 x 2-rupee coin; no 1-rupee coins needed; total 10 coins."})},
        {"role":"assistant", "content": json.dumps({"step":"output", "output":"Using the greedy approach: 87 = 8×10 + 1×5 + 1×2. So you need 8 ten-rupee coins, 1 five-rupee coin, 1 two-rupee coin, and 0 one-rupee coins (total 10 coins)."})},
        {"role":"assistant", "content": json.dumps({"step": "validate", "output": "Validation: 87 = 8*10 + 1*5 + 1*2 + 0*1; total coins = 8 + 1 + 1 + 0 = 10. Minimality check: The theoretical minimum number of coins is ceil(87/10) = 9. A 9-coin solution would require a valid combination of 9 coins from {10,5,2,1} summing to 87. Solving 10a + 5b + 2c + d = 87 with a + b + c + d = 9 yields 9a + 4b + c = 78, which has no nonnegative integer solutions under a + b + c ≤ 9. Therefore, 10 coins is indeed the minimal count."})}
     ]
)

print(response.choices[0].message.content)
'''

messages = [{"role":"system", "content":SYSTEM_PROMPT}]
query = input("Provide your query:\n")
messages.append({"role":"user", "content":query})

while True:

    response = client.chat.completions.create(
         model="gpt-5-nano",
         response_format= {"type":"json_object"},
         messages=messages
    )
    messages.append({"role":"assistant", "content":response.choices[0].message.content})

    parsed_response = json.loads(response.choices[0].message.content)

    if(parsed_response.get("step") != "result"):
        print(f'[{parsed_response.get("step").upper()}] : {parsed_response.get("output")}')
        continue
    else:
        print(parsed_response.get("output"))
        break


