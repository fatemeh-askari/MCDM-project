from django.db import models
class Method(models.Model):
    DECISION_METHOD_CHOICES = [
        ('method-ARAS', 'ARAS'),
        ('method-Borda', 'Borda'),
        ('method-CoCoSo', 'CoCoSo'),
        ('method-CODAS', 'CODAS'),
        ('method-Copeland', 'Copeland'),
        ('method-COPRAS', 'COPRAS'),
        ('method-CRADIS', 'CRADIS'),
        ('method-EDAS', 'EDAS'),
        ('method-GRA', 'GRA'),
        ('method-MABAC', 'MABAC'),
        ('method-MACBETH', 'MACBETH'),
        ('method-MAIRCA', 'MAIRCA'),
        ('method-MARA', 'MARA'),
        ('method-MARCOS', 'MARCOS'),
        ('method-MOORA', 'MOORA'),
        ('method-MOOSRA', 'MOOSRA'),
        ('method-OCRA', 'OCRA'),
        ('method-ORESTE', 'ORESTE'),
        ('method-PIV', 'PIV'),
        ('method-PSI', 'PSI'),
        ('method-REGIME', 'REGIME'),
        ('method-ROV', 'ROV'),
        ('method-SAW', 'SAW'),
        ('method-TODIM', 'TODIM'),
        ('method-TOPSIS', 'TOPSIS'),
        ('method-WSM', 'WSM'),
        ('method-WPM', 'WPM'),
        ('method-WASPAS', 'WASPAS'),
        ('method-Simple WISP', 'Simple WISP'),
        ('method-WISP', 'WISP'),
    ]
    name = models.CharField(max_length=70, choices=DECISION_METHOD_CHOICES)
    hyperparameter = models.FloatField(blank=True, null=True)

class Indicator(models.Model):
    POSITIVE = 'Positive'
    NEGATIVE = 'Negative'
    INDICATOR_TYPE_CHOICES = [
        (POSITIVE, 'Positive'),
        (NEGATIVE, 'Negative'),
    ]
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=30, choices=INDICATOR_TYPE_CHOICES)
    weight = models.FloatField()
    method = models.ForeignKey(Method, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Choice(models.Model):
    name = models.CharField(max_length=200)
    method = models.ForeignKey(Method, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Request(models.Model):
    method = models.ForeignKey(Method, on_delete=models.CASCADE)
    indicators = models.ManyToManyField(Indicator)
    choices = models.ManyToManyField(Choice)
    def __str__(self):
        return f"Request - Method: {self.method}"

class MatrixData(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    data = models.JSONField(blank=True)
    def __str__(self):
        return self.data

