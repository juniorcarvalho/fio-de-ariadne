import os

from django.core.validators import FileExtensionValidator
from django.db.models import (
    CharField,
    DateField,
    IntegerChoices,
    IntegerField,
    Model,
    TextField,
    URLField,
    ForeignKey,
    FileField,
    CASCADE,
)
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


class Kid(Model):
    class Color(IntegerChoices):
        BLACK = 1, _("Preto")
        BROWN = 2, _("Castanhos")
        BLONDE = 3, _("Loiro")
        RED = 4, _("Ruivo")
        BLUE = (
            5,
            _("Azul"),
        )
        SWARTHY = 6, _("Morena")
        WHITE = 7, _("Branca")

    # required fiels
    name = CharField("Nome", max_length=255, db_index=True, unique=True)
    url = URLField("URL")
    full_text = TextField()

    # optional indexed fields
    dob = DateField("Data de nascimento", null=True, blank=True, db_index=True)
    missing_since = DateField(
        "Desaparecida(o) desde", null=True, blank=True, db_index=True
    )
    eyes = CharField(
        "Cor dos olhos",
        max_length=50,
        choices=Color.choices,
        null=True,
        blank=True,
        db_index=True,
    )
    hair = CharField(
        "Cor dos cabelos",
        max_length=50,
        choices=Color.choices,
        null=True,
        blank=True,
        db_index=True,
    )
    skin = CharField(
        "Cor da pele",
        max_length=50,
        choices=Color.choices,
        null=True,
        blank=True,
        db_index=True,
    )

    # optional fields
    mother = CharField("Mãe", max_length=255, null=True, blank=True)
    father = CharField("Pai", max_length=255, null=True, blank=True)
    last_seen_at_city = CharField(
        "Cidade onde foi vista(o) pela última vez",
        max_length=255,
        null=True,
        blank=True,
        db_index=True,
    )
    last_seen_at_state = CharField(
        "UF onde foi vista(o) pela última vez",
        max_length=2,
        null=True,
        blank=True,
        db_index=True,
    )
    age_at_occurrence = IntegerField("Idade quando desapareceu", null=True, blank=True)

    class Meta:
        verbose_name = "criança"
        ordering = ("name",)

    def __str__(self):
        return self.name


def get_file_name_storage(instance, filename):
    return os.path.join(str(instance.kid.id), filename)


class KidImage(Model):
    kid = ForeignKey(Kid, on_delete=CASCADE, verbose_name="criança")
    image = FileField(
        upload_to=get_file_name_storage,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "gif"])
        ],
    )

    @property
    def image_render(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))

    class Meta:
        verbose_name = "criança imagem"
        verbose_name_plural = "criança imagens"

    def __str__(self):
        return "{0}".format(self.kid.name)
