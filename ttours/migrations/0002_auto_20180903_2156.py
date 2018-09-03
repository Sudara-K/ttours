# Generated by Django 2.1.1 on 2018-09-03 09:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ttours', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='player1_rating_delta',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='player2_rating_delta',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='season_players',
            name='last_match',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='season_players',
            name='losses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='season_players',
            name='win_percentage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='season_players',
            name='wins',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='match',
            name='last_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='match',
            name='match_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='player',
            name='last_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='season',
            name='last_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='season_players',
            name='last_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
