# Generated by Django 2.1.1 on 2018-09-02 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_time', models.DateTimeField()),
                ('player1_score', models.IntegerField(default=0)),
                ('player2_score', models.IntegerField(default=0)),
                ('last_modified', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=25)),
                ('created_date', models.DateTimeField(verbose_name='Date Joined')),
                ('pic_path', models.CharField(max_length=300)),
                ('last_modified', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(verbose_name='Season start date')),
                ('end_date', models.DateTimeField(verbose_name='Season end date')),
                ('name', models.CharField(max_length=200)),
                ('last_modified', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Season_Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=2000)),
                ('last_modified', models.DateTimeField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ttours.Player')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ttours.Season')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='player1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player1', to='ttours.Season_Players'),
        ),
        migrations.AddField(
            model_name='match',
            name='player2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player2', to='ttours.Season_Players'),
        ),
    ]