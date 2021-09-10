import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import copy
from functools import reduce
from pathlib import Path


class ReadingData:

    def __init__(self):
        pass

    def reading_data(self, file_name, date):
        print("Reading data " + date + "\n")
        my_sheet = 'dane'
        destination_path = date + '/'
        df = pd.read_excel(file_name, sheet_name=my_sheet)

        print("Printing columns headers")
        listColumns = df.columns.tolist()
        print(listColumns)
        df_A2 = df.iloc[:, 5:6].copy()
        df_A2 = self.five_step_scale_string_to_int(df_A2, 'A2', 1)
        df_A2.to_excel(destination_path + 'A2.xlsx')

        df_A3 = df.iloc[:, 6:7].copy()
        df_A3 = self.five_step_scale_string_to_int(df_A3, 'A3', 1)
        df_A3.to_excel(destination_path + 'A3.xlsx')

        df_B4 = df.iloc[:, 7:8].copy()
        df_B4.to_excel(destination_path + 'B4.xlsx')

        df_B5 = df.iloc[:, 8:9].copy()
        df_B5.to_excel(destination_path + 'B5.xlsx')

        df_B6 = df.iloc[:, 9:17].copy()
        df_B6.to_excel(destination_path + 'B6.xlsx')

        df_C10 = df.iloc[:, 28:33].copy()
        df_C10.to_excel(destination_path + 'C10.xlsx')

        df_C11 = df.iloc[:, 33:36].copy()
        df_C11.to_excel(destination_path + 'C11.xlsx')

        df_C12 = df.iloc[:, 36:37].copy()
        df_C12.to_excel(destination_path + 'C12.xlsx')

        df_C16 = df.iloc[:, 42:53].copy()
        df_C16.to_excel(destination_path + 'C16.xlsx')

        df_D18 = df.iloc[:, 58:59].copy()
        df_D18.to_excel(destination_path + 'D18.xlsx')

        df_D19 = df.iloc[:, 59:60].copy()
        df_D19.to_excel(destination_path + 'D19.xlsx')

        df_D20 = df.iloc[:, 60:64].copy()
        df_D20.to_excel(destination_path + 'D20.xlsx')

        df_D21 = df.iloc[:, 64:71].copy()
        df_D21.to_excel(destination_path + 'D21.xlsx')

        df_przedzial_wiekowy = df.iloc[:, 72:73].copy()
        df_przedzial_wiekowy = self.calculate_structure_population_age_based_number(df_przedzial_wiekowy)
        df_przedzial_wiekowy.to_excel(destination_path + 'przedzial_wiekowy.xlsx')
        df_przedzial_wiekowy["id"] = df_przedzial_wiekowy.index + 1

        df_E23_E26 = df.iloc[:, 73:76].copy()
        df_E23_E26.to_excel(destination_path + 'E23_E26.xlsx')
        df_E23_E26["id"] = df_E23_E26.index + 1

        df_E22 = df.iloc[:, 71:72]
        df_E22.to_excel(destination_path + 'E22.xlsx')

        df_E28 = df.iloc[:, 77:78]
        df_E28.to_excel(destination_path + 'E28.xlsx')

        df_wyksztalcenie = df.iloc[:, 73:74]
        df_wyksztalcenie.to_excel(destination_path + 'wyksztalcenie.xlsx')
        df_miejsce_zamieszkania = df.iloc[:, 75:76]
        df_miejsce_zamieszkania.to_excel(destination_path + 'miejsce_zamieszkania.xlsx')

        print("Removing unnecessary columns\n")
        df = df.drop(['LP'], axis=1)
        df = df.drop(df.iloc[:, 81:], axis=1)
        listColumns = df.columns.tolist()
        print(listColumns)
        df.to_excel(destination_path + 'merge.xlsx')

    def calculate_structure_population_age_based_year(self, df, year_survey):
        year_birth = (df.iloc[:, 0]).to_list()
        range_year = list()
        for year in year_birth:
            if (year_survey - 24) <= year <= (year_survey - 18):
                range_year.append(['18-24'])
            elif (year_survey - 34) <= year <= (year_survey - 25):
                range_year.append(['25-34'])
            elif (year_survey - 44) <= year <= (year_survey - 35):
                range_year.append(['35-44'])
            elif (year_survey - 54) <= year <= (year_survey - 45):
                range_year.append(['45-54'])
            elif (year_survey - 64) <= year <= (year_survey - 55):
                range_year.append(['55-64'])
            elif year <= (year_survey - 65):
                range_year.append(['65+'])
            else:
                continue
        range_year_df = pd.DataFrame(range_year)
        return range_year_df

    def calculate_structure_population_age_based_number(self, df):
        group_age = (df.iloc[:, 0]).to_list()
        print('group_age')
        print(group_age)
        range_year = list()
        for group in group_age:
            if group == 1:
                range_year.append(['18-24'])
            elif group == 2:
                range_year.append(['25-34'])
            elif group == 3:
                range_year.append(['35-44'])
            elif group == 4:
                range_year.append(['45-54'])
            elif group == 5:
                range_year.append(['55-64'])
            elif group == 6:
                range_year.append(['65+'])
            else:
                continue
        range_year_df = pd.DataFrame(range_year)
        return range_year_df

    def education_string_to_int(self, df):
        education = (df.iloc[:, 0]).to_list()
        education_list = list()
        for n in education:
            if n == "Podstawowe":
                education_list.append(1)
            elif n == "Zasadnicze zawodowe":
                education_list.append(2)
            elif n == "Średnie ogólnokształcące":
                education_list.append(3)
            elif n == "Średnie techniczne (technikum, liceum zawodowe)":
                education_list.append(4)
            elif n == "Pomaturalne":
                education_list.append(5)
            elif n == "Studia wyższe niepełne (w trakcie nauki, nieukończone)":
                education_list.append(6)
            elif n == "Studia wyższe ukończone (licencjat, magister, inżynier, wyższe niż magisterskie)":
                education_list.append(7)
            else:
                continue

        education_df = pd.DataFrame(education_list)
        return education_df

    def accomodation_string_to_int(self, df):
        accomodation = (df.iloc[:, 0]).to_list()
        accomodation_list = list()
        for n in accomodation:
            if n == "W wysokim bloku (co najmniej 5 pięter)":
                accomodation_list.append(1)
            elif n == "W niskim bloku (do 4 pięter)":
                accomodation_list.append(2)
            elif n == "W kamienicy":
                accomodation_list.append(3)
            elif n == "W domu w zabudowie szeregowej":
                accomodation_list.append(4)
            elif n == "W domu jednorodzinnym":
                accomodation_list.append(5)
            else:
                continue

        accomodation_df = pd.DataFrame(accomodation_list)
        return accomodation_df

    def five_step_scale_string_to_int(self, df, name, column_number):
        temp_dict = dict()
        for col in range(column_number):
            five_step_scale_df = df.iloc[:, col].to_list()
            temp_list = list()
            for n in five_step_scale_df:
                if n == "Zdecydowanie tak" or n == "1 - Zdecydowanie tak" or n == 1:
                    temp_list.append(1)
                elif n == "Raczej tak" or n == "2 - Raczej tak" or n == 2:
                    temp_list.append(2)
                elif n == "Ani tak, ani nie" or n == "3 - Ani tak, ani nie" or n == 3:
                    temp_list.append(3)
                elif n == "Raczej nie" or n == "4 - Raczej nie" or n == 4:
                    temp_list.append(4)
                elif n == "Zdecydowanie nie" or n == "5 - Zdecydowanie nie" or n == 5:
                    temp_list.append(5)
                else:
                    temp_list.append(0)  # "Nie wiem/trudno powiedzieć"
            temp_dict[name + "_" + str(col + 1)] = temp_list

        df = pd.DataFrame(temp_dict)
        # df.to_excel('C10.xlsx')
        return df

    def reading_question(self, directories, question):
        my_sheet = 'Sheet1'
        list_df = list()
        for i in directories:
            file_name = path + '/' + i + '/' + question + '.xlsx'
            df = pd.read_excel(file_name, sheet_name=my_sheet)
            list_df.append(df)
        return list_df

    def reading_question_to_index(self, directories, list_questions, columns_number):
        my_sheet = 'Sheet1'
        list_all = list()
        for i in directories:
            temp_dict = dict()
            for question, number in zip(list_questions, range(len(list_questions))):
                file_name = path + '/' + i + '/' + question + '.xlsx'
                df = pd.read_excel(file_name, sheet_name=my_sheet)
                for col in range(columns_number[number]):
                    temp_dict[question + '_' + str(col + 1)] = df.iloc[:, col + 1].to_list()
            list_index_df = pd.DataFrame(temp_dict)
            list_all.append(list_index_df)

        return list_all
