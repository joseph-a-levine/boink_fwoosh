"""
Python model "wrld3-03+.py"
Translated using PySD version 0.9.0
"""
from __future__ import division
import numpy as np
from pysd import utils
import xarray as xr

from pysd.py_backend.functions import cache
from pysd.py_backend import functions

_subscript_dict = {}

_namespace = {
    'TIME':
    'time',
    'Time':
    'time',
    'GDP pc unit':
    'gdp_pc_unit',
    'unit agricultural input':
    'unit_agricultural_input',
    'unit population':
    'unit_population',
    '"Absorption Land (GHA)"':
    'absorption_land_gha',
    '"Arable Land in Gigahectares (GHA)"':
    'arable_land_in_gigahectares_gha',
    'Education Index':
    'education_index',
    'Education Index LOOKUP':
    'education_index_lookup',
    'GDP Index':
    'gdp_index',
    'GDP per capita':
    'gdp_per_capita',
    'GDP per capita LOOKUP':
    'gdp_per_capita_lookup',
    'ha per Gha':
    'ha_per_gha',
    'ha per unit of pollution':
    'ha_per_unit_of_pollution',
    'Human Ecological Footprint':
    'human_ecological_footprint',
    'Human Welfare Index':
    'human_welfare_index',
    'Life Expectancy Index':
    'life_expectancy_index',
    'Life Expectancy Index LOOKUP':
    'life_expectancy_index_lookup',
    'one year':
    'one_year',
    'Ref Hi GDP':
    'ref_hi_gdp',
    'Ref Lo GDP':
    'ref_lo_gdp',
    'Total Land':
    'total_land',
    '"Urban Land (GHA)"':
    'urban_land_gha',
    'Arable Land':
    'arable_land',
    'initial arable land':
    'initial_arable_land',
    'development cost per hectare':
    'development_cost_per_hectare',
    'development cost per hectare table':
    'development_cost_per_hectare_table',
    'food':
    'food',
    'food per capita':
    'food_per_capita',
    'land development rate':
    'land_development_rate',
    'land fr cult':
    'land_fr_cult',
    'land fraction harvested':
    'land_fraction_harvested',
    'fraction of industrial output allocated to agriculture 1':
    'fraction_of_industrial_output_allocated_to_agriculture_1',
    'fraction industrial output allocated to agriculture table 1':
    'fraction_industrial_output_allocated_to_agriculture_table_1',
    'fraction of industrial output allocated to agriculture 2':
    'fraction_of_industrial_output_allocated_to_agriculture_2',
    'fraction industrial output allocated to agriculture table 2':
    'fraction_industrial_output_allocated_to_agriculture_table_2',
    'indicated food per capita 1':
    'indicated_food_per_capita_1',
    'indicated food per capita table 1':
    'indicated_food_per_capita_table_1',
    'indicated food per capita 2':
    'indicated_food_per_capita_2',
    'indicated food per capita table 2':
    'indicated_food_per_capita_table_2',
    'Potentially Arable Land':
    'potentially_arable_land',
    'initial potentially arable land':
    'initial_potentially_arable_land',
    'potentially arable land total':
    'potentially_arable_land_total',
    'processing loss':
    'processing_loss',
    'fraction of industrial output allocated to agriculture':
    'fraction_of_industrial_output_allocated_to_agriculture',
    'indicated food per capita':
    'indicated_food_per_capita',
    'total agricultural investment':
    'total_agricultural_investment',
    'Agricultural Inputs':
    'agricultural_inputs',
    'average life agricultural inputs':
    'average_life_agricultural_inputs',
    'agricultural input per hectare':
    'agricultural_input_per_hectare',
    'current agricultural inputs':
    'current_agricultural_inputs',
    'desired food ratio':
    'desired_food_ratio',
    'IND OUT IN 1970':
    'ind_out_in_1970',
    'land yield':
    'land_yield',
    'land yield multiplier from capital':
    'land_yield_multiplier_from_capital',
    'land yield multiplier from capital table':
    'land_yield_multiplier_from_capital_table',
    'average life of agricultural inputs 1':
    'average_life_of_agricultural_inputs_1',
    'average life of agricultural inputs 2':
    'average_life_of_agricultural_inputs_2',
    'land yield factor 1':
    'land_yield_factor_1',
    'land yield factor 2':
    'land_yield_factor_2',
    'land yield multipler from air pollution 1':
    'land_yield_multipler_from_air_pollution_1',
    'land yield multipler from air pollution table 1':
    'land_yield_multipler_from_air_pollution_table_1',
    'land yield multiplier from air pollution 2':
    'land_yield_multiplier_from_air_pollution_2',
    'land yield multipler from air pollution table 2':
    'land_yield_multipler_from_air_pollution_table_2',
    'land yield technology change rate multiplier':
    'land_yield_technology_change_rate_multiplier',
    'land yield technology change rate multiplier table':
    'land_yield_technology_change_rate_multiplier_table',
    'land yield multiplier from technology':
    'land_yield_multiplier_from_technology',
    'land yield multiplier from air pollution':
    'land_yield_multiplier_from_air_pollution',
    'air pollution policy implementation time':
    'air_pollution_policy_implementation_time',
    'Land Yield Technology':
    'land_yield_technology',
    'land yield technology change rate':
    'land_yield_technology_change_rate',
    'average life of land':
    'average_life_of_land',
    'average life of land normal':
    'average_life_of_land_normal',
    'land erosion rate':
    'land_erosion_rate',
    'land removal for urban and industrial use':
    'land_removal_for_urban_and_industrial_use',
    'land life multiplier from land yield 1':
    'land_life_multiplier_from_land_yield_1',
    'land life multiplier from land yield table 1':
    'land_life_multiplier_from_land_yield_table_1',
    'land life multiplier from land yield 2':
    'land_life_multiplier_from_land_yield_2',
    'land life multiplier from land yield table 2':
    'land_life_multiplier_from_land_yield_table_2',
    'land life multiplier from land yield':
    'land_life_multiplier_from_land_yield',
    'land life policy implementation time':
    'land_life_policy_implementation_time',
    'urban and industrial land development time':
    'urban_and_industrial_land_development_time',
    'urban and industrial land required per capita':
    'urban_and_industrial_land_required_per_capita',
    'urban and industrial land required per capita table':
    'urban_and_industrial_land_required_per_capita_table',
    'urban and industrial land required':
    'urban_and_industrial_land_required',
    'Urban and Industrial Land':
    'urban_and_industrial_land',
    'initial urban and industrial land':
    'initial_urban_and_industrial_land',
    'land fertility degredation':
    'land_fertility_degredation',
    'land fertility degredation rate':
    'land_fertility_degredation_rate',
    'land fertility degredation rate table':
    'land_fertility_degredation_rate_table',
    'Land Fertility':
    'land_fertility',
    'initial land fertility':
    'initial_land_fertility',
    'inherent land fertility':
    'inherent_land_fertility',
    'land fertility regeneration':
    'land_fertility_regeneration',
    'land fertility regeneration time':
    'land_fertility_regeneration_time',
    'land fertility regeneration time table':
    'land_fertility_regeneration_time_table',
    'Perceived Food Ratio':
    'perceived_food_ratio',
    'food ratio':
    'food_ratio',
    'food shortage perception delay':
    'food_shortage_perception_delay',
    'fraction of agricultural inputs for land maintenance':
    'fraction_of_agricultural_inputs_for_land_maintenance',
    'fraction of agricultural inputs for land maintenance table':
    'fraction_of_agricultural_inputs_for_land_maintenance_table',
    'subsistence food per capita':
    'subsistence_food_per_capita',
    'fraction of agricultural inputs allocated to land development':
    'fraction_of_agricultural_inputs_allocated_to_land_development',
    'fraction of agricultural inputs allocated to land development table':
    'fraction_of_agricultural_inputs_allocated_to_land_development_table',
    'marginal land yield multiplier from capital':
    'marginal_land_yield_multiplier_from_capital',
    'marginal land yield multiplier from capital table':
    'marginal_land_yield_multiplier_from_capital_table',
    'marginal productivity of agricultural inputs':
    'marginal_productivity_of_agricultural_inputs',
    'marginal productivity of land development':
    'marginal_productivity_of_land_development',
    'social discount':
    'social_discount',
    'industrial capital output ratio multiplier from resource conservation technology':
    'industrial_capital_output_ratio_multiplier_from_resource_conservation_technology',
    'industrial capital output ratio multiplier from pollution technology':
    'industrial_capital_output_ratio_multiplier_from_pollution_technology',
    'industrial capital output ratio multiplier from land yield technology':
    'industrial_capital_output_ratio_multiplier_from_land_yield_technology',
    'fraction of industrial output allocated to investment':
    'fraction_of_industrial_output_allocated_to_investment',
    'industrial capital depreciation':
    'industrial_capital_depreciation',
    'industrial capital investment':
    'industrial_capital_investment',
    'industrial capital output ratio multiplier from resource table':
    'industrial_capital_output_ratio_multiplier_from_resource_table',
    'industrial output per capita':
    'industrial_output_per_capita',
    'industrial output per capita desired':
    'industrial_output_per_capita_desired',
    'Industrial Capital':
    'industrial_capital',
    'initial industrial capital':
    'initial_industrial_capital',
    'industrial output':
    'industrial_output',
    'average life of industrial capital 1':
    'average_life_of_industrial_capital_1',
    'average life of industrial capital 2':
    'average_life_of_industrial_capital_2',
    'fraction of industrial output allocated to consumption constant':
    'fraction_of_industrial_output_allocated_to_consumption_constant',
    'fraction of industrial output allocated to consumption constant 1':
    'fraction_of_industrial_output_allocated_to_consumption_constant_1',
    'fraction of industrial output allocated to consumption constant 2':
    'fraction_of_industrial_output_allocated_to_consumption_constant_2',
    'fraction of industrial output allocated to consumption variable':
    'fraction_of_industrial_output_allocated_to_consumption_variable',
    'fraction of industrial output allocated to consumption variable table':
    'fraction_of_industrial_output_allocated_to_consumption_variable_table',
    'industrial capital output ratio 1':
    'industrial_capital_output_ratio_1',
    'industrial capital output ratio 2':
    'industrial_capital_output_ratio_2',
    'industrial capital output ratio multiplier from pollution table':
    'industrial_capital_output_ratio_multiplier_from_pollution_table',
    'average life of industrial capital':
    'average_life_of_industrial_capital',
    'fraction of industrial output allocated to consumption':
    'fraction_of_industrial_output_allocated_to_consumption',
    'industrial capital output ratio':
    'industrial_capital_output_ratio',
    'industrial equilibrium time':
    'industrial_equilibrium_time',
    'industrial capital output ratio multiplier table':
    'industrial_capital_output_ratio_multiplier_table',
    'Delayed Labor Utilization Fraction':
    'delayed_labor_utilization_fraction',
    'capacity utilization fraction':
    'capacity_utilization_fraction',
    'capacity utilization fraction table':
    'capacity_utilization_fraction_table',
    'jobs':
    'jobs',
    'jobs per hectare':
    'jobs_per_hectare',
    'jobs per hectare table':
    'jobs_per_hectare_table',
    'jobs per industrial capital unit':
    'jobs_per_industrial_capital_unit',
    'jobs per industrial capital unit table':
    'jobs_per_industrial_capital_unit_table',
    'jobs per service capital unit':
    'jobs_per_service_capital_unit',
    'jobs per service capital unit table':
    'jobs_per_service_capital_unit_table',
    'labor force':
    'labor_force',
    'labor force participation fraction':
    'labor_force_participation_fraction',
    'labor utilization fraction':
    'labor_utilization_fraction',
    'labor utilization fraction delay time':
    'labor_utilization_fraction_delay_time',
    'potential jobs agricultural sector':
    'potential_jobs_agricultural_sector',
    'potential jobs industrial sector':
    'potential_jobs_industrial_sector',
    'potential jobs service sector':
    'potential_jobs_service_sector',
    'average life of service capital 1':
    'average_life_of_service_capital_1',
    'average life of service capital 2':
    'average_life_of_service_capital_2',
    'fraction of industrial output allocated to services 1':
    'fraction_of_industrial_output_allocated_to_services_1',
    'fraction of industrial output allocated to services table 1':
    'fraction_of_industrial_output_allocated_to_services_table_1',
    'fraction of industrial output allocated to services 2':
    'fraction_of_industrial_output_allocated_to_services_2',
    'fraction of industrial output allocated to services table 2':
    'fraction_of_industrial_output_allocated_to_services_table_2',
    'indicated services output per capita 1':
    'indicated_services_output_per_capita_1',
    'indicated services output per capita table 1':
    'indicated_services_output_per_capita_table_1',
    'indicated services output per capita 2':
    'indicated_services_output_per_capita_2',
    'indicated services output per capita table 2':
    'indicated_services_output_per_capita_table_2',
    'service capital output ratio 1':
    'service_capital_output_ratio_1',
    'service capital output ratio 2':
    'service_capital_output_ratio_2',
    'average life of service capital':
    'average_life_of_service_capital',
    'fraction of industrial output allocated to services':
    'fraction_of_industrial_output_allocated_to_services',
    'indicated services output per capita':
    'indicated_services_output_per_capita',
    'service capital output ratio':
    'service_capital_output_ratio',
    'service capital depreciation':
    'service_capital_depreciation',
    'service capital investment':
    'service_capital_investment',
    'service output per capita':
    'service_output_per_capita',
    'Service Capital':
    'service_capital',
    'initial service capital':
    'initial_service_capital',
    'service output':
    'service_output',
    'FINAL TIME':
    'final_time',
    'INITIAL TIME':
    'initial_time',
    'SAVEPER':
    'saveper',
    'POLICY YEAR':
    'policy_year',
    'TIME STEP':
    'time_step',
    'agricultural material toxicity index':
    'agricultural_material_toxicity_index',
    'assimilation half life':
    'assimilation_half_life',
    'assimilation half life in 1970':
    'assimilation_half_life_in_1970',
    'assimilation half life multiplier':
    'assimilation_half_life_multiplier',
    'assimilation half life mult table':
    'assimilation_half_life_mult_table',
    'desired persistent pollution index':
    'desired_persistent_pollution_index',
    'fraction of agricultural inputs from persistent materials':
    'fraction_of_agricultural_inputs_from_persistent_materials',
    'fraction of resources from persistent materials':
    'fraction_of_resources_from_persistent_materials',
    'industrial material toxicity index':
    'industrial_material_toxicity_index',
    'industrial material emissions factor':
    'industrial_material_emissions_factor',
    'persistent pollution generation factor 1':
    'persistent_pollution_generation_factor_1',
    'persistent pollution generation factor 2':
    'persistent_pollution_generation_factor_2',
    'persistent pollution technology change multiplier':
    'persistent_pollution_technology_change_multiplier',
    'persistent pollution technology change mult table':
    'persistent_pollution_technology_change_mult_table',
    'Persistent Pollution':
    'persistent_pollution',
    'initial persistent pollution':
    'initial_persistent_pollution',
    'persistent pollution generation industry':
    'persistent_pollution_generation_industry',
    'persistent pollution generation agriculture':
    'persistent_pollution_generation_agriculture',
    'persistent pollution generation rate':
    'persistent_pollution_generation_rate',
    'persistent pollution appearance rate':
    'persistent_pollution_appearance_rate',
    'persistent pollution assimilation rate':
    'persistent_pollution_assimilation_rate',
    'persistent pollution in 1970':
    'persistent_pollution_in_1970',
    'persistent pollution index':
    'persistent_pollution_index',
    'Persistent Pollution Technology':
    'persistent_pollution_technology',
    'persistent pollution technology change rate':
    'persistent_pollution_technology_change_rate',
    'persistent pollution transmission delay':
    'persistent_pollution_transmission_delay',
    'persistent pollution generation factor':
    'persistent_pollution_generation_factor',
    'deaths 0 to 14':
    'deaths_0_to_14',
    'deaths 15 to 44':
    'deaths_15_to_44',
    'deaths 45 to 64':
    'deaths_45_to_64',
    'deaths 65 plus':
    'deaths_65_plus',
    'maturation 14 to 15':
    'maturation_14_to_15',
    'maturation 44 to 45':
    'maturation_44_to_45',
    'maturation 64 to 65':
    'maturation_64_to_65',
    'mortality 45 to 64':
    'mortality_45_to_64',
    'mortality 45 to 64 table':
    'mortality_45_to_64_table',
    'mortality 65 plus':
    'mortality_65_plus',
    'mortality 65 plus table':
    'mortality_65_plus_table',
    'mortality 0 to 14':
    'mortality_0_to_14',
    'mortality 0 to 14 table':
    'mortality_0_to_14_table',
    'mortality 15 to 44':
    'mortality_15_to_44',
    'mortality 15 to 44 table':
    'mortality_15_to_44_table',
    'Population 0 To 14':
    'population_0_to_14',
    'initial population 0 to 14':
    'initial_population_0_to_14',
    'Population 15 To 44':
    'population_15_to_44',
    'initial population 15 to 44':
    'initial_population_15_to_44',
    'Population 45 To 64':
    'population_45_to_64',
    'initial population 54 to 64':
    'initial_population_54_to_64',
    'Population 65 Plus':
    'population_65_plus',
    'initial population 65 plus':
    'initial_population_65_plus',
    'population':
    'population',
    'average industrial output per capita':
    'average_industrial_output_per_capita',
    'birth rate':
    'birth_rate',
    'births':
    'births',
    'completed multiplier from perceived lifetime':
    'completed_multiplier_from_perceived_lifetime',
    'completed multiplier from perceived lifetime table':
    'completed_multiplier_from_perceived_lifetime_table',
    'delayed industrial output per capita':
    'delayed_industrial_output_per_capita',
    'desired completed family size':
    'desired_completed_family_size',
    'desired completed family size normal':
    'desired_completed_family_size_normal',
    'desired total fertility':
    'desired_total_fertility',
    'family income expectation':
    'family_income_expectation',
    'family response to social norm':
    'family_response_to_social_norm',
    'family response to social norm table':
    'family_response_to_social_norm_table',
    'fecundity multiplier':
    'fecundity_multiplier',
    'fecundity multiplier table':
    'fecundity_multiplier_table',
    'fertility control allocation per capita':
    'fertility_control_allocation_per_capita',
    'fertility control effectiveness':
    'fertility_control_effectiveness',
    'fertility control effectiveness table':
    'fertility_control_effectiveness_table',
    'fertility control facilities per capita':
    'fertility_control_facilities_per_capita',
    'fraction services allocated to fertility control':
    'fraction_services_allocated_to_fertility_control',
    'fraction services allocated to fertility control table':
    'fraction_services_allocated_to_fertility_control_table',
    'income expectation averaging time':
    'income_expectation_averaging_time',
    'lifetime perception delay':
    'lifetime_perception_delay',
    'maximum total fertility':
    'maximum_total_fertility',
    'maximum total fertility normal':
    'maximum_total_fertility_normal',
    'need for fertility control':
    'need_for_fertility_control',
    'perceived life expectancy':
    'perceived_life_expectancy',
    'reproductive lifetime':
    'reproductive_lifetime',
    'social family size normal':
    'social_family_size_normal',
    'social family size normal table':
    'social_family_size_normal_table',
    'social adjustment delay':
    'social_adjustment_delay',
    'fertility control effectiveness time':
    'fertility_control_effectiveness_time',
    'population equilibrium time':
    'population_equilibrium_time',
    'zero population growth time':
    'zero_population_growth_time',
    'THOUSAND':
    'thousand',
    'total fertility':
    'total_fertility',
    'crowding multiplier from industry':
    'crowding_multiplier_from_industry',
    'crowding multiplier from industry table':
    'crowding_multiplier_from_industry_table',
    'death rate':
    'death_rate',
    'deaths':
    'deaths',
    'effective health services per capita':
    'effective_health_services_per_capita',
    'fraction of population urban':
    'fraction_of_population_urban',
    'fraction of population urban table':
    'fraction_of_population_urban_table',
    'health services per capita':
    'health_services_per_capita',
    'health services per capita table':
    'health_services_per_capita_table',
    'health services impact delay':
    'health_services_impact_delay',
    'life expectancy normal':
    'life_expectancy_normal',
    'life expectancy':
    'life_expectancy',
    'lifetime multiplier from crowding':
    'lifetime_multiplier_from_crowding',
    'lifetime multiplier from food':
    'lifetime_multiplier_from_food',
    'lifetime multiplier from food table':
    'lifetime_multiplier_from_food_table',
    'lifetime multiplier from health services':
    'lifetime_multiplier_from_health_services',
    'lifetime multiplier from health services 1':
    'lifetime_multiplier_from_health_services_1',
    'lifetime multiplier from health services 1 table':
    'lifetime_multiplier_from_health_services_1_table',
    'lifetime multiplier from health services 2':
    'lifetime_multiplier_from_health_services_2',
    'lifetime multiplier from health services 2 table':
    'lifetime_multiplier_from_health_services_2_table',
    'lifetime multiplier from persistent pollution':
    'lifetime_multiplier_from_persistent_pollution',
    'lifetime multiplier from persistent pollution table':
    'lifetime_multiplier_from_persistent_pollution_table',
    'desired resource use rate':
    'desired_resource_use_rate',
    'fraction of resources remaining':
    'fraction_of_resources_remaining',
    'resource usage rate':
    'resource_usage_rate',
    'initial nonrenewable resources':
    'initial_nonrenewable_resources',
    'Nonrenewable Resources':
    'nonrenewable_resources',
    'fraction of capital allocated to obtaining resources 1':
    'fraction_of_capital_allocated_to_obtaining_resources_1',
    'fraction of capital allocated to obtaining resources 1 table':
    'fraction_of_capital_allocated_to_obtaining_resources_1_table',
    'fraction of capital allocated to obtaining resources 2':
    'fraction_of_capital_allocated_to_obtaining_resources_2',
    'fraction of capital allocated to obtaining resources 2 table':
    'fraction_of_capital_allocated_to_obtaining_resources_2_table',
    'resource use factor 1':
    'resource_use_factor_1',
    'resource use fact 2':
    'resource_use_fact_2',
    'resource technology change rate multiplier':
    'resource_technology_change_rate_multiplier',
    'resource technology change mult table':
    'resource_technology_change_mult_table',
    'per capita resource use multiplier':
    'per_capita_resource_use_multiplier',
    'per capita resource use mult table':
    'per_capita_resource_use_mult_table',
    'Resource Conservation Technology':
    'resource_conservation_technology',
    'resource technology change rate':
    'resource_technology_change_rate',
    'fraction of industrial capital allocated to obtaining resources':
    'fraction_of_industrial_capital_allocated_to_obtaining_resources',
    'resource use factor':
    'resource_use_factor',
    'fraction of industrial capital allocated to obtaining resources switch time':
    'fraction_of_industrial_capital_allocated_to_obtaining_resources_switch_time',
    'technology development delay':
    'technology_development_delay',
    'consumed industrial output':
    'consumed_industrial_output',
    'consumed industrial output per capita':
    'consumed_industrial_output_per_capita',
    'fraction of output in agriculture':
    'fraction_of_output_in_agriculture',
    'fraction of output in industry':
    'fraction_of_output_in_industry',
    'fraction of output in services':
    'fraction_of_output_in_services',
    'persistent pollution intensity industry':
    'persistent_pollution_intensity_industry',
    'PRICE OF FOOD':
    'price_of_food',
    'resource use intensity':
    'resource_use_intensity'
}

