from pyspark.sql.types import StructType, StructField, LongType, \
    IntegerType, DateType, TimestampType, StringType, FloatType


class OmopSchema(object):
    def __init__(self):
        self.concept = StructType([
            StructField("concept_id", IntegerType(), False),
            StructField("concept_name", StringType(), True),
            StructField("domain_id", StringType(), True),
            StructField("vocabulary_id", StringType(), True),
            StructField("concept_class_id", StringType(), True),
            StructField("standard_concept", StringType(), True),
            StructField("concept_code", StringType(), True),
            StructField("valid_start_date", DateType(), True),
            StructField("valid_end_date", DateType(), True),
            StructField("invalid_reason", StringType(), True)
        ])

        self.vocabulary = StructType([
            StructField("vocabulary_id", StringType(), False),
            StructField("vocabulary_name", StringType(), True),
            StructField("vocabulary_reference", StringType(), True),
            StructField("vocabulary_version", StringType(), True),
            StructField("vocabulary_concept_id", IntegerType(), True)
        ])

        self.domain = StructType([
            StructField("domain_id", StringType(), False),
            StructField("domain_name", StringType(), True),
            StructField("domain_concept_id", IntegerType(), True)
        ])

        self.concept_class = StructType([
            StructField("concept_class_id", StringType(), False),
            StructField("concept_class_name", StringType(), True),
            StructField("concept_class_concept_id", IntegerType(), True)
        ])

        self.concept_relationship = StructType([
            StructField("concept_id_1", IntegerType(), False),
            StructField("concept_id_2", IntegerType(), False),
            StructField("relationship_id", StringType(), False),
            StructField("valid_start_date", DateType(), True),
            StructField("valid_end_date", DateType(), True),
            StructField("invalid_reason", StringType(), True)
        ])

        self.relationship = StructType([
            StructField("relationship_id", StringType(), False),
            StructField("relationship_name", StringType(), True),
            StructField("is_hierarchical", StringType(), True),
            StructField("defines_ancestry", StringType(), True),
            StructField("reverse_relationship_id", StringType(), True),
            StructField("relationship_concept_id", IntegerType(), True)
        ])

        self.concept_synonym = StructType([
            StructField("concept_id", IntegerType(), False),
            StructField("concept_synonym_name", StringType(), True),
            StructField("language_concept_id", IntegerType(), True)
        ])

        self.concept_ancestor = StructType([
            StructField("ancestor_concept_id", IntegerType(), False),
            StructField("descendant_concept_id", IntegerType(), False),
            StructField("min_levels_of_separation", IntegerType(), True),
            StructField("max_levels_of_separation", IntegerType(), True)
        ])

        self.source_to_concept_map = StructType([
            StructField("source_code", StringType(), False),
            StructField("source_concept_id", IntegerType(), True),
            StructField("source_vocabulary_id", StringType(), False),
            StructField("source_code_description", StringType(), True),
            StructField("target_concept_id", IntegerType(), False),
            StructField("target_vocabulary_id", StringType(), True),
            StructField("valid_start_date", DateType(), True),
            StructField("valid_end_date", DateType(), False),
            StructField("invalid_reason", StringType(), True)
        ])

        self.drug_strength = StructType([
            StructField("drug_concept_id", IntegerType(), False),
            StructField("ingredient_concept_id", IntegerType(), False),
            StructField("amount_value", FloatType(), True),
            StructField("amount_unit_concept_id", IntegerType(), True),
            StructField("numerator_value", FloatType(), True),
            StructField("numerator_unit_concept_id", IntegerType(), True),
            StructField("denominator_value", FloatType(), True),
            StructField("denominator_unit_concept_id", IntegerType(), True),
            StructField("box_size", IntegerType(), True),
            StructField("valid_start_date", DateType(), True),
            StructField("valid_end_date", DateType(), True),
            StructField("invalid_reason", StringType(), True)
        ])

        self.attribute_definition = StructType([
            StructField("attribute_definition_id", IntegerType(), False),
            StructField("attribute_name", StringType(), True),
            StructField("attribute_description", StringType(), True),
            StructField("attribute_type_concept_id", IntegerType(), False),
            StructField("attribute_syntax", StringType(), True)
        ])

        self.cdm_source = StructType([
            StructField("cdm_source_name", StringType(), False),
            StructField("cdm_source_abbreviation", StringType(), True),
            StructField("cdm_holder", StringType(), True),
            StructField("source_description", StringType(), True),
            StructField("source_documentation_reference", StringType(), True),
            StructField("cdm_etl_reference", StringType(), True),
            StructField("source_release_date", DateType(), True),
            StructField("cdm_release_date", DateType(), True),
            StructField("cdm_version", StringType(), True),
            StructField("vocabulary_version", StringType(), True)
        ])

        self.metadata = StructType([
            StructField("metadata_concept_id", IntegerType(), False),
            StructField("metadata_type_concept_id", IntegerType(), False),
            StructField("name", StringType(), True),
            StructField("value_as_string", StringType(), True),
            StructField("value_as_concept_id", IntegerType(), True),
            StructField("metadata_date", DateType(), True),
            StructField("metadata_datetime", TimestampType(), True)
        ])

        self.person = StructType([
            StructField("person_id", LongType(), False), 
            StructField("gender_concept_id", IntegerType(), True),
            StructField("year_of_birth", IntegerType(), True),
            StructField("month_of_birth", IntegerType(), True),
            StructField("day_of_birth", IntegerType(), True),
            StructField("birth_datetime", TimestampType(), True),
            StructField("death_datetime", TimestampType(), True),
            StructField("race_concept_id", IntegerType(), True),
            StructField("ethnicity_concept_id", IntegerType(), True),
            StructField("location_id", LongType(), True),
            StructField("provider_id", LongType(), True),
            StructField("care_site_id", LongType(), True),
            StructField("person_source_value", StringType(), True),
            StructField("gender_source_value", StringType(), True),
            StructField("gender_source_concept_id", IntegerType(), True),
            StructField("race_source_value", StringType(), True),
            StructField("race_source_concept_id", IntegerType(), True),
            StructField("ethnicity_source_value", StringType(), True),
            StructField("ethnicity_source_concept_id", IntegerType(), True)
        ])

        self.observation_period = StructType([
            StructField("observation_period_id", LongType(), False),
            StructField("person_id", LongType(), False),
            StructField("observation_period_start_date", DateType(), True),
            StructField("observation_period_end_date", DateType(), True),
            StructField("period_type_concept_id", IntegerType(), True)
        ])

        self.specimen = StructType([
            StructField("specimen_id", LongType(), False),
            StructField("person_id", LongType(), False),
            StructField("specimen_concept_id", IntegerType(), True),
            StructField("specimen_type_concept_id", IntegerType(), True),
            StructField("specimen_date", DateType(), True),
            StructField("specimen_datetime", TimestampType(), True),
            StructField("quantity", FloatType(), True),
            StructField("unit_concept_id", IntegerType(), True),
            StructField("anatomic_site_concept_id", IntegerType(), True),
            StructField("disease_status_concept_id", IntegerType(), True),
            StructField("specimen_source_id", StringType(), True),
            StructField("specimen_source_value", StringType(), True),
            StructField("unit_source_value", StringType(), True),
            StructField("anatomic_site_source_value", StringType(), True),
            StructField("disease_status_source_value", StringType(), True)
        ])

        self.visit_occurrence = StructType([
            StructField("visit_occurrence_id", LongType(), False),
            StructField("person_id", LongType(), False),
            StructField("visit_concept_id", IntegerType(), True),
            StructField("visit_start_date", DateType(), True),
            StructField("visit_start_datetime", TimestampType(), True),
            StructField("visit_end_date", DateType(), True),
            StructField("visit_end_datetime", TimestampType(), True),
            StructField("visit_type_concept_id", IntegerType(), True),
            StructField("provider_id", LongType(), True),
            StructField("care_site_id", LongType(), True),
            StructField("visit_source_value", StringType(), True),
            StructField("visit_source_concept_id", IntegerType(), True),
            StructField("admitted_from_concept_id", IntegerType(), True),   
            StructField("admitted_from_source_value", StringType(), True),
            StructField("discharge_to_source_value", StringType(), True),
            StructField("discharge_to_concept_id", IntegerType(), True),
            StructField("preceding_visit_occurrence_id", LongType(), True)
        ])

        self.visit_detail = StructType([
            StructField("visit_detail_id", LongType(), False),
            StructField("person_id", LongType(), False),
            StructField("visit_detail_concept_id", IntegerType(), True),
            StructField("visit_detail_start_date", DateType(), True),
            StructField("visit_detail_start_datetime", TimestampType(), True),
            StructField("visit_detail_end_date", DateType(), True),
            StructField("visit_detail_end_datetime", TimestampType(), True),
            StructField("visit_detail_type_concept_id", IntegerType(), True),
            StructField("provider_id", LongType(), True),
            StructField("care_site_id", LongType(), True),
            StructField("discharge_to_concept_id", IntegerType(), True),
            StructField("admitted_from_concept_id", IntegerType(), True), 
            StructField("admitted_from_source_value", StringType(), True),
            StructField("visit_detail_source_value", StringType(), True),
            StructField("visit_detail_source_concept_id", IntegerType(), True),
            StructField("discharge_to_source_value", StringType(), True),
            StructField("preceding_visit_detail_id", LongType(), True),
            StructField("visit_detail_parent_id", LongType(), True),
            StructField("visit_occurrence_id", LongType(), True)
        ])

        self.procedure_occurrence = StructType([
            StructField("procedure_occurrence_id", LongType(), False),
            StructField("person_id", LongType(), False),
            StructField("procedure_concept_id", IntegerType(), True),
            StructField("procedure_date", DateType(), True),
            StructField("procedure_datetime", TimestampType(), True),
            StructField("procedure_type_concept_id", IntegerType(), True),
            StructField("modifier_concept_id", IntegerType(), True),
            StructField("quantity", IntegerType(), True),
            StructField("provider_id", LongType(), True),
            StructField("visit_occurrence_id", LongType(), True),
            StructField("visit_detail_id", LongType(), True),
            StructField("procedure_source_value", StringType(), True),
            StructField("procedure_source_concept_id", IntegerType(), True),
            StructField("modifier_source_value", StringType(), True)
        ])

        self.drug_exposure = StructType([
            StructField("drug_exposure_id", LongType(), False),
            StructField("person_id", LongType(), False),
            StructField("drug_concept_id", IntegerType(), True),
            StructField("drug_exposure_start_date", DateType(), True),
            StructField("drug_exposure_start_datetime", TimestampType(), True),
            StructField("drug_exposure_end_date", DateType(), True),
            StructField("drug_exposure_end_datetime", TimestampType(), True),
            StructField("verbatim_end_date", DateType(), True),
            StructField("drug_type_concept_id", IntegerType(), True),
            StructField("stop_reason", StringType(), True),
            StructField("refills", IntegerType(), True),
            StructField("quantity", FloatType(), True),
            StructField("days_supply", IntegerType(), True),
            StructField("sig", StringType(), True),
            StructField("route_concept_id", IntegerType(), True),
            StructField("lot_number", StringType(), True),
            StructField("provider_id", LongType(), True),
            StructField("visit_occurrence_id", LongType(), True),
            StructField("visit_detail_id", LongType(), True),
            StructField("drug_source_value", StringType(), True),
            StructField("drug_source_concept_id", IntegerType(), True),
            StructField("route_source_value", StringType(), True),
            StructField("dose_unit_source_value", StringType(), True)
        ])

        self.device_exposure = StructType([
            StructField("device_exposure_id", LongType(), False),
            StructField("person_id", LongType(), False),
            StructField("device_concept_id", IntegerType(), True),
            StructField("device_exposure_start_date", DateType(), True),
            StructField("device_exposure_start_datetime", TimestampType(), True),
            StructField("device_exposure_end_date", DateType(), True),
            StructField("device_exposure_end_datetime", TimestampType(), True),
            StructField("device_type_concept_id", IntegerType(), True),
            StructField("unique_device_id", StringType(), True),
            StructField("quantity", IntegerType(), True),
            StructField("provider_id", LongType(), True),
            StructField("visit_occurrence_id", LongType(), True),
            StructField("visit_detail_id", LongType(), True),
            StructField("device_source_value", StringType(), True),
            StructField("device_source_concept_id", IntegerType(), True)
        ])

        self.condition_occurrence = StructType([
            StructField("condition_occurrence_id", LongType(), False),
            StructField("person_id", LongType(), False),
            StructField("condition_concept_id", IntegerType(), True),
            StructField("condition_start_date", DateType(), True),
            StructField("condition_start_datetime", TimestampType(), True),
            StructField("condition_end_date", DateType(), True),
            StructField("condition_end_datetime", TimestampType(), True),
            StructField("condition_type_concept_id", IntegerType(), True),
            StructField("condition_status_concept_id", IntegerType(), True),
            StructField("stop_reason", StringType(), True),
            StructField("provider_id", LongType(), True),
            StructField("visit_occurrence_id", LongType(), True),
            StructField("visit_detail_id", LongType(), True),
            StructField("condition_source_value", StringType(), True),
            StructField("condition_source_concept_id", IntegerType(), True),
            StructField("condition_status_source_value", StringType(), True)
        ])

        self.measurement = StructType([
            StructField("measurement_id", LongType(), False),
            StructField("person_id", LongType(), False),
            StructField("measurement_concept_id", IntegerType(), True),
            StructField("measurement_date", DateType(), True),
            StructField("measurement_datetime", TimestampType(), True),
            StructField("measurement_time", StringType(), True),
            StructField("measurement_type_concept_id", IntegerType(), True),
            StructField("operator_concept_id", IntegerType(), True),
            StructField("value_as_number", FloatType(), True),
            StructField("value_as_concept_id", IntegerType(), True),
            StructField("unit_concept_id", IntegerType(), True),
            StructField("range_low", FloatType(), True),
            StructField("range_high", FloatType(), True),
            StructField("provider_id", LongType(), True),
            StructField("visit_occurrence_id", LongType(), True),
            StructField("visit_detail_id", LongType(), True),
            StructField("measurement_source_value", StringType(), True),
            StructField("measurement_source_concept_id", IntegerType(), True),
            StructField("unit_source_value", StringType(), True),
            StructField("value_source_value", StringType(), True)
        ])

        self.note = StructType([
            StructField("note_id", LongType(), False),
            StructField("person_id", LongType(), False),
            StructField("note_event_id", LongType(), True), 
            StructField("note_event_field_concept_id", IntegerType(), True), 
            StructField("note_date", DateType(), True),
            StructField("note_datetime", TimestampType(), True),
            StructField("note_type_concept_id", IntegerType(), True),
            StructField("note_class_concept_id", IntegerType(), True),
            StructField("note_title", StringType(), True),
            StructField("note_text", StringType(), True),
            StructField("encoding_concept_id", IntegerType(), True),
            StructField("language_concept_id", IntegerType(), True),
            StructField("provider_id", LongType(), True),
            StructField("visit_occurrence_id", LongType(), True),
            StructField("visit_detail_id", LongType(), True),
            StructField("note_source_value", StringType(), True)
        ])

        self.note_nlp = StructType([
            StructField("note_nlp_id", LongType(), False),
            StructField("note_id", LongType(), False),
            StructField("section_concept_id", IntegerType(), True),
            StructField("snippet", StringType(), True),
            StructField("offset", StringType(), True),
            StructField("lexical_variant", StringType(), True),
            StructField("note_nlp_concept_id", IntegerType(), True),
            StructField("nlp_system", StringType(), True),
            StructField("nlp_date", DateType(), True),
            StructField("nlp_datetime", TimestampType(), True),
            StructField("term_exists", StringType(), True),
            StructField("term_temporal", StringType(), True),
            StructField("term_modifiers", StringType(), True),
            StructField("note_nlp_source_concept_id", IntegerType(), True)
        ])

        self.observation = StructType([
            StructField("observation_id", LongType(), False),
            StructField("person_id", LongType(), False),
            StructField("observation_concept_id", IntegerType(), True),
            StructField("observation_date", DateType(), True),
            StructField("observation_datetime", TimestampType(), True),
            StructField("observation_type_concept_id", IntegerType(), True),
            StructField("value_as_number", FloatType(), True),
            StructField("value_as_string", StringType(), True),
            StructField("value_as_concept_id", IntegerType(), True),
            StructField("qualifier_concept_id", IntegerType(), True),
            StructField("unit_concept_id", IntegerType(), True),
            StructField("provider_id", LongType(), True),
            StructField("visit_occurrence_id", LongType(), True),
            StructField("visit_detail_id", LongType(), True),
            StructField("observation_source_value", StringType(), True),
            StructField("observation_source_concept_id", IntegerType(), True),
            StructField("unit_source_value", StringType(), True),
            StructField("qualifier_source_value", StringType(), True),
            StructField("observation_event_id", LongType(), True), 
            StructField("obs_event_field_concept_id", IntegerType(), True), 
            StructField("value_as_datetime", TimestampType(), True)
        ])

        self.survey_conduct = StructType([
            StructField("survey_conduct_id", LongType(), False),
            StructField("person_id", LongType(), False),
            StructField("survey_concept_id", IntegerType(), True),
            StructField("survey_start_date", DateType(), True),
            StructField("survey_start_datetime", TimestampType(), True),
            StructField("survey_end_date", DateType(), True),
            StructField("survey_end_datetime", TimestampType(), True),
            StructField("provider_id", LongType(), True),
            StructField("assisted_concept_id", IntegerType(), True),
            StructField("respondent_type_concept_id", IntegerType(), True),
            StructField("timing_concept_id", IntegerType(), True),
            StructField("collection_method_concept_id", IntegerType(), True),
            StructField("assisted_source_value", StringType(), True),
            StructField("respondent_type_source_value", StringType(), True),
            StructField("timing_source_value", StringType(), True),
            StructField("collection_method_source_value", StringType(), True),
            StructField("survey_source_value", StringType(), True),
            StructField("survey_source_concept_id", IntegerType(), True),
            StructField("survey_source_identifier", StringType(), True),
            StructField("validated_survey_concept_id", IntegerType(), True),
            StructField("validated_survey_source_value", StringType(), True),
            StructField("survey_version_number", StringType(), True),
            StructField("visit_occurrence_id", LongType(), True),
            StructField("visit_detail_id", LongType(), True),
            StructField("response_visit_occurrence_id", LongType(), True)
        ])

        self.fact_relationship = StructType([
            StructField("domain_concept_id_1", IntegerType(), False),
            StructField("fact_id_1", LongType(), False),
            StructField("domain_concept_id_2", IntegerType(), False),
            StructField("fact_id_2", LongType(), False),
            StructField("relationship_concept_id", IntegerType(), False)
        ])

        self.location = StructType([
            StructField("location_id", LongType(), False),
            StructField("address_1", StringType(), True),
            StructField("address_2", StringType(), True),
            StructField("city", StringType(), True),
            StructField("state", StringType(), True),
            StructField("zip", StringType(), True),
            StructField("county", StringType(), True),
            StructField("country", StringType(), True),
            StructField("location_source_value", StringType(), True),
            StructField("latitude", FloatType(), True),
            StructField("longitude", FloatType(), True)
        ])

        self.location_history = StructType([
            StructField("location_history_id", LongType(), False),
            StructField("location_id", LongType(), True),
            StructField("relationship_type_concept_id", IntegerType(), True), 
            StructField("domain_id", StringType(), True),
            StructField("entity_id", LongType(), True),
            StructField("start_date", DateType(), True),
            StructField("end_date", DateType(), True)
        ])

        self.care_site = StructType([
            StructField("care_site_id", LongType(), False),
            StructField("care_site_name", StringType(), True),
            StructField("place_of_service_concept_id", IntegerType(), True),
            StructField("location_id", LongType(), True),
            StructField("care_site_source_value", StringType(), True),
            StructField("place_of_service_source_value", StringType(), True)
        ])

        self.provider = StructType([
            StructField("provider_id", LongType(), False),
            StructField("provider_name", StringType(), True),
            StructField("NPI", StringType(), True),
            StructField("DEA", StringType(), True),
            StructField("specialty_concept_id", IntegerType(), True),
            StructField("care_site_id", LongType(), True),
            StructField("year_of_birth", IntegerType(), True),
            StructField("gender_concept_id", IntegerType(), True),
            StructField("provider_source_value", StringType(), True),
            StructField("specialty_source_value", StringType(), True),
            StructField("specialty_source_concept_id", IntegerType(), True),
            StructField("gender_source_value", StringType(), True),
            StructField("gender_source_concept_id", IntegerType(), True)
        ])

        self.payer_plan_period = StructType([
            StructField("payer_plan_period_id", LongType(), False),
            StructField("person_id", LongType(), False),
            StructField("contract_person_id", LongType(), True),
            StructField("payer_plan_period_start_date", DateType(), True),
            StructField("payer_plan_period_end_date", DateType(), True),
            StructField("payer_concept_id", IntegerType(), True),
            StructField("plan_concept_id", IntegerType(), True),
            StructField("contract_concept_id", IntegerType(), True),
            StructField("sponsor_concept_id", IntegerType(), True),
            StructField("stop_reason_concept_id", IntegerType(), True),
            StructField("payer_source_value", StringType(), True),
            StructField("payer_source_concept_id", IntegerType(), True),
            StructField("plan_source_value", StringType(), True),
            StructField("plan_source_concept_id", IntegerType(), True),
            StructField("contract_source_value", StringType(), True),
            StructField("contract_source_concept_id", IntegerType(), True),
            StructField("sponsor_source_value", StringType(), True),
            StructField("sponsor_source_concept_id", IntegerType(), True),
            StructField("family_source_value", StringType(), True),
            StructField("stop_reason_source_value", StringType(), True),
            StructField("stop_reason_source_concept_id", IntegerType(), True)
        ])

        self.cost = StructType([
            StructField("cost_id", LongType(), False),
            StructField("person_id", LongType(), False),
            StructField("cost_event_id", LongType(), True),
            StructField("cost_event_field_concept_id", IntegerType(), True), 
            StructField("cost_concept_id", IntegerType(), True),
            StructField("cost_type_concept_id", IntegerType(), True),
            StructField("currency_concept_id", IntegerType(), True),
            StructField("cost", FloatType(), True),
            StructField("incurred_date", DateType(), True),
            StructField("billed_date", DateType(), True),
            StructField("paid_date", DateType(), True),
            StructField("revenue_code_concept_id", IntegerType(), True),
            StructField("drg_concept_id", IntegerType(), True),
            StructField("cost_source_value", StringType(), True),
            StructField("cost_source_concept_id", IntegerType(), True),
            StructField("revenue_code_source_value", StringType(), True),
            StructField("drg_source_value", StringType(), True),
            StructField("payer_plan_period_id", LongType(), True)
        ])

        self.drug_era = StructType([
            StructField("drug_era_id", LongType(), False),
            StructField("person_id", LongType(), False),
            StructField("drug_concept_id", IntegerType(), True),
            StructField("drug_era_start_datetime", TimestampType(), True),
            StructField("drug_era_end_datetime", TimestampType(), True),
            StructField("drug_exposure_count", IntegerType(), True),
            StructField("gap_days", IntegerType(), True)
        ])

        self.dose_era = StructType([
            StructField("dose_era_id", LongType(), False),
            StructField("person_id", LongType(), False),
            StructField("drug_concept_id", IntegerType(), True),
            StructField("unit_concept_id", IntegerType(), True),
            StructField("dose_value", FloatType(), True),
            StructField("dose_era_start_datetime", TimestampType(), True),
            StructField("dose_era_end_datetime", TimestampType(), True)
        ])

        self.condition_era = StructType([
            StructField("condition_era_id", LongType(), False),
            StructField("person_id", LongType(), False),
            StructField("condition_concept_id", IntegerType(), True),
            StructField("condition_era_start_datetime", TimestampType(), True),
            StructField("condition_era_end_datetime", TimestampType(), True),
            StructField("condition_occurrence_count", IntegerType(), True)
        ])
