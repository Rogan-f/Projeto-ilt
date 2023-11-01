# Generated by Django 4.2 on 2023-11-01 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=300),
        ),
    ]