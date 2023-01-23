from django.db import models

# Create your models here.

class AudiometerThresholdDecimats(models.Model):
        # audio_th_dec_id = models.AutoField(primary_key=True)
        # emp_id = models.IntegerField()
        right_ac_500 = models.IntegerField()
        right_bc_500 = models.IntegerField()
        right_ac_1000 = models.IntegerField()
        right_bc_1000 = models.IntegerField()
        right_ac_2000 = models.IntegerField()
        right_bc_2000 = models.IntegerField()
        right_ac_4000 = models.IntegerField()
        right_bc_4000 = models.IntegerField()
        right_ac_5000 = models.IntegerField()
        right_bc_5000 = models.IntegerField()
        left_ac_500 = models.IntegerField()
        left_bc_500 = models.IntegerField()
        left_ac_1000 = models.IntegerField()
        left_bc_1000 = models.IntegerField()
        left_ac_2000 = models.IntegerField()
        left_bc_2000 = models.IntegerField()
        left_ac_4000 = models.IntegerField()
        left_bc_4000 = models.IntegerField()
        left_ac_5000 = models.IntegerField()
        left_bc_5000 = models.IntegerField()
        for_right_ear = models.IntegerField()
        for_left_ear = models.IntegerField()
        audiometery = models.IntegerField()
        xray_report = models.IntegerField()
        ultra_sonographic = models.IntegerField()




class BloodTest(models.Model):
        # blood_test_id = models.AutoField(primary_key=True)
        # emp_id = models.IntegerField()
        blood_cholestrol = models.IntegerField()
        creatinine = models.IntegerField(null=True, blank=True)
        blood_urea = models.IntegerField(null=True, blank=True)
        fasting_blood_glucose = models.IntegerField(null=True, blank=True)
        random_blood_glucose = models.IntegerField(null=True, blank=True)
        post_prandial_blood_glucose = models.IntegerField(null=True, blank=True)
        total_bilirubin = models.IntegerField(null=True, blank=True)
        direct_bilirubin = models.IntegerField(null=True, blank=True)
        indirect_bilirubin = models.IntegerField(null=True, blank=True)
        sgpt = models.IntegerField(null=True, blank=True)
        sgot = models.IntegerField(null=True, blank=True)
        alkaline_phosphatase = models.IntegerField(null=True, blank=True)
        ggt = models.IntegerField(null=True, blank=True)
        total_cholesterol = models.IntegerField(null=True, blank=True)
        triglycerides = models.IntegerField(null=True, blank=True)
        direct_hdl = models.IntegerField(null=True, blank=True)
        vldl = models.IntegerField(null=True, blank=True)
        ldl = models.IntegerField(null=True, blank=True)
        ch_ratio = models.IntegerField(null=True, blank=True)
        lh_ratio = models.IntegerField(null=True, blank=True)
        rdw_sd = models.IntegerField(null=True, blank=True)  # Field name made lowercase.
        plcc = models.IntegerField(null=True, blank=True)  # Field name made lowercase.
        plcr = models.IntegerField(null=True, blank=True)  # Field name made lowercase.
        vitaminb12 = models.IntegerField(null=True, blank=True)
        vitamind3 = models.IntegerField(null=True, blank=True)
        hcv = models.IntegerField(null=True, blank=True)
        psa = models.IntegerField(null=True, blank=True)
        bun = models.IntegerField(null=True, blank=True)

class  Urine_Examination(models.Model):
        volume = models.CharField(max_length=222)
        transparency = models.CharField(max_length=255)
        deposit = models.CharField(max_length=255)
        colour = models.CharField(max_length=255)
        sp_gravity = models.IntegerField()
        ph_reaction = models.IntegerField()
        pus_cells = models.IntegerField()
        rbc = models.IntegerField()
        epi_cells = models.IntegerField()
        casts = models.CharField(max_length=225)
        crystals = models.CharField(max_length=255)
        bacteria = models.CharField(max_length=255)
        yeast_cells = models.CharField(max_length=255)
        trichomonas = models.CharField(max_length=255)
        amorphous_deposit = models.CharField(max_length=255)
        albumin = models.CharField(max_length=255)
        sugar = models.CharField(max_length=255)
        acetone = models.CharField(max_length=255)
        bile_pigments = models.CharField(max_length=255)
        bile_salts = models.CharField(max_length=255)
        urobilinogen = models.CharField(max_length=255)

