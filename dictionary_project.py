import sys
import PySimpleGUI as pg
import json
from my_json import Dictionary

pg.theme("DarkTeal10")
fontsize=("Times","16", "bold italic")
def dump(self):
    js = open("C:\\Users\\MARIAM\\Desktop\\MY DICTIONARY PROJECT\\filtered.json")
    tot = json.load(js)
    return tot.get(self.word,  "Word not found")
def meaning(self):
    return self.dump().get("MEANINGS",  "Word not found")
def antonyms(self):
    return self.dump().get("ANTONYMS",  "Word not found")
def synonyms(self):
    return self.dump().get("SYNONYMS",  "Word not found")


layout = [
    [pg.Text("HM WEBSTER  2023", font=("Verdana","16","bold italic"), background_color="Red" ,expand_x = False, justification="centre", pad=(20, 25))],
    [pg.Input("Search word!", font = fontsize, expand_x = True, pad=(20, 15), key="search_input", background_color="White")],
    [pg.Button("Search", font = fontsize, expand_x = True, pad=(15, 10)), pg.Button("Clear", font = fontsize, expand_x = False, pad=(10, 5))],
    [pg.Text("MEANING:", font=("Verdana","16","bold italic"),expand_x = False, pad=(20, 10))],
    [pg.Output(expand_x = True, expand_y = True, font=("helvetica 16"), pad=(15,10), text_color="#1f3f42", background_color="White")],
    
]

win = pg.Window("HM WESTER", layout=layout, resizable=True, margins=(20, 15), size=(650, 600), finalize=True)

while True:
    evt, values = win.Read()
    if evt=="Clear":
        win["search_input"].update(value="")
    if evt=="Search":
        dc = Dictionary(values["search_input"])
        print("MEANING:")
        for m in dc.meaning():
            print(f"{m[1]} ({m[0]})")
        print("MEANING:")
        for m in dc.antonyms():
            print(m)

        print("MEANING:")
        print(dc.synonyms())
    if evt == pg.WIN_CLOSED:
        sys.exit()
        win.close()



