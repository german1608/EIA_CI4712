'''
Validadores de los modelos de django
'''
import re
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

CI_VALIDATOR = RegexValidator(
    re.compile('^[V|E|J|P][0-9]{5,9}$'),
    _('Cédula incorrecta'),
    'invalid')
