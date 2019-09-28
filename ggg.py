# -*- coding: utf-8 -*-
from statments import cash_flow_2017, cash_flow_2018
from statments import balance_2017,   balance_2018
from statments import income_2017, income_2018
from data import GPI_premium_series, GPI_premium_list,GPI_reinsurance,years_projected
import numpy as np
import pandas as pd
desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',15)
growth_dict={}