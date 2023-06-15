# Generated by Django 3.2.16 on 2023-01-12 19:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('environment', '0003_alter_soilph_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soilph',
            name='name',
            field=models.DecimalField(choices=[(0.0, '0.0'), (0.1, '0.1'), (0.2, '0.2'), (0.3, '0.3'), (0.4, '0.4'), (0.5, '0.5'), (0.6, '0.6'), (0.7, '0.7'), (0.8, '0.8'), (0.9, '0.9'), (1.0, '1.0'), (1.1, '1.1'), (1.2, '1.2'), (1.3, '1.3'), (1.4, '1.4'), (1.5, '1.5'), (1.6, '1.6'), (1.7, '1.7'), (1.8, '1.8'), (1.9, '1.9'), (2.0, '2.0'), (2.1, '2.1'), (2.2, '2.2'), (2.3, '2.3'), (2.4, '2.4'), (2.5, '2.5'), (2.6, '2.6'), (2.7, '2.7'), (2.8, '2.8'), (2.9, '2.9'), (3.0, '3.0'), (3.1, '3.1'), (3.2, '3.2'), (3.3, '3.3'), (3.4, '3.4'), (3.5, '3.5'), (3.6, '3.6'), (3.7, '3.7'), (3.8, '3.8'), (3.9, '3.9'), (4.0, '4.0'), (4.1, '4.1'), (4.2, '4.2'), (4.3, '4.3'), (4.4, '4.4'), (4.5, '4.5'), (4.6, '4.6'), (4.7, '4.7'), (4.8, '4.8'), (4.9, '4.9'), (5.0, '5.0'), (5.1, '5.1'), (5.2, '5.2'), (5.3, '5.3'), (5.4, '5.4'), (5.5, '5.5'), (5.6, '5.6'), (5.7, '5.7'), (5.8, '5.8'), (5.9, '5.9'), (6.0, '6.0'), (6.1, '6.1'), (6.2, '6.2'), (6.3, '6.3'), (6.4, '6.4'), (6.5, '6.5'), (6.6, '6.6'), (6.7, '6.7'), (6.8, '6.8'), (6.9, '6.9'), (7.0, '7.0'), (7.1, '7.1'), (7.2, '7.2'), (7.3, '7.3'), (7.4, '7.4'), (7.5, '7.5'), (7.6, '7.6'), (7.7, '7.7'), (7.8, '7.8'), (7.9, '7.9'), (8.0, '8.0'), (8.1, '8.1'), (8.2, '8.2'), (8.3, '8.3'), (8.4, '8.4'), (8.5, '8.5'), (8.6, '8.6'), (8.7, '8.7'), (8.8, '8.8'), (8.9, '8.9'), (9.0, '9.0'), (9.1, '9.1'), (9.2, '9.2'), (9.3, '9.3'), (9.4, '9.4'), (9.5, '9.5'), (9.6, '9.6'), (9.7, '9.7'), (9.8, '9.8'), (9.9, '9.9'), (10.0, '10.0'), (10.1, '10.1'), (10.2, '10.2'), (10.3, '10.3'), (10.4, '10.4'), (10.5, '10.5'), (10.6, '10.6'), (10.7, '10.7'), (10.8, '10.8'), (10.9, '10.9'), (11.0, '11.0'), (11.1, '11.1'), (11.2, '11.2'), (11.3, '11.3'), (11.4, '11.4'), (11.5, '11.5'), (11.6, '11.6'), (11.7, '11.7'), (11.8, '11.8'), (11.9, '11.9'), (12.0, '12.0'), (12.1, '12.1'), (12.2, '12.2'), (12.3, '12.3'), (12.4, '12.4'), (12.5, '12.5'), (12.6, '12.6'), (12.7, '12.7'), (12.8, '12.8'), (12.9, '12.9'), (13.0, '13.0'), (13.1, '13.1'), (13.2, '13.2'), (13.3, '13.3'), (13.4, '13.4'), (13.5, '13.5'), (13.6, '13.6'), (13.7, '13.7'), (13.8, '13.8'), (13.9, '13.9'), (14.0, '14.0')], decimal_places=1, max_digits=2, null=True, unique=True, validators=[django.core.validators.MinValueValidator(0, 'Уровень кислотности не может быть меньше 0'), django.core.validators.MaxValueValidator(14, 'Уровень кислотности не может быть больше 14')], verbose_name='Название'),
        ),
    ]
