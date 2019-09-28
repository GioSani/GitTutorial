# -*- coding: utf-8 -*-
from statments import cash_flow_2017, cash_flow_2018
from statments import balance_2017,   balance_2018
from statments import income_2017, income_2018
#from data import GPI_premium_series, GPI_premium_list,GPI_reinsurance,years_projected
from data import ran, years_projected
import numpy as np
import pandas as pd
desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',15)
def fcfefunction():
#INCOME STATMENT GROWTH RATES
    depretiation_growth = float(cash_flow_2018['ცვეთა და ამორტიზაცია'])/balance_2018['ძირითადი საშუალებები']
    depretiation_growth = round(depretiation_growth,2)
    dziritadi_sashualebebi_growth = float(balance_2018['ძირითადი საშუალებები'])/income_2018['მოზიდული პრემია, ბრუტო']
    dziritadi_sashualebebi_growth = round(dziritadi_sashualebebi_growth,2)
    #print dziritadi_sashualebebi_growth
    #print (len(GPI_premium_list))
    sakomisio_shemosavali_gadazgvevidan_growth = float(income_2018['საკომისიო შემოსავალი გადაზღვევიდან'])/income_2018['მოზიდული პრემია, ბრუტო']
    sakomisio_shemosavali_gadazgvevidan_growth=round(sakomisio_shemosavali_gadazgvevidan_growth,2)
    #print sakomisio_shemosavali_gadazgvevidan_growth
    sainvesticio_sxva_shemosavali = float(income_2018['საინვესტიციო და სხვა შემოსავალი'])/income_2018['მოზიდული პრემია, ბრუტო']
    sainvesticio_sxva_shemosavali = round(sainvesticio_sxva_shemosavali,2)
    #print sainvesticio_sxva_shemosavali
    sadazgveo_zaralebi_NETO = float(income_2018['სადაზღვეო ზარალები, ნეტო'])/income_2018['მოზიდული პრემია, ბრუტო']
    sadazgveo_zaralebi_NETO=round(sadazgveo_zaralebi_NETO,2)
    #print sadazgveo_zaralebi_NETO
    sxva_saoperacio_xarjebi_growth = float(21203)/income_2018['მოზიდული პრემია, ბრუტო']
    sxva_saoperacio_xarjebi_growth=round(sxva_saoperacio_xarjebi_growth,2)
#print sxva_saoperacio_xarjebi_growth
    saprocento_xarji_growth = float(income_2018['საპროცენტო ხარჯი'])*1/income_2018['მოზიდული პრემია, ბრუტო']
    saprocento_xarji_growth=round(saprocento_xarji_growth,4)
#print 'saprocento xarji'
#print saprocento_xarji_growth

# BALANCE GROWTH RATES
#ASSETS
    investiciebi_shvilobil_growth = float(balance_2018['ინვესტიციები შვილობილ კომპანიებში'])/income_2018['მოზიდული პრემია, ბრუტო']
    investiciebi_shvilobil_growth=round(investiciebi_shvilobil_growth,2)
#print investiciebi_shvilobil_growth
    sabanko_depozitebi_growth = float(balance_2018['საბანკო დეპოზიტები'])/income_2018['მოზიდული პრემია, ბრუტო']
    sabanko_depozitebi_growth = round(sabanko_depozitebi_growth,2)
#print sabanko_depozitebi_growth
    gacemuli_sesxebi_growth = float(balance_2018['გაცემული სესხები'])/income_2018['მოზიდული პრემია, ბრუტო']
    gacemuli_sesxebi_growth = round(gacemuli_sesxebi_growth,2)
#print gacemuli_sesxebi_growth
    gadazgvevis_aqtivebi_growth = float(balance_2018['გადაზღვევის აქტივები'])/income_2018['მოზიდული პრემია, ბრუტო']
    gadazgvevis_aqtivebi_growth = round(gadazgvevis_aqtivebi_growth,2)
