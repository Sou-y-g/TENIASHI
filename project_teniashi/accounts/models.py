from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _      ##多言語対応のライブラリ
from django.utils import timezone
from django.core.mail import send_mail

class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, **extra_fields):      ##**exta_fieldsは可変長引数を辞書型で格納
        if not username:
            raise ValueError('Users must have an name')     ##ユーザー名が未入力の場合のエラー。emaliも一緒
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)     ##パスワードのハッシュ化
        user.save(using=self._db)
        return user

    def create_user(self, username, email, **extra_fields):
        extra_fields.setdefault('is_staff', False)                ##extra_fieldsに{'is_staff':False}という辞書の値を追加
        extra_fields.setdefault('is_superuser', False)            ##これで普通のユーザーは権限を持たないということをexra_fieldsに記載している
        return self._create_user(username, email, password=None, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self._create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
        validators=[username_validator],
        error_messages={
            'unique': _('そのユーザー名は既に使用されています')
        },
    )
    email = models.EmailField(_('email address'),unique=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this adimn site'
        ),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether the user can log into this admin site'
            'Unselect this instead of deleting accounts.'
        ),
    )
        
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'           #ユーザーモデルにあるメールのフィールド名を文字列で記述します。この値は get_email_field_name()で返される
    USERNAME_FIELD = 'username'     #ここをemailにすればemailでログインができる正し、unique=Trueの値のみ入れられる
    REQUIRED_FIELDS = []            #ここはterminalからcreatesuperuserするときに必要とする項目

    class Meta:
        verbose_name = _('user') #adminページでテーブルの名前をわかりやすくしてる
        verbose_name_plural = _('users') #上の行だけだと、語尾にsがつくのでそれをなくす？

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
        #メールアドレスの正規化(大文字小文字の区別をなくして同じものとみなす？)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)