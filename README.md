Simple python script that gets baselinker invoices to data json

- Enter the date format UNIX
- Enter your token
- Run script

First of all the baselinker api has a limit of 100 requests, so the idea that the script will be refreshed every 10 seconds.

Secondly, the date in UNIX format will generate the file every 2 hours because new invoices may be added every 2 hours or more often, and we want to have all

# Baselinker_all_invoices_from_API
