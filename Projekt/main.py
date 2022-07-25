import tkinter as tk
import random
import pandas as pd
from typing import Tuple
from pandas import DataFrame
from sklearn import linear_model


class Check:
    @staticmethod
    def validate(P):
        if 5 >= len(P) > 0:
            try:
                float(P)
                return True
            except ValueError:
                return False
        elif len(P) == 0:
            return True
        else:
            return False

    @staticmethod
    def validateFM(P):
        if len(P) <= 1:
            if P == 'k' or P == 'm':
                return True
            elif P == '':
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def checkoptions():
        return options.index(clicked.get())

    @staticmethod
    def isResultPossible():
        try:
            plec = plecEntry.get()
            wysokosc = float(wysokoscEntry.get())
            obwodSzyi = float(obwodSzyiEntry.get())
            obwodKlatkiPiersiowej = float(obwodKlatkiPiersiowejEntry.get())
            obwodPasa = float(obwodPasaEntry.get())
            obwodBioder = float(obwodBioderEntry.get())
            obwodUda = float(obwodUdaEntry.get())
            obwodRamienia = float(obwodRamieniaEntry.get())

            Predictor.calculate(plec, wysokosc, obwodSzyi, obwodKlatkiPiersiowej, obwodPasa, obwodBioder, obwodUda,
                                obwodRamienia)
        except:
            Widgets.resultLabel('Brak danych', 'brak')