__pysd_version__ = "0.9.0"


@cache('run')
def gdp_pc_unit():
    """
    Real Name: GDP pc unit
    Original Eqn: 1
    Units: $/Person/year
    Limits: (None, None)
    Type: constant


    """
    return 1


@cache('run')
def unit_agricultural_input():
    """
    Real Name: unit agricultural input
    Original Eqn: 1
    Units: $/hectare/year
    Limits: (None, None)
    Type: constant


    """
    return 1


@cache('run')
def unit_population():
    """
    Real Name: unit population
    Original Eqn: 1
    Units: Person
    Limits: (None, None)
    Type: constant


    """
    return 1


@cache('step')
def absorption_land_gha():
    """
    Real Name: "Absorption Land (GHA)"
    Original Eqn: persistent pollution generation rate*ha per unit of pollution/ha per Gha
    Units: Ghectares
    Limits: (None, None)
    Type: component


    """
    return persistent_pollution_generation_rate() * ha_per_unit_of_pollution() / ha_per_gha()


@cache('step')
def arable_land_in_gigahectares_gha():
    """
    Real Name: "Arable Land in Gigahectares (GHA)"
    Original Eqn: Arable Land/ha per Gha
    Units: Ghectares
    Limits: (None, None)
    Type: component


    """
    return arable_land() / ha_per_gha()


@cache('step')
def education_index():
    """
    Real Name: Education Index
    Original Eqn: Education Index LOOKUP(GDP per capita/GDP pc unit)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return education_index_lookup(gdp_per_capita() / gdp_pc_unit())


def education_index_lookup(x):
    """
    Real Name: Education Index LOOKUP
    Original Eqn: ((0,0),(1000,0.81),(2000,0.88),(3000,0.92),(4000,0.95),(5000,0.98),(6000,0.99),(7000,1))
    Units: Dmnl
    Limits: (None, None)
    Type: lookup


    """
    return functions.lookup(x, [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000],
                            [0, 0.81, 0.88, 0.92, 0.95, 0.98, 0.99, 1])


@cache('step')
def gdp_index():
    """
    Real Name: GDP Index
    Original Eqn: LOG(GDP per capita/Ref Lo GDP,10)/LOG(Ref Hi GDP/Ref Lo GDP,10)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.log(gdp_per_capita() / ref_lo_gdp(), 10) / functions.log(
        ref_hi_gdp() / ref_lo_gdp(), 10)


@cache('step')
def gdp_per_capita():
    """
    Real Name: GDP per capita
    Original Eqn: GDP per capita LOOKUP(industrial output per capita/GDP pc unit)
    Units: $/(year*Person)
    Limits: (None, None)
    Type: component


    """
    return gdp_per_capita_lookup(industrial_output_per_capita() / gdp_pc_unit())


def gdp_per_capita_lookup(x):
    """
    Real Name: GDP per capita LOOKUP
    Original Eqn: ((0,120),(200,600),(400,1200),(600,1800),(800,2500),(1000,3200))
    Units: $/(year*Person)
    Limits: (None, None)
    Type: lookup


    """
    return functions.lookup(x, [0, 200, 400, 600, 800, 1000], [120, 600, 1200, 1800, 2500, 3200])


@cache('run')
def ha_per_gha():
    """
    Real Name: ha per Gha
    Original Eqn: 1e+09
    Units: hectare/Ghectare
    Limits: (None, None)
    Type: constant


    """
    return 1e+09


@cache('run')
def ha_per_unit_of_pollution():
    """
    Real Name: ha per unit of pollution
    Original Eqn: 4
    Units: hectares/(Pollution units/year)
    Limits: (None, None)
    Type: constant


    """
    return 4


@cache('step')
def human_ecological_footprint():
    """
    Real Name: Human Ecological Footprint
    Original Eqn: ("Arable Land in Gigahectares (GHA)"+"Urban Land (GHA)"+"Absorption Land (GHA)" )/Total Land
    Units: Dmnl
    Limits: (None, None)
    Type: component

    See Appendix 2 of Limits to Growth - the 30-Year Update for discussion of
        this index
    """
    return (arable_land_in_gigahectares_gha() + urban_land_gha() +
            absorption_land_gha()) / total_land()


@cache('step')
def human_welfare_index():
    """
    Real Name: Human Welfare Index
    Original Eqn: (Life Expectancy Index+Education Index+GDP Index)/3
    Units: Dmnl
    Limits: (None, None)
    Type: component

    See Appendix 2 of Limits to Growth - the 30-Year Update for discussion of
        this index
    """
    return (life_expectancy_index() + education_index() + gdp_index()) / 3


@cache('step')
def life_expectancy_index():
    """
    Real Name: Life Expectancy Index
    Original Eqn: Life Expectancy Index LOOKUP(life expectancy/one year)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return life_expectancy_index_lookup(life_expectancy() / one_year())


def life_expectancy_index_lookup(x):
    """
    Real Name: Life Expectancy Index LOOKUP
    Original Eqn: ((25,0),(35,0.16),(45,0.33),(55,0.5),(65,0.67),(75,0.84),(85,1))
    Units: Dmnl
    Limits: (None, None)
    Type: lookup


    """
    return functions.lookup(x, [25, 35, 45, 55, 65, 75, 85], [0, 0.16, 0.33, 0.5, 0.67, 0.84, 1])


@cache('run')
def one_year():
    """
    Real Name: one year
    Original Eqn: 1
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 1


@cache('run')
def ref_hi_gdp():
    """
    Real Name: Ref Hi GDP
    Original Eqn: 9508
    Units: $/(year*Person)
    Limits: (None, None)
    Type: constant


    """
    return 9508


@cache('run')
def ref_lo_gdp():
    """
    Real Name: Ref Lo GDP
    Original Eqn: 24
    Units: $/(year*Person)
    Limits: (None, None)
    Type: constant


    """
    return 24


@cache('run')
def total_land():
    """
    Real Name: Total Land
    Original Eqn: 1.91
    Units: Ghectares
    Limits: (None, None)
    Type: constant


    """
    return 1.91


@cache('step')
def urban_land_gha():
    """
    Real Name: "Urban Land (GHA)"
    Original Eqn: Urban and Industrial Land/ha per Gha
    Units: Ghectares
    Limits: (None, None)
    Type: component


    """
    return urban_and_industrial_land() / ha_per_gha()


@cache('step')
def arable_land():
    """
    Real Name: Arable Land
    Original Eqn: INTEG( land development rate - land erosion rate - land removal for urban and industrial use , initial arable land )
    Units: hectare
    Limits: (None, None)
    Type: component

    Arable land (AL#85).
    """
    return integ_arable_land()


@cache('run')
def initial_arable_land():
    """
    Real Name: initial arable land
    Original Eqn: 9e+08
    Units: hectare
    Limits: (None, None)
    Type: constant

    The initial amount of land that is arable.                 (ALI#85.2).
    """
    return 9e+08


@cache('step')
def development_cost_per_hectare():
    """
    Real Name: development cost per hectare
    Original Eqn: development cost per hectare table ( Potentially Arable Land / potentially arable land total )
    Units: $/hectare
    Limits: (None, None)
    Type: component

    Development cost per hectare (DCPH#97).
    """
    return development_cost_per_hectare_table(
        potentially_arable_land() / potentially_arable_land_total())


