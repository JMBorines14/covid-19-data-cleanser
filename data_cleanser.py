import pandas as pd #Make sure that pandas is installed in your PC.
import numpy as np  #Make sure that numpy is installed in your PC.

# Import the CSV file. For simplicity, CSV file and Python file must be in the same directory.
# Case Information file must be named case_information.csv. Otherwise, the program will return an error.
data_to_read = pd.read_csv('case_information.csv')

# Assign a new column named 'Repatriate' that outputs YES if Region of Residence is "ROF" and NO otherwise.
data_to_read = data_to_read.assign(Repatriate = lambda x: x.RegionRes == "ROF")

#Change AgeGroup according to specified format
data_to_read['AgeGroup'] = data_to_read['AgeGroup'].replace(
    ['0 to 4', '5 to 9', ' '],
    ['00 to 04', '05 to 09', 'NO DATA'])

#Change RegionRes to specified format
data_to_read['RegionRes'] = data_to_read['RegionRes'].replace(
    ['Region I: Ilocos Region', 'CAR', 'Region II: Cagayan Valley', 'Region III: Central Luzon', 'NCR', 'Region IV-A: CALABARZON', 'Region IV-B: MIMAROPA', 'Region V: Bicol Region', 'Region VI: Western Visayas'],
    ['01 - Region 1', '02 - CAR', '03 - Region 2', '04 - Region 3', '05 - NCR', '06 - Region 4A', '07 - Region 4B', '08 - Region 5', '09 - Region 6'])

data_to_read['RegionRes'] = data_to_read['RegionRes'].replace(
    ['Region VII: Central Visayas', 'Region VIII: Eastern Visayas', 'Region IX: Zamboanga Peninsula', 'Region X: Northern Mindanao', 'CARAGA', 'BARMM', 'Region XI: Davao Region', 'Region XII: SOCCSKSARGEN', 'ROF'], 
    ['10 - Region 7', '11 - Region 8', '12 - Region 9', '13 - Region 10', '14 - CARAGA', '15 - BARMM', '16 - Region 11', '17 - Region 12', np.nan])

#Change date formatting to specified format
#Note: There may be no visible changes when opened at Excel
data_to_read['DateSpecimen'] = pd.to_datetime(data_to_read['DateSpecimen']).dt.strftime("%m/%d/%Y")
data_to_read['DateResultRelease'] = pd.to_datetime(data_to_read['DateResultRelease']).dt.strftime("%m/%d/%Y")
data_to_read['DateRepConf'] = pd.to_datetime(data_to_read['DateRepConf']).dt.strftime("%m/%d/%Y")
data_to_read['DateDied'] = pd.to_datetime(data_to_read['DateDied']).dt.strftime("%m/%d/%Y")
data_to_read['DateRecover'] = pd.to_datetime(data_to_read['DateRecover']).dt.strftime("%m/%d/%Y")
data_to_read['DateOnset'] = pd.to_datetime(data_to_read['DateOnset']).dt.strftime("%m/%d/%Y")

#Replace all existing characters from enye to N
data_to_read = data_to_read.replace('Ñ', 'N', regex = True)

#Drop all columns that will affect the database
#The following columns have been droped: BarangayPSGC, CityMuniPSGC, BarangayRes, ValidationStatus
data_to_read.drop(columns=['BarangayPSGC','CityMuniPSGC','BarangayRes','ValidationStatus'], inplace = True)

#Export changes to CSV File.
data_to_read.to_csv('data_cleansed.csv', index=False)
print('Conversion successful.')