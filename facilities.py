# script that gets all the relevant facilites and cleans that JSON for relevant data
import requests
import pandas as pd
import numpy as np
import json

# baseURL = https://ofmpub.epa.gov/frs_public2/frs_rest_services.get_facilities


currURL = "https://ofmpub.epa.gov/frs_public2/frs_rest_services.get_facilities?state_abbr=PA&city_name=Pittsburgh&city_name=Pittsburgh,%20City%20of&pgm_sys_acrnm=NPDES&city_name=Pittsburgh,%20PA&county_name=Allegheny&county_name=Allegheny%20County&program_output=yes&output=JSON"
# state_abbr = PA
# city_name = Pittsburgh
# city_name = Pittsburgh, City of
# city_name = Pittsburgh, PA
# county_name = Allegheny
# county_name = Allegheny County
# program_output = Yes
# output = JSON

response = requests.get(currURL)

data = response.json()

# with open('./facilities.json', 'w') as f:
#     json.dump(data, f) 

results = data["Results"]
results = results["FRSFacility"]
facility_df = pd.DataFrame(results)
print(facility_df.head())

for index, row in facility_df.iterrows():
    prgms = row["ProgramFacilities"]
    
    for prgm_dict in prgms:
        if prgm_dict["ProgramSystemAcronym"] == "NPDES":
            print("here")


