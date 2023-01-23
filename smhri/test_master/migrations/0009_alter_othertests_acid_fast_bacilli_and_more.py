# Generated by Django 4.1.4 on 2022-12-21 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_master', '0008_alter_complaints_allergic_to_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='othertests',
            name='acid_fast_bacilli',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='ag_ratio',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='avg_blood_glucose_level',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='gppd',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='hba1c',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='hbsag',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='hiv_method',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='hiv_remark',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='hiv_result',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='hs_crp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='s_albumin_bcg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='s_globulin',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='s_protein_total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='serum_cholinesterase',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_adults_warm',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_bacteria',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_blood',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_color',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_cyst',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_epithelial_cell',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_fat_globules',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_larva',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_macrophages',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_mucus',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_muscle_fibers',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_occult_blood',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_ova',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_parasites',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_ph',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_pus',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_puscells',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_rbcs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_reducing_substances',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_starch_granules',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_trophozoites',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_vegetable_cell',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='stool_yeast_cells',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='thyroid_t3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='thyroid_t4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='thyroid_tsh',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='othertests',
            name='vdrl',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]