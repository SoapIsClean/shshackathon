#!/usr/bin/env python
# coding: utf-8

# In[120]:


from tkinter import *
import time

class Interface():
    def __init__(self):
        global master
        master = Tk()
        
        # grid
        
        mainframe = Frame(master)
        mainframe.grid(column=0,row=0, sticky=(N,W,E,S), padx = 50, pady = 50)
        mainframe.columnconfigure(0, weight = 1)
        mainframe.rowconfigure(0, weight = 1)

        
        # rucc
        ruccDef = StringVar(master)
        ruccCodes = {0, 1, 2, 3, 4, 5, 6, 7, 8, 'RUCC code'}
        ruccDef.set('rucc code')
        ruccPop = OptionMenu(mainframe, ruccDef, *ruccCodes)
        ruccPop.grid(row = 0, column = 0, padx = 40, pady =20)
        
        def change_Rucc(*args):
            print(ruccDef.get())            
        ruccDef.trace('w', change_Rucc)
        
        def popupRucc():
            popup = Tk()
            popup.wm_title("rucc codes")
            label = Label(popup, text='RUCC code description', font=("Verdana", 12))
            label.pack(side="top", fill="x", pady=10)
            codes = ["'Metro - Counties in metro areas of fewer than 250,000 population': 0", "'Metro - Counties in metro areas of 1 million population or more': 1",
                     "'Nonmetro - Urban population of 2,500 to 19,999, adjacent to a metro area': 2", "'Nonmetro - Urban population of 2,500 to 19,999, not adjacent to a metro area': 3",
                     "'Nonmetro - Urban population of 20,000 or more, adjacent to a metro area': 4", "'Metro - Counties in metro areas of 250,000 to 1 million population': 5",
                     "'Nonmetro - Completely rural or less than 2,500 urban population, not adjacent to a metro area': 6",
                     "'Nonmetro - Completely rural or less than 2,500 urban population, adjacent to a metro area': 7",
                     "'Nonmetro - Urban population of 20,000 or more, not adjacent to a metro area': 8"]
            for i in range(9):
                defs = Label(popup, text=codes[i], font =("Verdana", 10))
                defs.pack(fill = "x", pady=10)
            B1 = Button(popup, text="Okay", command = popup.destroy)
            B1.pack()
            popup.mainloop()
            
        codeDef = Button(master, text = "RUCC Code Info", command = popupRucc)
        codeDef.grid(row=0, column=3, padx = 10, pady =10)
        
        # Urban Influence
        urbDef = StringVar(master)
        urbCodes = {'Urban Influence', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
        urbDef.set('Urban Influence')
        urbPop = OptionMenu(mainframe, urbDef, *urbCodes)
        urbPop.grid(row = 0, column = 3, padx = 40, pady =20)
        
        def change_Urb(*args):
            print(urbDef.get())            
        urbDef.trace('w', change_Urb)
        
        def popupUrb():
            popup = Tk()
            popup.wm_title("Urban Influence Number")
            label = Label(popup, text='Urban Influence Number Description', font=("Verdana", 12))
            label.pack(side="top", fill="x", pady=10)
            codes = ["'Small-in a metro area with fewer than 1 million residents': 0", "'Large-in a metro area with at least 1 million residents or more': 1",
                     "'Noncore adjacent to a small metro with town of at least 2,500 residents': 2",
                     "'Noncore not adjacent to a metro/micro area and contains a town of 2,500  or more residents': 3", "'Micropolitan adjacent to a small metro area': 4",
                     "'Noncore adjacent to a large metro area': 5", "'Micropolitan not adjacent to a metro area': 6",
                     "'Noncore not adjacent to a metro/micro area and does not contain a town of at least 2,500 residents': 7",
                     "'Noncore adjacent to micro area and does not contain a town of at least 2,500 residents': 8", "'Micropolitan adjacent to a large metro area': 9",
                     "'Noncore adjacent to a small metro and does not contain a town of at least 2,500 residents': 10",
                     "'Noncore adjacent to micro area and contains a town of 2,500-19,999 residents': 11"]
            for i in range(12):
                defs = Label(popup, text = codes[i], font = ("Verdana", 10))
                defs.pack(fill = "x", pady = 10)
            B1 = Button(popup, text="Okay", command = popup.destroy)
            B1.pack()
            popup.mainloop() 
            
        urbCodeDef = Button(master, text = "Urban Influence Info", command = popupUrb)
        urbCodeDef.grid(row=0, column=4)
        
        # Economic dependency
        
        ecoDef = StringVar(master)
        ecoCodes = {0, 1, 2, 3, 4, 5, 'Economic Dependency'}
        ecoDef.set('Economic Dependency')
        ecoPop = OptionMenu(mainframe, ecoDef, *ecoCodes)
        ecoPop.grid(row = 0, column = 2, padx = 40, pady = 20)
        
        def change_Eco(*args):
            print(ecoDef.get())            
        ecoDef.trace('w', change_Eco)
        
        def popupEco():
            popup = Tk()
            popup.wm_title("Economic Dependency")
            label = Label(popup, text='Economic Dependency Codes', font=("Verdana", 12))
            label.pack(side="top", fill="x", pady=10)
            codes = ["'Manufacturing-dependent': 0", "'Mining-dependent': 1", "'Nonspecialized': 2", "'Federal/State government-dependent': 3", "'Farm-dependent': 4", "'Recreation': 5"]
            for i in range(6):
                defs = Label(popup, text=codes[i], font =("Verdana", 10))
                defs.pack(fill = "x", pady=10)
            B1 = Button(popup, text="Okay", command = popup.destroy)
            B1.pack()
            popup.mainloop()
            
        ecoCodeDef = Button(master, text = "Economic Dependency Info", command = popupEco)
        ecoCodeDef.grid(row=0, column=5)
        
        # Numerical Data

                
        varNames = ["Civilian Labor", "Unemployment", "Uninsured Adults", "Adult Obesity", "Adult Smoking", "Diabetes", "Low Birthweight", "Excessive Drinking",
                      "Physical Inactivity", "Air Pollution Particulate Matter", "Homicides Per 100k", "Motor Vehicle Crash Deaths per 100k", "Population Per Dentist",
                      "Population Per Primary Care Physician", "Percent Female", "Percent Below 18", "Percent Aged 65 And Older", "Percent Hispanic",
                      "Percent Nonhispanic African American", "Percent Nonhispanic White", "Percent American Indian or Alaskan Native",
                      "Percent Asian", "Percent Adults Without High School Diploma", "Percent Adults With Only High School Diploma", "Percent Adults With Some College",
                      "Percent Adults With Bachelors or Higher", "Birth Rate Per 1k", "Death Rate Per 1k"]
        boxes = []
        sliders = []
        
        for i in range(28):
            label = Label(master, text = varNames[i], padx = 10, pady = 10)
            boxes.append(Entry(master))
            sliders.append(Scale(master, from_=0, to=1000, orient=HORIZONTAL))
            if(i == )
            
            label.grid(row = 2 * int(i / 2) + 2, column = 0 + (i % 2) * 3)
            boxes[i].grid(row = 2 * int(i / 2) + 2, column = 1 + (i % 2) * 3)
            sliders[i].grid(row = 2 * int(i / 2) + 2, column = 2 + (i % 2) * 3)
        
        mainloop()

app = Interface()


# In[118]:


app = Interface()

