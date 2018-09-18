# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storyframes', '0002_auto_20180120_1449'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storyframe',
            options={'verbose_name_plural': 'StoryFrame'},
        ),
    ]
