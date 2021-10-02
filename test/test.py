import nice_prompts

n = nice_prompts.NicePrompt()

print(n.selection({"I like pizza": "Good taste",
    "I respectfully disagree with the opinion of liking pizza": "Fair enough, good day",
    "I hate pizza": "Bad sport 👎"})) # Select one from the keys, return the value

print(n.multiselection({"I like pizza": "Good taste",
    "I respectfully disagree with the opinion of liking pizza": "Fair enough, good day",
    "I hate pizza": "Bad sport 👎"}, amount=2, required=2)) # Select multiple from the keys, return the values. You must select 2


print(n.multiselection({"I like pizza": "Good taste",
    "I respectfully disagree with the opinion of liking pizza": "Fair enough, good day",
    "I hate pizza": "Bad sport 👎"}, required=0))  # Select multiple from the keys, return the values. No max, can be left blank