def development_cost_per_hectare_table(x):
    """
    Real Name: development cost per hectare table
    Original Eqn: ( (0,100000),(0.1,7400),(0.2,5200),(0.3,3500),(0.4,2400),(0.5,1500) ,(0.6,750),(0.7,300),(0.8,150),(0.9,75),(1,50) )
    Units: $/hectare
    Limits: (None, None)
    Type: lookup

    Table relating undeveloped land to the cost of land                 development (DCPHT#97.1).
    """
    return functions.lookup(x, [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
                            [100000, 7400, 5200, 3500, 2400, 1500, 750, 300, 150, 75, 50])


@cache('step')
def food():
    """
    Real Name: food
    Original Eqn: land yield * Arable Land * land fraction harvested * ( 1 - processing loss )
    Units: Veg eq kg/year
    Limits: (None, None)
    Type: component

    The total amount of usable food (F#87).
    """
    return land_yield() * arable_land() * land_fraction_harvested() * (1 - processing_loss())


@cache('step')
def food_per_capita():
    """
    Real Name: food per capita
    Original Eqn: food / population
    Units: Veg eq kg/(Person*year)
    Limits: (None, None)
    Type: component

    Food per capita (FPC#88)
    """
    return food() / population()


@cache('step')
def land_development_rate():
    """
    Real Name: land development rate
    Original Eqn: total agricultural investment * fraction of agricultural inputs allocated to land development / development cost per hectare
    Units: hectare/year
    Limits: (None, None)
    Type: component

    The land developmen rate (LDR#96).
    """
    return total_agricultural_investment(
    ) * fraction_of_agricultural_inputs_allocated_to_land_development(
    ) / development_cost_per_hectare()


@cache('step')
def land_fr_cult():
    """
    Real Name: land fr cult
    Original Eqn: Arable Land / potentially arable land total
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Land fraction under cultivarion (LFC#84).
    """
    return arable_land() / potentially_arable_land_total()


@cache('run')
def land_fraction_harvested():
    """
    Real Name: land fraction harvested
    Original Eqn: 0.7
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Land fraction harvested (LFH#87.1).
    """
    return 0.7


@cache('step')
def fraction_of_industrial_output_allocated_to_agriculture_1():
    """
    Real Name: fraction of industrial output allocated to agriculture 1
    Original Eqn: fraction industrial output allocated to agriculture table 1 ( food per capita\ / indicated food per capita )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Fraction of industrial output allocated to                 agriculture before policy time (FIOAA1#94).
    """
    return fraction_industrial_output_allocated_to_agriculture_table_1(
        food_per_capita() / indicated_food_per_capita())


def fraction_industrial_output_allocated_to_agriculture_table_1(x):
    """
    Real Name: fraction industrial output allocated to agriculture table 1
    Original Eqn: ( (0,0.4),(0.5,0.2),(1,0.1),(1.5,0.025),(2,0),(2.5,0) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating food per capita to the fraction of                industrial output allocated to agriculture                 (FIOAA1T#94.1).
    """
    return functions.lookup(x, [0, 0.5, 1, 1.5, 2, 2.5], [0.4, 0.2, 0.1, 0.025, 0, 0])


@cache('step')
def fraction_of_industrial_output_allocated_to_agriculture_2():
    """
    Real Name: fraction of industrial output allocated to agriculture 2
    Original Eqn: fraction industrial output allocated to agriculture table 2 ( food per capita\ / indicated food per capita )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Fraction of industrial output allocated to                 agriculture after policy time (FIOAA2#95).
    """
    return fraction_industrial_output_allocated_to_agriculture_table_2(
        food_per_capita() / indicated_food_per_capita())


def fraction_industrial_output_allocated_to_agriculture_table_2(x):
    """
    Real Name: fraction industrial output allocated to agriculture table 2
    Original Eqn: ( (0,0.4),(0.5,0.2),(1,0.1),(1.5,0.025),(2,0),(2.5,0) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating food per capita to the fraction of                industrial output allocated to agriculture                 (FIOAA2T#95.1).
    """
    return functions.lookup(x, [0, 0.5, 1, 1.5, 2, 2.5], [0.4, 0.2, 0.1, 0.025, 0, 0])


@cache('step')
def indicated_food_per_capita_1():
    """
    Real Name: indicated food per capita 1
    Original Eqn: indicated food per capita table 1 ( industrial output per capita/GDP pc unit )
    Units: Veg eq kg/(Person*year)
    Limits: (None, None)
    Type: component

    Indicated foord per capita befor policy time                 (IFPC1#90).
    """
    return indicated_food_per_capita_table_1(industrial_output_per_capita() / gdp_pc_unit())


def indicated_food_per_capita_table_1(x):
    """
    Real Name: indicated food per capita table 1
    Original Eqn: ( (0,230),(200,480),(400,690),(600,850),(800,970),(1000,1070) ,(1200,1150),(1400,1210),(1600,1250) )
    Units: Veg eq kg/(Person*year)
    Limits: (None, None)
    Type: lookup

    Table relating industrial output to indicated food                 requirements 1 (IFPC1T#90.1).
    """
    return functions.lookup(x, [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600],
                            [230, 480, 690, 850, 970, 1070, 1150, 1210, 1250])


@cache('step')
def indicated_food_per_capita_2():
    """
    Real Name: indicated food per capita 2
    Original Eqn: indicated food per capita table 2 ( industrial output per capita/GDP pc unit )
    Units: Veg eq kg/(Person*year)
    Limits: (None, None)
    Type: component

    Indicated foord per capita after policy time                 (IFPC1#90).
    """
    return indicated_food_per_capita_table_2(industrial_output_per_capita() / gdp_pc_unit())


def indicated_food_per_capita_table_2(x):
    """
    Real Name: indicated food per capita table 2
    Original Eqn: ( (0,230),(200,480),(400,690),(600,850),(800,970),(1000,1070) ,(1200,1150),(1400,1210),(1600,1250) )
    Units: Veg eq kg/(Person*year)
    Limits: (None, None)
    Type: lookup

    Table relating industrial output to indicated food                 requirements 2 (IFPC2T#90.2).
    """
    return functions.lookup(x, [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600],
                            [230, 480, 690, 850, 970, 1070, 1150, 1210, 1250])


@cache('step')
def potentially_arable_land():
    """
    Real Name: Potentially Arable Land
    Original Eqn: INTEG( ( - land development rate ) , initial potentially arable land )
    Units: hectare
    Limits: (None, None)
    Type: component

    POTENTIALLY ARABLE LAND (PAL#86).
    """
    return integ_potentially_arable_land()


@cache('run')
def initial_potentially_arable_land():
    """
    Real Name: initial potentially arable land
    Original Eqn: 2.3e+09
    Units: hectare
    Limits: (None, None)
    Type: constant

    The initial amount of potentially arable land                 (PALI#86.2).
    """
    return 2.3e+09


@cache('run')
def potentially_arable_land_total():
    """
    Real Name: potentially arable land total
    Original Eqn: 3.2e+09
    Units: hectare
    Limits: (None, None)
    Type: constant

    POTENTIALLY ARABLE LAND TOTAL (PALT#84.1).
    """
    return 3.2e+09


@cache('run')
def processing_loss():
    """
    Real Name: processing loss
    Original Eqn: 0.1
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    PROCESSING LOSS (PL#87.2)
    """
    return 0.1


@cache('step')
def fraction_of_industrial_output_allocated_to_agriculture():
    """
    Real Name: fraction of industrial output allocated to agriculture
    Original Eqn: IF THEN ELSE ( Time >= POLICY YEAR , fraction of industrial output allocated to agriculture 2 , fraction of industrial output allocated to agriculture 1 )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    FRACTION OF INDUSTRIAL OUTPUT ALLOCATED TO                 AGRICULTURE (FIOAA#93).
    """
    return functions.if_then_else(time() >= policy_year(),
                                  fraction_of_industrial_output_allocated_to_agriculture_2(),
                                  fraction_of_industrial_output_allocated_to_agriculture_1())


@cache('step')
def indicated_food_per_capita():
    """
    Real Name: indicated food per capita
    Original Eqn: IF THEN ELSE ( Time >= POLICY YEAR , indicated food per capita 2 , indicated food per capita 1 )
    Units: Veg eq kg/(Person*year)
    Limits: (None, None)
    Type: component

    Indicated food per capita (IFPC#89).
    """
    return functions.if_then_else(time() >= policy_year(), indicated_food_per_capita_2(),
                                  indicated_food_per_capita_1())


@cache('step')
def total_agricultural_investment():
    """
    Real Name: total agricultural investment
    Original Eqn: industrial output * fraction of industrial output allocated to agriculture
    Units: $/year
    Limits: (None, None)
    Type: component

    TOTAL AGRICULTURAL INVESTMENT (TAI#92)
    """
    return industrial_output() * fraction_of_industrial_output_allocated_to_agriculture()


@cache('step')
def agricultural_inputs():
    """
    Real Name: Agricultural Inputs
    Original Eqn: SMOOTH (current agricultural inputs, average life agricultural inputs )
    Units: $/year
    Limits: (None, None)
    Type: component

    AGRICULTURAL INPUTS (AI#99)
    """
    return smooth_current_agricultural_inputs_average_life_agricultural_inputs_current_agricultural_inputs_1(
    )


@cache('step')
def average_life_agricultural_inputs():
    """
    Real Name: average life agricultural inputs
    Original Eqn: IF THEN ELSE ( Time >= POLICY YEAR , average life of agricultural inputs 2 , average life of agricultural inputs 1 )
    Units: year
    Limits: (None, None)
    Type: component

    AVERAGE LIFETIME OF AGRICULTURAL INPUTS (ALAI#100)
    """
    return functions.if_then_else(time() >= policy_year(), average_life_of_agricultural_inputs_2(),
                                  average_life_of_agricultural_inputs_1())


@cache('step')
def agricultural_input_per_hectare():
    """
    Real Name: agricultural input per hectare
    Original Eqn: Agricultural Inputs * ( 1 - fraction of agricultural inputs for land maintenance ) / Arable Land
    Units: $/(year*hectare)
    Limits: (None, None)
    Type: component

    AGRICULTURAL INPUTS PER HECTARE (AIPH#101)
    """
    return agricultural_inputs() * (
        1 - fraction_of_agricultural_inputs_for_land_maintenance()) / arable_land()


@cache('step')
def current_agricultural_inputs():
    """
    Real Name: current agricultural inputs
    Original Eqn: ACTIVE INITIAL( total agricultural investment * ( 1 - fraction of agricultural inputs allocated to land development\ ) , 5e+09)
    Units: $/year
    Limits: (None, None)
    Type: component

    CURRENT AGRICULTURAL INPUTS (CAI#98).
    """
    return functions.active_initial(lambda: total_agricultural_investment()*(1-fraction_of_agricultural_inputs_allocated_to_land_development()), lambda: 5e+09)


@cache('run')
def desired_food_ratio():
    """
    Real Name: desired food ratio
    Original Eqn: 2
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    desired food ratio (DFR#--)
    """
    return 2


@cache('run')
def ind_out_in_1970():
    """
    Real Name: IND OUT IN 1970
    Original Eqn: 7.9e+11
    Units: $/year
    Limits: (None, None)
    Type: constant

    INDUSTRIAL OUTPUT IN 1970 (IO70#107.2)
    """
    return 7.9e+11


@cache('step')
def land_yield():
    """
    Real Name: land yield
    Original Eqn: land yield multiplier from technology * Land Fertility * land yield multiplier from capital * land yield multiplier from air pollution
    Units: Veg eq kg/(year*hectare)
    Limits: (None, None)
    Type: component

    LAND YIELD (LY#103)
    """
    return land_yield_multiplier_from_technology() * land_fertility(
    ) * land_yield_multiplier_from_capital() * land_yield_multiplier_from_air_pollution()


@cache('step')
def land_yield_multiplier_from_capital():
    """
    Real Name: land yield multiplier from capital
    Original Eqn: land yield multiplier from capital table ( agricultural input per hectare/unit agricultural input )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    LAND YIELD MULTIPLIER FROM CAPITAL (LYMC#102)
    """
    return land_yield_multiplier_from_capital_table(
        agricultural_input_per_hectare() / unit_agricultural_input())


def land_yield_multiplier_from_capital_table(x):
    """
    Real Name: land yield multiplier from capital table
    Original Eqn: ( (0,1),(40,3),(80,4.5),(120,5),(160,5.3),(200,5.6),(240,5.9) ,(280,6.1),(320,6.35),(360,6.6),(400,6.9),(440,7.2),(480,7.4) ,(520,7.6),(560,7.8),(600,8),(640,8.2),(680,8.4),(720,8.6) ,(760,8.8),(800,9),(840,9.2),(880,9.4),(920,9.6),(960,9.8) ,(1000,10) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating agricultural inputs to land yeild                 (LYMCT#102.1).
    """
    return functions.lookup(x, [
        0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600, 640, 680, 720,
        760, 800, 840, 880, 920, 960, 1000
    ], [
        1, 3, 4.5, 5, 5.3, 5.6, 5.9, 6.1, 6.35, 6.6, 6.9, 7.2, 7.4, 7.6, 7.8, 8, 8.2, 8.4, 8.6,
        8.8, 9, 9.2, 9.4, 9.6, 9.8, 10
    ])


@cache('run')
def average_life_of_agricultural_inputs_1():
    """
    Real Name: average life of agricultural inputs 1
    Original Eqn: 2
    Units: year
    Limits: (None, None)
    Type: constant

    The average life of agricultural inputs before                 policy time (ALAI1#100.1)
    """
    return 2


@cache('run')
def average_life_of_agricultural_inputs_2():
    """
    Real Name: average life of agricultural inputs 2
    Original Eqn: 2
    Units: year
    Limits: (None, None)
    Type: constant

    The average life of agricultural inputs after policy                 time (ALAI2#100.2)
    """
    return 2.5


@cache('run')
def land_yield_factor_1():
    """
    Real Name: land yield factor 1
    Original Eqn: 1
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Land yield factor before policy year (LYF1#104.1).
    """
    return 1


@cache('step')
def land_yield_factor_2():
    """
    Real Name: land yield factor 2
    Original Eqn: SMOOTH3 ( Land Yield Technology , technology development delay )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Land yield factor after policy year (LYF2#104.2).
    """
    return smooth_land_yield_technology_technology_development_delay_land_yield_technology_3()


@cache('step')
def land_yield_multipler_from_air_pollution_1():
    """
    Real Name: land yield multipler from air pollution 1
    Original Eqn: land yield multipler from air pollution table 1 ( industrial output / IND OUT IN 1970 )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Land yield multiplier from air pollution before air                 poll time (LYMAP1#106).
    """
    return land_yield_multipler_from_air_pollution_table_1(industrial_output() / ind_out_in_1970())


def land_yield_multipler_from_air_pollution_table_1(x):
    """
    Real Name: land yield multipler from air pollution table 1
    Original Eqn: ( (0,1),(10,1),(20,0.7),(30,0.4) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating non-persistent pollution from                 industry to agricultural output (LYMAP1T#106.1).
    """
    return functions.lookup(x, [0, 10, 20, 30], [1, 1, 0.7, 0.4])


@cache('step')
def land_yield_multiplier_from_air_pollution_2():
    """
    Real Name: land yield multiplier from air pollution 2
    Original Eqn: land yield multipler from air pollution table 2 ( industrial output / IND OUT IN 1970 )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Land yield multiplier from air pollution after air                 poll time (LYMAP2#107).
    """
    return land_yield_multipler_from_air_pollution_table_2(industrial_output() / ind_out_in_1970())


def land_yield_multipler_from_air_pollution_table_2(x):
    """
    Real Name: land yield multipler from air pollution table 2
    Original Eqn: ( (0,1),(10,1),(20,0.98),(30,0.95) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating non-persistent pollution from                 industry to agricultural output (LYMAP2T#107.1).
    """
    return functions.lookup(x, [0, 10, 20, 30], [1, 1, 0.98, 0.95])


@cache('step')
def land_yield_technology_change_rate_multiplier():
    """
    Real Name: land yield technology change rate multiplier
    Original Eqn: land yield technology change rate multiplier table ( desired food ratio - food ratio )
    Units: 1/year
    Limits: (None, None)
    Type: component

    Land yield from technology change multiplier                 (LYCM#--)
    """
    return land_yield_technology_change_rate_multiplier_table(desired_food_ratio() - food_ratio())


def land_yield_technology_change_rate_multiplier_table(x):
    """
    Real Name: land yield technology change rate multiplier table
    Original Eqn: ( (0,0),(1,0) )
    Units: 1/year
    Limits: (None, None)
    Type: lookup

    Table relating the food ratio gap to the change in                 agricultural technology (LYCMT#--).
    """
    return functions.lookup(x, [0, 1], [0, 0.04])


@cache('step')
def land_yield_multiplier_from_technology():
    """
    Real Name: land yield multiplier from technology
    Original Eqn: IF THEN ELSE ( Time >= POLICY YEAR , land yield factor 2 , land yield factor 1 )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Land Yield factor (LYF#104)
    """
    return functions.if_then_else(time() >= policy_year(), land_yield_factor_2(),
                                  land_yield_factor_1())


@cache('step')
def land_yield_multiplier_from_air_pollution():
    """
    Real Name: land yield multiplier from air pollution
    Original Eqn: IF THEN ELSE ( Time >= air pollution policy implementation time , land yield multiplier from air pollution 2 , land yield multipler from air pollution 1 )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Land yield multiplier from air pollution                 (LYMAP#105).
    """
    return functions.if_then_else(time() >= air_pollution_policy_implementation_time(),
                                  land_yield_multiplier_from_air_pollution_2(),
                                  land_yield_multipler_from_air_pollution_1())


@cache('run')
def air_pollution_policy_implementation_time():
    """
    Real Name: air pollution policy implementation time
    Original Eqn: 4000
    Units: year
    Limits: (None, None)
    Type: constant

    Air Pollution switch time (ARPTM#--)
    """
    return 4000


@cache('step')
def land_yield_technology():
    """
    Real Name: Land Yield Technology
    Original Eqn: INTEG ( land yield technology change rate , 1)
    Units: Dmnl
    Limits: (None, None)
    Type: component

    LAND YIELD TECHNOLOGY INITIATED (LYTD#--)
    """
    return integ_land_yield_technology()


@cache('step')
def land_yield_technology_change_rate():
    """
    Real Name: land yield technology change rate
    Original Eqn: IF THEN ELSE ( Time >= POLICY YEAR , Land Yield Technology * land yield technology change rate multiplier , 0)
    Units: 1/year
    Limits: (None, None)
    Type: component

    Land yield from technology change rate (LYTDR#--)
    """
    return functions.if_then_else(
        time() >= policy_year(),
        land_yield_technology() * land_yield_technology_change_rate_multiplier(), 0)


@cache('step')
def average_life_of_land():
    """
    Real Name: average life of land
    Original Eqn: average life of land normal * land life multiplier from land yield
    Units: year
    Limits: (None, None)
    Type: component

    Average life of land (ALL#112).
    """
    return average_life_of_land_normal() * land_life_multiplier_from_land_yield()


@cache('run')
def average_life_of_land_normal():
    """
    Real Name: average life of land normal
    Original Eqn: 1000
    Units: year
    Limits: (None, None)
    Type: constant

    AVERAGE LIFE OF LAND NORMAL (ALLN#112.1).
    """
    return 1000


@cache('step')
def land_erosion_rate():
    """
    Real Name: land erosion rate
    Original Eqn: Arable Land / average life of land
    Units: hectare/year
    Limits: (None, None)
    Type: component

    Land erosion rate (LER#
    """
    return arable_land() / average_life_of_land()


@cache('step')
def land_removal_for_urban_and_industrial_use():
    """
    Real Name: land removal for urban and industrial use
    Original Eqn: MAX(0, urban and industrial land required - Urban and Industrial Land ) / urban and industrial land development time
    Units: hectare/year
    Limits: (None, None)
    Type: component

    LAND REMOVAL FOR URBAN-INDUSTRIAL USE (LRUI#119).
    """
    return np.maximum(0,
                      urban_and_industrial_land_required() -
                      urban_and_industrial_land()) / urban_and_industrial_land_development_time()


@cache('step')
def land_life_multiplier_from_land_yield_1():
    """
    Real Name: land life multiplier from land yield 1
    Original Eqn: land life multiplier from land yield table 1 ( land yield / inherent land fertility )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Land life multiplier from yield before switch time                 (LLMY1#114).
    """
    return land_life_multiplier_from_land_yield_table_1(land_yield() / inherent_land_fertility())


def land_life_multiplier_from_land_yield_table_1(x):
    """
    Real Name: land life multiplier from land yield table 1
    Original Eqn: ( (0,1.2),(1,1),(2,0.63),(3,0.36),(4,0.16),(5,0.055),(6,0.04) ,(7,0.025),(8,0.015),(9,0.01) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating yield to the effect on land life                 (LLMY1T#114.1).
    """
    return functions.lookup(x, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1.2, 1, 0.63, 0.36, 0.16, 0.055, 0.04, 0.025, 0.015, 0.01])


@cache('step')
def land_life_multiplier_from_land_yield_2():
    """
    Real Name: land life multiplier from land yield 2
    Original Eqn: land life multiplier from land yield table 2 ( land yield / inherent land fertility )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Land life multiplier from yield after switch time                 (LLMY2#115).
    """
    return land_life_multiplier_from_land_yield_table_2(land_yield() / inherent_land_fertility())


def land_life_multiplier_from_land_yield_table_2(x):
    """
    Real Name: land life multiplier from land yield table 2
    Original Eqn: ( (0,1.2),(1,1),(2,0.63),(3,0.36),(4,0.29),(5,0.26),(6,0.24) ,(7,0.22),(8,0.21),(9,0.2) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating yield to the effect on land life                 (LLMY2T#115.1).
    """
    return functions.lookup(x, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1.2, 1, 0.63, 0.36, 0.29, 0.26, 0.24, 0.22, 0.21, 0.2])


@cache('step')
def land_life_multiplier_from_land_yield():
    """
    Real Name: land life multiplier from land yield
    Original Eqn: IF THEN ELSE ( Time >= land life policy implementation time , ( 0.95 ^ (( Time - land life policy implementation time )/one year ) ) * land life multiplier from land yield 1 + ( 1 - 0.95 ^ (( Time - land life policy implementation time )/one year\ )) * land life multiplier from land yield 2 , land life multiplier from land yield 1 )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    LAND LIFE MULTIPLIER FROM YIELD (LLMY#113).
    """
    return functions.if_then_else(
        time() >= land_life_policy_implementation_time(),
        (0.95**((time() - land_life_policy_implementation_time()) / one_year())) *
        land_life_multiplier_from_land_yield_1() + (1 - 0.95**(
            (time() - land_life_policy_implementation_time()) / one_year())) *
        land_life_multiplier_from_land_yield_2(), land_life_multiplier_from_land_yield_1())


@cache('run')
def land_life_policy_implementation_time():
    """
    Real Name: land life policy implementation time
    Original Eqn: 4000
    Units: year
    Limits: (None, None)
    Type: constant

    Land life multiplier from yield switch time                 (LLMYTM#--)
    """
    return 2002


@cache('run')
def urban_and_industrial_land_development_time():
    """
    Real Name: urban and industrial land development time
    Original Eqn: 10
    Units: year
    Limits: (None, None)
    Type: constant

    Urban industrial land development time                 (UILDT#119.1).
    """
    return 10


@cache('step')
def urban_and_industrial_land_required_per_capita():
    """
    Real Name: urban and industrial land required per capita
    Original Eqn: urban and industrial land required per capita table ( industrial output per capita/GDP pc unit )
    Units: hectare/Person
    Limits: (None, None)
    Type: component

    Urban industrial land per capita (UILPC#117).
    """
    return urban_and_industrial_land_required_per_capita_table(
        industrial_output_per_capita() / gdp_pc_unit())


def urban_and_industrial_land_required_per_capita_table(x):
    """
    Real Name: urban and industrial land required per capita table
    Original Eqn: ( (0,0.005),(200,0.008),(400,0.015),(600,0.025),(800,0.04),(1000,0.055) ,(1200,0.07),(1400,0.08),(1600,0.09) )
    Units: hectare/Person
    Limits: (None, None)
    Type: lookup

    Table relating industrial output to urban industrial                 land (UILPCT#117.1)
    """
    return functions.lookup(x, [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600],
                            [0.005, 0.008, 0.015, 0.025, 0.04, 0.055, 0.07, 0.08, 0.09])


@cache('step')
def urban_and_industrial_land_required():
    """
    Real Name: urban and industrial land required
    Original Eqn: urban and industrial land required per capita * population
    Units: hectare
    Limits: (None, None)
    Type: component

    Urban industrial land required (UILR#118).
    """
    return urban_and_industrial_land_required_per_capita() * population()


@cache('step')
def urban_and_industrial_land():
    """
    Real Name: Urban and Industrial Land
    Original Eqn: INTEG( ( land removal for urban and industrial use ) , initial urban and industrial land )
    Units: hectare
    Limits: (None, None)
    Type: component

    URBAN-INDUSTRIAL LAND (UIL#120).
    """
    return integ_urban_and_industrial_land()


@cache('run')
def initial_urban_and_industrial_land():
    """
    Real Name: initial urban and industrial land
    Original Eqn: 8.2e+06
    Units: hectare
    Limits: (None, None)
    Type: constant

    URBAN-INDUSTRIAL LAND INITIAL (UILI#120.1).
    """
    return 8.2e+06


@cache('step')
def land_fertility_degredation():
    """
    Real Name: land fertility degredation
    Original Eqn: Land Fertility * land fertility degredation rate
    Units: Veg eq kg/(year*year*hectare)
    Limits: (None, None)
    Type: component

    LAND FERTILITY DEGRADATION (LFD#123).
    """
    return land_fertility() * land_fertility_degredation_rate()


@cache('step')
def land_fertility_degredation_rate():
    """
    Real Name: land fertility degredation rate
    Original Eqn: land fertility degredation rate table ( persistent pollution index )
    Units: 1/year
    Limits: (None, None)
    Type: component

    Land fertility degradation rate (LFDR#122).
    """
    return land_fertility_degredation_rate_table(persistent_pollution_index())


def land_fertility_degredation_rate_table(x):
    """
    Real Name: land fertility degredation rate table
    Original Eqn: ( (0,0),(10,0.1),(20,0.3),(30,0.5) )
    Units: 1/year
    Limits: (None, None)
    Type: lookup

    Table relating persistent pollution to land                 fertility degradation (LFDRT#122.1).
    """
    return functions.lookup(x, [0, 10, 20, 30], [0, 0.1, 0.3, 0.5])


@cache('step')
def land_fertility():
    """
    Real Name: Land Fertility
    Original Eqn: INTEG( ( land fertility regeneration - land fertility degredation ) , initial land fertility )
    Units: Veg eq kg/(year*hectare)
    Limits: (None, None)
    Type: component

    Land fertility (LFERT#121).
    """
    return integ_land_fertility()


