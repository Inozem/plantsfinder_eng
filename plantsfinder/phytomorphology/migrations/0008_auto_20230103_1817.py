# Generated by Django 3.2.16 on 2023-01-03 15:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('phytomorphology', '0007_bloomcolour'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloomingPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[], default=uuid.uuid1, max_length=50, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Период цветения',
                'verbose_name_plural': 'Периоды цветения',
            },
        ),
        migrations.AlterField(
            model_name='bloomcolour',
            name='name',
            field=models.CharField(choices=[('Белый', 'Белый'), ('Бронзоватый', 'Бронзоватый'), ('Голубой', 'Голубой'), ('Желтый', 'Желтый'), ('Зеленый', 'Зеленый'), ('Красный', 'Красный'), ('Оранжевый', 'Оранжевый'), ('Розовый', 'Розовый'), ('Серебристый', 'Серебристый'), ('Серый', 'Серый'), ('Сизый', 'Сизый'), ('Синий', 'Синий'), ('Фиолетовый', 'Фиолетовый'), ('Не являются декоративными', 'Не являются декоративными'), ('Отсутствуют', 'Отсутствуют')], default=uuid.uuid1, max_length=50, unique=True, verbose_name='Name'),
        ),
    ]
