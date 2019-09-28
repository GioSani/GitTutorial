import numpy as np
import pandas as pd
import random


past_years = [2018,2017,2016,2015,2014,2013,2012,2011,2010]
years_projected = [2019,2020,2021,2022,2023,2024,2025,2026,2027,2028]
#print d.values()
insurance_market_premium=pd.Series([542200592,441400962,393038614,359798773,
                                    302640671,471066120,515471427,321147047,361457160],
                                   index = past_years)
insurance_market_re=pd.Series([129923157,96626439,81132131,83226631,
                               79352317,52091504,54616800,48441801,53857557],
                              index = past_years)
#print "Insurance Market Premium"
#print (insurance_market_premium)
#print "Insurance Market Reinsurance"
#print (insurance_market_re)
#Reinsurance share in premium (Market)
reinsurance_share = insurance_market_re/insurance_market_premium
#print "Reinsurance share in premium(PAST)"
#print (reinsurance_share)
st_reinsurance_share = np.std(reinsurance_share)

#print st_reinsurance_share
#random.normal(loc=0.0, scale=1.0, size=None)
mean_reinsurance_share = np.mean(reinsurance_share)
#print mean_reinsurance_share
#print mean_reinsurance_share
nd_reinsurance_list=np.random.normal(loc=mean_reinsurance_share, scale=st_reinsurance_share, size=10)
#print "Reinsurance share in premium"
nd_reinsurance_share = pd.Series(nd_reinsurance_list, index=years_projected)
#print nd_reinsurance_share

# projecting GPI premium from GDP and GDP Growth

GDP_GROWTH = pd.Series([4.7,4.8,2.8,2.8,4.6,3.4,6.4,7.2,6.2,-3.2,2.4,12.2,9.4,9.6,5.7])
GDP_Growth_mean= np.mean(GDP_GROWTH)
#print 'GDP Growth mean'
GDP_Growth_mean=round(GDP_Growth_mean,3)
print 'mean'
print GDP_Growth_mean

#print 'GDP Growth STDIV'
GDP_GROWTH_ST = np.std(GDP_GROWTH)
GDP_GROWTH_ST = round(GDP_GROWTH_ST,3)
#print 'stdiv'
#print GDP_GROWTH_ST
def ran():
    nd_GDP_GROWTH = np.random.normal(loc=GDP_Growth_mean,scale=GDP_GROWTH_ST,size=10)
    gdp_growth_persent = nd_GDP_GROWTH/100+1
#print 'GDP Growth persents (Normal Distribution)'
    nd_gdp_growth_persent=pd.Series(nd_GDP_GROWTH,index=years_projected)
#print 'gdp growth'
#print nd_gdp_growth_persent

    gdp = 41077
#persent of insurance premium of market to GDP
    market_premium_to_GDP = round(float(insurance_market_premium[2018]/10000)/gdp,2)/100
#persent of insurance premium of market to GDP

#print 'gdp to ppremium'
#print float(market_premium_to_GDP)
#print gdp_growth_persent
    gdp_growth_list = gdp_growth_persent
    gdp_list = []
    for g in gdp_growth_list:

        g=round(g,4)
        gdp=gdp*round(g,3)

        gdp_list.append(gdp)
#print gdp_list
    gdp_series = pd.Series(gdp_list,index=years_projected)
#print 'GDP (Normal Distribution)'
#print gdp_series
    market_insurance_premium = gdp_series * market_premium_to_GDP

#print 'Market Insurance Premium (Normal Distribution)'
#print market_insurance_premium

    GPI_market_share_holding = [0.195,0.195,0.205,0.205,0.21,0.21,0.22,0.22,0.22]
    GPI_premium_list = []
    for i in market_insurance_premium:
        n=0
        item = i*GPI_market_share_holding[n]
        n+=1
        GPI_premium_list.append(item)
#print GPI_premium_list


    GPI_premium_series = pd.Series(GPI_premium_list,index = years_projected)
    GPI_premium_series

#print 'GPI Premium BRUTO (Projection)'
#print GPI_premium_series
#print 'GPI Reinsurance (Projected)'

    GPI_reinsurance=np.multiply(GPI_premium_series,nd_reinsurance_share)
#print GPI_reinsurance
#print 'GPI Premium NETO'
    GPI_premium_neto=GPI_premium_series-GPI_reinsurance
    return GPI_premium_series
#print GPI_premium_neto
print ran()