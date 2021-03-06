from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for quest in question_data:
    question_text = quest["question"]
    question_answer = quest["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print("ðï¸ðï¸you've completed the quizðï¸ðï¸")
print(f"your final score was: {quiz.score}/{quiz.question_number}")
print ("ðï¸ððï¸ððï¸ððï¸ððï¸ððï¸ð")