class Widgets:
    @staticmethod
    def combobox():
        global options
        options = [
            'Waga [kg]',
            'Masa tłuszczu [kg]',
            'Masa mięśniowa [kg]',
            'BMI',
            'Procent tłuszczu [%]',
        ]
        global clicked
        clicked = tk.StringVar()
        clicked.set(options[0])

        combo = tk.OptionMenu(root, clicked, *options)
        combo.place(x=600, y=200, width=165)

    @staticmethod
    def entries():
        validate = (root.register(Check.validate), '%P')
        validate2 = (root.register(Check.validateFM), '%P')

        global plecEntry
        global wysokoscEntry
        global obwodSzyiEntry
        global obwodKlatkiPiersiowejEntry
        global obwodPasaEntry
        global obwodBioderEntry
        global obwodUdaEntry
        global obwodRamieniaEntry

        plecEntry = tk.Entry(root, justify=tk.CENTER, font=("Helvetica", 20), width=6, validate="key",
                             validatecommand=validate2)
        plecEntry.place(x=100, y=250)

        wysokoscEntry = tk.Entry(root, justify=tk.CENTER, font=("Helvetica", 20), width=6, validate="key",
                                 validatecommand=validate)
        wysokoscEntry.place(x=100, y=350)

        obwodSzyiEntry = tk.Entry(root, justify=tk.CENTER, font=("Helvetica", 20), width=6, validate="key",
                                  validatecommand=validate)
        obwodSzyiEntry.place(x=200, y=250)

        obwodKlatkiPiersiowejEntry = tk.Entry(root, justify=tk.CENTER, font=("Helvetica", 20), width=6, validate="key",
                                              validatecommand=validate)
        obwodKlatkiPiersiowejEntry.place(x=200, y=350)

        obwodPasaEntry = tk.Entry(root, justify=tk.CENTER, font=("Helvetica", 20), width=6, validate="key",
                                  validatecommand=validate)
        obwodPasaEntry.place(x=300, y=250)

        obwodBioderEntry = tk.Entry(root, justify=tk.CENTER, font=("Helvetica", 20), width=6, validate="key",
                                    validatecommand=validate)
        obwodBioderEntry.place(x=300, y=350)

        obwodUdaEntry = tk.Entry(root, justify=tk.CENTER, font=("Helvetica", 20), width=6, validate="key",
                                 validatecommand=validate)
        obwodUdaEntry.place(x=400, y=250)

        obwodRamieniaEntry = tk.Entry(root, justify=tk.CENTER, font=("Helvetica", 20), width=6, validate="key",
                                      validatecommand=validate)
        obwodRamieniaEntry.place(x=400, y=350)

    @staticmethod
    def variableLabels():
        pleclabel = tk.Label(root, text='Płeć(k lub m)', font=("Helvetica", 10), width=12)
        pleclabel.place(x=100, y=200)

        wysokosclabel = tk.Label(root, text='Wysokość', font=("Helvetica", 10), width=12)
        wysokosclabel.place(x=100, y=300)

        obwodSzyilabel = tk.Label(root, text='Obwód Szyi', font=("Helvetica", 10), width=12)
        obwodSzyilabel.place(x=200, y=200)

        obwodKlatkiPiersiowejlabel = tk.Label(root, text='Obwód Klatki', font=("Helvetica", 10), width=12)
        obwodKlatkiPiersiowejlabel.place(x=200, y=300)

        obwodPasalabel = tk.Label(root, text='Obwód Pasa', font=("Helvetica", 10), width=12)
        obwodPasalabel.place(x=300, y=200)

        obwodBioderlabel = tk.Label(root, text='Obwód Bioder', font=("Helvetica", 10), width=12)
        obwodBioderlabel.place(x=300, y=300)

        obwodUdalabel = tk.Label(root, text='Obwód Uda', font=("Helvetica", 10), width=12)
        obwodUdalabel.place(x=400, y=200)

        obwodRamienialabel = tk.Label(root, text='Obwód Ramienia', font=("Helvetica", 10), width=12)
        obwodRamienialabel.place(x=400, y=300)

        errorlabel = tk.Label(root, text='Średni błąd bezwzględny', font=("Helvetica", 11), width=18)
        errorlabel.place(x=600, y=320)

    @staticmethod
    def resultLabel(text: str, plec: str):
        result = tk.Label(root, justify=tk.CENTER, font=("Helvetica", 20), width=10, text=text)
        result.place(x=600, y=235)
        index = Check.checkoptions()
        if plec == 'k':
            error = "~" + str(errorsF[index])[1:6]
        elif plec == 'm':
            error = "~" + str(errorsM[index])[1:6]
        else:
            error = ''

        resulterror = tk.Label(root, justify=tk.CENTER, font=("Helvetica", 20), width=10, text=error)
        resulterror.place(x=600, y=350)

    @staticmethod
    def buttons():
        # przycisk liczenia
        button = tk.Button(root, text="Licz",
                           command=Check.isResultPossible, font=("Helvetica", 20))
        button.place(x=265, y=410)

        # przycisk wyjścia
        button = tk.Button(root, text="Wyjście", command=exit, font=("Helvetica", 20))
        button.place(x=375, y=465)


