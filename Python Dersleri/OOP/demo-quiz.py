# Question

class Question():
    def __init__(self,text,choices,answer): # text = sorunun içerik kısmı, choices = şıklar, answer = cevaplar
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self,answer):
        return self.answer == answer

# Quiz
class Quiz():
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionsIndex = 0 # 1. Soruyu Belli Ettik

    def qetQuestion(self):
        return self.questions[self.questionsIndex]

    def quess(self,answer):
            question = self.qetQuestion()

            if question.checkAnswer(answer):
                self.score += 1
            self.questionsIndex +=1

    def displayQuestion(self):
        question = self.qetQuestion()
        print(f"Soru {self.questionsIndex + 1}: {question.text}")

        for q in question.choices:
            print("-" + q)

        answer = input("Lütfen Doğru Cevabı Yazınız: ")
        self.quess(answer)
        self.loadQuestion()

    def loadQuestion(self):
        if len(self.questions) == self.questionsIndex :
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print("Scorunuz: ", self.score)        

    def displayProgress(self):
         totelQuestion = len(self.questions) 
         questionNumber = self.questionsIndex + 1

         if(questionNumber > totelQuestion):
             print("Quiz Bitti.")
         else:
            print(f"Question {questionNumber} of {totelQuestion}".center(100,'*'))

q1 = Question("En İyi Programlama Dili Hangisidir ? ",['C#','Python','JavaScript','Java'],'Python')
q2 = Question("En Popüler Programlama Dili Hangisidir ? ",['Python','JavaScript','C#','Java'],'Python')
q3 = Question("En Çok Kazandıran Dili Hangisidir ? ",['C#','JavaScript','Java','Python'],'Python')
questions = [q1,q2,q3]

quiz = Quiz(questions)

quiz.loadQuestion()
