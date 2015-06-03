#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#       Title: PTC Referral Script
#       Author: PhoenixIT
#       Web: https://phoenixit.org
#       Twitter: @phoenixits
#       Email: admin@phoenixit.org
#
#       Description:
#               This script was made to do simple calculations
#               on EvolutionScript PTC platforms. What it does is
#               simply to calculate earnings: daily, weekly, yearly
#               on rented referrals and direct referrals.


'''value change this to fit the PTC program'''
value = 0.001
'''direct referral clicks'''
drc = float(raw_input("DR Clicks: "))
'''rented referral clicks'''
rrc = float(raw_input("RR Clicks: "))
'''autopay'''
atp = float(raw_input("Autopay: "))
'''total amount clicks'''
clicks = drc+rrc
'''calculate profits from click'''
profit = clicks*value
'''withdraw autopay to get'''
total = profit-atp
'''daily profits'''
print("Daily Profit: $",total)
'''calculate weekly profits'''
wp = total*7
print("Weekly profits: $", wp)
'''calculate monthly profits'''
mp = wp*4
print("Monthly profits: $", mp)
'''calculate yearly profits'''
yp = mp*12
print("Yearly profits: $", yp)
