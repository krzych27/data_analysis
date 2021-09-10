import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import copy
from functools import reduce
from datetime import datetime, timedelta
from pathlib import Path
from plots import Plots
from reading_data import ReadingData

if __name__ == "__main__":
    preprocessing_data = ReadingData()
    preprocessing_data.reading_data('data/marzec_2014_2.xlsx', 'results/2014_marzec')
    preprocessing_data.reading_data('data/wrzesien_2014_2.xlsx', 'results/2014_wrzesien')

    path = 'results'
    directories = ['2014_marzec', '2014_wrzesien', '2015_czerwiec', '2015_wrzesien', '2016_marzec', '2016_wrzesien',
                   '2017_czerwiec', '2017_wrzesien', '2018_czerwiec', '2018_wrzesien', '2019_sierpien']

    list_range_year = preprocessing_data.reading_question(directories, 'przedzial_wiekowy')
    list_education = preprocessing_data.reading_question(directories, 'wyksztalcenie')
    list_accomodation = preprocessing_data.reading_question(directories, 'miejsce_zamieszkania')
    list_A2 = preprocessing_data.reading_question(directories, 'A2')
    list_A3 = preprocessing_data.reading_question(directories, 'A3')
    fear_list_questions = ['B4', 'B5', 'C10', 'C11', 'C16']
    fear_columns_number = [1, 1, 5, 3, 11]
    list_fear_index = preprocessing_data.reading_question_to_index(directories, fear_list_questions,
                                                                   fear_columns_number)

    plot = Plots()
    list_range_year_dict = plot.calculate_structure_population_age_based_range(list_range_year, directories)
    list_education_dict = plot.calculate_structure_education(list_education, directories)
    list_accomodation_dict = plot.calculate_structure_accomodation(list_accomodation, directories)
    list_A2_dict = plot.calculate_A2(list_A2, directories)
    list_A2_dict_with_3_cat = plot.calculate_A2_with_3_cat(list_A2, directories)
    list_fear, list_fear_dict, list_fear_dict_3_cat, affective_dict, cognitive_dict, \
    behavioral_dict = plot.calculate_fear_index(list_fear_index, directories)

    label_list = ["Zdecydowanie tak", "Raczej tak", "Ani tak, ani nie",
                  "Raczej nie", "Zdecydowanie nie"]

    label_list_3_cat = ["tak", "Ani tak, ani nie", "nie"]

    label_list_fear = ["bardzo niski", "raczej niski", "średni",
                       "raczej wysoki", "bardzo wysoki"]
    label_list_fear_3_cat = ["niski", "średni", "wysoki"]

    plot.create_time_series(list_A2_dict, 'A2', 5, label_list)
    plot.create_time_series(list_fear_dict, 'fear_index', 5, label_list_fear)








