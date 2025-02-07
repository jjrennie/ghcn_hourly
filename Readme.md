# Get Hourly Station Data from GHCNh
## Written By Jared Rennie (@jjrennie)

Taps into the NCEI Website to get hourly station data for a particular year. This repo also has a file tiltled 'get_ghcnh_por.sh' that gets data for its period of record, but fair warning the file sizes are very large (hundreds of MBs)

- GHCNh Info: https://www.ncei.noaa.gov/products/global-historical-climatology-network-hourly
- GHCNh Documentation: https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/doc/ghcnh_DOCUMENTATION.pdf

### What You Need

First off, the entire codebase works in Python 3. In addition to base Python, you will need the following packages installed: 
- pandas (to slice annd dice the data)
    
The "easiest" way is to install these is by installing <a href='https://www.anaconda.com' target="_blank">anaconda</a>, and then applying <a href='https://conda-forge.org/' target="_blank">conda-forge</a>. Afterward, then you can install the above packages. 

### Importing Packages
Assuming you did the above, it should (in theory) import everything no problem: