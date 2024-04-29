import tkinter as tk, json, requests as rq, pandas as pd
from pprint import pprint

#Filter for finding facilities that match search
def flt(ind:str) -> bool:
    ind, item = ind
    return val.upper() in dt[ind][1][1].upper()

def printValue(PID:str)->str:
    ret = ''
    response = (rq.get(f'https://echodata.epa.gov/echo/eff_rest_services.get_effluent_chart?p_id={PID}&output=JSON'))
    ret = response.json()
    return ret

def main():
    global val, dt, window, frame
    df = printValue('PA0028177')['Results']
    pprint(df)
    #pprint(df.iloc['PermFeatures'])
if __name__ == "__main__":
    main()