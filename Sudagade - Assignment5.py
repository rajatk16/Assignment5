import numpy as np
# The University of Texas At Dallas
# MS FERM
# Financial Information and Analytics
# Assignment 5
# Cost of Capital

# Question 1: 
# The Down and Out Co. just issued a dividend of $2.06 per share on its common stock. 
# The company is expected to maintain a constant 6 percent growth rate in its dividends indefinitely. 
# If the stock sells for $55 a share, what is the company's cost of equity? (Do not round your intermediate calculations.)
# (2.23(1.05)/30) + 0.05
# Using Dividend Growth Model
dividend = 2.06
growth_rate = 0.06
selling_price = 55
cost_of_equity = (dividend * ((1 + growth_rate)/(selling_price)))+growth_rate
print("""Question 1:
The cost of equity is {:,.2f}%\n""".format(cost_of_equity*100))

# Question 2:
# The Up and Coming Corporation’s common stock has a beta of 1.2. 
# If the risk-free rate is 5 percent and the expected return on the market is 11 percent, what is the company's cost of equity capital? (Do not round your Intermediate calculations.)
# 0.055 + 1.2(0.13 - 0.055)
# Using CAPM
beta = 1.2
risk_free_rate = 0.05
expected_return = 0.11
cost_of_equity_capital = risk_free_rate + beta*(expected_return - risk_free_rate)
print("""Question 2:
The Cost Of Equity Capital is: {:,.2f}%\n""".format(cost_of_equity_capital*100))

# Question 3:
# Stock in Country Road Industries has a beta of 0.64. 
# The market risk premium is 8 percent, and T-bills are currently yielding 5.5 percent. 
# The company's most recent dividend was $1.8 per share, and dividends are expected to grow at a 4.5 percent annual rate indefinitely. 
# If the stock sells for $37 per share, what is your best estimate of the company's cost of equity? (Do not round your Intermediate calculations.)
# Using CAPM,
beta = 0.64
risk_free_rate = 0.055
market_risk_premium = 0.08
capm_coc = risk_free_rate + beta*market_risk_premium
# Using Dividend Growth Model
dividend = 1.8
growth_rate = 0.045
selling_price = 37
dgm_coc = (dividend * ((1 + growth_rate)/(selling_price)))+growth_rate
estimate_cost_of_equity = (capm_coc + dgm_coc)/2
print("""Question 3:
The Estimated Cost of Capital is: {:,.2f}%\n""".format(estimate_cost_of_equity*100))

# Question 4:
# Holdup Bank has an issue of preferred stock with a $7 stated dividend that just sold for $93 per share. 
# What is the bank's cost of preferred stock?
dividend = 7
selling_price = 93
cost_of_preferred_stock = dividend / selling_price
print("""Question 4:
The Cost of Preferred Stock is {:,.2f}%\n""".format(cost_of_preferred_stock*100))

# Question 5:
# Waller, Inc., is trying to determine its cost of debt. 
# The firm has a debt issue outstanding with 9 years to maturity that is quoted at 102 percent of face value. 
# The issue makes semiannual payments and has an embedded cost of 12 percent annually.
# a.	What is the company's pretax cost of debt? (Do not round your intermediate calculations.)
# b.	If the tax rate is 34 percent, what is the after tax cost of debt? (Do not round your intermediate calculations.)
face_value = 1000
coupon_rate = 0.12
period = 2
pmt = face_value*(coupon_rate/period)
pv = -(face_value*1.02)
years_to_maturity = 9
nper = period * years_to_maturity
pre_tax_cod = np.rate(nper,pmt,pv,face_value)*2
after_tax_cod = pre_tax_cod*(1 - 0.34)
print("""Question 5:
a. The Pretax Cost of Debt is: {0:,.2f}%
b. THe After-Tax Cost of Debt is: {1:,.2f}%\n""".format(pre_tax_cod*100, after_tax_cod*100))