@cache('run')
def initial_land_fertility():
    """
    Real Name: initial land fertility
    Original Eqn: 600
    Units: Veg eq kg/(year*hectare)
    Limits: (None, None)
    Type: constant

    LAND FERTILITY INITIAL (LFERTI#121.2)
    """
    return 600


@cache('run')
def inherent_land_fertility():
    """
    Real Name: inherent land fertility
    Original Eqn: 600
    Units: Veg eq kg/(year*hectare)
    Limits: (None, None)
    Type: constant

    INHERENT LAND FERTILITY (ILF#124.1).
    """
    return 600


@cache('step')
def land_fertility_regeneration():
    """
    Real Name: land fertility regeneration
    Original Eqn: ( inherent land fertility - Land Fertility ) / land fertility regeneration time
    Units: Veg eq kg/(year*year*hectare)
    Limits: (None, None)
    Type: component

    Land fertility regeneration (LFR#124).
    """
    return (inherent_land_fertility() - land_fertility()) / land_fertility_regeneration_time()


@cache('step')
def land_fertility_regeneration_time():
    """
    Real Name: land fertility regeneration time
    Original Eqn: land fertility regeneration time table ( fraction of agricultural inputs for land maintenance )
    Units: year
    Limits: (None, None)
    Type: component

    LAND FERTILITY REGENERATION TIME (LFRT#125)
    """
    return land_fertility_regeneration_time_table(
        fraction_of_agricultural_inputs_for_land_maintenance())


def land_fertility_regeneration_time_table(x):
    """
    Real Name: land fertility regeneration time table
    Original Eqn: ( (0,20),(0.02,13),(0.04,8),(0.06,4),(0.08,2),(0.1,2) )
    Units: year
    Limits: (None, None)
    Type: lookup

    Table relating inputs to land maintenance to land                 fertility regeneration (LFRTT#125.1).
    """
    return functions.lookup(x, [0, 0.02, 0.04, 0.06, 0.08, 0.1], [20, 13, 8, 4, 2, 2])


@cache('step')
def perceived_food_ratio():
    """
    Real Name: Perceived Food Ratio
    Original Eqn: SMOOTH (food ratio, food shortage perception delay )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    PERCEIVED FOOD RATIO (PFR#128).
    """
    return smooth_food_ratio_food_shortage_perception_delay_food_ratio_1()


@cache('step')
def food_ratio():
    """
    Real Name: food ratio
    Original Eqn: ACTIVE INITIAL( food per capita / subsistence food per capita , 1)
    Units: Dmnl
    Limits: (None, None)
    Type: component

    FOOD RATIO (FR#127)
    """
    return functions.active_initial(lambda: food_per_capita() / subsistence_food_per_capita(),
                                    lambda: 1)


@cache('run')
def food_shortage_perception_delay():
    """
    Real Name: food shortage perception delay
    Original Eqn: 2
    Units: year
    Limits: (None, None)
    Type: constant

    FOOD SHORTAGE PERCEPTION DELAY (FSPD#128.2)
    """
    return 2


@cache('step')
def fraction_of_agricultural_inputs_for_land_maintenance():
    """
    Real Name: fraction of agricultural inputs for land maintenance
    Original Eqn: fraction of agricultural inputs for land maintenance table ( Perceived Food Ratio\ )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    FRACTION OF INPUTS ALLOCATED TO LAND MAINTENANCE                 (FALM#126).
    """
    return fraction_of_agricultural_inputs_for_land_maintenance_table(perceived_food_ratio())


def fraction_of_agricultural_inputs_for_land_maintenance_table(x):
    """
    Real Name: fraction of agricultural inputs for land maintenance table
    Original Eqn: ( (0,0),(1,0.04),(2,0.07),(3,0.09),(4,0.1) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating the perceived food ratio to the                fraction of input used for land maintenance                 (FALMT#126.1).
    """
    return functions.lookup(x, [0, 1, 2, 3, 4], [0, 0.04, 0.07, 0.09, 0.1])


@cache('run')
def subsistence_food_per_capita():
    """
    Real Name: subsistence food per capita
    Original Eqn: 230
    Units: Veg eq kg/(Person*year)
    Limits: (None, None)
    Type: constant

    Subsistence food per capita (SFPC#127.1).
    """
    return 230


@cache('step')
def fraction_of_agricultural_inputs_allocated_to_land_development():
    """
    Real Name: fraction of agricultural inputs allocated to land development
    Original Eqn: fraction of agricultural inputs allocated to land development table ( ( marginal productivity of land development / marginal productivity of agricultural inputs ) )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Fraction of inputs allocated to land devlelopment                 (FIALD#108).
    """
    return fraction_of_agricultural_inputs_allocated_to_land_development_table(
        (marginal_productivity_of_land_development() /
         marginal_productivity_of_agricultural_inputs()))


def fraction_of_agricultural_inputs_allocated_to_land_development_table(x):
    """
    Real Name: fraction of agricultural inputs allocated to land development table
    Original Eqn: ( (0,0),(0.25,0.05),(0.5,0.15),(0.75,0.3),(1,0.5),(1.25,0.7) ,(1.5,0.85),(1.75,0.95),(2,1) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating the marginal productivity of land to                the fraction of inputs allocated to new land                 development (FIALDT#108.1).
    """
    return functions.lookup(x, [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2],
                            [0, 0.05, 0.15, 0.3, 0.5, 0.7, 0.85, 0.95, 1])


@cache('step')
def marginal_land_yield_multiplier_from_capital():
    """
    Real Name: marginal land yield multiplier from capital
    Original Eqn: marginal land yield multiplier from capital table ( agricultural input per hectare/unit agricultural input )
    Units: hectare/$
    Limits: (None, None)
    Type: component

    MARGINAL LAND YIELD MULTIPLIER FROM CAPITAL                 (MLYMC#111).
    """
    return marginal_land_yield_multiplier_from_capital_table(
        agricultural_input_per_hectare() / unit_agricultural_input())


def marginal_land_yield_multiplier_from_capital_table(x):
    """
    Real Name: marginal land yield multiplier from capital table
    Original Eqn: ( (0,0.075),(40,0.03),(80,0.015),(120,0.011),(160,0.009),(200,0.008) ,(240,0.007),(280,0.006),(320,0.005),(360,0.005),(400,0.005) ,(440,0.005),(480,0.005),(520,0.005),(560,0.005),(600,0.005) )
    Units: hectare/$
    Limits: (None, None)
    Type: lookup

    Table relating agricultural inputs to marginal land                 yield (MLYMCT#111.1).
    """
    return functions.lookup(
        x, [0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600], [
            0.075, 0.03, 0.015, 0.011, 0.009, 0.008, 0.007, 0.006, 0.005, 0.005, 0.005, 0.005,
            0.005, 0.005, 0.005, 0.005
        ])


@cache('step')
def marginal_productivity_of_agricultural_inputs():
    """
    Real Name: marginal productivity of agricultural inputs
    Original Eqn: average life agricultural inputs * land yield * marginal land yield multiplier from capital / land yield multiplier from capital
    Units: Veg eq kg/$
    Limits: (None, None)
    Type: component

    MARGINAL PRODUCTIVITY OF AGRICULTURAL INPUTS                 (MPAI#110).
    """
    return average_life_agricultural_inputs() * land_yield(
    ) * marginal_land_yield_multiplier_from_capital() / land_yield_multiplier_from_capital()


@cache('step')
def marginal_productivity_of_land_development():
    """
    Real Name: marginal productivity of land development
    Original Eqn: land yield / ( development cost per hectare * social discount )
    Units: Veg eq kg/$
    Limits: (None, None)
    Type: component

    The marginal productivity of land development                 (MPLD#109)
    """
    return land_yield() / (development_cost_per_hectare() * social_discount())


@cache('run')
def social_discount():
    """
    Real Name: social discount
    Original Eqn: 0.07
    Units: 1/year
    Limits: (None, None)
    Type: constant

    SOCIAL DISCOUNT (SD#109.1)
    """
    return 0.07


@cache('step')
def industrial_capital_output_ratio_multiplier_from_resource_conservation_technology():
    """
    Real Name: industrial capital output ratio multiplier from resource conservation technology
    Original Eqn: industrial capital output ratio multiplier from resource table ( resource use factor )
    Units: year
    Limits: (None, None)
    Type: component

    Technology driven industrial capital output ratio                 (ICOR2T#--)
    """
    return industrial_capital_output_ratio_multiplier_from_resource_table(resource_use_factor())


@cache('step')
def industrial_capital_output_ratio_multiplier_from_pollution_technology():
    """
    Real Name: industrial capital output ratio multiplier from pollution technology
    Original Eqn: industrial capital output ratio multiplier from pollution table ( persistent pollution generation factor )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Pollution control technology multiplier for capital                 output ratio (COPM#--).
    """
    return industrial_capital_output_ratio_multiplier_from_pollution_table(
        persistent_pollution_generation_factor())


@cache('step')
def industrial_capital_output_ratio_multiplier_from_land_yield_technology():
    """
    Real Name: industrial capital output ratio multiplier from land yield technology
    Original Eqn: industrial capital output ratio multiplier table ( land yield multiplier from technology\ )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    CAPITAL OUTPUT YIELD MULTIPLIER (COYM#--)
    """
    return industrial_capital_output_ratio_multiplier_table(
        land_yield_multiplier_from_technology())


@cache('step')
def fraction_of_industrial_output_allocated_to_investment():
    """
    Real Name: fraction of industrial output allocated to investment
    Original Eqn: ( 1 - fraction of industrial output allocated to agriculture - fraction of industrial output allocated to services - fraction of industrial output allocated to consumption )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Fraction of industrial output allocated to industry                 (FIOAI#56).
    """
    return (1 - fraction_of_industrial_output_allocated_to_agriculture() -
            fraction_of_industrial_output_allocated_to_services() -
            fraction_of_industrial_output_allocated_to_consumption())


@cache('step')
def industrial_capital_depreciation():
    """
    Real Name: industrial capital depreciation
    Original Eqn: Industrial Capital / average life of industrial capital
    Units: $/year
    Limits: (None, None)
    Type: component

    Industrial capital depreciation rate (ICDR#53).
    """
    return industrial_capital() / average_life_of_industrial_capital()


@cache('step')
def industrial_capital_investment():
    """
    Real Name: industrial capital investment
    Original Eqn: ( ( industrial output ) ) * ( fraction of industrial output allocated to investment )
    Units: $/year
    Limits: (None, None)
    Type: component

    Industrial capital investment rate (ICIR#55).
    """
    return ((industrial_output())) * (fraction_of_industrial_output_allocated_to_investment())


