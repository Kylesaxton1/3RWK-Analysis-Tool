# script that cleans JSON for relevant data
import pandas as pd
import json

# load in the response file 
with open('./facilities_raw.json') as f:
   data = json.load(f)

# only work with the actual data, "unwrap" until the correct set
results = data["Results"]
results = results["FRSFacility"]
facility_df = pd.DataFrame(results)

# the "ProgramFacilites" column holds all programs that facility is associated with
# we only want NPDES and so we will replace that cell with only the NPDES dictionary
npdes = {}
for index, row in facility_df.iterrows():
    prgms = row["ProgramFacilities"]
    for prgm_dict in prgms:
        if prgm_dict["ProgramSystemAcronym"] == "NPDES":
            npdes = prgm_dict
            row["ProgramFacilities"] = npdes

# drop the "ProgramFacilites" column in order to add new columns with the dictionary data
npdes_info = facility_df["ProgramFacilities"]
facility_df = facility_df.drop("ProgramFacilities", axis='columns')

# for each key in the dictionaries, create a separate dictionary mapped to the cooresponding index of the facility 
i = 0
pacronym = {}
pid = {}
pfacilityname = {}
for npdes_dict in npdes_info:
    pacronym[i] = npdes_dict["ProgramSystemAcronym"]
    pid[i] = npdes_dict["ProgramSystemId"]
    pfacilityname[i] = npdes_dict["ProgramFacilityName"]
    i += 1

# add columns to the dataframe via mapping
facility_df['ProgramSystemAcronym'] = facility_df.index.map(pacronym) 
facility_df['PID'] = facility_df.index.map(pid) 
facility_df['ProgramFacilityName'] = facility_df.index.map(pfacilityname) 

# print(facility_df.head())

# save the cleaned dataframe to a JSON file
facility_df.to_json("./facilities.json")





