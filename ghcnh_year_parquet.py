# Python Code to get Hourly Station Data from GHCNh parquet files.
# Input is Station ID and Year, and outputs data into a csv file.

# Import Packages
import sys
import pandas as pd

# Read in Arguments (Station ID and Year)
if len(sys.argv) < 3:
    sys.exit("USAGE: <STATION ID> <YEAR>")  
stationID = sys.argv[1]
inYear= sys.argv[2]

# DEFINE URL (parquet)
ghcnh_url = 'https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/access/by-year/'+str(inYear)+'/parquet/GHCNh_'+str(stationID)+'_'+str(inYear)+'.parquet'

# Pull Data into Pandas DataFrame
try:
  ghcnhPandas = pd.read_parquet(ghcnh_url)
except Exception as e:
  sys.exit(e)

# Get a subset of Data based on User inputs
subsetCols=['Station_ID','Station_name','DATE','Latitude','Longitude','Elevation',
            'temperature','dew_point_temperature','sea_level_pressure','wind_direction','wind_speed','wind_gust','precipitation','visibility','remarks']
subsetPandas = ghcnhPandas[subsetCols] 

# Send to CSV
outFile='./'+stationID+'_Hourly_'+str(inYear)+'.csv'
subsetPandas.to_csv(outFile,index=False)

# If you made it this far. Success!
print('SUCESSFULLY GOT DATA AND PUT IN:',outFile)
sys.exit()
