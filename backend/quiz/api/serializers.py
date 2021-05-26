from rest_framework import serializers
from quiz.models import Answer,Question,Choice

class MyAnswerSerializer:

    class Meta:
        model=Answer
        fields=('answer',)

class MyChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Choice
        fields=('id','choice')

class MyQuizSerializer(serializers.ModelSerializer):
    answers=MyAnswerSerializer()
    option=MyChoiceSerializer(many=True)
    class Meta:
        model=Question
        fields=('question','level','option','answers')

    # def get_fields(self):
    #     fields = super().get_fields()
    #     fields['choice'] = ChoiceSerializer()
    #     return fields

    # def get_choices(self):
    #     return self.choice_set.all()