#print gadazgvevis_aqtivebi_growth
    sadazgveo_motxovnebi_growth = float(balance_2018['სადაზღვეო მოთხოვნები'])/income_2018['მოზიდული პრემია, ბრუტო']
    sadazgveo_motxovnebi_growth = round(sadazgveo_motxovnebi_growth,2)
#print sadazgveo_motxovnebi_growth
    gadavadebuli_akv_xarjebi = float(balance_2018['გადავადებული აკვიზიციური ხარჯები'])/income_2018['მოზიდული პრემია, ბრუტო']
    gadavadebuli_akv_xarjebi = round(gadavadebuli_akv_xarjebi,2)
#print gadavadebuli_akv_xarjebi
    sxva_aktivebi = float(balance_2018['სხვა აქტივები'])/income_2018['მოზიდული პრემია, ბრუტო']
    sxva_aktivebi=round(sxva_aktivebi,2)
#print sxva_aktivebi

#LIABILITIES
    sadazgveo_premiis_rezervebi_growth = float(balance_2018['სადაზღვეო პრემიის რეზერვები'])/income_2018['მოზიდული პრემია, ბრუტო']
    sadazgveo_premiis_rezervebi_growth = round(sadazgveo_premiis_rezervebi_growth,2)
#print sadazgveo_premiis_rezervebi_growth
    asanazgaurebeli_zaralebi_growth = float(balance_2018['სანაზღაურებელი ზარალებია'])/income_2018['მოზიდული პრემია, ბრუტო']
    asanazgaurebeli_zaralebi_growth = round(asanazgaurebeli_zaralebi_growth,2)
#print asanazgaurebeli_zaralebi_growth
    gadazgvevis_valdebulebebi_growth=float(balance_2018['დაზღვევის და გადაზღვევის ვალდებულებები'])/income_2018['მოზიდული პრემია, ბრუტო']
    gadazgvevis_valdebulebebi_growth=round(gadazgvevis_valdebulebebi_growth,2)
#print gadazgvevis_valdebulebebi_growth
    sainvesticio_valdebulebebi_growth = float(balance_2018['საინვესტიციო ხელშეკრულების ვალდებულებები'])/income_2018['მოზიდული პრემია, ბრუტო']
    sainvesticio_valdebulebebi_growth=round(sainvesticio_valdebulebebi_growth,2)
#print sainvesticio_valdebulebebi_growth
    savachro_valdebulebebi_growth = float(balance_2018['სავაჭრო და სხვა ვალდებულებები'])/income_2018['მოზიდული პრემია, ბრუტო']
    savachro_valdebulebebi_growth=round(savachro_valdebulebebi_growth,2)
#print savachro_valdebulebebi_growth
    gadavadebuli_valdebulebebi_growth = float(balance_2018['გადავადებული საგადასახადო ვალდებულება'])/income_2018['მოზიდული პრემია, ბრუტო']
    gadavadebuli_valdebulebebi_growth=round(gadavadebuli_valdebulebebi_growth,4)
#print gadavadebuli_valdebulebebi_growth



    income_forecast_index = ['მოზიდული პრემია, ბრუტო','გამოკლებული: გადამზღვევლის კუთვნილი პრემია','მოზიდული პრემია, ნეტო','საკომისიო შემოსავალი გადაზღვევიდან',
                         'საინვესტიციო და სხვა შემოსავალი','სულ შემოსავალი','სადაზღვეო ზარალები, ნეტო','სხვა საოპერაციო ხარჯი','საპროცენტო ხარჯი','სულ ხარჯები',
                         'მოგება დაბეგვრამდე','მოგების გადასახადის ხარჯი (tax - 15%)','წლის წმინდა მოგება']
    income_forecast = pd.Series([1],index = ['1'])
    net_income_forecast = pd.DataFrame([1,2],columns=['2019'])

    dict={}
#dict['მოზიდული პრემია']=GPI_premium_list

