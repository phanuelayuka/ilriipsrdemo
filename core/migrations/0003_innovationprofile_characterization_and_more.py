# Generated by Django 4.0.6 on 2022-07-10 05:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_innovationreferencematerialurl_innovationimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='innovationprofile',
            name='characterization',
            field=models.CharField(choices=[('incremental', 'Incremental innovation (constant, steady progress or improvement to existing innovations; aims at improving existing products, systems, processes, policies, etc.)'), ('radical', 'Radical innovation (new innovations that replace existing products, systems, processes and policies)'), ('disruptive', 'Disruptive innovation (new innovations that cause/ require broader reconfiguration of the farming, market or policy systems and business models in which they are embedded)'), ('other', 'Other/ I’m not sure/ This characterization does not work for my innovation')], default='incremental', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='innovationprofile',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='innovationprofile',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='innovationprofile',
            name='deleted_on',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='innovationprofile',
            name='improved_varieties_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='innovationprofile',
            name='new_improved_variety_breed',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='innovationprofile',
            name='topology',
            field=models.CharField(choices=[('technological', 'Technological innovation (e.g. varieties/ breeds; crop and livestock management practices; machines; processing technologies; big data and information systems; etc.)'), ('capacity_dvt', 'Capacity development innovation (e.g. farmer, extension or investor decision-support tools; farmer service provision model; training programs and curricula; online courses; etc.)'), ('policy_or_model', 'Policy, organizational or institutional innovation (e.g. policy engagement strategies; business models; policy arrangements; finance and regulatory mechanisms; partnership models or mechanisms; public or private delivery strategies; etc.)'), ('other', 'Other/ I’m not sure/ This typology does not work for my innovation')], default='technological', max_length=100),
            preserve_default=False,
        ),
    ]