def industrial_capital_output_ratio_multiplier_from_resource_table(x):
    """
    Real Name: industrial capital output ratio multiplier from resource table
    Original Eqn: ( (0,3.75),(0.1,3.6),(0.2,3.47),(0.3,3.36),(0.4,3.25),(0.5,3.16) ,(0.6,3.1),(0.7,3.06),(0.8,3.02),(0.9,3.01),(1,3) )
    Units: year
    Limits: (None, None)
    Type: lookup

    CAPITAL OUTPUT FROM RESOURCES technology multiplier                 TABLE (ICOR2TT#--)
    """
    return functions.lookup(x, [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
                            [3.75, 3.6, 3.47, 3.36, 3.25, 3.16, 3.1, 3.06, 3.02, 3.01, 3])


@cache('step')
def industrial_output_per_capita():
    """
    Real Name: industrial output per capita
    Original Eqn: industrial output / population
    Units: $/(Person*year)
    Limits: (None, None)
    Type: component

    INDUSTRIAL OUTPUT PER CAPITA (IOPC#49)
    """
    return industrial_output() / population()


@cache('run')
def industrial_output_per_capita_desired():
    """
    Real Name: industrial output per capita desired
    Original Eqn: 400
    Units: $/(Person*year)
    Limits: (None, None)
    Type: constant

    Industrial output per capita desired (IOPCD#59.2).
    """
    return 350


@cache('step')
def industrial_capital():
    """
    Real Name: Industrial Capital
    Original Eqn: INTEG( ( industrial capital investment - industrial capital depreciation ) , initial industrial capital )
    Units: $
    Limits: (None, None)
    Type: component

    INDUSTRIAL CAPITAL (IC#52).
    """
    return integ_industrial_capital()


@cache('run')
def initial_industrial_capital():
    """
    Real Name: initial industrial capital
    Original Eqn: 2.1e+11
    Units: $
    Limits: (None, None)
    Type: constant

    INDUSTRIAL CAPITAL INITIAL (ICI#52.1).
    """
    return 2.1e+11


@cache('step')
def industrial_output():
    """
    Real Name: industrial output
    Original Eqn: ( ( ( Industrial Capital ) ) * ( 1 - fraction of industrial capital allocated to obtaining resources )\ ) * ( capacity utilization fraction ) / industrial capital output ratio
    Units: $/year
    Limits: (None, None)
    Type: component

    Industrial output (IO#50)
    """
    return (((industrial_capital())) *
            (1 - fraction_of_industrial_capital_allocated_to_obtaining_resources())) * (
                capacity_utilization_fraction()) / industrial_capital_output_ratio()


@cache('run')
def average_life_of_industrial_capital_1():
    """
    Real Name: average life of industrial capital 1
    Original Eqn: 14
    Units: year
    Limits: (None, None)
    Type: constant

    Average life of industrial capital before policy                 year (ALIC1#54.1).
    """
    return 14


@cache('run')
def average_life_of_industrial_capital_2():
    """
    Real Name: average life of industrial capital 2
    Original Eqn: 14
    Units: year
    Limits: (None, None)
    Type: constant

    Average life of industrial capital after policy year                 (ALIC2#54.2)
    """
    return 18


@cache('step')
def fraction_of_industrial_output_allocated_to_consumption_constant():
    """
    Real Name: fraction of industrial output allocated to consumption constant
    Original Eqn: IF THEN ELSE ( Time >= POLICY YEAR , fraction of industrial output allocated to consumption constant 2 , fraction of industrial output allocated to consumption constant 1 )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Fraction of output allocated to consumption CONSTANT                 (FIOACC#58).
    """
    return functions.if_then_else(
        time() >= policy_year(),
        fraction_of_industrial_output_allocated_to_consumption_constant_2(),
        fraction_of_industrial_output_allocated_to_consumption_constant_1())


@cache('run')
def fraction_of_industrial_output_allocated_to_consumption_constant_1():
    """
    Real Name: fraction of industrial output allocated to consumption constant 1
    Original Eqn: 0.43
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Fraction of output allocated to consuption constant                 1 (FIOAC1#58.1).
    """
    return 0.43


@cache('run')
def fraction_of_industrial_output_allocated_to_consumption_constant_2():
    """
    Real Name: fraction of industrial output allocated to consumption constant 2
    Original Eqn: 0.43
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Fraction of output allocated to consuption constant                 2 (FIOAC2#58.2).
    """
    return 0.43


@cache('step')
def fraction_of_industrial_output_allocated_to_consumption_variable():
    """
    Real Name: fraction of industrial output allocated to consumption variable
    Original Eqn: fraction of industrial output allocated to consumption variable table ( industrial output per capita / industrial output per capita desired )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Fraction industrial output allocated to consumption                 variable (FIOACV#59)
    """
    return fraction_of_industrial_output_allocated_to_consumption_variable_table(
        industrial_output_per_capita() / industrial_output_per_capita_desired())


def fraction_of_industrial_output_allocated_to_consumption_variable_table(x):
    """
    Real Name: fraction of industrial output allocated to consumption variable table
    Original Eqn: ( (0,0.3),(0.2,0.32),(0.4,0.34),(0.6,0.36),(0.8,0.38),(1,0.43) ,(1.2,0.73),(1.4,0.77),(1.6,0.81),(1.8,0.82),(2,0.83) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Fraction of industrial output allocated to                 consumption variable TABLE (FIOACVT#59.1)
    """
    return functions.lookup(x, [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2],
                            [0.3, 0.32, 0.34, 0.36, 0.38, 0.43, 0.73, 0.77, 0.81, 0.82, 0.83])


@cache('run')
def industrial_capital_output_ratio_1():
    """
    Real Name: industrial capital output ratio 1
    Original Eqn: 3
    Units: year
    Limits: (None, None)
    Type: constant

    Industrial capital output ratio prior to the policy                 year (ICOR1#51.1)
    """
    return 3


@cache('step')
def industrial_capital_output_ratio_2():
    """
    Real Name: industrial capital output ratio 2
    Original Eqn: industrial capital output ratio multiplier from resource conservation technology\ * industrial capital output ratio multiplier from land yield technology * industrial capital output ratio multiplier from pollution technology
    Units: year
    Limits: (None, None)
    Type: component

    Industrial capital output ratio after the policy                 year (ICOR2#51.2)
    """
    return industrial_capital_output_ratio_multiplier_from_resource_conservation_technology(
    ) * industrial_capital_output_ratio_multiplier_from_land_yield_technology(
    ) * industrial_capital_output_ratio_multiplier_from_pollution_technology()


def industrial_capital_output_ratio_multiplier_from_pollution_table(x):
    """
    Real Name: industrial capital output ratio multiplier from pollution table
    Original Eqn: ( (0,1.25),(0.1,1.2),(0.2,1.15),(0.3,1.11),(0.4,1.08),(0.5,1.05) ,(0.6,1.03),(0.7,1.02),(0.8,1.01),(0.9,1),(1,1) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating pollution correction technology to                 the capital output ratio (COPMT#--)
    """
    return functions.lookup(x, [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
                            [1.25, 1.2, 1.15, 1.11, 1.08, 1.05, 1.03, 1.02, 1.01, 1, 1])


@cache('step')
def average_life_of_industrial_capital():
    """
    Real Name: average life of industrial capital
    Original Eqn: IF THEN ELSE ( Time >= POLICY YEAR , average life of industrial capital 2 , average life of industrial capital 1 )
    Units: year
    Limits: (None, None)
    Type: component

    AVERAGE LIFETIME OF INDUSTRIAL CAPITAL (ALIC#54).
    """
    return functions.if_then_else(time() >= policy_year(), average_life_of_industrial_capital_2(),
                                  average_life_of_industrial_capital_1())


@cache('step')
def fraction_of_industrial_output_allocated_to_consumption():
    """
    Real Name: fraction of industrial output allocated to consumption
    Original Eqn: IF THEN ELSE ( Time >= industrial equilibrium time , fraction of industrial output allocated to consumption variable , fraction of industrial output allocated to consumption constant )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Fraction of industrial output allocated to                 consumption (FIOAC#58)
    """
    return functions.if_then_else(
        time() >= industrial_equilibrium_time(),
        fraction_of_industrial_output_allocated_to_consumption_variable(),
        fraction_of_industrial_output_allocated_to_consumption_constant())


@cache('step')
def industrial_capital_output_ratio():
    """
    Real Name: industrial capital output ratio
    Original Eqn: IF THEN ELSE ( Time >= POLICY YEAR , industrial capital output ratio 2 , industrial capital output ratio 1 )
    Units: year
    Limits: (None, None)
    Type: component

    INDUSTRIAL CAPITAL-OUTPUT RATIO (ICOR#51)
    """
    return functions.if_then_else(time() >= policy_year(), industrial_capital_output_ratio_2(),
                                  industrial_capital_output_ratio_1())


@cache('run')
def industrial_equilibrium_time():
    """
    Real Name: industrial equilibrium time
    Original Eqn: 4000
    Units: year
    Limits: (None, None)
    Type: constant

    INDUSTRIAL EQUILIBRIUM TIME (IET#57.1).
    """
    return 2002


def industrial_capital_output_ratio_multiplier_table(x):
    """
    Real Name: industrial capital output ratio multiplier table
    Original Eqn: ( [(1,0.8)-(2,2)],(1,1),(1.2,1.05),(1.4,1.12),(1.6,1.25),(1.8,1.35),(2,1.5))
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating the yield of technology to the effect                 on the capital output ratio (COYMT#--)
!
!
    """
    return functions.lookup(x, [1, 1.2, 1.4, 1.6, 1.8, 2], [1, 1.05, 1.12, 1.25, 1.35, 1.5])


@cache('step')
def delayed_labor_utilization_fraction():
    """
    Real Name: Delayed Labor Utilization Fraction
    Original Eqn: SMOOTHI (labor utilization fraction, labor utilization fraction delay time ,1 )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    LABOR UTILIZATION FRACTION DELAYED (LUFD#82)
    """
    return smooth_labor_utilization_fraction_labor_utilization_fraction_delay_time_1_1()


@cache('step')
def capacity_utilization_fraction():
    """
    Real Name: capacity utilization fraction
    Original Eqn: ACTIVE INITIAL( capacity utilization fraction table ( Delayed Labor Utilization Fraction\ ) , 1)
    Units: Dmnl
    Limits: (None, None)
    Type: component

    CAPITAL UTILIZATION FRACTION (CUF#83)
    """
    return functions.active_initial(
        lambda: capacity_utilization_fraction_table(delayed_labor_utilization_fraction()),
        lambda: 1)


def capacity_utilization_fraction_table(x):
    """
    Real Name: capacity utilization fraction table
    Original Eqn: ( (1,1),(3,0.9),(5,0.7),(7,0.3),(9,0.1),(11,0.1) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating labor utilization to capacity                 utilization (CUFT#83.2).
    """
    return functions.lookup(x, [1, 3, 5, 7, 9, 11], [1, 0.9, 0.7, 0.3, 0.1, 0.1])


@cache('step')
def jobs():
    """
    Real Name: jobs
    Original Eqn: potential jobs industrial sector + potential jobs agricultural sector + potential jobs service sector
    Units: Person
    Limits: (None, None)
    Type: component

    JOBS (J#73).
    """
    return potential_jobs_industrial_sector() + potential_jobs_agricultural_sector(
    ) + potential_jobs_service_sector()


@cache('step')
def jobs_per_hectare():
    """
    Real Name: jobs per hectare
    Original Eqn: jobs per hectare table ( agricultural input per hectare/unit agricultural input )
    Units: Person/hectare
    Limits: (None, None)
    Type: component

    Jobs per hectare in agriculture (JPH#79).
    """
    return jobs_per_hectare_table(agricultural_input_per_hectare() / unit_agricultural_input())


def jobs_per_hectare_table(x):
    """
    Real Name: jobs per hectare table
    Original Eqn: ( (2,2),(6,0.5),(10,0.4),(14,0.3),(18,0.27),(22,0.24),(26,0.2) ,(30,0.2) )
    Units: Person/hectare
    Limits: (None, None)
    Type: lookup

    Table relating agricultural input intensity to the                number of jobs per hectare in agriculture                 (JPHT#79.1).
    """
    return functions.lookup(x, [2, 6, 10, 14, 18, 22, 26, 30],
                            [2, 0.5, 0.4, 0.3, 0.27, 0.24, 0.2, 0.2])


@cache('step')
def jobs_per_industrial_capital_unit():
    """
    Real Name: jobs per industrial capital unit
    Original Eqn: ( jobs per industrial capital unit table ( industrial output per capita/GDP pc unit \ ) ) * 0.001
    Units: Person/$
    Limits: (None, None)
    Type: component

    Jobs per industrial capital units (JPICU#75).
    """
    return (jobs_per_industrial_capital_unit_table(
        industrial_output_per_capita() / gdp_pc_unit())) * 0.001


def jobs_per_industrial_capital_unit_table(x):
    """
    Real Name: jobs per industrial capital unit table
    Original Eqn: ( (50,0.37),(200,0.18),(350,0.12),(500,0.09),(650,0.07),(800,0.06) )
    Units: Person/$
    Limits: (None, None)
    Type: lookup

    Table relating industrial output per capita to job                 per industrial capital unit (JPICUT#75.1).
    """
    return functions.lookup(x, [50, 200, 350, 500, 650, 800], [0.37, 0.18, 0.12, 0.09, 0.07, 0.06])


@cache('step')
def jobs_per_service_capital_unit():
    """
    Real Name: jobs per service capital unit
    Original Eqn: ( jobs per service capital unit table ( service output per capita/GDP pc unit ) ) * 0.001
    Units: Person/$
    Limits: (None, None)
    Type: component

    Jobs per service capital unit (JPSCU#77).
    """
    return (jobs_per_service_capital_unit_table(
        service_output_per_capita() / gdp_pc_unit())) * 0.001


def jobs_per_service_capital_unit_table(x):
    """
    Real Name: jobs per service capital unit table
    Original Eqn: ( (50,1.1),(200,0.6),(350,0.35),(500,0.2),(650,0.15),(800,0.15) )
    Units: Person/$
    Limits: (None, None)
    Type: lookup

    Table relating service output per capita to job per                 service capital unit (JPSCUT#77.1).
    """
    return functions.lookup(x, [50, 200, 350, 500, 650, 800], [1.1, 0.6, 0.35, 0.2, 0.15, 0.15])


@cache('step')
def labor_force():
    """
    Real Name: labor force
    Original Eqn: ( Population 15 To 44 + Population 45 To 64 ) * labor force participation fraction
    Units: Person
    Limits: (None, None)
    Type: component

    LABOR FORCE (LF#80).
    """
    return (population_15_to_44() + population_45_to_64()) * labor_force_participation_fraction()


@cache('run')
def labor_force_participation_fraction():
    """
    Real Name: labor force participation fraction
    Original Eqn: 0.75
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    LABOR FORCE PARTICIPATION FRACTION (LFPF#80.1)
    """
    return 0.75


@cache('step')
def labor_utilization_fraction():
    """
    Real Name: labor utilization fraction
    Original Eqn: jobs / labor force
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Labor utilization fraction (LUF#81).
    """
    return jobs() / labor_force()


@cache('run')
def labor_utilization_fraction_delay_time():
    """
    Real Name: labor utilization fraction delay time
    Original Eqn: 2
    Units: year
    Limits: (None, None)
    Type: constant

    Labor utilization fraction delay time (LUFDT#82.1)
    """
    return 2


@cache('step')
def potential_jobs_agricultural_sector():
    """
    Real Name: potential jobs agricultural sector
    Original Eqn: ( ( jobs per hectare ) ) * ( Arable Land )
    Units: Person
    Limits: (None, None)
    Type: component

    Potential jobs in the agricultural sector (PJAS#78).
    """
    return ((jobs_per_hectare())) * (arable_land())


@cache('step')
def potential_jobs_industrial_sector():
    """
    Real Name: potential jobs industrial sector
    Original Eqn: Industrial Capital * jobs per industrial capital unit
    Units: Person
    Limits: (None, None)
    Type: component

    POTENTIAL JOBS IN INDUSTRIAL SECTOR (PKIS#74).
    """
    return industrial_capital() * jobs_per_industrial_capital_unit()


@cache('step')
def potential_jobs_service_sector():
    """
    Real Name: potential jobs service sector
    Original Eqn: ( ( Service Capital ) ) * ( jobs per service capital unit )
    Units: Person
    Limits: (None, None)
    Type: component

    Potential jobs in the service sector (PJSS#76).
    """
    return ((service_capital())) * (jobs_per_service_capital_unit())


@cache('run')
def average_life_of_service_capital_1():
    """
    Real Name: average life of service capital 1
    Original Eqn: 20
    Units: year
    Limits: (None, None)
    Type: constant

    Average lifetime of service capital before policy                 time (ALSC1#69.1).
    """
    return 20


@cache('run')
def average_life_of_service_capital_2():
    """
    Real Name: average life of service capital 2
    Original Eqn: 20
    Units: year
    Limits: (None, None)
    Type: constant

    Average lifetime of service capital after policy                 time (ALSC2#69.2).
    """
    return 25


@cache('step')
def fraction_of_industrial_output_allocated_to_services_1():
    """
    Real Name: fraction of industrial output allocated to services 1
    Original Eqn: fraction of industrial output allocated to services table 1 ( service output per capita\ / indicated services output per capita )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    FRACTION OF INDUSTRIAL OUTPUT ALLOCATED TO SERVICES                 before policy year (FIOAS1#64).
    """
    return fraction_of_industrial_output_allocated_to_services_table_1(
        service_output_per_capita() / indicated_services_output_per_capita())


def fraction_of_industrial_output_allocated_to_services_table_1(x):
    """
    Real Name: fraction of industrial output allocated to services table 1
    Original Eqn: ( (0,0.3),(0.5,0.2),(1,0.1),(1.5,0.05),(2,0) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating service output to the fraction of                industrial output allocated to service                 (FIOAS1T#64.1).
    """
    return functions.lookup(x, [0, 0.5, 1, 1.5, 2], [0.3, 0.2, 0.1, 0.05, 0])


@cache('step')
def fraction_of_industrial_output_allocated_to_services_2():
    """
    Real Name: fraction of industrial output allocated to services 2
    Original Eqn: fraction of industrial output allocated to services table 2 ( service output per capita\ / indicated services output per capita )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    FRACTION OF INDUSTRIAL OUTPUT ALLOCATED TO SERVICES                 after policy year (FIOAS2#65).
    """
    return fraction_of_industrial_output_allocated_to_services_table_2(
        service_output_per_capita() / indicated_services_output_per_capita())


def fraction_of_industrial_output_allocated_to_services_table_2(x):
    """
    Real Name: fraction of industrial output allocated to services table 2
    Original Eqn: ( (0,0.3),(0.5,0.2),(1,0.1),(1.5,0.05),(2,0) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating service output to the fraction of                industrial output allocated to service                 (FIOAS2T#65.1).
    """
    return functions.lookup(x, [0, 0.5, 1, 1.5, 2], [0.3, 0.2, 0.1, 0.05, 0])


@cache('step')
def indicated_services_output_per_capita_1():
    """
    Real Name: indicated services output per capita 1
    Original Eqn: indicated services output per capita table 1 ( industrial output per capita/GDP pc unit\ )
    Units: $/(Person*year)
    Limits: (None, None)
    Type: component

    Indicated service output per capita before policy                 year (ISOPC1#61).
    """
    return indicated_services_output_per_capita_table_1(
        industrial_output_per_capita() / gdp_pc_unit())


def indicated_services_output_per_capita_table_1(x):
    """
    Real Name: indicated services output per capita table 1
    Original Eqn: ( (0,40),(200,300),(400,640),(600,1000),(800,1220),(1000,1450) ,(1200,1650),(1400,1800),(1600,2000) )
    Units: $/(Person*year)
    Limits: (None, None)
    Type: lookup

    Table relating industrial output per capita to the                indicated service output per capita before policy                 year (ISOPC1T#61.1).
    """
    return functions.lookup(x, [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600],
                            [40, 300, 640, 1000, 1220, 1450, 1650, 1800, 2000])


@cache('step')
def indicated_services_output_per_capita_2():
    """
    Real Name: indicated services output per capita 2
    Original Eqn: indicated services output per capita table 2 ( industrial output per capita/GDP pc unit\ )
    Units: $/(Person*year)
    Limits: (None, None)
    Type: component

    Indicated service output per capita after policy                 year (ISOPC2#62).
    """
    return indicated_services_output_per_capita_table_2(
        industrial_output_per_capita() / gdp_pc_unit())


def indicated_services_output_per_capita_table_2(x):
    """
    Real Name: indicated services output per capita table 2
    Original Eqn: ( (0,40),(200,300),(400,640),(600,1000),(800,1220),(1000,1450) ,(1200,1650),(1400,1800),(1600,2000) )
    Units: $/(Person*year)
    Limits: (None, None)
    Type: lookup

    Table relating industrial output per capita to the                indicated service output per capita afte policy                 year (ISOPC2T#62.2).
    """
    return functions.lookup(x, [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600],
                            [40, 300, 640, 1000, 1220, 1450, 1650, 1800, 2000])


@cache('run')
def service_capital_output_ratio_1():
    """
    Real Name: service capital output ratio 1
    Original Eqn: 1
    Units: year
    Limits: (None, None)
    Type: constant

    Service capital output ratio before policy year                 (SCOR1#72.1).
    """
    return 1


@cache('run')
def service_capital_output_ratio_2():
    """
    Real Name: service capital output ratio 2
    Original Eqn: 1
    Units: year
    Limits: (None, None)
    Type: constant

    Service capital output ratio after policy year                 (SCOR2#72.2).
    """
    return 1


@cache('step')
def average_life_of_service_capital():
    """
    Real Name: average life of service capital
    Original Eqn: IF THEN ELSE ( Time >= POLICY YEAR , average life of service capital 2 , average life of service capital 1 )
    Units: year
    Limits: (None, None)
    Type: component

    AVERAGE LIFETIME OF SERVICE CAPITAL (ALSC#69)
    """
    return functions.if_then_else(time() >= policy_year(), average_life_of_service_capital_2(),
                                  average_life_of_service_capital_1())


@cache('step')
def fraction_of_industrial_output_allocated_to_services():
    """
    Real Name: fraction of industrial output allocated to services
    Original Eqn: IF THEN ELSE ( Time >= POLICY YEAR , fraction of industrial output allocated to services 2 , fraction of industrial output allocated to services 1 )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    FRACTION OF INDUSTRIAL OUTPUT ALLOCATED TO SERVICES                 (FIOAS#63).
    """
    return functions.if_then_else(time() >= policy_year(),
                                  fraction_of_industrial_output_allocated_to_services_2(),
                                  fraction_of_industrial_output_allocated_to_services_1())


@cache('step')
def indicated_services_output_per_capita():
    """
    Real Name: indicated services output per capita
    Original Eqn: IF THEN ELSE ( Time >= POLICY YEAR , indicated services output per capita 2 , indicated services output per capita 1 )
    Units: $/(Person*year)
    Limits: (None, None)
    Type: component

    Indicated service output per capita (ISOPC#60).
    """
    return functions.if_then_else(time() >= policy_year(),
                                  indicated_services_output_per_capita_2(),
                                  indicated_services_output_per_capita_1())


@cache('step')
def service_capital_output_ratio():
    """
    Real Name: service capital output ratio
    Original Eqn: IF THEN ELSE ( Time >= POLICY YEAR , service capital output ratio 2 , service capital output ratio 1 )
    Units: year
    Limits: (None, None)
    Type: component

    Service capital output ratio (SCOR#72).
    """
    return functions.if_then_else(time() >= policy_year(), service_capital_output_ratio_2(),
                                  service_capital_output_ratio_1())


@cache('step')
def service_capital_depreciation():
    """
    Real Name: service capital depreciation
    Original Eqn: Service Capital / average life of service capital
    Units: $/year
    Limits: (None, None)
    Type: component

    SERVICE CAPITAL DEPRECIATION RATE (SCDR#68).
    """
    return service_capital() / average_life_of_service_capital()


@cache('step')
def service_capital_investment():
    """
    Real Name: service capital investment
    Original Eqn: ( ( industrial output ) ) * ( fraction of industrial output allocated to services )
    Units: $/year
    Limits: (None, None)
    Type: component

    SERVICE CAPITAL INVESTMENT RATE (SCIR#66).
    """
    return ((industrial_output())) * (fraction_of_industrial_output_allocated_to_services())


@cache('step')
def service_output_per_capita():
    """
    Real Name: service output per capita
    Original Eqn: service output / population
    Units: $/(Person*year)
    Limits: (None, None)
    Type: component

    SERVICE OUTPUT PER CAPITA (SOPC#71).
    """
    return service_output() / population()


@cache('step')
def service_capital():
    """
    Real Name: Service Capital
    Original Eqn: INTEG( ( service capital investment - service capital depreciation ) , initial service capital )
    Units: $
    Limits: (None, None)
    Type: component

    Service capital (SC#67).
    """
    return integ_service_capital()


@cache('run')
def initial_service_capital():
    """
    Real Name: initial service capital
    Original Eqn: 1.44e+11
    Units: $
    Limits: (None, None)
    Type: constant

    The initial level of service capital (SCI#67.2)
    """
    return 1.44e+11


@cache('step')
def service_output():
    """
    Real Name: service output
    Original Eqn: ( ( Service Capital ) ) * ( capacity utilization fraction ) / service capital output ratio
    Units: $/year
    Limits: (None, None)
    Type: component

    Service output (SO#70).
    """
    return (
        (service_capital())) * (capacity_utilization_fraction()) / service_capital_output_ratio()


@cache('run')
def final_time():
    """
    Real Name: FINAL TIME
    Original Eqn: 2100
    Units: year
    Limits: (None, None)
    Type: constant

    The time at which simulation stops.
    """
    return 2100


@cache('run')
def initial_time():
    """
    Real Name: INITIAL TIME
    Original Eqn: 1900
    Units: year
    Limits: (None, None)
    Type: constant

    The time at which the simulation begins.
    """
    return 1900


@cache('step')
def saveper():
    """
    Real Name: SAVEPER
    Original Eqn: TIME STEP
    Units: year
    Limits: (None, None)
    Type: component

    The frequency with which results are saved.
    """
    return time_step()


@cache('run')
def policy_year():
    """
    Real Name: POLICY YEAR
    Original Eqn: 1995
    Units: year
    Limits: (None, None)
    Type: constant

    The time at which policies are implemented                 (PYEAR#150.1).
    """
    return 2002


@cache('run')
def time_step():
    """
    Real Name: TIME STEP
    Original Eqn: 0.5
    Units: year
    Limits: (None, None)
    Type: constant

    The time step for computing the model
    """
    return 0.5


@cache('run')
def agricultural_material_toxicity_index():
    """
    Real Name: agricultural material toxicity index
    Original Eqn: 1
    Units: Pollution units/$
    Limits: (None, None)
    Type: constant

    Agricultural material toxicity index (AMTI#140.2).
    """
    return 1


@cache('step')
def assimilation_half_life():
    """
    Real Name: assimilation half life
    Original Eqn: assimilation half life in 1970 * assimilation half life multiplier
    Units: year
    Limits: (None, None)
    Type: component

    ASSIMILATION HALF-LIFE (AHL#146).
    """
    return assimilation_half_life_in_1970() * assimilation_half_life_multiplier()


@cache('run')
def assimilation_half_life_in_1970():
    """
    Real Name: assimilation half life in 1970
    Original Eqn: 1.5
    Units: year
    Limits: (None, None)
    Type: constant

    Assimilation half life of persistent pollution int                 1970 (AHL70#146.1).
    """
    return 1.5


@cache('step')
def assimilation_half_life_multiplier():
    """
    Real Name: assimilation half life multiplier
    Original Eqn: assimilation half life mult table ( persistent pollution index )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Assimilation half life of multiplier of persistent                 pollution (AHLM#145)
    """
    return assimilation_half_life_mult_table(persistent_pollution_index())


def assimilation_half_life_mult_table(x):
    """
    Real Name: assimilation half life mult table
    Original Eqn: ( (1,1),(251,11),(501,21),(751,31),(1001,41) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating the level of persisten pollution to                 its assimilation rate (AHLMT#145.1).
    """
    return functions.lookup(x, [1, 251, 501, 751, 1001], [1, 11, 21, 31, 41])


@cache('run')
def desired_persistent_pollution_index():
    """
    Real Name: desired persistent pollution index
    Original Eqn: 1.2
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Desires persistent pollution index (DPOLX#--).
    """
    return 1.2


@cache('run')
def fraction_of_agricultural_inputs_from_persistent_materials():
    """
    Real Name: fraction of agricultural inputs from persistent materials
    Original Eqn: 0.001
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Fraction of inputs as persistent materials                 (FIPM#140.1).
    """
    return 0.001


@cache('run')
def fraction_of_resources_from_persistent_materials():
    """
    Real Name: fraction of resources from persistent materials
    Original Eqn: 0.02
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Fraction of resources as persistent materials                 (FRPM#139.1)
    """
    return 0.02


@cache('run')
def industrial_material_toxicity_index():
    """
    Real Name: industrial material toxicity index
    Original Eqn: 10
    Units: Pollution units/Resource unit
    Limits: (None, None)
    Type: constant

    Industrial materials toxicity index (IMTI#139.3)
    """
    return 10


@cache('run')
def industrial_material_emissions_factor():
    """
    Real Name: industrial material emissions factor
    Original Eqn: 0.1
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Industrial materials emission factor (IMEF#139.2).
    """
    return 0.1


@cache('run')
def persistent_pollution_generation_factor_1():
    """
    Real Name: persistent pollution generation factor 1
    Original Eqn: 1
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Persistent pollution generation factor before policy                 time (PPGF1#138.1).
    """
    return 1


@cache('step')
def persistent_pollution_generation_factor_2():
    """
    Real Name: persistent pollution generation factor 2
    Original Eqn: SMOOTH3 ( Persistent Pollution Technology , technology development delay )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Persistent pollution generation factor after policy                 time (PPGF2#138.2).
    """
    return smooth_persistent_pollution_technology_technology_development_delay_persistent_pollution_technology_3(
    )


@cache('step')
def persistent_pollution_technology_change_multiplier():
    """
    Real Name: persistent pollution technology change multiplier
    Original Eqn: persistent pollution technology change mult table ( 1 - persistent pollution index / desired persistent pollution index )
    Units: 1/year
    Limits: (None, None)
    Type: component

    POLLUTION CONTROL TECHNOLOGY CHANGE MULTIPLIER                 (POLGFM#--).
    """
    return persistent_pollution_technology_change_mult_table(
        1 - persistent_pollution_index() / desired_persistent_pollution_index())


def persistent_pollution_technology_change_mult_table(x):
    """
    Real Name: persistent pollution technology change mult table
    Original Eqn: ( (-1,0),(0,0) )
    Units: 1/year
    Limits: (None, None)
    Type: lookup

    Table relating persisten pollution to changes due to                 technology (POLGFMT#--).
    """
    return functions.lookup(x, [-1, 0], [-0.04, 0])


@cache('step')
def persistent_pollution():
    """
    Real Name: Persistent Pollution
    Original Eqn: INTEG( ( persistent pollution appearance rate - persistent pollution assimilation rate ) , initial persistent pollution )
    Units: Pollution units
    Limits: (None, None)
    Type: component

    Persistent pollution (PPOL#142).
    """
    return integ_persistent_pollution()


@cache('run')
def initial_persistent_pollution():
    """
    Real Name: initial persistent pollution
    Original Eqn: 2.5e+07
    Units: Pollution units
    Limits: (None, None)
    Type: constant

    persistent pollution initial (PPOLI#142.2)
    """
    return 2.5e+07


@cache('step')
def persistent_pollution_generation_industry():
    """
    Real Name: persistent pollution generation industry
    Original Eqn: per capita resource use multiplier * population * fraction of resources from persistent materials * industrial material emissions factor * industrial material toxicity index
    Units: Pollution units/year
    Limits: (None, None)
    Type: component

    Persistent pollution generated by industrial output.                 (PPGIO#139)
    """
    return per_capita_resource_use_multiplier() * population(
    ) * fraction_of_resources_from_persistent_materials() * industrial_material_emissions_factor(
    ) * industrial_material_toxicity_index()


@cache('step')
def persistent_pollution_generation_agriculture():
    """
    Real Name: persistent pollution generation agriculture
    Original Eqn: agricultural input per hectare * Arable Land * fraction of agricultural inputs from persistent materials * agricultural material toxicity index
    Units: Pollution units/year
    Limits: (None, None)
    Type: component

    Persistent pollution generated by agriculture                 (PPGAO#140)
    """
    return agricultural_input_per_hectare() * arable_land(
    ) * fraction_of_agricultural_inputs_from_persistent_materials(
    ) * agricultural_material_toxicity_index()


@cache('step')
def persistent_pollution_generation_rate():
    """
    Real Name: persistent pollution generation rate
    Original Eqn: ( persistent pollution generation industry + persistent pollution generation agriculture ) * ( persistent pollution generation factor )
    Units: Pollution units/year
    Limits: (None, None)
    Type: component

    PERSISTENT POLLUTION GENERATION RATE (PPGR#137).
    """
    return (persistent_pollution_generation_industry() +
            persistent_pollution_generation_agriculture()) * (
                persistent_pollution_generation_factor())


@cache('step')
def persistent_pollution_appearance_rate():
    """
    Real Name: persistent pollution appearance rate
    Original Eqn: DELAY3 ( persistent pollution generation rate , persistent pollution transmission delay )
    Units: Pollution units/year
    Limits: (None, None)
    Type: component

    Persistent pollution appearance rate (PPAPR#141)
    """
    return delay_persistent_pollution_generation_rate_persistent_pollution_transmission_delay_persistent_pollution_generation_rate_3(
    )


@cache('step')
def persistent_pollution_assimilation_rate():
    """
    Real Name: persistent pollution assimilation rate
    Original Eqn: Persistent Pollution / ( assimilation half life * 1.4)
    Units: Pollution units/year
    Limits: (None, None)
    Type: component

    PERSISTENT POLLUTION ASSIMILATION RATE (PPASR#144).
    """
    return persistent_pollution() / (assimilation_half_life() * 1.4)


@cache('run')
def persistent_pollution_in_1970():
    """
    Real Name: persistent pollution in 1970
    Original Eqn: 1.36e+08
    Units: Pollution units
    Limits: (None, None)
    Type: constant

    PERSISTENT POLLUTION IN 1970 (PPOL70#143.1).
    """
    return 1.36e+08


@cache('step')
def persistent_pollution_index():
    """
    Real Name: persistent pollution index
    Original Eqn: Persistent Pollution / persistent pollution in 1970
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Persistent pollution index relative to 1970                 (PPOLX#143).
    """
    return persistent_pollution() / persistent_pollution_in_1970()


@cache('step')
def persistent_pollution_technology():
    """
    Real Name: Persistent Pollution Technology
    Original Eqn: INTEG( persistent pollution technology change rate , 1)
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Pollution control technology initiated (PTD#--)
    """
    return integ_persistent_pollution_technology()


@cache('step')
def persistent_pollution_technology_change_rate():
    """
    Real Name: persistent pollution technology change rate
    Original Eqn: IF THEN ELSE ( Time >= POLICY YEAR , Persistent Pollution Technology * persistent pollution technology change multiplier , 0)
    Units: 1/year
    Limits: (None, None)
    Type: component

    pollution control technology change rate (PTDR#--)
    """
    return functions.if_then_else(
        time() >= policy_year(),
        persistent_pollution_technology() * persistent_pollution_technology_change_multiplier(), 0)


@cache('run')
def persistent_pollution_transmission_delay():
    """
    Real Name: persistent pollution transmission delay
    Original Eqn: 20
    Units: year
    Limits: (None, None)
    Type: constant

    Persistent pollution transmission delay                 (PPTD#141.1).
    """
    return 20


@cache('step')
def persistent_pollution_generation_factor():
    """
    Real Name: persistent pollution generation factor
    Original Eqn: IF THEN ELSE ( Time >= POLICY YEAR , persistent pollution generation factor 2 , persistent pollution generation factor 1 )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    PERSISTENT POLLUTION GENERATED FACTOR (PPGF#138).
    """
    return functions.if_then_else(time() >= policy_year(),
                                  persistent_pollution_generation_factor_2(),
                                  persistent_pollution_generation_factor_1())


@cache('step')
def deaths_0_to_14():
    """
    Real Name: deaths 0 to 14
    Original Eqn: Population 0 To 14 * mortality 0 to 14
    Units: Person/year
    Limits: (None, None)
    Type: component

    The number of deaths per year among people 0 to 14                 years of age (D1#3).
    """
    return population_0_to_14() * mortality_0_to_14()


@cache('step')
def deaths_15_to_44():
    """
    Real Name: deaths 15 to 44
    Original Eqn: Population 15 To 44 * mortality 15 to 44
    Units: Person/year
    Limits: (None, None)
    Type: component

    The number of deaths per year among people 15 to 44                 years of age (D2#7).
    """
    return population_15_to_44() * mortality_15_to_44()


@cache('step')
def deaths_45_to_64():
    """
    Real Name: deaths 45 to 64
    Original Eqn: Population 45 To 64 * mortality 45 to 64
    Units: Person/year
    Limits: (None, None)
    Type: component

    The number of deaths per year among people 55 to 64                 years of age (D3#11).
    """
    return population_45_to_64() * mortality_45_to_64()


@cache('step')
def deaths_65_plus():
    """
    Real Name: deaths 65 plus
    Original Eqn: Population 65 Plus * mortality 65 plus
    Units: Person/year
    Limits: (None, None)
    Type: component

    The number of deaths per year among people 65 and                 older (D4#15).
    """
    return population_65_plus() * mortality_65_plus()


@cache('step')
def maturation_14_to_15():
    """
    Real Name: maturation 14 to 15
    Original Eqn: ( ( Population 0 To 14 ) ) * ( 1 - mortality 0 to 14 ) / 15
    Units: Person/year
    Limits: (None, None)
    Type: component

    The fractional rate at which people aged 0-14 mature                 into the next age cohort (MAT1#5).
    """
    return ((population_0_to_14())) * (1 - mortality_0_to_14()) / 15


@cache('step')
def maturation_44_to_45():
    """
    Real Name: maturation 44 to 45
    Original Eqn: ( ( Population 15 To 44 ) ) * ( 1 - mortality 15 to 44 ) / 30
    Units: Person/year
    Limits: (None, None)
    Type: component

    The fractional rate at which people aged 15-44                 mature into the next age cohort (MAT2#9).
    """
    return ((population_15_to_44())) * (1 - mortality_15_to_44()) / 30


@cache('step')
def maturation_64_to_65():
    """
    Real Name: maturation 64 to 65
    Original Eqn: ( ( Population 45 To 64 ) ) * ( 1 - mortality 45 to 64 ) / 20
    Units: Person/year
    Limits: (None, None)
    Type: component

    The fractional rate at which people aged 45-64                 mature into the next age cohort (MAT3#13).
    """
    return ((population_45_to_64())) * (1 - mortality_45_to_64()) / 20


@cache('step')
def mortality_45_to_64():
    """
    Real Name: mortality 45 to 64
    Original Eqn: mortality 45 to 64 table ( life expectancy/one year )
    Units: 1/year
    Limits: (None, None)
    Type: component

    The fractional mortality rate for people aged 45-64                 (M3#12).
    """
    return mortality_45_to_64_table(life_expectancy() / one_year())


def mortality_45_to_64_table(x):
    """
    Real Name: mortality 45 to 64 table
    Original Eqn: ( (20,0.0562),(30,0.0373),(40,0.0252),(50,0.0171),(60,0.0118) ,(70,0.0083),(80,0.006) )
    Units: 1/year
    Limits: (None, None)
    Type: lookup

    The table relating average life to mortality in the                 45 to 64 age group (M2T#12.1).
    """
    return functions.lookup(x, [20, 30, 40, 50, 60, 70, 80],
                            [0.0562, 0.0373, 0.0252, 0.0171, 0.0118, 0.0083, 0.006])


@cache('step')
def mortality_65_plus():
    """
    Real Name: mortality 65 plus
    Original Eqn: mortality 65 plus table ( life expectancy/one year )
    Units: 1/year
    Limits: (None, None)
    Type: component

    The fractional mortality rate for people over 65                 (M4#16).
    """
    return mortality_65_plus_table(life_expectancy() / one_year())


def mortality_65_plus_table(x):
    """
    Real Name: mortality 65 plus table
    Original Eqn: ( (20,0.13),(30,0.11),(40,0.09),(50,0.07),(60,0.06),(70,0.05) ,(80,0.04) )
    Units: 1/year
    Limits: (None, None)
    Type: lookup

    The table relating average life expectancy to                 mortality among people over 65 (M4T#16.1)
    """
    return functions.lookup(x, [20, 30, 40, 50, 60, 70, 80],
                            [0.13, 0.11, 0.09, 0.07, 0.06, 0.05, 0.04])


@cache('step')
def mortality_0_to_14():
    """
    Real Name: mortality 0 to 14
    Original Eqn: mortality 0 to 14 table ( life expectancy/one year )
    Units: 1/year
    Limits: (None, None)
    Type: component

    The fractional mortality rate for people aged 0-14                 (M1#4).
    """
    return mortality_0_to_14_table(life_expectancy() / one_year())


def mortality_0_to_14_table(x):
    """
    Real Name: mortality 0 to 14 table
    Original Eqn: ( (20,0.0567),(30,0.0366),(40,0.0243),(50,0.0155),(60,0.0082) ,(70,0.0023),(80,0.001) )
    Units: 1/year
    Limits: (None, None)
    Type: lookup

    The table relating average life to mortality in the                 0 to 14 age group (M1T#4.1).
    """
    return functions.lookup(x, [20, 30, 40, 50, 60, 70, 80],
                            [0.0567, 0.0366, 0.0243, 0.0155, 0.0082, 0.0023, 0.001])


@cache('step')
def mortality_15_to_44():
    """
    Real Name: mortality 15 to 44
    Original Eqn: mortality 15 to 44 table ( life expectancy/one year )
    Units: 1/year
    Limits: (None, None)
    Type: component

    The fractional mortality rate for people aged 15-44                 (M2#8).
    """
    return mortality_15_to_44_table(life_expectancy() / one_year())


def mortality_15_to_44_table(x):
    """
    Real Name: mortality 15 to 44 table
    Original Eqn: ( (20,0.0266),(30,0.0171),(40,0.011),(50,0.0065),(60,0.004), (70,0.0016),(80,0.0008) )
    Units: 1/year
    Limits: (None, None)
    Type: lookup

    The table relating average life to mortality in the                 15 to 44 age group (M2T#8.1).
    """
    return functions.lookup(x, [20, 30, 40, 50, 60, 70, 80],
                            [0.0266, 0.0171, 0.011, 0.0065, 0.004, 0.0016, 0.0008])


@cache('step')
def population_0_to_14():
    """
    Real Name: Population 0 To 14
    Original Eqn: INTEG( ( births - deaths 0 to 14 - maturation 14 to 15 ) , initial population 0 to 14 )
    Units: Person
    Limits: (None, None)
    Type: component

    World population, AGES 0-14 (P1#2)
    """
    return integ_population_0_to_14()


@cache('run')
def initial_population_0_to_14():
    """
    Real Name: initial population 0 to 14
    Original Eqn: 6.5e+08
    Units: Person
    Limits: (None, None)
    Type: constant

    The initial number of people aged 0 to 14 (P1I#2.2).
    """
    return 6.5e+08


@cache('step')
def population_15_to_44():
    """
    Real Name: Population 15 To 44
    Original Eqn: INTEG( ( maturation 14 to 15 - deaths 15 to 44 - maturation 44 to 45 ) , initial population 15 to 44 )
    Units: Person
    Limits: (None, None)
    Type: component

    World population, AGES 15-44 (P2#6)
    """
    return integ_population_15_to_44()


@cache('run')
def initial_population_15_to_44():
    """
    Real Name: initial population 15 to 44
    Original Eqn: 7e+08
    Units: Person
    Limits: (None, None)
    Type: constant

    The initial number of people aged 15 to 44                 (P2I#6.2).
    """
    return 7e+08


@cache('step')
def population_45_to_64():
    """
    Real Name: Population 45 To 64
    Original Eqn: INTEG( ( maturation 44 to 45 - deaths 45 to 64 - maturation 64 to 65 ) , initial population 54 to 64 )
    Units: Person
    Limits: (None, None)
    Type: component

    The world population aged 0 to 14 (P3#10).
    """
    return integ_population_45_to_64()


@cache('run')
def initial_population_54_to_64():
    """
    Real Name: initial population 54 to 64
    Original Eqn: 1.9e+08
    Units: Person
    Limits: (None, None)
    Type: constant

    The initial number of people aged 45 to 64                 (P3I#10.2).
    """
    return 1.9e+08


@cache('step')
def population_65_plus():
    """
    Real Name: Population 65 Plus
    Original Eqn: INTEG( ( maturation 64 to 65 - deaths 65 plus ) , initial population 65 plus )
    Units: Person
    Limits: (None, None)
    Type: component

    The world population aged 65 and over (P4#14).
    """
    return integ_population_65_plus()


@cache('run')
def initial_population_65_plus():
    """
    Real Name: initial population 65 plus
    Original Eqn: 6e+07
    Units: Person
    Limits: (None, None)
    Type: constant

    The initial number of people aged 65 and over                 (P4I#14.2)
    """
    return 6e+07


@cache('step')
def population():
    """
    Real Name: population
    Original Eqn: Population 0 To 14 + Population 15 To 44 + Population 45 To 64 + Population 65 Plus
    Units: Person
    Limits: (None, None)
    Type: component

    Total world population in all age groups (POP#1).
    """
    return population_0_to_14() + population_15_to_44() + population_45_to_64(
    ) + population_65_plus()


@cache('step')
def average_industrial_output_per_capita():
    """
    Real Name: average industrial output per capita
    Original Eqn: SMOOTH ( industrial output per capita , income expectation averaging time )
    Units: $/(Person*year)
    Limits: (None, None)
    Type: component

    Average industrial output per capita (AIOPC#43).
    """
    return smooth_industrial_output_per_capita_income_expectation_averaging_time_industrial_output_per_capita_1(
    )


@cache('step')
def birth_rate():
    """
    Real Name: birth rate
    Original Eqn: THOUSAND * births / population
    Units: C/year
    Limits: (None, None)
    Type: component

    The crude birth rate measured in people per thousand                 people per year (CBR#31).
    """
    return thousand() * births() / population()


@cache('step')
def births():
    """
    Real Name: births
    Original Eqn: IF THEN ELSE ( Time >= population equilibrium time , deaths , ( total fertility * Population 15 To 44 * 0.5 / reproductive lifetime ) )
    Units: Person/year
    Limits: (None, None)
    Type: component

    The total number of births in the world (B#30).
    """
    return functions.if_then_else(
        time() >= population_equilibrium_time(), deaths(),
        (total_fertility() * population_15_to_44() * 0.5 / reproductive_lifetime()))


@cache('step')
def completed_multiplier_from_perceived_lifetime():
    """
    Real Name: completed multiplier from perceived lifetime
    Original Eqn: completed multiplier from perceived lifetime table ( perceived life expectancy/one year\ )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    COMPENSATORY MULTIPLIER FROM PERCEIVED LIFE                 EXPECTANCY (CMPLE#36).
    """
    return completed_multiplier_from_perceived_lifetime_table(
        perceived_life_expectancy() / one_year())


def completed_multiplier_from_perceived_lifetime_table(x):
    """
    Real Name: completed multiplier from perceived lifetime table
    Original Eqn: ( (0,3),(10,2.1),(20,1.6),(30,1.4),(40,1.3),(50,1.2),(60,1.1) ,(70,1.05),(80,1) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating perceived life expectancy to birth                 rate compensation (CMPLET#36.1).
    """
    return functions.lookup(x, [0, 10, 20, 30, 40, 50, 60, 70, 80],
                            [3, 2.1, 1.6, 1.4, 1.3, 1.2, 1.1, 1.05, 1])


@cache('step')
def delayed_industrial_output_per_capita():
    """
    Real Name: delayed industrial output per capita
    Original Eqn: SMOOTH3 ( industrial output per capita , social adjustment delay )
    Units: $/(Person*year)
    Limits: (None, None)
    Type: component

    Delayed industrial output per capita (DIOPC#40).
    """
    return smooth_industrial_output_per_capita_social_adjustment_delay_industrial_output_per_capita_3(
    )


@cache('step')
def desired_completed_family_size():
    """
    Real Name: desired completed family size
    Original Eqn: IF THEN ELSE ( Time >= zero population growth time , 2, desired completed family size normal * family response to social norm * social family size normal )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Desired completed family size (DCFS#38)
    """
    return functions.if_then_else(
        time() >= zero_population_growth_time(), 2,
        desired_completed_family_size_normal() * family_response_to_social_norm() *
        social_family_size_normal())


@cache('run')
def desired_completed_family_size_normal():
    """
    Real Name: desired completed family size normal
    Original Eqn: 3.8
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    DESIRED COMPLETED FAMILY SIZE NORMAL (DCFSN#38.2).
    """
    return 3.8


@cache('step')
def desired_total_fertility():
    """
    Real Name: desired total fertility
    Original Eqn: desired completed family size * completed multiplier from perceived lifetime
    Units: Dmnl
    Limits: (None, None)
    Type: component

    DESIRED TOTAL FERTILITY (DTF#35).
    """
    return desired_completed_family_size() * completed_multiplier_from_perceived_lifetime()


@cache('step')
def family_income_expectation():
    """
    Real Name: family income expectation
    Original Eqn: ( industrial output per capita - average industrial output per capita ) / average industrial output per capita
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Family income expectations (FIE#42).
    """
    return (industrial_output_per_capita() -
            average_industrial_output_per_capita()) / average_industrial_output_per_capita()


@cache('step')
def family_response_to_social_norm():
    """
    Real Name: family response to social norm
    Original Eqn: family response to social norm table ( family income expectation )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    FAMILY RESPONSE TO SOCIAL NORM (FRSN#41).
    """
    return family_response_to_social_norm_table(family_income_expectation())


def family_response_to_social_norm_table(x):
    """
    Real Name: family response to social norm table
    Original Eqn: ( (-0.2,0.5),(-0.1,0.6),(0,0.7),(0.1,0.85),(0.2,1) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    The table relating income expectations to family                 size (FRSNT#41.1).
    """
    return functions.lookup(x, [-0.2, -0.1, 0, 0.1, 0.2], [0.5, 0.6, 0.7, 0.85, 1])


@cache('step')
def fecundity_multiplier():
    """
    Real Name: fecundity multiplier
    Original Eqn: fecundity multiplier table ( life expectancy/one year )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    FECUNDITY MULTIPLIER (FM#34).
    """
    return fecundity_multiplier_table(life_expectancy() / one_year())


def fecundity_multiplier_table(x):
    """
    Real Name: fecundity multiplier table
    Original Eqn: ( (0,0),(10,0.2),(20,0.4),(30,0.6),(40,0.7),(50,0.75),(60,0.79) ,(70,0.84),(80,0.87) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating life expectancy to fecundity                 (FMT#34.1).
    """
    return functions.lookup(x, [0, 10, 20, 30, 40, 50, 60, 70, 80],
                            [0, 0.2, 0.4, 0.6, 0.7, 0.75, 0.79, 0.84, 0.87])


@cache('step')
def fertility_control_allocation_per_capita():
    """
    Real Name: fertility control allocation per capita
    Original Eqn: fraction services allocated to fertility control * service output per capita
    Units: $/(Person*year)
    Limits: (None, None)
    Type: component

    FERTILITY CONTROL ALLOCATIONS PER CAPITA (FCAPC#47).
    """
    return fraction_services_allocated_to_fertility_control() * service_output_per_capita()


@cache('step')
def fertility_control_effectiveness():
    """
    Real Name: fertility control effectiveness
    Original Eqn: IF THEN ELSE ( Time >= fertility control effectiveness time , 1 , ( fertility control effectiveness table ( fertility control facilities per capita/GDP pc unit ) ) )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Fertility control effectiveness (FCE#45).
    """
    return functions.if_then_else(time() >= fertility_control_effectiveness_time(), 1,
                                  (fertility_control_effectiveness_table(
                                      fertility_control_facilities_per_capita() / gdp_pc_unit())))


def fertility_control_effectiveness_table(x):
    """
    Real Name: fertility control effectiveness table
    Original Eqn: ( (0,0.75),(0.5,0.85),(1,0.9),(1.5,0.95),(2,0.98),(2.5,0.99) ,(3,1) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Fertility control effectiveness table (FCET#45.2).
    """
    return functions.lookup(x, [0, 0.5, 1, 1.5, 2, 2.5, 3], [0.75, 0.85, 0.9, 0.95, 0.98, 0.99, 1])


@cache('step')
def fertility_control_facilities_per_capita():
    """
    Real Name: fertility control facilities per capita
    Original Eqn: SMOOTH3 ( fertility control allocation per capita , health services impact delay )
    Units: $/(Person*year)
    Limits: (None, None)
    Type: component

    FERTILITY CONTROL FACILITIES PER CAPITA (FCFPC#46).
    """
    return smooth_fertility_control_allocation_per_capita_health_services_impact_delay_fertility_control_allocation_per_capita_3(
    )


@cache('step')
def fraction_services_allocated_to_fertility_control():
    """
    Real Name: fraction services allocated to fertility control
    Original Eqn: fraction services allocated to fertility control table ( need for fertility control\ )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    FRACTION OF SERVICES ALLOCATED TO FERTILITY CONTROL                 (FSAFC#48).
    """
    return fraction_services_allocated_to_fertility_control_table(need_for_fertility_control())


def fraction_services_allocated_to_fertility_control_table(x):
    """
    Real Name: fraction services allocated to fertility control table
    Original Eqn: ( (0,0),(2,0.005),(4,0.015),(6,0.025),(8,0.03),(10,0.035) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating the need for fertility control to                 services allocated. (FSAFCT#48.1).
    """
    return functions.lookup(x, [0, 2, 4, 6, 8, 10], [0, 0.005, 0.015, 0.025, 0.03, 0.035])


@cache('run')
def income_expectation_averaging_time():
    """
    Real Name: income expectation averaging time
    Original Eqn: 3
    Units: year
    Limits: (None, None)
    Type: constant

    Income expectation averaging time (IEAT#43.1)
    """
    return 3


@cache('run')
def lifetime_perception_delay():
    """
    Real Name: lifetime perception delay
    Original Eqn: 20
    Units: year
    Limits: (None, None)
    Type: constant

    Lifetime perception delay (LPD#37.1)
    """
    return 20


@cache('step')
def maximum_total_fertility():
    """
    Real Name: maximum total fertility
    Original Eqn: maximum total fertility normal * fecundity multiplier
    Units: Dmnl
    Limits: (None, None)
    Type: component

    MAXIMUM TOTAL FERTILITY (MTF#33).
    """
    return maximum_total_fertility_normal() * fecundity_multiplier()


@cache('run')
def maximum_total_fertility_normal():
    """
    Real Name: maximum total fertility normal
    Original Eqn: 12
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    The normal maximum fertility that would be realized                if people had sufficient food and perfect health.                 (MTFN#33.1)
    """
    return 12


@cache('step')
def need_for_fertility_control():
    """
    Real Name: need for fertility control
    Original Eqn: ( maximum total fertility / desired total fertility ) - 1
    Units: Dmnl
    Limits: (None, None)
    Type: component

    NEED FOR FERTILITY CONTROL (NFC#44).
    """
    return (maximum_total_fertility() / desired_total_fertility()) - 1


@cache('step')
def perceived_life_expectancy():
    """
    Real Name: perceived life expectancy
    Original Eqn: SMOOTH3 ( life expectancy , lifetime perception delay )
    Units: year
    Limits: (None, None)
    Type: component

    Perceived life expectancy (PLE#37)
    """
    return smooth_life_expectancy_lifetime_perception_delay_life_expectancy_3()


@cache('run')
def reproductive_lifetime():
    """
    Real Name: reproductive lifetime
    Original Eqn: 30
    Units: year
    Limits: (None, None)
    Type: constant

    The number of years people can reproduce (RLT#30.1)
    """
    return 30


@cache('step')
def social_family_size_normal():
    """
    Real Name: social family size normal
    Original Eqn: social family size normal table ( delayed industrial output per capita/GDP pc unit )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    SOCIAL FAMILY SIZE NORM (SFN#39).
    """
    return social_family_size_normal_table(delayed_industrial_output_per_capita() / gdp_pc_unit())


def social_family_size_normal_table(x):
    """
    Real Name: social family size normal table
    Original Eqn: ( (0,1.25),(200,0.94),(400,0.715),(600,0.59),(800,0.5))
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating material well being to family size                 (SFNT#39.1)
    """
    return functions.lookup(x, [0, 200, 400, 600, 800], [1.25, 0.94, 0.715, 0.59, 0.5])


@cache('run')
def social_adjustment_delay():
    """
    Real Name: social adjustment delay
    Original Eqn: 20
    Units: year
    Limits: (None, None)
    Type: constant

    SOCIAL ADJUSTMENT DELAY (SAD#40.1).
    """
    return 20


@cache('run')
def fertility_control_effectiveness_time():
    """
    Real Name: fertility control effectiveness time
    Original Eqn: 4000
    Units: year
    Limits: (None, None)
    Type: constant

    FERTILITY CONTROL EFFECTIVENESS SET TIME                 (FCEST#45.1).
    """
    return 2002


@cache('run')
def population_equilibrium_time():
    """
    Real Name: population equilibrium time
    Original Eqn: 4000
    Units: year
    Limits: (None, None)
    Type: constant

    The time at which, as a model test, the population                 is forced to remain constant. (PET#30.2)
    """
    return 4000


@cache('run')
def zero_population_growth_time():
    """
    Real Name: zero population growth time
    Original Eqn: 4000
    Units: year
    Limits: (None, None)
    Type: constant

    TIME WHEN DESIRED FAMILY SIZE EQUALS 2 CHILDREN                 (ZPGT#38.1)
    """
    return 2002


@cache('run')
def thousand():
    """
    Real Name: THOUSAND
    Original Eqn: 1000
    Units: C
    Limits: (None, None)
    Type: constant

    Units converted for /1000 rates (--).
    """
    return 1000


@cache('step')
def total_fertility():
    """
    Real Name: total fertility
    Original Eqn: MIN ( maximum total fertility , ( maximum total fertility * ( 1 - fertility control effectiveness ) + desired total fertility * fertility control effectiveness ) )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    TOTAL FERTILITY (TF#32).
    """
    return np.minimum(maximum_total_fertility(),
                      (maximum_total_fertility() * (1 - fertility_control_effectiveness()) +
                       desired_total_fertility() * fertility_control_effectiveness()))


@cache('step')
def crowding_multiplier_from_industry():
    """
    Real Name: crowding multiplier from industry
    Original Eqn: crowding multiplier from industry table ( industrial output per capita/GDP pc unit )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    CROWDING MULTIPLIER FROM INDUSTRIALIZATION (CMI#27).
    """
    return crowding_multiplier_from_industry_table(industrial_output_per_capita() / gdp_pc_unit())


def crowding_multiplier_from_industry_table(x):
    """
    Real Name: crowding multiplier from industry table
    Original Eqn: ( (0,0.5),(200,0.05),(400,-0.1),(600,-0.08),(800,-0.02),(1000,0.05) ,(1200,0.1),(1400,0.15),(1600,0.2) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating industrial output to crowding                 (CMIT#27.1).
    """
    return functions.lookup(x, [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600],
                            [0.5, 0.05, -0.1, -0.08, -0.02, 0.05, 0.1, 0.15, 0.2])


@cache('step')
def death_rate():
    """
    Real Name: death rate
    Original Eqn: THOUSAND * deaths / population
    Units: C/year
    Limits: (None, None)
    Type: component

    CRUDE DEATH RATE (CDR#18)
    """
    return thousand() * deaths() / population()


@cache('step')
def deaths():
    """
    Real Name: deaths
    Original Eqn: deaths 0 to 14 + deaths 15 to 44 + deaths 45 to 64 + deaths 65 plus
    Units: Person/year
    Limits: (None, None)
    Type: component

    The total number of deaths per year for all age                 groups (D#17).
    """
    return deaths_0_to_14() + deaths_15_to_44() + deaths_45_to_64() + deaths_65_plus()


@cache('step')
def effective_health_services_per_capita():
    """
    Real Name: effective health services per capita
    Original Eqn: SMOOTH ( health services per capita , health services impact delay )
    Units: $/(Person*year)
    Limits: (None, None)
    Type: component

    Effective health services per capita - delayed from                 allocation (EHSPC#22)
    """
    return smooth_health_services_per_capita_health_services_impact_delay_health_services_per_capita_1(
    )


@cache('step')
def fraction_of_population_urban():
    """
    Real Name: fraction of population urban
    Original Eqn: fraction of population urban table ( population/unit population )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    FRACTION OF POPULATION URBAN (FPU#26).
    """
    return fraction_of_population_urban_table(population() / unit_population())


def fraction_of_population_urban_table(x):
    """
    Real Name: fraction of population urban table
    Original Eqn: ( (0,0),(2e+09,0.2),(4e+09,0.4),(6e+09,0.5),(8e+09,0.58) ,(1e+10,0.65),(1.2e+10,0.72),(1.4e+10,0.78),(1.6e+10,0.8) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating population to the fraction of                 population that is urban (FPUT#26.1).
    """
    return functions.lookup(x, [0, 2e+09, 4e+09, 6e+09, 8e+09, 1e+10, 1.2e+10, 1.4e+10, 1.6e+10],
                            [0, 0.2, 0.4, 0.5, 0.58, 0.65, 0.72, 0.78, 0.8])


@cache('step')
def health_services_per_capita():
    """
    Real Name: health services per capita
    Original Eqn: health services per capita table ( service output per capita/GDP pc unit )
    Units: $/(Person*year)
    Limits: (None, None)
    Type: component

    Health services allocation per capita (HSAPC#21).
    """
    return health_services_per_capita_table(service_output_per_capita() / gdp_pc_unit())


def health_services_per_capita_table(x):
    """
    Real Name: health services per capita table
    Original Eqn: ( (0,0),(250,20),(500,50),(750,95),(1000,140),(1250,175),(1500,200) ,(1750,220),(2000,230) )
    Units: $/(Person*year)
    Limits: (None, None)
    Type: lookup

    The table relating service output to health services                 (HSAPCT#21.1).
    """
    return functions.lookup(x, [0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000],
                            [0, 20, 50, 95, 140, 175, 200, 220, 230])


@cache('run')
def health_services_impact_delay():
    """
    Real Name: health services impact delay
    Original Eqn: 20
    Units: year
    Limits: (None, None)
    Type: constant

    The delay between allocating health services, and                 realizing the benefit (HSID#22.1).
    """
    return 20


@cache('run')
def life_expectancy_normal():
    """
    Real Name: life expectancy normal
    Original Eqn: 28
    Units: year
    Limits: (None, None)
    Type: constant

    The normal life expectancy with subsistance food, no                 medical care and no industrialization (LEN#19.1)
    """
    return 28


@cache('step')
def life_expectancy():
    """
    Real Name: life expectancy
    Original Eqn: life expectancy normal * lifetime multiplier from food * lifetime multiplier from health services * lifetime multiplier from persistent pollution * lifetime multiplier from crowding
    Units: year
    Limits: (None, None)
    Type: component

    The average life expectancy (LE#19).
    """
    return life_expectancy_normal() * lifetime_multiplier_from_food(
    ) * lifetime_multiplier_from_health_services() * lifetime_multiplier_from_persistent_pollution(
    ) * lifetime_multiplier_from_crowding()


@cache('step')
def lifetime_multiplier_from_crowding():
    """
    Real Name: lifetime multiplier from crowding
    Original Eqn: 1 - ( crowding multiplier from industry * fraction of population urban )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    LIFETIME MULTIPLIER FROM CROWDING (LMC#28)
    """
    return 1 - (crowding_multiplier_from_industry() * fraction_of_population_urban())


@cache('step')
def lifetime_multiplier_from_food():
    """
    Real Name: lifetime multiplier from food
    Original Eqn: lifetime multiplier from food table ( food per capita / subsistence food per capita )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    The life expectancy multiplier from food (LMF#20)
    """
    return lifetime_multiplier_from_food_table(food_per_capita() / subsistence_food_per_capita())


def lifetime_multiplier_from_food_table(x):
    """
    Real Name: lifetime multiplier from food table
    Original Eqn: ( (0,0),(1,1),(2,1.43),(3,1.5),(4,1.5),(5,1.5) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    The table ralating relative food to the life                 expectancy multiplier for food (LMFT#20.1)
    """
    return functions.lookup(x, [0, 1, 2, 3, 4, 5], [0, 1, 1.43, 1.5, 1.5, 1.5])


@cache('step')
def lifetime_multiplier_from_health_services():
    """
    Real Name: lifetime multiplier from health services
    Original Eqn: IF THEN ELSE ( Time > 1940, lifetime multiplier from health services 2 , lifetime multiplier from health services 1 )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    The life expectancy multiplier from health services                 (LMHS#23).
    """
    return functions.if_then_else(time() > 1940, lifetime_multiplier_from_health_services_2(),
                                  lifetime_multiplier_from_health_services_1())


@cache('step')
def lifetime_multiplier_from_health_services_1():
    """
    Real Name: lifetime multiplier from health services 1
    Original Eqn: lifetime multiplier from health services 1 table ( effective health services per capita/GDP pc unit )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    The life expectancy multiplier from health services                 before 1940 (LMHS1#24).
    """
    return lifetime_multiplier_from_health_services_1_table(
        effective_health_services_per_capita() / gdp_pc_unit())


def lifetime_multiplier_from_health_services_1_table(x):
    """
    Real Name: lifetime multiplier from health services 1 table
    Original Eqn: ( (0,1),(20,1.1),(40,1.4),(60,1.6),(80,1.7),(100,1.8) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating effective health care to life                 expectancy (LMHS1T#24.1).
    """
    return functions.lookup(x, [0, 20, 40, 60, 80, 100], [1, 1.1, 1.4, 1.6, 1.7, 1.8])


@cache('step')
def lifetime_multiplier_from_health_services_2():
    """
    Real Name: lifetime multiplier from health services 2
    Original Eqn: lifetime multiplier from health services 2 table ( effective health services per capita/GDP pc unit )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    The life expectancy multipier from health services                 value after 1940 (LMHS2#25).
    """
    return lifetime_multiplier_from_health_services_2_table(
        effective_health_services_per_capita() / gdp_pc_unit())


def lifetime_multiplier_from_health_services_2_table(x):
    """
    Real Name: lifetime multiplier from health services 2 table
    Original Eqn: ( (0,1),(20,1.5),(40,1.9),(60,2),(80,2),(100,2) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating effective health care to life                 expectancy (LMHS2T#25.1)
    """
    return functions.lookup(x, [0, 20, 40, 60, 80, 100], [1, 1.5, 1.9, 2, 2, 2])


@cache('step')
def lifetime_multiplier_from_persistent_pollution():
    """
    Real Name: lifetime multiplier from persistent pollution
    Original Eqn: lifetime multiplier from persistent pollution table ( persistent pollution index\ )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    LIFETIME MULTIPLIER FROM PERSISTENT POLLUTION                 (LMP#29)
    """
    return lifetime_multiplier_from_persistent_pollution_table(persistent_pollution_index())


def lifetime_multiplier_from_persistent_pollution_table(x):
    """
    Real Name: lifetime multiplier from persistent pollution table
    Original Eqn: ( (0,1),(10,0.99),(20,0.97),(30,0.95),(40,0.9),(50,0.85),(60,0.75) ,(70,0.65),(80,0.55),(90,0.4),(100,0.2) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating persistent pollution to life                 expectancy (LMPT#29.1)
    """
    return functions.lookup(x, [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
                            [1, 0.99, 0.97, 0.95, 0.9, 0.85, 0.75, 0.65, 0.55, 0.4, 0.2])


@cache('run')
def desired_resource_use_rate():
    """
    Real Name: desired resource use rate
    Original Eqn: 4.8e+09
    Units: Resource units/year
    Limits: (None, None)
    Type: constant

    Desired non-renewable resource usage rate (DNRUR#--)
    """
    return 4.8e+09


@cache('step')
def fraction_of_resources_remaining():
    """
    Real Name: fraction of resources remaining
    Original Eqn: Nonrenewable Resources / initial nonrenewable resources
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Non-renewable resource fraction remaining                 (NRFR#133).
    """
    return nonrenewable_resources() / initial_nonrenewable_resources()


@cache('step')
def resource_usage_rate():
    """
    Real Name: resource usage rate
    Original Eqn: ( ( ( population ) ) * ( per capita resource use multiplier ) ) * ( resource use factor )
    Units: Resource units/year
    Limits: (None, None)
    Type: component

    Non-renewable resource use rate (NRUR#130).
    """
    return (((population())) * (per_capita_resource_use_multiplier())) * (resource_use_factor())


@cache('run')
def initial_nonrenewable_resources():
    """
    Real Name: initial nonrenewable resources
    Original Eqn: 1e+12
    Units: Resource units
    Limits: (None, None)
    Type: constant

    NONRENEWABLE RESOURCE INITIAL (NRI#129.2).
    """
    return 2e+12


@cache('step')
def nonrenewable_resources():
    """
    Real Name: Nonrenewable Resources
    Original Eqn: INTEG( ( - resource usage rate ) , initial nonrenewable resources )
    Units: Resource units
    Limits: (None, None)
    Type: component

    Non-renewable resource (NR#129)
    """
    return integ_nonrenewable_resources()


@cache('step')
def fraction_of_capital_allocated_to_obtaining_resources_1():
    """
    Real Name: fraction of capital allocated to obtaining resources 1
    Original Eqn: fraction of capital allocated to obtaining resources 1 table ( fraction of resources remaining )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Fraction of capital allocated to obtaining resources                 before switch time (FCAOR1#135).
    """
    return fraction_of_capital_allocated_to_obtaining_resources_1_table(
        fraction_of_resources_remaining())


def fraction_of_capital_allocated_to_obtaining_resources_1_table(x):
    """
    Real Name: fraction of capital allocated to obtaining resources 1 table
    Original Eqn: ( (0,1),(0.1,0.9),(0.2,0.7),(0.3,0.5),(0.4,0.2),(0.5,0.1),(0.6,0.05) ,(0.7,0.05),(0.8,0.05),(0.9,0.05),(1,0.05) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating the fraction of resources remaining                to capital allocated to resource extraction                 (FCAOR1T#135.1).
    """
    return functions.lookup(x, [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
                            [1, 0.9, 0.7, 0.5, 0.2, 0.1, 0.05, 0.05, 0.05, 0.05, 0.05])


@cache('step')
def fraction_of_capital_allocated_to_obtaining_resources_2():
    """
    Real Name: fraction of capital allocated to obtaining resources 2
    Original Eqn: fraction of capital allocated to obtaining resources 2 table ( fraction of resources remaining )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Fraction of capital allocated to obtaining resources                 after switch time (FCAOR2#136).
    """
    return fraction_of_capital_allocated_to_obtaining_resources_2_table(
        fraction_of_resources_remaining())


def fraction_of_capital_allocated_to_obtaining_resources_2_table(x):
    """
    Real Name: fraction of capital allocated to obtaining resources 2 table
    Original Eqn: ( (0,1),(0.1,0.2),(0.2,0.1),(0.3,0.05),(0.4,0.05),(0.5,0.05) ,(0.6,0.05),(0.7,0.05),(0.8,0.05),(0.9,0.05),(1,0.05) )
    Units: Dmnl
    Limits: (None, None)
    Type: lookup

    Table relating the fraction of resources remaining                to capital allocated to resource extraction                 (FCAOR2T#136.1).
    """
    return functions.lookup(x, [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
                            [1, 0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05])


@cache('run')
def resource_use_factor_1():
    """
    Real Name: resource use factor 1
    Original Eqn: 1
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    The nonrenewable resource usage factor before the                 policy year (NRUF1#131.1).
    """
    return 1


@cache('step')
def resource_use_fact_2():
    """
    Real Name: resource use fact 2
    Original Eqn: SMOOTH3 ( Resource Conservation Technology , technology development delay )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    The nonrenewable resource usage factor after the                 policy year (NRUF2#131.2).
    """
    return smooth_resource_conservation_technology_technology_development_delay_resource_conservation_technology_3(
    )


@cache('step')
def resource_technology_change_rate_multiplier():
    """
    Real Name: resource technology change rate multiplier
    Original Eqn: resource technology change mult table ( 1 - resource usage rate / desired resource use rate )
    Units: Dmnl/year
    Limits: (None, None)
    Type: component

    Resource technology change multiplier (NRCM#--)
    """
    return resource_technology_change_mult_table(
        1 - resource_usage_rate() / desired_resource_use_rate())


def resource_technology_change_mult_table(x):
    """
    Real Name: resource technology change mult table
    Original Eqn: ( (-1,0),(0,0) )
    Units: Dmnl/year
    Limits: (None, None)
    Type: lookup

    Table relating resource use to technological change.                 (NRCMT#--)
    """
    return functions.lookup(x, [-1, 0], [-0.04, 0])


@cache('step')
def per_capita_resource_use_multiplier():
    """
    Real Name: per capita resource use multiplier
    Original Eqn: per capita resource use mult table ( industrial output per capita/GDP pc unit )
    Units: Resource unit/(Person*year)
    Limits: (None, None)
    Type: component

    Per capita resource usage multiplier (PCRUM#132).
    """
    return per_capita_resource_use_mult_table(industrial_output_per_capita() / gdp_pc_unit())


def per_capita_resource_use_mult_table(x):
    """
    Real Name: per capita resource use mult table
    Original Eqn: ( (0,0),(200,0.85),(400,2.6),(600,3.4),(800,3.8),(1000,4.1), (1200,4.4),(1400,4.7),(1600,5) )
    Units: Resource units/(Person*year)
    Limits: (None, None)
    Type: lookup

    Table relating industrial output to resource usage                 per capita (PCRUMT#132.1).
    """
    return functions.lookup(x, [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600],
                            [0, 0.85, 2.6, 3.4, 3.8, 4.1, 4.4, 4.7, 5])


@cache('step')
def resource_conservation_technology():
    """
    Real Name: Resource Conservation Technology
    Original Eqn: INTEG ( resource technology change rate , 1)
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Non-renewable resource technology (NRTD#--)
    """
    return integ_resource_conservation_technology()


@cache('step')
def resource_technology_change_rate():
    """
    Real Name: resource technology change rate
    Original Eqn: IF THEN ELSE ( Time >= POLICY YEAR , Resource Conservation Technology * resource technology change rate multiplier , 0)
    Units: 1/year
    Limits: (None, None)
    Type: component

    RESOURCE TECHNOLOGY IMPROVEMENT RATE (NRATE-##).
    """
    return functions.if_then_else(
        time() >= policy_year(),
        resource_conservation_technology() * resource_technology_change_rate_multiplier(), 0)


@cache('step')
def fraction_of_industrial_capital_allocated_to_obtaining_resources():
    """
    Real Name: fraction of industrial capital allocated to obtaining resources
    Original Eqn: IF THEN ELSE ( Time >= fraction of industrial capital allocated to obtaining resources switch time\ , fraction of capital allocated to obtaining resources 2 , fraction of capital allocated to obtaining resources 1 )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    FRACTION OF CAPITAL ALLOCATED TO OBTAINING RESOURCES                 (FCAOR#134).
    """
    return functions.if_then_else(
        time() >= fraction_of_industrial_capital_allocated_to_obtaining_resources_switch_time(),
        fraction_of_capital_allocated_to_obtaining_resources_2(),
        fraction_of_capital_allocated_to_obtaining_resources_1())


@cache('step')
def resource_use_factor():
    """
    Real Name: resource use factor
    Original Eqn: IF THEN ELSE ( Time >= POLICY YEAR , resource use fact 2 , resource use factor 1 )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    NONRENEWABLE RESOURCE USAGE FACTOR (NRUF#131).
    """
    return functions.if_then_else(time() >= policy_year(), resource_use_fact_2(),
                                  resource_use_factor_1())


@cache('run')
def fraction_of_industrial_capital_allocated_to_obtaining_resources_switch_time():
    """
    Real Name: fraction of industrial capital allocated to obtaining resources switch time
    Original Eqn: 4000
    Units: year
    Limits: (None, None)
    Type: constant

    Time at which to switch between alternative fraction                of capital alocated to obtaining resources                 (FCAORTM#--).
    """
    return 2002


@cache('run')
def technology_development_delay():
    """
    Real Name: technology development delay
    Original Eqn: 20
    Units: year
    Limits: (None, None)
    Type: constant

    The technology development delay (TDD#--)
    """
    return 20


@cache('step')
def consumed_industrial_output():
    """
    Real Name: consumed industrial output
    Original Eqn: industrial output * fraction of industrial output allocated to consumption
    Units: $/year
    Limits: (None, None)
    Type: component

    Consumed industrial output (CIO#--).
    """
    return industrial_output() * fraction_of_industrial_output_allocated_to_consumption()


@cache('step')
def consumed_industrial_output_per_capita():
    """
    Real Name: consumed industrial output per capita
    Original Eqn: consumed industrial output / population
    Units: $/(Person*year)
    Limits: (None, None)
    Type: component

    Consumption Industrial Output per Capita (CIOPC#--)
    """
    return consumed_industrial_output() / population()


@cache('step')
def fraction_of_output_in_agriculture():
    """
    Real Name: fraction of output in agriculture
    Original Eqn: ( PRICE OF FOOD * food ) / ( PRICE OF FOOD * food + service output + industrial output )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    FRACTION OF OUTPUT IN AGRICULTURE (FAO#147)
    """
    return (price_of_food() * food()) / (
        price_of_food() * food() + service_output() + industrial_output())


@cache('step')
def fraction_of_output_in_industry():
    """
    Real Name: fraction of output in industry
    Original Eqn: industrial output / ( PRICE OF FOOD * food + service output + industrial output )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Fraction of output that is industrial output                 (FOI#148).
    """
    return industrial_output() / (
        price_of_food() * food() + service_output() + industrial_output())


@cache('step')
def fraction_of_output_in_services():
    """
    Real Name: fraction of output in services
    Original Eqn: service output / ( PRICE OF FOOD * food + service output + industrial output )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    FRACTION OF OUTPUT IN SERVICES (FOS#149).
    """
    return service_output() / (price_of_food() * food() + service_output() + industrial_output())


@cache('step')
def persistent_pollution_intensity_industry():
    """
    Real Name: persistent pollution intensity industry
    Original Eqn: persistent pollution generation industry * persistent pollution generation factor / industrial output
    Units: Pollution units/$
    Limits: (None, None)
    Type: component

    pollution intensity indicator (PLINID#--).
    """
    return persistent_pollution_generation_industry() * persistent_pollution_generation_factor(
    ) / industrial_output()


@cache('run')
def price_of_food():
    """
    Real Name: PRICE OF FOOD
    Original Eqn: 0.22
    Units: $/Veg eq kg
    Limits: (None, None)
    Type: constant

    The price of food used as a basis for comparing                 agricultural and industrial output. (--).
    """
    return 0.22


@cache('step')
def resource_use_intensity():
    """
    Real Name: resource use intensity
    Original Eqn: resource usage rate / industrial output
    Units: Resource units/$
    Limits: (None, None)
    Type: component

    ADAPTIVE TECHNOLOGICAL CONTROL CARDS nonrenewable                 resource usage intensity (RESINT#--)
    """
    return resource_usage_rate() / industrial_output()


integ_arable_land = functions.Integ(lambda: land_development_rate()-land_erosion_rate()-land_removal_for_urban_and_industrial_use(), lambda: initial_arable_land())

integ_potentially_arable_land = functions.Integ(lambda: (-land_development_rate()),
                                                lambda: initial_potentially_arable_land())

smooth_current_agricultural_inputs_average_life_agricultural_inputs_current_agricultural_inputs_1 = functions.Smooth(
    lambda: current_agricultural_inputs(), lambda: average_life_agricultural_inputs(),
    lambda: current_agricultural_inputs(), lambda: 1)

smooth_land_yield_technology_technology_development_delay_land_yield_technology_3 = functions.Smooth(
    lambda: land_yield_technology(), lambda: technology_development_delay(),
    lambda: land_yield_technology(), lambda: 3)

integ_land_yield_technology = functions.Integ(lambda: land_yield_technology_change_rate(),
                                              lambda: 1)

integ_urban_and_industrial_land = functions.Integ(
    lambda: (land_removal_for_urban_and_industrial_use()),
    lambda: initial_urban_and_industrial_land())

integ_land_fertility = functions.Integ(
    lambda: (land_fertility_regeneration() - land_fertility_degredation()),
    lambda: initial_land_fertility())

smooth_food_ratio_food_shortage_perception_delay_food_ratio_1 = functions.Smooth(
    lambda: food_ratio(), lambda: food_shortage_perception_delay(), lambda: food_ratio(),
    lambda: 1)

integ_industrial_capital = functions.Integ(
    lambda: (industrial_capital_investment() - industrial_capital_depreciation()),
    lambda: initial_industrial_capital())

smooth_labor_utilization_fraction_labor_utilization_fraction_delay_time_1_1 = functions.Smooth(
    lambda: labor_utilization_fraction(), lambda: labor_utilization_fraction_delay_time(),
    lambda: 1, lambda: 1)

integ_service_capital = functions.Integ(
    lambda: (service_capital_investment() - service_capital_depreciation()),
    lambda: initial_service_capital())

smooth_persistent_pollution_technology_technology_development_delay_persistent_pollution_technology_3 = functions.Smooth(
    lambda: persistent_pollution_technology(), lambda: technology_development_delay(),
    lambda: persistent_pollution_technology(), lambda: 3)

integ_persistent_pollution = functions.Integ(
    lambda: (persistent_pollution_appearance_rate() - persistent_pollution_assimilation_rate()),
    lambda: initial_persistent_pollution())

delay_persistent_pollution_generation_rate_persistent_pollution_transmission_delay_persistent_pollution_generation_rate_3 = functions.Delay(
    lambda: persistent_pollution_generation_rate(),
    lambda: persistent_pollution_transmission_delay(),
    lambda: persistent_pollution_generation_rate(), lambda: 3)

integ_persistent_pollution_technology = functions.Integ(
    lambda: persistent_pollution_technology_change_rate(), lambda: 1)

integ_population_0_to_14 = functions.Integ(
    lambda: (births() - deaths_0_to_14() - maturation_14_to_15()),
    lambda: initial_population_0_to_14())

integ_population_15_to_44 = functions.Integ(
    lambda: (maturation_14_to_15() - deaths_15_to_44() - maturation_44_to_45()),
    lambda: initial_population_15_to_44())

integ_population_45_to_64 = functions.Integ(
    lambda: (maturation_44_to_45() - deaths_45_to_64() - maturation_64_to_65()),
    lambda: initial_population_54_to_64())

integ_population_65_plus = functions.Integ(lambda: (maturation_64_to_65() - deaths_65_plus()),
                                           lambda: initial_population_65_plus())

smooth_industrial_output_per_capita_income_expectation_averaging_time_industrial_output_per_capita_1 = functions.Smooth(
    lambda: industrial_output_per_capita(), lambda: income_expectation_averaging_time(),
    lambda: industrial_output_per_capita(), lambda: 1)

smooth_industrial_output_per_capita_social_adjustment_delay_industrial_output_per_capita_3 = functions.Smooth(
    lambda: industrial_output_per_capita(), lambda: social_adjustment_delay(),
    lambda: industrial_output_per_capita(), lambda: 3)

smooth_fertility_control_allocation_per_capita_health_services_impact_delay_fertility_control_allocation_per_capita_3 = functions.Smooth(
    lambda: fertility_control_allocation_per_capita(), lambda: health_services_impact_delay(),
    lambda: fertility_control_allocation_per_capita(), lambda: 3)

smooth_life_expectancy_lifetime_perception_delay_life_expectancy_3 = functions.Smooth(
    lambda: life_expectancy(), lambda: lifetime_perception_delay(), lambda: life_expectancy(),
    lambda: 3)

smooth_health_services_per_capita_health_services_impact_delay_health_services_per_capita_1 = functions.Smooth(
    lambda: health_services_per_capita(), lambda: health_services_impact_delay(),
    lambda: health_services_per_capita(), lambda: 1)

integ_nonrenewable_resources = functions.Integ(lambda: (-resource_usage_rate()),
                                               lambda: initial_nonrenewable_resources())

smooth_resource_conservation_technology_technology_development_delay_resource_conservation_technology_3 = functions.Smooth(
    lambda: resource_conservation_technology(), lambda: technology_development_delay(),
    lambda: resource_conservation_technology(), lambda: 3)

integ_resource_conservation_technology = functions.Integ(lambda: resource_technology_change_rate(),
                                                         lambda: 1)
