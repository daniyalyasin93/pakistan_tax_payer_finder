# pakistan_tax_payer_finder
A helpful script i wrote to find NTN info of a registered tax payer in Pakistan

Usage: -f[Path To xlsx file] -n[Search strings] -n[Search strings]

Get the file form FBR web site: https://www.fbr.gov.pk/download-atl/132041

The program will cache the xlsx file after its fully parsed. This cache will be stored in a pickle file in the same directory, if this file is present when the program is run, the search will be much faster

Example:

python3 search.py -f'/home/dyasin/Downloads/2022091965328335ATL_IT.xlsx' -nGREEN -nPHARMACY
