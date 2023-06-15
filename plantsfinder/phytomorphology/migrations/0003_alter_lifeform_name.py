# Generated by Django 3.2.16 on 2023-01-03 13:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('phytomorphology', '0002_alter_lifeform_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifeform',
            name='name',
            field=models.CharField(choices=[('Дерево', 'Дерево'), ('Кустарник', 'Кустарник'), ('Почвопокровный кустарник', 'Почвопокровный кустарник'), ('Лиана', 'Лиана')], default=uuid.uuid1, max_length=50, unique=True, verbose_name='Name'),
        ),
    ]