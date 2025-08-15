from question import question
ques_prompt = [
    "Which one is the biggest country in Asia.?\n(a) India\n(b) Pakistan\n(c) China\n(d) Nepal\n\n",
    "What is the name of current US president.?\n(a) Donald Trump\n(b) W Bush\n(c) B Obaama \n(d) Joe Biden\n\n",
    "What is your favourite fruit.?\n(a) Mango\n(b) Apple\n(c) Banana\n(d) Grapps\n\n",
]

questions = [
    question(ques_prompt[0], "a"),
    question(ques_prompt[1], "a"),
    question(ques_prompt[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.ques_prompt)
        if answer == question.answer:
            score = + 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
run_test(questions)