#income_forecast = pd.Series(data = [],index = income_forecast_index)
    dict['[მოზიდული პრემია]']=ran()
    dict['გადამზღვევლის კუთვნილი პრემია']=-ran()*0.20

    dict['მოზიდული პრემია, ნეტო']=dict['[მოზიდული პრემია]']+dict['გადამზღვევლის კუთვნილი პრემია']
    dict['საკომისიო შემოსავალი გადაზღვევიდან']=dict['[მოზიდული პრემია]']*sakomisio_shemosavali_gadazgvevidan_growth
    dict['საინვესტიციო და სხვა შემოსავალი']=dict['[მოზიდული პრემია]']*sainvesticio_sxva_shemosavali
    dict['სულ შემოსავალი'] = dict['მოზიდული პრემია, ნეტო']+dict['საკომისიო შემოსავალი გადაზღვევიდან']+dict['საინვესტიციო და სხვა შემოსავალი']
    dict['სადაზღვეო ზარალები, ნეტო']=sadazgveo_zaralebi_NETO*dict['[მოზიდული პრემია]']
    dict['სხვა საოპერაციო ხარჯი']=-sxva_saoperacio_xarjebi_growth*dict['[მოზიდული პრემია]']
    dict['საპროცენტო ხარჯი']=saprocento_xarji_growth*dict['მოზიდული პრემია, ნეტო']
    dict['სულ ხარჯები'] = dict['სადაზღვეო ზარალები, ნეტო']+dict['სხვა საოპერაციო ხარჯი']+dict['საპროცენტო ხარჯი']
    dict['მოგება დაბეგვრამდე'] = dict['სულ შემოსავალი']+dict['სულ ხარჯები']
    dict['მოგების გადასახადის ხარჯი (tax - 15%)']=dict['მოგება დაბეგვრამდე']*0.15
    dict['წლის წმინდა მოგება']=dict['მოგება დაბეგვრამდე']-dict['მოგების გადასახადის ხარჯი (tax - 15%)']

    income_forecast = pd.DataFrame(dict,columns=['[მოზიდული პრემია]','გადამზღვევლის კუთვნილი პრემია','მოზიდული პრემია, ნეტო','საკომისიო შემოსავალი გადაზღვევიდან','საინვესტიციო და სხვა შემოსავალი',
                                             'სულ შემოსავალი','სადაზღვეო ზარალები, ნეტო','სხვა საოპერაციო ხარჯი','საპროცენტო ხარჯი','სულ ხარჯები','მოგება დაბეგვრამდე',
                                             'მოგების გადასახადის ხარჯი (tax - 15%)','წლის წმინდა მოგება'])
    #print income_forecast
#print income_forecast
    dict_wc_ass={}
    dict_wc_li={}
    dict_wc_ass['ინვესტიციები შვილობილ კომპანიებში']=dict['[მოზიდული პრემია]']*investiciebi_shvilobil_growth
    dict_wc_ass['საბანკო დეპოზიტები']=dict['[მოზიდული პრემია]']*sabanko_depozitebi_growth
    dict_wc_ass['გაცემული სესხები']=dict['[მოზიდული პრემია]']*gacemuli_sesxebi_growth
    dict_wc_ass['გადაზღვევის აქტივები']=dict['[მოზიდული პრემია]']*gadazgvevis_aqtivebi_growth
    dict_wc_ass['სადაზღვეო მოთხოვნები']=dict['[მოზიდული პრემია]']*sadazgveo_motxovnebi_growth
    dict_wc_ass['გადავადებული აკვიზიციური ხარჯები']=dict['[მოზიდული პრემია]']*gadavadebuli_akv_xarjebi
    dict_wc_ass['სხვა აქტივები']=dict['[მოზიდული პრემია]']*sxva_aktivebi
    dict_wc_ass['ოპერაციული აქტივები']=sum(dict_wc_ass.values())

    balance_forcast_ass = pd.DataFrame(dict_wc_ass,columns=['ინვესტიციები შვილობილ კომპანიებში','საბანკო დეპოზიტები','გაცემული სესხები','გადაზღვევის აქტივები','სადაზღვეო მოთხოვნები',
                                                'გადავადებული აკვიზიციური ხარჯები','სხვა აქტივები','ოპერაციული აქტივები'])