class Complaints(models.Model):
        # complaint_id = models.AutoField(primary_key=True)
        # emp_id = models.IntegerField()
        present_complaints = models.CharField(max_length=255, null=True, blank=True)
        occupational_complaints = models.CharField(max_length=255, null=True, blank=True)
        family_health_history = models.CharField(max_length=255, null=True, blank=True)
        personal_health_history = models.CharField(max_length=255, null=True, blank=True)
        past_history = models.CharField(max_length=255, null=True, blank=True)
        allergic_to = models.CharField(max_length=255, null=True, blank=True)
        id_mark_scar = models.CharField(max_length=255, null=True, blank=True)
        id_mark_mole = models.CharField(max_length=255, null=True, blank=True)




class Hematology(models.Model):
        # hematology_id = models.AutoField(primary_key=True)
        # emp_id = models.IntegerField()
        blood_group = models.CharField(max_length=50)
        hemoglobin = models.CharField(max_length=50)
        total_wbc_count = models.IntegerField()
        polymorphs = models.IntegerField()
        lymphocytes = models.IntegerField()
        eosinophils = models.IntegerField()
        monocytes = models.IntegerField()
        basophils = models.IntegerField()
        leucocytes_count = models.IntegerField()
        platelet_count = models.IntegerField()
        esr = models.IntegerField()
        hct = models.IntegerField()  # Field name made lowercase.
        rdw_cv = models.IntegerField()  # Field name made lowercase.
        pdw = models.IntegerField()  # Field name made lowercase.
        mpv = models.IntegerField()  # Field name made lowercase.
        mch = models.IntegerField()  # Field name made lowercase.
        mchc = models.IntegerField()  # Field name made lowercase.
        pct = models.IntegerField()  # Field name made lowercase.
        mcv = models.IntegerField()  # Field name made lowercase.
        peripheral_smear = models.IntegerField()





class LungFunctionTest(models.Model):
        # lung_function_test_id = models.AutoField(primary_key=True)
        # emp_id = models.IntegerField()
        fvc = models.IntegerField()
        fev1 = models.IntegerField()
        fev1_fvc = models.IntegerField()
        peak_exp_flow = models.IntegerField()
        fef50 = models.IntegerField()
        fvc_predicted = models.IntegerField()
        fev1_predicted = models.IntegerField()
        fev1_fvc_predicted = models.IntegerField()
        pefr_predicted = models.IntegerField()
        fef50_predicted = models.IntegerField()
        fvc_per_predicted = models.IntegerField()
        fev1_per_predicted = models.IntegerField()
        fev1_fvc_per_predicted = models.IntegerField()
        pefr_per_predicted = models.IntegerField()
        fef50_per_predicted = models.IntegerField()
        spirometry = models.IntegerField()



class MicroscopicExamination(models.Model):
        # micro_exam_id = models.AutoField(primary_key=True)
        # emp_id = models.IntegerField()
        red_blood_cells = models.IntegerField()
        pus_cells = models.IntegerField()
        epithelial_cells = models.IntegerField()
        urine_report = models.IntegerField()
        casts = models.IntegerField()
        crystais = models.IntegerField()
        material = models.CharField(max_length=255)



