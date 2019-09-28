# -*- coding: utf-8 -*-
from statments import cash_flow_2017, cash_flow_2018
from statments import balance_2017,   balance_2018
from statments import income_2017, income_2018
from data import ran, years_projected
from projections import fcfefunction

#import matplotlib.pyplot as plt

#print fcfefunction()
import projections
import numpy as np
import pandas as pd
#from data import nd_gdp_growth_persent
desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',15)


#fcff_data = pd.DataFrame({'წმინდა სამუშაო კაპიტალის ცვლილება':wc_change_dict,'ცვეთა და ამორტიზაცია':dep,'CAPEX':capex_s,'წლის წმინდა მოგება':dict['წლის წმინდა მოგება']},columns=['წმინდა სამუშაო კაპიტალის ცვლილება','ცვეთა და ამორტიზაცია','CAPEX','წლის წმინდა მოგება'])
#print fcff_data
fcfe =fcfefunction()
#fcfe = fcff_data['წლის წმინდა მოგება']+fcff_data['ცვეთა და ამორტიზაცია']-fcff_data['წმინდა სამუშაო კაპიტალის ცვლილება']-fcff_data['CAPEX']
#print fcfe
#print fcff_data
#print fcff[2028]
Adjusted_cost_of_equity=0.1173

mean = 5.267

standard_div = 3.527
def discoundetFCFE(Adjusted_cost_of_equity):
    nd_gdp_growth_persent=np.random.normal(loc=7.267,scale=1.527,size=10)
    nd_gdp_growth_persent=nd_gdp_growth_persent/100+1

    k=0
    equity_list=[]
    #while k<1000:
    fcfe=fcfefunction()['წლის წმინდა მოგება']+fcfefunction()['ცვეთა და ამორტიზაცია']-fcfefunction()['წმინდა სამუშაო კაპიტალის ცვლილება']-fcfefunction()['CAPEX']
    #print fcfe
    n=1
        #print fcfe
    dfcfe_list=[]
    for i in fcfe:

        dfcfe = i/(1+Adjusted_cost_of_equity)**n
        n+=1
        dfcfe_list.append(dfcfe)


    terminal = dfcfe_list[len(fcfe)-1]/(Adjusted_cost_of_equity-nd_gdp_growth_persent[9]/100)

    disc_terminal = terminal/(1+Adjusted_cost_of_equity)**len(fcfe)

    value_equity=sum(dfcfe_list)+disc_terminal
    equity_list.append(value_equity)
    k=k+1
        #print equity_list
    return value_equity

#print discoundetFCFE(Adjusted_cost_of_equity)

def montecarlo(trails,Adjusted_cost_of_equity):
    k=0
    equity_list=[]
    while k<trails:
        value = discoundetFCFE(Adjusted_cost_of_equity)
        equity_list.append(value)
        k=k+1

    hst=pd.Series(equity_list)
    hst.hist(bins=40)
    #plt.hist(equity_list, bins=40)
    return equity_list


montecarlo(100,Adjusted_cost_of_equity)
