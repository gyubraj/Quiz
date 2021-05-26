from django.db import models
import random
language_choices=(
        ('NEP','nepali'),
        ('ENG','english')
    )
level_choices=(
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
    ('11','11'),
    ('12','12'),
    ('13','13')
)
class Question(models.Model):
    # class NepaliQuestion(models.Manager):
    #     def get_queryset(self):
    #         return super().get_queryset().filter(language='NEP')
    # class EnglishQuestion(models.Manager):
    #     def get_queryset(self):
    #         return super().get_queryset().filter(language='ENG')

    question=models.CharField(max_length=255)
    language=models.CharField(choices=language_choices,max_length=50)
    level=models.CharField(choices=level_choices,max_length=20)
    # nepaliquestion=NepaliQuestion()
    # englishquestion=EnglishQuestion()
    # objects=models.Manager()

    def __str__(self):
        return self.question

    @property
    def option(self):
        return self.choice_set.all()

    @property
    def answers(self):
        return Answer.objects.values('answer').get(question=self)['answer']


    def get_13_question(self,lan:str):
        question=[]
        for i in range(1,14):
            level_question=self.get_level_question(self,str(i),lan)
            question.append(level_question)
        return question


    def get_level_question(self,lvl:str,lan:str):
        return random.choice(self.objects.filter(level=lvl,language=lan))

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice=models.CharField(max_length=255)

    def __str__(self):
        return self.choice

class Answer(models.Model):
    question=models.OneToOneField(Question,on_delete=models.CASCADE)
    answer=models.OneToOneField(Choice,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.answer.id)
