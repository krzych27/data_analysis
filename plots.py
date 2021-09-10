import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits import mplot3d
import pandas as pd
import numpy as np
import seaborn as sns
import copy
import collections
from functools import reduce
from pathlib import Path
from statistical_tests import StatisticalTests
from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates


class Plots:

    def __init__(self):
        pass

    def change_to_percents(self, df, label_list, number_columns):
        sum_elements = sum(list(df.values()))
        temp_value = [0 for i in range(number_columns + 1)]
        res_dict = dict(zip(label_list, temp_value))
        for i in label_list:
            res_dict[i] = (df[i] / sum_elements) * 100

        return res_dict

    def calculate_structure_population_age_based_range(self, list_df, save_name):
        x_pos = list()
        y_pos = ['2014a', '2014b', '2015a', '2015b', '2016a', '2016b', '2017a', '2017b', '2018a', '2018b', '2019']
        z_pos = list()
        # label_list = [i + 1 for i in range(6)]
        label_list = ['18-24', "25-34", '35-44', '45-54', '55-64', '65+']
        temp_value = [0 for i in range(6)]
        structure_population_list = list()
        for df, save in zip(list_df, save_name):
            # print('df in calculate')
            # print(df)
            range_birth = (df.iloc[:, 1]).to_list()
            # print('range_birth')
            # print(range_birth)
            structure_population = dict(zip(label_list, temp_value))
            for year in range_birth:
                if year == '18-24':
                    structure_population[label_list[0]] += 1
                elif year == '25-34':
                    structure_population[label_list[1]] += 1
                elif year == '35-44':
                    structure_population[label_list[2]] += 1
                elif year == '45-54':
                    structure_population[label_list[3]] += 1
                elif year == '55-64':
                    structure_population[label_list[4]] += 1
                elif year == '65+':
                    structure_population[label_list[5]] += 1
                else:
                    continue

            structure_population_list.append(structure_population)

            x_pos.append(structure_population.values())
            z_pos.append(structure_population.keys())
            plt.bar(structure_population.keys(), structure_population.values())
            plt.ylim(top=1000)
            plt.ylim(bottom=0)
            plt.xlabel('Grupa wiekowa')
            plt.ylabel('Ilość osób')
            temp_name = save.split('_')
            year = temp_name[0]
            month = temp_name[1]
            plt.title('Histogram struktury wieku uczestników badania - ' + year + ' ' + month, fontsize=10)
            plt.savefig('results/histograms/population_age/hist_' + save + '.png')
            plt.clf()

        plt.savefig('results/histograms/population_age/hist_3d.png')
        plt.clf()
        return structure_population_list

    def calculate_structure_education(self, list_df, save_name):
        legend_list = ["Podstawowe", "Zasadnicze zawodowe", "Średnie ogólnokształcące", "Średnie techniczne",
                       "Pomaturalne", "Studia wyższe niepełne", "Studia wyższe ukończone"]
        temp_value = [0 for i in range(7)]
        label_list = [i + 1 for i in range(7)]
        education_list = list()
        for df, save in zip(list_df, save_name):
            temp = df.iloc[:, 1].to_list()
            education_dict = dict(zip(label_list, temp_value))
            for i in df.iloc[:, 1].to_list():
                if i == 1:
                    education_dict[label_list[0]] += 1
                elif i == 2:
                    education_dict[label_list[1]] += 1
                elif i == 3:
                    education_dict[label_list[2]] += 1
                elif i == 4:
                    education_dict[label_list[3]] += 1
                elif i == 5:
                    education_dict[label_list[4]] += 1
                elif i == 6:
                    education_dict[label_list[5]] += 1
                elif i == 7:
                    education_dict[label_list[6]] += 1

            education_dict_percents = self.change_to_percents(education_dict, label_list, 7)
            education_list.append(education_dict_percents)
            colors = list('rgbkymc')
            handles = list()
            plt.bar(education_dict.keys(), education_dict.values(), color=colors)
            handles = list()
            for name, number, color in zip(legend_list, label_list, colors):
                handles.append(mpatches.Patch(color=color, label=str(number) + ' - ' + name))
            plt.legend(handles=handles)
            plt.xlabel('Poziom wykształcenia')
            plt.ylabel('Ilość osób')
            plt.ylim(top=1200)
            plt.ylim(bottom=0)
            temp_name = save.split('_')
            year = temp_name[0]
            month = temp_name[1]
            plt.title('Histogram poziomu wykształcenia uczestników badania - ' + year + ' ' + month, fontsize=10)
            plt.savefig('results/histograms/education/hist_' + save + '.png')
            plt.clf()

        return education_list

    def calculate_structure_accomodation(self, list_df, save_name):
        legend_list = ["W wysokim bloku (>= 5 pięter)", "W niskim bloku (<= 4 pięter)", "W kamienicy",
                       "W domu w zabudowie szeregowej", "W domu jednorodzinnym"]
        temp_value = [0 for i in range(5)]
        label_list = [i + 1 for i in range(5)]
        accommodation_list = list()
        for df, save in zip(list_df, save_name):
            accommodation_dict = dict(zip(label_list, temp_value))
            for i in df.iloc[:, 1].to_list():
                if i == 1:
                    accommodation_dict[label_list[0]] += 1
                elif i == 2:
                    accommodation_dict[label_list[1]] += 1
                elif i == 3:
                    accommodation_dict[label_list[2]] += 1
                elif i == 4:
                    accommodation_dict[label_list[3]] += 1
                elif i == 5:
                    accommodation_dict[label_list[4]] += 1

            accommodation_dict_percents = self.change_to_percents(accommodation_dict, label_list, 5)
            accommodation_list.append(accommodation_dict_percents)
            colors = list('rgbkymc')
            handles = list()
            plt.bar(accommodation_dict.keys(), accommodation_dict.values(), color=colors)
            for name, number, color in zip(legend_list, label_list, colors):
                handles.append(mpatches.Patch(color=color, label=str(number) + ' - ' + name))
            plt.legend(handles=handles)
            plt.ylim(top=1000)
            plt.ylim(bottom=0)
            plt.xlabel('Miejsce zamieszkania')
            plt.ylabel('Ilość osób')
            temp_name = save.split('_')
            year = temp_name[0]
            month = temp_name[1]
            plt.title('Histogram rozkładu miejsca zamieszkania uczestników badania - ' + year + ' ' + month, fontsize=9)
            plt.savefig('results/histograms/accomodation/hist_' + save + '.png')
            plt.clf()

        return accommodation_list

    def calculate_A2(self, list_df, save_name):
        legend_list = ["Zdecydowanie tak", "Raczej tak", "Ani tak, ani nie",
                       "Raczej nie", "Zdecydowanie nie"]
        temp_value = [0 for i in range(5)]
        label_list = [i + 1 for i in range(5)]

        a2_list = list()
        for df, save in zip(list_df, save_name):
            A2_dict = dict(zip(label_list, temp_value))
            for i in df.iloc[:, 1].to_list():
                if i == 1:
                    A2_dict[label_list[0]] += 1
                elif i == 2:
                    A2_dict[label_list[1]] += 1
                elif i == 3:
                    A2_dict[label_list[2]] += 1
                elif i == 4:
                    A2_dict[label_list[3]] += 1
                elif i == 5:
                    A2_dict[label_list[4]] += 1

            error_dict = dict(zip(label_list, temp_value))
            for i in label_list:
                error_dict[i] = np.sqrt(A2_dict[i])
            a2_list.append(A2_dict)
            colors = list('rgbymc')
            handles = list()
            plt.bar(A2_dict.keys(), A2_dict.values(), color=colors, yerr=error_dict.values(), ecolor='black',
                    capsize=10)
            for name, number, color in zip(legend_list, label_list, colors):
                handles.append(mpatches.Patch(color=color, label=str(number) + ' - ' + name))
            plt.legend(handles=handles)
            plt.xlabel('5-stopniowa skala oceny')
            plt.ylabel('Ilość osób')
            plt.ylim(top=1850)
            plt.ylim(bottom=0)
            temp_name = save.split('_')
            year = temp_name[0]
            month = temp_name[1]
            plt.title('Ocena poczucia bezpieczeństwa w Krakowie - ' + year + ' ' + month, fontsize=10)
            plt.savefig('results/histograms/A2/hist_' + save + '.png')
            plt.clf()

        return a2_list

    def calculate_A2_with_3_cat(self, list_df, save_name):
        legend_list = ["tak", "Ani tak, ani nie", "nie"]
        temp_value = [0 for i in range(3)]
        label_list = [i + 1 for i in range(3)]

        a2_list = list()
        for df, save in zip(list_df, save_name):
            A2_dict = dict(zip(label_list, temp_value))
            for i in df.iloc[:, 1].to_list():
                if i == 1 or i == 2:
                    A2_dict[label_list[0]] += 1
                elif i == 3:
                    A2_dict[label_list[1]] += 1
                elif i == 4 or i == 5:
                    A2_dict[label_list[2]] += 1

            A2_dict_percents = self.change_to_percents(A2_dict, label_list, 3)
            a2_list.append(A2_dict_percents)
            error_dict = dict(zip(label_list, temp_value))
            for i in label_list:
                error_dict[i] = np.sqrt(A2_dict[i])

            colors = list('rgbymc')
            handles = list()
            plt.bar(A2_dict.keys(), A2_dict.values(), color=colors, yerr=error_dict.values(), ecolor='black',
                    capsize=10)
            plt.xticks(range(1, 4))
            plt.ylim(top=1850)
            plt.ylim(bottom=0)
            for name, number, color in zip(legend_list, label_list, colors):
                handles.append(mpatches.Patch(color=color, label=str(number) + ' - ' + name))
            plt.legend(handles=handles)
            plt.xlabel('3-stopniowa skala oceny')
            plt.ylabel('Ilość osób')
            temp_name = save.split('_')
            year = temp_name[0]
            month = temp_name[1]
            plt.title('Ocena poczucia bezpieczeństwa w Krakowie - ' + year + ' ' + month, fontsize=10)
            plt.savefig('results/histograms/A2_ver_2/hist_' + save + '.png')
            plt.clf()

        return a2_list

    def calculate_fear_index_affective_part(self, list_df):
        df_dict = dict()
        for df, number in zip(list_df, range(11)):
            affective_list = list()
            affective_dict = dict()
            for i in range(2):
                temp = list()
                df_list = df.iloc[:, i].to_list()
                for col in df_list:
                    if pd.isna(col):
                        temp.append(0)
                    else:
                        col = int(col)
                    if col == 1 or col == 6 or col == 7 or col == 95 or col == 96 or col == 0:
                        temp.append(0)
                    elif col == 2:
                        temp.append(7.5)
                    elif col == 3:
                        temp.append(15)
                    elif col == 4:
                        temp.append(22.5)
                    elif col == 5:
                        temp.append(30)
                    affective_dict[str(i + 1)] = temp
            for i, j in zip(affective_dict['1'], affective_dict['2']):
                affective_list.append((i + j) / 2)
            df_dict[number] = affective_list

        return df_dict

    def calculate_fear_index_cognitive_part(self, list_df):
        df_dict = dict()
        for df, number in zip(list_df, range(11)):
            list_all = list()
            cognitive_dict = dict()
            for i in range(2, 10):
                temp = list()
                for col in df.iloc[:, i].to_list():
                    if pd.isna(col):
                        temp.append(0)
                    else:
                        col = int(col)
                    if col == 1:
                        temp.append(3.75)
                    elif col == 2:
                        temp.append(2.81)
                    elif col == 3:
                        temp.append(1.88)
                    elif col == 4:
                        temp.append(0.94)
                    elif col == 5 or col == 6 or col == 7 or col == 95 or col == 96 or col == 0:
                        temp.append(0)
                    cognitive_dict[str(i)] = temp
            for i in cognitive_dict.keys():
                list_all.append(cognitive_dict[i])
            list_all = np.array(list_all)
            cognitive_list = np.sum(list_all, axis=0)
            df_dict[number] = cognitive_list
        return df_dict

    def calculate_fear_index_behavioral_part(self, list_df):
        df_dict = dict()
        for df, number in zip(list_df, range(11)):
            list_all = list()
            behavioral_dict = dict()
            for i in range(10, 21):
                temp = list()
                for col in df.iloc[:, i].to_list():
                    if pd.isna(col):
                        temp.append(0)
                    else:
                        col = int(col)
                    if col == 1:
                        temp.append(2.73)
                    elif col == 2:
                        temp.append(2.05)
                    elif col == 3:
                        temp.append(1.36)
                    elif col == 4:
                        temp.append(0.68)
                    elif col == 5 or col == 6 or col == 7 or col == 95 or col == 96 or col == 0:
                        temp.append(0)
                    behavioral_dict[str(i)] = temp
            for i in behavioral_dict.keys():
                list_all.append(behavioral_dict[i])
            list_all = np.array(list_all)
            behavioral_list = np.sum(list_all, axis=0)
            df_dict[number] = behavioral_list
        return df_dict

    def calculate_fear_index(self, list_df, save_name):
        legend_list = ["bardzo niski", "raczej niski", "średni",
                       "raczej wysoki", "bardzo wysoki"]
        legend_list_3_cat = ["niski", "średni", "wysoki"]
        affective_dict = self.calculate_fear_index_affective_part(list_df)
        cognitive_dict = self.calculate_fear_index_cognitive_part(list_df)
        behavioral_dict = self.calculate_fear_index_behavioral_part(list_df)
        list_all = list()
        for i in affective_dict.keys():
            temp = np.array([affective_dict[i], cognitive_dict[i], behavioral_dict[i]])
            list_all.append(np.sum(temp, axis=0))

        label_list = [i + 1 for i in range(5)]
        temp_value = [0 for i in range(5)]
        label_list_3_cat = [i + 1 for i in range(3)]
        temp_value_3_cat = [0 for i in range(3)]
        fear_list_df = list()
        fear_list_df_3_cat = list()
        for element, save in zip(list_all, save_name):
            fear_index_dict = dict(zip(label_list, temp_value))
            fear_index_dict_3_cat = dict(zip(label_list_3_cat, temp_value_3_cat))
            for i in element:
                if 0 <= i < 30:
                    fear_index_dict[label_list[0]] += 1
                    fear_index_dict_3_cat[label_list_3_cat[0]] += 1
                elif 30 <= i < 40:
                    fear_index_dict[label_list[1]] += 1
                    fear_index_dict_3_cat[label_list_3_cat[1]] += 1
                elif 40 <= i < 50:
                    fear_index_dict[label_list[2]] += 1
                    fear_index_dict_3_cat[label_list_3_cat[1]] += 1
                elif 50 <= i < 60:
                    fear_index_dict[label_list[3]] += 1
                    fear_index_dict_3_cat[label_list_3_cat[1]] += 1
                elif 60 <= i <= 90:
                    fear_index_dict[label_list[4]] += 1
                    fear_index_dict_3_cat[label_list_3_cat[2]] += 1

            error_dict = dict(zip(label_list_3_cat, temp_value_3_cat))
            for i in label_list_3_cat:
                error_dict[i] = np.sqrt(fear_index_dict_3_cat[i])
            fear_index_dict_percents = self.change_to_percents(fear_index_dict, label_list, 5)
            fear_list_df.append(fear_index_dict_percents)
            fear_index_dict_percents_3_cat = self.change_to_percents(fear_index_dict_3_cat, label_list_3_cat, 3)
            fear_list_df_3_cat.append(fear_index_dict_percents_3_cat)
            colors = list('rgb')
            handles = list()
            plt.bar(fear_index_dict_3_cat.keys(), fear_index_dict_3_cat.values(), yerr=error_dict.values(),
                    ecolor='black', capsize=10, color=colors)
            plt.ylim(top=1850)
            plt.ylim(bottom=0)
            plt.xticks(range(1, 4))
            for name, number, color in zip(legend_list_3_cat, label_list_3_cat, colors):
                handles.append(mpatches.Patch(color=color, label=str(number) + ' - ' + name))
            plt.legend(handles=handles)
            plt.xlabel('Wartość indeksu strachu')
            plt.ylabel('Ilość osób')
            temp_name = save.split('_')
            year = temp_name[0]
            month = temp_name[1]
            plt.title('Indeks strachu - ' + year + ' ' + month, fontsize=10)
            plt.savefig('results/histograms/fear_index_3_cat/hist_' + save + '.png')
            plt.clf()

        return list_all, fear_list_df, fear_list_df_3_cat, affective_dict, cognitive_dict, behavioral_dict

    def calculate_A3(self, list_df, save_name):
        legend_list = ["Zdecydowanie tak", "Raczej tak", "Ani tak, ani nie",
                       "Raczej nie", "Zdecydowanie nie"]
        legend_list_cat3 = ["tak", "Ani tak, ani nie", "nie"]
        temp_value = [0 for i in range(5)]
        label_list = [i + 1 for i in range(5)]
        temp_value_3_cat = [0 for i in range(3)]
        label_list_3_cat = [i + 1 for i in range(3)]
        a3_list = list()
        a3_list_3_cat = list()
        for df, save in zip(list_df, save_name):
            A3_dict = dict(zip(label_list, temp_value))
            A3_dict_3_cat = dict(zip(label_list_3_cat, temp_value_3_cat))
            for i in df.iloc[:, 1].to_list():
                if i == 1:
                    A3_dict[label_list[0]] += 1
                    A3_dict_3_cat[label_list[0]] += 1
                elif i == 2:
                    A3_dict[label_list[1]] += 1
                    A3_dict_3_cat[label_list[0]] += 1
                elif i == 3:
                    A3_dict[label_list[2]] += 1
                    A3_dict_3_cat[label_list[1]] += 1
                elif i == 4:
                    A3_dict[label_list[3]] += 1
                    A3_dict_3_cat[label_list[2]] += 1
                elif i == 5:
                    A3_dict[label_list[4]] += 1
                    A3_dict_3_cat[label_list[2]] += 1

            colors = list('rgbkymc')
            handles = list()
            A3_dict_percents = self.change_to_percents(A3_dict, label_list, 5)
            A3_dict_percents_3_cat = self.change_to_percents(A3_dict_3_cat, label_list_3_cat, 3)
            a3_list.append(A3_dict_percents)
            a3_list_3_cat.append(A3_dict_percents_3_cat)
            error_dict = dict(zip(label_list, temp_value))
            for i in label_list:
                error_dict[i] = np.sqrt(A3_dict[i])
            plt.bar(A3_dict.keys(), A3_dict.values(), yerr=error_dict.values(), ecolor='black', capsize=10,
                    color=colors)
            for name, number, color in zip(legend_list, label_list, colors):
                handles.append(mpatches.Patch(color=color, label=str(number) + ' - ' + name))
            plt.legend(handles=handles)
            plt.xlabel('5-stopniowa skala oceny')
            plt.ylabel('Ilość osób')
            plt.ylim(top=1850)
            plt.ylim(bottom=0)
            temp_name = save.split('_')
            year = temp_name[0]
            month = temp_name[1]
            plt.title('Ocena poczucia bezpieczeństwa w poszczególnych dzielnicach Krakowa - ' + year + ' ' + month,
                      fontsize='10')
            plt.savefig('results/histograms/A3/hist_' + save + '.png')
            plt.clf()
        return a3_list, a3_list_3_cat

    def create_time_series(self, list_dicts, question, number_of_answers, label_x):
        label_list = [i + 1 for i in range(number_of_answers)]
        data_label = ['2014 III', '2014 IX', '2015 VI', '2015 IX', '2016 III', '2016 IX',
                      '2017 VI', '2017 IX', '2018 VI', '2018 IX', '2019 VIII']

        dates = [
            datetime(2014, 3, 1),
            datetime(2014, 9, 1),
            datetime(2015, 6, 1),
            datetime(2015, 9, 1),
            datetime(2016, 3, 1),
            datetime(2016, 9, 1),
            datetime(2017, 6, 1),
            datetime(2017, 9, 1),
            datetime(2018, 6, 1),
            datetime(2018, 9, 1),
            datetime(2019, 8, 1)]

        temp_dict = collections.defaultdict(list)
        error_dict = collections.defaultdict(list)
        error_value_up_dict = collections.defaultdict(list)
        error_value_down_dict = collections.defaultdict(list)
        for i in list_dicts:
            for label in label_list:
                temp_dict[label].append(i[label])
                error = np.sqrt(i[label])
                error_dict[label].append(error)
                error_value_up_dict[label].append(i[label] + error)
                error_value_down_dict[label].append(i[label] - error)

        for i, label in zip(label_list, label_x):
            plt.xticks(fontsize=7)
            plt.plot_date(dates, temp_dict[i], linestyle='solid', color='black')
            plt.plot_date(dates, error_value_up_dict[i], fmt='--', color='k', linewidth=0.5)
            plt.plot_date(dates, error_value_down_dict[i], fmt='--', color='k', linewidth=0.5)
            plt.ylim(top=100)
            plt.ylim(bottom=0)
            plt.xlabel('Data')
            plt.ylabel('Procent respodentów')
            plt.title("Zmiana odpowiedzi '" + label + "' dla skali subiektywnego ryzyka wiktymizacjii", fontsize='9')

            plt.savefig('results/time_series/' + question + '/' + str(i) + '.png', dpi=300)
            plt.clf()
