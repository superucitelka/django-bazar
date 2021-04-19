from django.core.validators import MinValueValidator
from django.db import models

class Druh(models.Model):
    oznaceni_druhu = models.CharField(max_length=50, unique=True, verbose_name="Označení druhu zboží",
                            help_text='Zadejte text o maximální délce 50 znaků; text musí být jedinečný')
    OBLAST = (
        ('elektro', 'Elektro'),
        ('nábytek', 'Nábytek'),
        ('domácí potřeby', 'Domácí potřeby'),
        ('hobby', 'Hobby'),
        ('ostatní', 'Ostatní'),
    )
    oblast = models.CharField(max_length=20, choices=OBLAST, blank=True, default='elektro', verbose_name="Oblast", help_text='Vyberte označení oblasti')

    class Meta:
        ordering = ["oznaceni_druhu"]
        verbose_name = 'Druh zboží'
        verbose_name_plural = 'Druh zboží'

    def __str__(self):
        return f"{self.oznaceni_druhu}, {self.oblast}"


class Zbozi(models.Model):
    nazev = models.CharField(max_length=100, verbose_name="Název zboží", help_text='Zadejte text o maximální délce 100 znaků')
    popis = models.TextField(blank=True, null=True, verbose_name="Popis zboží")
    cena = models.FloatField(validators=[MinValueValidator(0.0)], null=True, help_text="Zadejte nezáporné desetinné číslo", verbose_name="Cena")
    STAV = (
        ('5', 'jako nový'),
        ('4', 'málo používaný'),
        ('3', 'často používaný'),
        ('2', 'opotřebovaný'),
        ('1', 'funkční vady'),
    )
    stav = models.CharField(max_length=20, choices=STAV, blank=True, default='3', verbose_name="Stav zboží", help_text='Vyberte označení stavu')
    foto = models.ImageField(upload_to='zbozi/%Y/%m/%d/', blank=True, null=True, verbose_name="Fotka zboží")
    druh = models.ForeignKey(Druh, on_delete=models.RESTRICT)

    class Meta:
        ordering = ["-cena", "nazev"]
        verbose_name = 'Zboží'
        verbose_name_plural = 'Zboží'

    def __str__(self):
        return f"{self.nazev}, {self.cena}"