# Question 6:
# Jiminy's Cricket Farm issued a 3O-year, 7 percent semi-annual bond 9 years ago. 
# The bond currently sells for 87 percent of its face value. 
# The book value of the debt issue is $23 million.  
# The company's tax rate is 34 percent.
# In addition, the company has a second debt issue on the market, a zero coupon bond with 9 years left to maturity; the book value of this issue is $85 million and the bonds sell for 80 percent of par.
# a.	What is the company's total book value of debt? (Do not round your intermediate calculations.)
# b.	What is the company's total market value of debt? (Do not round your intermediate calculations.)
# c.	What is your best estimate of the after tax cost of debt? (Do not round your intermediate calculations.)
years = 21
period = 2
nper1 = years * 2  
percent = 0.07
face_value = 1000
selling_price_percent1 = 0.87
selling_price_percent2 = 0.8
book_value1 = 23000000
tax_rate = 0.34
book_value2 = 85000000
years2 = 9
nper2 = years2*2
pmt1 = face_value*(percent/period)
bvd = book_value1 + book_value2
print("""Question 6:
a. The Company's total book value of debt is ${:,.2f}""".format(bvd))
mvd = (selling_price_percent1*book_value1) + (selling_price_percent2*book_value2)
print("b. The company's total market value of debt is ${:,.2f}".format(mvd))
pv1 = -(face_value*selling_price_percent1)
ytm1 = np.rate(nper1,pmt1,pv1,face_value)*2
after_tax_cod1 = ytm1*(1 - tax_rate)
pv2 = -(face_value*selling_price_percent2)
ytm2 = np.rate(nper2,0,pv2,face_value)*2
after_tax_cod2 = ytm2*(1 - tax_rate)
after_tax_cod = (after_tax_cod1*((selling_price_percent1*book_value1)/mvd)) + (after_tax_cod2*((selling_price_percent2*book_value2)/mvd))
print("c. My best estimate of the after tax cost of debt is {:,.2f}%\n".format(after_tax_cod*100))
# Question 7:
# Sixx AM Manufacturing has a target debt-equity ratio of 0.53. 
# Its cost of equity is 18 percent, and its cost of debt is 12 percent. 
# If the tax rate is 31 percent, what is the company's WACC?
target_debt_equity = 0.53
cost_of_equity = 0.18
cost_of_debt = 0.12
tax_rate = 0.31
wacc = (cost_of_equity*(1/(1 + target_debt_equity))) + (0.1*((target_debt_equity/(1 + target_debt_equity)))*(1 - tax_rate))
print("""Question 7:
The Company's WACC is {:,.2f}%\n""".format(wacc*100))

# Question 8:
# Fama's Llamas has a weighted average cost of capital of 11 percent.  
# The company's cost of equity is 17 percent, and its pretax cost of debt is 8 percent. 
# The tax rate is 34 percent. 
# What is the company's target debt-equity ratio? (Do not round your Intermediate calculations.)
wacc = 0.11
cost_of_debt = 0.08
cost_of_equity = 0.17
tax_rate = 0.34
after_tax_cod = cost_of_debt * (1 - tax_rate)
weight_of_equity = (wacc - after_tax_cod)/(cost_of_equity - after_tax_cod)
weight_of_debt = 1 - weight_of_equity
debt_equity_ratio = weight_of_debt/weight_of_equity
print("""Question 8:
The Company's target debt-equity ratio is {:,.2f}\n""".format(debt_equity_ratio))