class Predictor:
    # liczy dane, dla danej próbki
    @staticmethod
    def calculate(plec: str, wysokosc: float, obwodSzyi: float, obwodKlatkiPiersiowej: float, obwodPasa: float,
                  obwodBioder: float, obwodUda: float, obwodRamienia: float):
        predicted = 'Brak danych'
        index = Check.checkoptions()
        if plec == 'k':
            predicted = regsFemale[index].predict(
                [[wysokosc, obwodSzyi, obwodKlatkiPiersiowej, obwodPasa, obwodBioder, obwodUda, obwodRamienia]])
        elif plec == 'm':
            predicted = regsMale[index].predict(
                [[wysokosc, obwodSzyi, obwodKlatkiPiersiowej, obwodPasa, obwodBioder, obwodUda, obwodRamienia]])
        if predicted >= 0:
            Widgets.resultLabel(str(predicted)[1:6], plec)
        else:
            Widgets.resultLabel('Złe dane', 'brak')

    # zbiory dla regresji
    @staticmethod
    def makeregs(dataT):
        regs = []  # kolejnosc: Waga, Masa tłuszczu, Masa mięsniowa, BMI, Procent Tłuszczu

        # tworzenie modelu regresji liniowej wielu zmiennych dla kobiet
        for column in dataT.columns.tolist()[7:]:
            reg = linear_model.LinearRegression()
            # tworzenie zbioru treningowego z inbody kobiet dla danych zmiennych
            reg.fit(dataT[['Wysokosc', 'ObwodSzyi', 'ObwodKlatkiPiersiowej', 'ObwodPasa', 'ObwodBioder', 'ObwodUda',
                           'ObwodRamienia']], dataT[column])
            regs.append(reg)

        return regs

    @staticmethod
    def error_calc(regs, dataV):
        error_tup = []
        for j in range(5):
            error_of_line = 0
            for i in range(len(dataV)):
                predicted = regs[j].predict([[dataV.iat[i, 0], dataV.iat[i, 1], dataV.iat[i, 2], dataV.iat[i, 3],
                                              dataV.iat[i, 4], dataV.iat[i, 5], dataV.iat[i, 6]]])
                error = dataV.iat[i, 7 + j] - predicted
                error = abs(error)
                error_of_line += error
            error_tup.append(error_of_line / len(dataV))

        return error_tup


class ProcessingData:
    # przygotowanie zbiorów
    @staticmethod
    def prepareData():
        dataF = pd.read_csv('Resources/CSV_files/FinishedResources/female.csv')
        dataM = pd.read_csv('Resources/CSV_files/FinishedResources/male.csv')

        # tasowanie i podzieleenie na dwa zbiory datasetu F
        valid_and_training_dataset_tuple_female = ProcessingData.shuffleAndSplit(dataF)
        validFemale = valid_and_training_dataset_tuple_female[1]
        trainingFemale = valid_and_training_dataset_tuple_female[0]

        # tasowanie i podzieleenie na dwa zbiory datasetu M
        valid_and_training_dataset_tuple_male = ProcessingData.shuffleAndSplit(dataM)
        validMale = valid_and_training_dataset_tuple_male[1]
        trainingMale = valid_and_training_dataset_tuple_male[0]

        return validFemale, trainingFemale, validMale, trainingMale

    @staticmethod
    def shuffleAndSplit(data: pd.DataFrame) -> Tuple[DataFrame, DataFrame]:
        for idx in range(len(data) - 1, 0, -1):  # tablica od tyłu
            rand_idx = random.randint(0, idx)  # losowanie
            data.iloc[idx], data.iloc[rand_idx] = data.iloc[rand_idx], data.iloc[idx]

        # zbiór treningowy ustaliłem na na 70%
        n = len(data)
        h = int(0.7 * n)
        return data.head(h), data.tail(n - h)


def menu():
    # combobox
    Widgets.combobox()

    # hints
    Widgets.variableLabels()

    # entries
    Widgets.entries()

    # buttons
    Widgets.buttons()

    # result
    Widgets.resultLabel('brak', 'brak')


# root
if __name__ == '__main__':
    # root
    root = tk.Tk()
    root.title('Project')
    root.resizable(width=False, height=False)
    root.geometry('850x850')

    # Background
    start_image = tk.PhotoImage(file='Resources/antropometria.png')
    imagelabel = tk.Label(root, image=start_image)
    imagelabel.place(x=0, y=0, relwidth=1)

    # tworzenie zbiorów
    wholetuple = ProcessingData.prepareData()
    validF = wholetuple[0]
    trainingF = wholetuple[1]
    validM = wholetuple[2]
    trainingM = wholetuple[3]

    # zbiory dla regresji
    regsFemale = Predictor.makeregs(trainingF)
    regsMale = Predictor.makeregs(trainingM)

    # wyliczenie błędów
    errorsF = Predictor.error_calc(regsFemale, validF)
    errorsM = Predictor.error_calc(regsMale, validM)

    # przejscie do menu
    menu()
    root.mainloop()
