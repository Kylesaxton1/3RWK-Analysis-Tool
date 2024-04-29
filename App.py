import tkinter as tk, json, requests as rq, sys, os
from pprint import pprint

dataFS:str = ''
if getattr(sys, 'frozen', False):
    dataFS = file=os.path.join(sys._MEIPASS, "Data/facilities.json")
else:
    dataFS = "Data/facilities.json"

#Filter for finding facilities that match search
def flt(ind:str) -> bool:
    ind, item = ind
    return val.upper() in dt[ind][1][1].upper()

#Event Handler for search button/enter
def EnterClick(Event):
    global val
    
    #retrieve search value
    strs: list[str] = []
    for entry in entries:
        strs.append(entry.get()); entry.delete(0, tk.END)

    #make global variable for search value
    val = strs[0]

    #make new window and frame
    window2: tk.Tk = tk.Tk()
    frame2 = tk.Frame(master = window2, width = 115)
    frame2.pack()

    #get filtered data
    filt = filter(flt, dt.items())
    
    #Produce string to display
    finalStr = ''
    for facility in filt:
        for lst in facility:
            if str == type(lst):
                continue
            for tup in lst:
                if tup[1] == None:
                    finalStr += "NONE\t"
                else:
                    finalStr += tup[1][:6] + '\t'
            finalStr += '\n'
    #print(finalStr)
   
    #Make filtered data visible        
    text = tk.Text(frame2, height = 300, width=115)
    text.insert(tk.END, "RegId\tFacNm\tLocAd\tSuppL\tCityN\tCounty\tStAbr\tZipCode\tFIPSC\tLat83\tLon83\tPSA\ttPID\tPFN\n")
    text.insert(tk.END, finalStr)
    text.pack()

#Put all features on page
def toutpacker(): 
    for label in labels:
        label.pack()

    for entry in entries:
        entry.pack()

    for button in buttons:
        button.pack()

#Main Entry point
def main():
    global labels, entries, buttons, dt, val, window, frame
    labels = []
    entries = []
    buttons= []
    dt = {}


    val = ''

    with open(dataFS) as data:
        d:dict[str, dict[str, str]] = json.load(data)
        for i in d:
            #print(i)
            for j in d[i]:
                try:
                    dt.get(j).append((i, d[i][j]))
                except:
                    dt.update({j:[(i, d[i][j])]})

    window = tk.Tk(); frame = tk.Frame(master=window, width=200, height=300)
    frame.pack()
    window.bind("<Key-Return>",EnterClick)

    labels.append(tk.Label(master=frame, text = "Three Rivers Water Keeping"))
    labels.append(tk.Label(master=frame, text = "Facility Name"))

    entries.append(tk.Entry(master=frame, text = "Facility Name"))

    buttons.append(tk.Button(master=frame, text = "Enter"))
    buttons[0].bind("<Button-1>", EnterClick)
    toutpacker()
    window.mainloop()

if __name__ == "__main__":
    main()
