"""
All `telegram_bot` models.

models: 
    - TelegramProfile
"""
import random
import string
from django.db import models

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class TelegramProfile(models.Model):
    """
    A class to represent the link between a django user and the telegram account
    """

    id = models.IntegerField(_("telegram user ID"), primary_key=True)
    chat_id = models.IntegerField(_("chat ID"), unique=True)
    username = models.CharField(
        _("telegram username"), max_length=256, unique=True
    )

    user = models.OneToOneField(
        User, verbose_name=_("user"), on_delete=models.CASCADE
    )


def generate_token_str() -> str:
    """generate random letters of length 5"""

    token = "".join(random.choices(string.ascii_letters, k=5))
    return token


class Token(models.Model):
    """
    This model to create user tokens,
    to verify their Telegram identity
    and connect them to our `User` model.
    """

    token = models.CharField(
        _("token"),
        max_length=5,
        help_text=_("random generated"),
        default=generate_token_str,
    )
    user = models.ForeignKey(
        User, verbose_name=_("user"), on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("token")
        verbose_name_plural = _("tokens")

    def __str__(self):
        return str(self.token)
