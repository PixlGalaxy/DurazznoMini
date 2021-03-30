#GitHub Version

import requests
import time
import os



url = 'https://drive.google.com/uc?export=download&id=1JFuS6IqMyhOSK4giOAY7ui95NXEmJPf1'
r = requests.get(url, allow_redirects=True)

open('DURAZZNO MINI.pyw', 'wb').write(r.content)

url = 'https://drive.google.com/uc?export=download&id=1XIebvdGvIyw-XPLqMkAbpAS6Wmz5NO5y'
r = requests.get(url, allow_redirects=True)

open('psp.pyw', 'wb').write(r.content)

url = 'https://drive.google.com/uc?export=download&id=1xF_SGEPB_ydm2tNgach2WCd-TNLGK09H'
r = requests.get(url, allow_redirects=True)

open('papp.pyw', 'wb').write(r.content)


url = 'https://drive.google.com/uc?export=download&id=11H6FCK7Ut5Mhi7USVhHPOBFI3wCDJ8bD'
r = requests.get(url, allow_redirects=True)

open('papp.png', 'wb').write(r.content)


url = 'https://drive.google.com/uc?export=download&id=1AiBXtmozNKCGe1e52n7fvflt67hObeq1'
r = requests.get(url, allow_redirects=True)

open('acad.png', 'wb').write(r.content)

url = 'https://drive.google.com/uc?export=download&id=1v7yindDAfCEjndA9TMnra-j1dQSQgxA_'
r = requests.get(url, allow_redirects=True)

open('aacr.png', 'wb').write(r.content)

url = 'https://drive.google.com/uc?export=download&id=11Z1C8RKWR0PtcZ4Rwwip1YyMWqdrhsQO'
r = requests.get(url, allow_redirects=True)

open('tlau.png', 'wb').write(r.content)










os.startfile("DURAZZNO MINI.pyw")
os.startfile("upd.pyw")