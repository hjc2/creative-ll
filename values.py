

# prompt for generating a question.
qgen = "generate a hard question about politics and conflicts? Be specific. Make it short, less than 12 words Ex. Should we ban books that include hate speech? How do we solve the isreali palestinian conflict? How can governments address income inequality? How do we stop school shootings in America?"

# assembles the prompt for decisions
def decideGen(question, answer):
    return("Question: " + question + " Answer: " + answer + ". Prompt: Is this is a good answer to the question? Answer Yes or No.")

# assembles the prompt for explanations
def explainGen(question, answer):
    # return("Question: " + question + " Answer: " + answer + ". Respond as a professor who is experienced in foreign policy and political science. Explain why this is an incorrect answer.")
    return("Question: " + question + " Answer: " + answer + ". Respond as a professor who is experienced in foreign policy and political science. Explain why this is an incorrect answer. Do not say who you are")

# assembles the prompt for yes or no # backup for if No
def yesNo(answer):
    return(answer + "does this answer say more Yes or No? Answer Yes or No.")