class OtherTests(models.Model):
        # othertest_id = models.AutoField(primary_key=True)
        # emp_id = models.IntegerField()
        serum_cholinesterase = models.IntegerField(null=True, blank=True)
        hs_crp = models.IntegerField(null=True, blank=True)
        gppd = models.IntegerField(null=True, blank=True)
        hba1c = models.IntegerField(null=True, blank=True)
        avg_blood_glucose_level = models.IntegerField(null=True, blank=True)
        hbsag = models.IntegerField(null=True, blank=True)
        hiv_result = models.IntegerField(null=True, blank=True)
        hiv_method = models.IntegerField(null=True, blank=True)
        hiv_remark = models.IntegerField(null=True, blank=True)
        s_protein_total = models.IntegerField(null=True, blank=True)
        s_albumin_bcg = models.IntegerField(null=True, blank=True)
        s_globulin = models.IntegerField(null=True, blank=True)
        ag_ratio = models.IntegerField(null=True, blank=True)
        acid_fast_bacilli = models.IntegerField(null=True, blank=True)
        stool_color = models.IntegerField(null=True, blank=True)
        stool_blood = models.IntegerField(null=True, blank=True)
        stool_mucus = models.IntegerField(null=True, blank=True)
        stool_adults_warm = models.IntegerField(null=True, blank=True)
        stool_parasites = models.IntegerField(null=True, blank=True)
        stool_pus = models.IntegerField(null=True, blank=True)
        stool_ph = models.IntegerField(null=True, blank=True)
        stool_occult_blood = models.IntegerField(null=True, blank=True)
        stool_reducing_substances = models.IntegerField(null=True, blank=True)
        stool_rbcs = models.IntegerField(null=True, blank=True)
        stool_puscells = models.IntegerField(null=True, blank=True)
        stool_fat_globules = models.IntegerField(null=True, blank=True)
        stool_macrophages = models.IntegerField(null=True, blank=True)
        stool_epithelial_cell = models.IntegerField(null=True, blank=True)
        stool_muscle_fibers = models.IntegerField(null=True, blank=True)
        stool_vegetable_cell = models.IntegerField(null=True, blank=True)
        stool_bacteria = models.IntegerField(null=True, blank=True)
        stool_cyst = models.IntegerField(null=True, blank=True)
        stool_ova = models.IntegerField(null=True, blank=True)
        stool_trophozoites = models.IntegerField(null=True, blank=True)
        stool_larva = models.IntegerField(null=True, blank=True)
        stool_yeast_cells = models.IntegerField(null=True, blank=True)
        stool_starch_granules = models.IntegerField(null=True, blank=True)
        thyroid_tsh = models.IntegerField(null=True, blank=True)
        thyroid_t3 = models.IntegerField(null=True, blank=True)
        thyroid_t4 = models.IntegerField(null=True, blank=True)
        vdrl = models.IntegerField(null=True, blank=True)




class PhysiologicalTest(models.Model):
        # phy_test_id = models.AutoField(primary_key=True)
        # emp_id = models.IntegerField()
        height = models.IntegerField()
        weight = models.IntegerField()
        blood_pressure = models.IntegerField()
        pulse = models.IntegerField()
        heart_sound = models.IntegerField()
        chest_on_expiration = models.IntegerField()
        chest_on_inspiration = models.IntegerField()
        waist = models.IntegerField()
        hips = models.IntegerField()
        waist_hip_ratio = models.IntegerField()
        remarks_and_advice = models.IntegerField()




class SystematicExamination(models.Model):
        # sys_exm_id = models.AutoField(primary_key=True)
        # emp_id = models.IntegerField()
        skin = models.CharField(max_length=100)
        respiratory_system = models.CharField(max_length=255)
        cardiovascular_system = models.CharField(max_length=255)
        genito_urinary_system = models.CharField(max_length=255)
        skeletal_system = models.CharField(max_length=255)
        cns = models.CharField(max_length=255)
        breath_sound = models.CharField(max_length=255)
        abdomen = models.CharField(max_length=255)
        other_finding = models.CharField(max_length=255)
        ecg_report = models.CharField(max_length=255)



class VisualTest(models.Model):
        # visual_test_id = models.AutoField(primary_key=True)
        # emp_id = models.IntegerField()
        nearvision_without_glass = models.IntegerField()
        distance_vision_without_glass = models.IntegerField()
        nearvision_with_glass = models.IntegerField()
        distance_vision_with_glass = models.IntegerField()
        nearvision_without_glass_right = models.IntegerField()
        distance_vision_without_glass_right = models.IntegerField()
        nearvision_with_glass_right = models.IntegerField()
        distance_vision_with_glass_right = models.IntegerField()
        vision_remark = models.IntegerField()



class TestMaster(models.Model):
        # test_id = models.AutoField(primary_key=True)
        test_name = models.CharField(max_length=255)
        test_desc = models.CharField(max_length=255)
        status = models.CharField(max_length=255)
        test_model = models.CharField(max_length=255)

















