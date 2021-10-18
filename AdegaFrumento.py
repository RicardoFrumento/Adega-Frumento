from tkinter import *
import os

class Wine:
    def __init__(self, w = "NULL", g = "NULL", y = "NULL", v = "NULL", c = "NULL", t = "NULL"):
        self.wine = w
        self.grape = g
        self.year = y
        self.vinyard = v
        self.country = c
        self.type = t

    def __eq__(self, other):
             if self.wine == other.wine and self.grape == other.grape and self.year == other.year and self.vinyard == other.vinyard and self.country == other.country and self.type == other.type:
                  return 1
             else:
                  return 0
    
    def getData(self):
        s = self.wine + " " + self.grape + " " + self.year + " " + self.vinyard + " " + self.country + " " + self.type
        return s

wines = []

file = open("vinhos.txt", 'r+')
lines = file.readlines()

for line in lines:
    temp = line.split()
    newWine = Wine(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5])
    wines.append(newWine)

window = Tk()
window.title("Adega Frumento")
window.geometry('800x400')

wineLabel = Label(window, text = "Vinho")
wineLabel.grid(column = 0, row = 1)

wineText = Entry(window, width = 10)
wineText.grid(column = 1, row = 1)

grapeLabel = Label(window, text = "Uva")
grapeLabel.grid(column = 2, row = 1)

grapeText = Entry(window, width = 10)
grapeText.grid(column = 3, row = 1)

yearLabel = Label(window, text = "Ano")
yearLabel.grid(column = 4, row = 1)

yearText = Entry(window, width = 10)
yearText.grid(column = 5, row = 1)

vinyardLabel = Label(window, text = "Vinhedo")
vinyardLabel.grid(column = 0, row = 2)

vinyardText = Entry(window, width = 10)
vinyardText.grid(column = 1, row = 2)

countryLabel = Label(window, text = "Pais")
countryLabel.grid(column = 2, row = 2)

countryText = Entry(window, width = 10)
countryText.grid(column = 3, row = 2)

typeLabel = Label(window, text = "Tipo")
typeLabel.grid(column = 4, row = 2)

typeText = Entry(window, width = 10)
typeText.grid(column = 5, row = 2)

def clickedOk():
    newWine = Wine(wineText.get(), grapeText.get(), yearText.get(), vinyardText.get(), countryText.get(), typeText.get())
    for i in range(len(wines)):
        if newWine == wines[i]:
            return
    wines.append(newWine)

def clickedDelete():
    w = Wine(wineText.get(), grapeText.get(), yearText.get(), vinyardText.get(), countryText.get(), typeText.get())
    for i in range(len(wines)):
        if wines[i] == w:
            wines.remove(wines[i])
            break

def clickedSave():
    file.seek(0)
    file.truncate()
    for i in range(len(wines)):
        file.write(wines[i].getData() + "\n")

def clickedClose():
    file.close()
    window.destroy()

def clickedYear():
    wines.sort(key = lambda wine: wine.year)

def clickedCountry():
    wines.sort(key = lambda wine: wine.country)

buttonOk = Button(window, text = "Adicionar", command = clickedOk)
buttonOk.grid(column = 2, row = 4)

buttonSave = Button(window, text = "Salvar", command = clickedSave)
buttonSave.grid(column = 4, row = 4)

buttonRemove = Button(window, text = "Remover", command = clickedDelete)
buttonRemove.grid(column = 3, row = 4)

buttonClose = Button(window, text = "Fechar", command = clickedClose)
buttonClose.grid(column = 5, row = 4)

buttonYear = Button(window, text = "Ano", command = clickedYear)
buttonYear.grid(column = 2, row = 5)

buttonCountry = Button(window, text = "Pais", command = clickedCountry)
buttonCountry.grid(column = 3, row = 5)

window.mainloop()