#print balance_forcast_ass
    dict_wc_li['სადაზღვეო პრემიის რეზერვები']=dict['[მოზიდული პრემია]']*sadazgveo_premiis_rezervebi_growth-0.1

    dict_wc_li['სანაზღაურებელი ზარალებია']=dict['[მოზიდული პრემია]']*asanazgaurebeli_zaralebi_growth-0.08
    dict_wc_li['დაზღვევის და გადაზღვევის ვალდებულებები']=dict['[მოზიდული პრემია]']*gadazgvevis_valdebulebebi_growth
    dict_wc_li['საინვესტიციო ხელშეკრულების ვალდებულებები']=dict['[მოზიდული პრემია]']*sainvesticio_valdebulebebi_growth
    dict_wc_li['სავაჭრო და სხვა ვალდებულებები']=dict['[მოზიდული პრემია]']*savachro_valdebulebebi_growth
    dict_wc_li['გადავადებული საგადასახადო ვალდებულება']=dict['[მოზიდული პრემია]']*gadavadebuli_valdebulebebi_growth
    dict_wc_li['ოპერაციული ვალდებულებები']=sum(dict_wc_li.values())
    balance_forcast_li = pd.DataFrame(dict_wc_li,columns=['სადაზღვეო პრემიის რეზერვები','სანაზღაურებელი ზარალებია','დაზღვევის და გადაზღვევის ვალდებულებები','საინვესტიციო ხელშეკრულების ვალდებულებები',
                                                      'სავაჭრო და სხვა ვალდებულებები','გადავადებული საგადასახადო ვალდებულება','ოპერაციული ვალდებულებები'])
#print dict_wc_ass['ოპერაციული აქტივები']-dict_wc_li['ოპერაციული ვალდებულებები']
    dict_wc={}
    dict_wc['წმინდა სამუშაო კაპიტალის']=dict_wc_ass['ოპერაციული აქტივები']-dict_wc_li['ოპერაციული ვალდებულებები']
#print dict_wc
    wc_list=[]
    wc=38
    for i in dict_wc['წმინდა სამუშაო კაპიტალის']:

        wc_change=i-wc
        wc_list.append(wc_change)
        wc = i
#print wc_list
    dict_wc['წმინდა სამუშაო კაპიტალის ცვლილება']=wc_list
    wc_change_dict=pd.Series(wc_list,index=years_projected)
    dep_dict={}
    dep_dict['ძირითადი საშუალებები']=dict['[მოზიდული პრემია]']*dziritadi_sashualebebi_growth
    dep_dict['ცვეთა და ამორტიზაცია']=dep_dict['ძირითადი საშუალებები']*depretiation_growth

    dep_list=[]
    for i in dep_dict['ცვეთა და ამორტიზაცია']:
    #print i
        dep_list.append(i)
#print dep_dict['ცვეთა და ამორტიზაცია']
#print dep_list
    dep=pd.Series(dep_list,index=years_projected)

#print dep_dict['ძირითადი საშუალებები']
    dziritadi = 4
    capex_list = []
    for i in dep_dict['ძირითადი საშუალებები']:


        capex=i-dziritadi
        capex_list.append(capex)
        dziritadi=i


    capex_s=pd.Series(capex_list,index=years_projected)

    fcff_data = pd.DataFrame({'წმინდა სამუშაო კაპიტალის ცვლილება':wc_change_dict,'ცვეთა და ამორტიზაცია':dep,'CAPEX':capex_s,'წლის წმინდა მოგება':dict['წლის წმინდა მოგება']},columns=['წმინდა სამუშაო კაპიტალის ცვლილება','ცვეთა და ამორტიზაცია','CAPEX','წლის წმინდა მოგება'])
    return fcff_data
#print fcfefunction()

#k=0
#while k<10:
#    print fcfefunction()
#    k=k+1