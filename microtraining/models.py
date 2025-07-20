from django.db import models
from apps.phishing.models import Language  # Importiere die vorhandene Language-Tabelle

class MicroTrainingCategory(models.Model):
    name = models.CharField(max_length=255)
    default_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class MicroTraining(models.Model):
    name = models.CharField(max_length=255)
    default_active = models.BooleanField(default=True)
    category = models.ForeignKey(MicroTrainingCategory, related_name='microtrainings', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class MicroTrainingTranslation(models.Model):
    microtraining = models.ForeignKey(MicroTraining, related_name='translations', on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()

    question_text = models.TextField()
    answer1 = models.CharField(max_length=255)
    answer2 = models.CharField(max_length=255)
    answer3 = models.CharField(max_length=255)
    correct_answer_index = models.IntegerField()

    class Meta:
        unique_together = ('microtraining', 'language')

    def __str__(self):
        return f"{self.microtraining.name} ({self.language.name})"