# Question 9:
# Filer Manufacturing has 9.1 million shares of common stock outstanding. 
# The current share price is $47, and the book value per share is $3. 
# Filer Manufacturing also has two bond issues outstanding.  
# The first bond issue has a face value of $66 million, has an 8 percent coupon, and sells for 93 percent of par. 
# The second issue has a face value of $62.79 million, has an 8 percent coupon, and sells for 95.9 percent of par. 
# The first issue matures in 10 years, the second in 7 years.
# Requirement 1:
# a.	What is Filer's capital structure weight of equity on a book value basis? (Do not round your intermediate calculations.)
# b.	What is Filer's capital structure weight of debt on a book value basis? (Do not round your intermediate calculations.)
# Requirement 2:
# a.	What is Filer's capital structure weight of equity on a market value basis? (Do not round your intermediate calculations.)
# b.	What is Filer's capital structure weight of debt on a market value basis? (Do not round your intermediate calculations.)
no_of_shares = 9100000
book_value_per_share = 3
current_share_price = 47
book_value_of_equity = no_of_shares * (book_value_per_share)
book_value_of_debt1 = 66000000
book_value_of_debt2 = 62790000
bond_selling_price1 = 0.93
bond_selling_price2 = 0.959
total_book_value_of_debt = book_value_of_debt1 + book_value_of_debt2
total_book_value_of_firm = book_value_of_equity + total_book_value_of_debt
book_weight_of_equity = book_value_of_equity / total_book_value_of_firm
book_weight_of_debt = total_book_value_of_debt / total_book_value_of_firm
print("""Question 9:
Requirement 1:
a. Filer's capital structure weight of equity on a book value basis is {0:,.2f}%
b. Filer's capital structure weight of debt on a book value basis is {1:,.2f}%""".format(book_weight_of_equity*100, book_weight_of_debt*100))
market_value_of_equity = no_of_shares * current_share_price
market_value_of_debt1 = book_value_of_debt1 * bond_selling_price1
market_value_of_debt2 = book_value_of_debt2 * bond_selling_price2
total_book_value_of_debt = market_value_of_debt1 + market_value_of_debt2
total_book_value_of_firm = market_value_of_equity + total_book_value_of_debt
market_weight_of_equity = market_value_of_equity / total_book_value_of_firm
market_weight_of_debt = total_book_value_of_debt / total_book_value_of_firm
print("""Requirement 2:
a. Filer's capital structure weight of equity on a market value basis is {0:,.2f}%
b. Filer's capital structure weight of debt on a market value basis is {1:,.2f}%\n""".format(market_weight_of_equity*100, market_weight_of_debt*100))

# Question 10:
# 10.	Filer Manufacturing has 5 million shares of common stock outstanding. 
# The current share price is $84, and the book value per share is $7. 
# Filer Manufacturing also has two bond issues outstanding. 
# The first bond issue has a face value of $60 million, has a 7 percent coupon, and sells for 94 percent of par. 
# The second issue has a face value of $35 million, has an 8 percent coupon, and sells for 107 percent of par. 
# The first issue matures in 22 years, the second in 4 years.
# The most recent dividend was $5.6 and the dividend growth rate is 8 percent. 
# Assume that the overall cost of debt is the weighted average of that implied by the two outstanding debt issues. 
# Both bonds make semiannual payments. 
# The tax rate is 35 percent.
# Required: What is the company's WACC? (Do not round your Intermediate calculations.)
shares = 5000000
tax_rate = 0.35
current_share_price = 84
mve = shares * current_share_price
face_value1 = 60000000
percent1 = 0.94
face_value2 = 35000000
percent2 = 1.07
mvd = (percent1 * face_value1) + (percent2 * face_value2) 
v = mve + mvd
ev = mve/v
dv = 1-ev
dividend = 5.6
growth_rate = 0.08
cost_of_equity = ((dividend*(1 + growth_rate))/ current_share_price) + growth_rate
ytm1 = (np.rate(44,35,-940,1000))*2
ytm2 = (np.rate(16,40,-1070,1000))*2
wd1 = percent1*((face_value1)/mvd)
wd2 = percent2*((face_value2)/mvd)
wa = (1 - tax_rate)*((wd1*ytm1) + (wd2 * ytm2))
wacc = (ev * cost_of_equity) + (dv * wa)
print("""Question 10:
The WACC of the Company is: {:,.2f}%""".format(wacc*100))