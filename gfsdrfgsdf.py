class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer.lower()

questions = [
    Question("🐍 What is the output of print(2 * 3)?\n(a) 6\n(b) 8\n(c) 5\n", "a"),
    Question("🧮 What keyword defines a function?\n(a) func\n(b) define\n(c) def\n", "c"),
    Question("🔁 Which loop checks a condition before running?\n(a) for\n(b) while\n(c) repeat\n", "b"),
]

score = 0
for q in questions:
    answer = input(q.prompt)
    if answer.lower() == q.answer:
        score += 1
        print("✅ Correct!")
    else:
        print("❌ Incorrect. The correct answer was:", q.answer)