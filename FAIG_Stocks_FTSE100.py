#IF YOU FOUND THIS USEFUL, Please Donate some Bitcoin .... 1FWt366i5PdrxCC6ydyhD8iywUHQ2C7BWC

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import datetime
import requests
import json
import logging
import sys
import urllib
from time import time, sleep
import random
import time as systime
from statistics import mean, median
import numpy as np
# We are gonna use Scikit's LinearRegression model
from sklearn.linear_model import LinearRegression
import quandl
import math
import sys, os

predict_accuracy = 0.91
price_compare = "bid"

# FORMAT EXAMPLE
# epic_id = "KA.D.LLOY.DAILY.IP"
# epic_id = "KA.D.BARC.DAILY.IP"
# QUAND_REF = "LSE/LLOY"
# QUAND_REF = "LSE/BARC"

quandl.ApiConfig.api_key = "***********************"
#MORE INFORMATION HERE:
#http://help.quandl.com/article/320-where-can-i-find-my-api-key

########################################################################################################################
#REAL_OR_NO_REAL = 'https://demo-api.ig.com/gateway/deal'
#API_ENDPOINT = "https://demo-api.ig.com/gateway/deal/session"
#API_KEY = '**********************' 
##API_KEY = '*****************************'
#data = {"identifier":"******************","password": "*******************"}
########################################################################################################################
########################################################################################################################
########################################################################################################################
# FOR REAL....
########################################################################################################################
########################################################################################################################
########################################################################################################################
REAL_OR_NO_REAL = 'https://api.ig.com/gateway/deal'
API_ENDPOINT = "https://api.ig.com/gateway/deal/session"
API_KEY = '************************'
data = {"identifier":"*********************","password": "*********************"}

headers = {'Content-Type':'application/json; charset=utf-8',
        'Accept':'application/json; charset=utf-8',
        'X-IG-API-KEY':API_KEY,
        'Version':'2'
        }

r = requests.post(API_ENDPOINT, data=json.dumps(data), headers=headers)
 
headers_json = dict(r.headers)
CST_token = headers_json["CST"]
print (R"CST : " + CST_token)
x_sec_token = headers_json["X-SECURITY-TOKEN"]
print (R"X-SECURITY-TOKEN : " + x_sec_token)

#GET ACCOUNTS
base_url = REAL_OR_NO_REAL + '/accounts'
authenticated_headers = {'Content-Type':'application/json; charset=utf-8',
        'Accept':'application/json; charset=utf-8',
        'X-IG-API-KEY':API_KEY,
        'CST':CST_token,
        'X-SECURITY-TOKEN':x_sec_token}

auth_r = requests.get(base_url, headers=authenticated_headers)
d = json.loads(auth_r.text)

# print(auth_r.status_code)
# print(auth_r.reason)
# print (auth_r.text)

for i in d['accounts']:
    if str(i['accountType']) == "SPREADBET":
        print ("Spreadbet Account ID is : " + str(i['accountId']))
        spreadbet_acc_id = str(i['accountId'])

#SET SPREAD BET ACCOUNT AS DEFAULT
base_url = REAL_OR_NO_REAL + '/session'
data = {"accountId":spreadbet_acc_id,"defaultAccount": "True"}
auth_r = requests.put(base_url, data=json.dumps(data), headers=authenticated_headers)

# print(auth_r.status_code)
# print(auth_r.reason)
# print (auth_r.text)
#ERROR about account ID been the same, Ignore! 

###################################################################################
##########################END OF LOGIN CODE########################################
##########################END OF LOGIN CODE########################################
##########################END OF LOGIN CODE########################################
##########################END OF LOGIN CODE########################################
###################################################################################

#UNIT TEST FOR OTHER STUFF
limitDistance_value = "4" #Initial Limit (Take Profit), Worked out later per trade
orderType_value = "MARKET"
size_value = "3"
expiry_value = "DFB"
guaranteedStop_value = True
currencyCode_value = "GBP"
forceOpen_value = True
stopDistance_value = "20" #Initial Stop loss, Worked out later per trade

epic_ids = ['KA.D.AAL.DAILY.IP', 'KA.D.ABF.DAILY.IP', 'KA.D.ADMLN.DAILY.IP', 'AB.D.LNKAU.DAILY.IP', 'KA.D.AGK.DAILY.IP', 'KA.D.ANTO.DAILY.IP', 'KA.D.ARM.DAILY.IP', 'KC.D.KAYLN.DAILY.IP', 'KA.D.ASHM.DAILY.IP', 'KA.D.AGOLLN.DAILY.IP', 'KA.D.AGOULN.DAILY.IP', 'KA.D.AV.DAILY.IP', 'KA.D.AZN.DAILY.IP', 'KA.D.BA.DAILY.IP', 'KA.D.RBS.DAILY.IP', 'KA.D.LLOY.DAILY.IP', 'KA.D.BAY.DAILY.IP', 'KA.D.BAG.DAILY.IP', 'KA.D.BARC.DAILY.IP', 'KA.D.ZHYGLN.DAILY.IP', 'KA.D.GLTLLN.DAILY.IP', 'KA.D.TRSYLN.DAILY.IP', 'KA.D.USTYLN.DAILY.IP', 'KA.D.UBTPLN.DAILY.IP', 'KA.D.SBEGLN.DAILY.IP', 'KA.D.BATS.DAILY.IP', 'KA.D.BGEO.DAILY.IP', 'KA.D.BLND.DAILY.IP', 'KA.D.BLT.DAILY.IP', 'KA.D.BNZL.DAILY.IP', 'KA.D.BP.DAILY.IP', 'KA.D.XX300021E.DAILY.IP', 'KA.D.BRBY.DAILY.IP', 'KA.D.BSY.DAILY.IP', 'KA.D.BLZ.DAILY.IP', 'KA.D.BA.DAILY.IP', 'KA.D.BT.DAILY.IP', 'KA.D.BGC.DAILY.IP', 'KA.D.CCLLN.DAILY.IP', 'KA.D.CNA.DAILY.IP', 'KA.D.CPG.DAILY.IP', 'KA.D.CPI.DAILY.IP', 'KA.D.CRDA.DAILY.IP', 'KA.D.CRHLN.DAILY.IP', 'KA.D.DGE.DAILY.IP', 'KA.D.EMG.DAILY.IP', 'KA.D.EVRLN.DAILY.IP', 'KA.D.EXPN.DAILY.IP', 'KA.D.FRES.DAILY.IP', 'KA.D.GFS.DAILY.IP', 'KA.D.GKN.DAILY.IP', 'KA.D.GLEN.DAILY.IP', 'KA.D.GLVLN.DAILY.IP', 'KA.D.GSK.DAILY.IP', 'KA.D.HL.DAILY.IP', 'KA.D.XLVSLN.DAILY.IP', 'KA.D.HMSO.DAILY.IP', 'KA.D.HSBA.DAILY.IP', 'KA.D.BAY.DAILY.IP', 'KA.D.IAP.DAILY.IP', 'KA.D.IHG.DAILY.IP', 'KA.D.IMI.DAILY.IP', 'KA.D.SJPALN.DAILY.IP', 'KA.D.IJPALN.DAILY.IP', 'KA.D.EMIMLN.DAILY.IP', 'KA.D.UKSRLN.DAILY.IP', 'KA.D.EIMILN.DAILY.IP', 'KA.D.IMT.DAILY.IP', 'KA.D.IPRVLN.DAILY.IP', 'KA.D.IPRPLN.DAILY.IP', 'KA.D.ITRK.DAILY.IP', 'KA.D.ITV.DAILY.IP', 'KA.D.JMAT.DAILY.IP', 'KA.D.KAZ.DAILY.IP', 'KA.D.KGF.DAILY.IP', 'KA.D.LAND.DAILY.IP', 'KA.D.BLND.DAILY.IP', 'KA.D.LGEN.DAILY.IP', 'KA.D.LLOY.DAILY.IP', 'KA.D.JLT.DAILY.IP', 'KA.D.MGGT.DAILY.IP', 'KA.D.MKS.DAILY.IP', 'KA.D.MRW.DAILY.IP', 'KA.D.NGT.DAILY.IP', 'KA.D.NXT.DAILY.IP', 'KA.D.OML.DAILY.IP', 'KA.D.PFC.DAILY.IP', 'KA.D.POLY.DAILY.IP', 'KA.D.PLPLN.DAILY.IP', 'KA.D.BPI.DAILY.IP', 'KA.D.PRU.DAILY.IP', 'KA.D.PSON.DAILY.IP', 'KA.D.RB.DAILY.IP', 'KA.D.RBS.DAILY.IP', 'KA.D.RDSB.DAILY.IP', 'KA.D.REL.DAILY.IP', 'KA.D.REX.DAILY.IP', 'KA.D.RIO.DAILY.IP', 'KA.D.RR.DAILY.IP', 'KA.D.RRS.DAILY.IP', 'KA.D.RSA.DAILY.IP', 'KA.D.AV.DAILY.IP', 'KA.D.SAB.DAILY.IP', 'KA.D.SBRY.DAILY.IP', 'KA.D.SDR.DAILY.IP', 'KA.D.SDRC.DAILY.IP', 'KA.D.SGE.DAILY.IP', 'KA.D.SGEALN.DAILY.IP', 'KA.D.SHP.DAILY.IP', 'KA.D.SLLN.DAILY.IP', 'KA.D.SLET.DAILY.IP', 'KA.D.SMIN.DAILY.IP', 'KA.D.SN.DAILY.IP', 'KA.D.SNLDLN.DAILY.IP', 'KA.D.SRP.DAILY.IP', 'KA.D.SSE.DAILY.IP', 'KA.D.STAN.DAILY.IP', 'KA.D.CAY.DAILY.IP', 'KA.D.SVT.DAILY.IP', 'KA.D.TATE.DAILY.IP', 'KA.D.TLW.DAILY.IP', 'KA.D.TSCO.DAILY.IP', 'KA.D.ULVR.DAILY.IP', 'KA.D.UU.DAILY.IP', 'KA.D.VED.DAILY.IP', 'KA.D.VOD.DAILY.IP', 'KA.D.WEIR.DAILY.IP', 'KA.D.SMWH.DAILY.IP', 'KA.D.WPP.DAILY.IP', 'KA.D.WTB.DAILY.IP', 'KA.D.XAR.DAILY.IP']

symbols = ['AAL', 'ABF', 'ADM', 'ADN', 'AGK', 'AMEC', 'ANTO', 'ARM', 'ASHM', 'AV', 'AZN', 'BA', 'BARC', 'BATS', 'BG', 'BLND', 'BLT', 'BNZL', 'BP', 'BRBY', 'BSY', 'BT-A', 'CCL', 'CNA', 'CPG', 'CPI', 'CRDA', 'CRH', 'CSCG', 'DGE', 'EMG', 'ENRC', 'EVR', 'EXPN', 'FRES', 'GFS', 'GKN', 'GLEN', 'GSK', 'HL', 'HMSO', 'HSBA', 'IAG', 'IAP', 'IHG', 'IMI', 'IMT', 'IPR', 'ITRK', 'ITV', 'JMAT', 'KAZ', 'KGF', 'LAND', 'LGEN', 'LLOY', 'MGGT', 'MKS', 'MRW', 'NG', 'NXT', 'OML', 'PFC', 'POLY', 'PRU', 'PSON', 'RB', 'RBS', 'RDSB', 'REL', 'REX', 'RIO', 'RR', 'RRS', 'RSA', 'RSL', 'SAB', 'SBRY', 'SDR', 'SDRC', 'SGE', 'SHP', 'SL', 'SMIN', 'SN', 'SRP', 'SSE', 'STAN', 'SVT', 'TATE', 'TLW', 'TSCO', 'ULVR', 'UU', 'VED', 'VOD', 'WEIR', 'WOS', 'WPP', 'WTB', 'XTA']


#*******************************************************************
#*******************************************************************
#*******************************************************************
#*******************************************************************

TIME_WAIT_MULTIPLIER = 60
#STOP_LOSS_MULTIPLIER = 4 #Not currently in use, 13th Jan
predict_accuracy = 0.89
profitable_trade_count = 0
previous_traded_epic_id = "None"
Tight_Spread = False

print ("START TIME : " + str(datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")))

def humanize_time(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    return '%02d:%02d:%02d' % (hours, mins, secs)   
    
for times_round_loop in range(1, 9999):

#*******************************************************************
#*******************************************************************
#*******************************************************************
#*******************************************************************
    DO_A_THING = False
    Price_Change_OK = False
    Tight_Spread = False
    Start_loop_time = time()
    price_compare = "bid"
    Price_Change_Day_percent = 0
    low_price_list = []
    high_price_list = []
    close_price_list = []
    volume_list = []
    # Your input data, X and Y are lists (or Numpy Arrays)
    #THIS IS YOUR TRAINING DATA
    x = [] #This is Low Price, Volume
    y = [] #This is High Price
    
 
    while not Price_Change_OK:
        random.shuffle(symbols)
        symbol = random.choice(symbols)
        QUAND_REF = "LSE/" + str(symbol)
        print (QUAND_REF)
        epic_id = "KA.D." + str(symbol) + ".DAILY.IP"
        print (epic_id)
        if epic_id not in epic_ids:
            Price_Change_OK = False
            print ("!!DEBUG!! : Is this even a valid IG Epic??")
            continue
       
        
        print ("-----------------------------------------")
        print("!!DEBUG : Random epic_id is : " + str(epic_id))
        base_url = REAL_OR_NO_REAL + '/markets/' + epic_id
        auth_r = requests.get(base_url, headers=authenticated_headers)
        d = json.loads(auth_r.text)
        systime.sleep(2)

        # print ("-----------------DEBUG-----------------")
        # print(auth_r.status_code)
        # print(auth_r.reason)
        # print (auth_r.text)
        # print ("-----------------DEBUG-----------------")

        MARKET_ID = d['instrument']['marketId']
        current_price = d['snapshot']['bid']
        Price_Change_Day = d['snapshot']['netChange']
        Price_Change_Day_percent = float(d['snapshot']['percentageChange'])

        print ("Price Change Percentage on day is " + str(Price_Change_Day_percent))
        bid_price = d['snapshot']['bid']
        ask_price = d['snapshot']['offer']
        #PUT SOME DEBUGGING HERE IF IT FAILS
        spread = float(bid_price) - float(ask_price)
        print ("spread : " + str(spread))
        ##################################################################################################################
        ##################################################################################################################
        #e.g Spread is -30, That is too big, In-fact way too big. Spread is -1.7, This is not too bad, We can trade on this reasonably well.
        #Spread is 0.8. This is considered a tight spread
        ##################################################################################################################
        ##################################################################################################################
        #if spread is less than -2, It's too big
        if float(spread) < -2:
         print ("!!DEBUG!! :- SPREAD NOT OK")
         Price_Change_OK = False
         systime.sleep(2)
        elif float(spread) > -2:
         Price_Change_OK = True


    while not DO_A_THING:
        print ("!!Internal Notes only - Top of Loop!! : " + str(datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")))

        #data = quandl.get("LSE/UK3L", collapse="monthly", returns="numpy") #Good, But we do our own thing with these arrays
        #data = quandl.get("LSE/UK3L", collapse="daily") #TOO MANY NaN's returned!!
        #data = quandl.get("LSE/BARC", collapse="daily", start_date="2013-12-05", end_date="2017-12-08") #Automate this
        data = quandl.get(QUAND_REF, collapse="daily")
        tmp_price_list = data['Low'].values.tolist()
        tmp_volume_list = data['Volume'].values.tolist()
        high_prices = data['High'].values.tolist()
        main_list = []
        ##############################################################
        ##############################################################
        ##############################################################
        #TWO LISTS FOR PREDICTIONS
        ##############################################################
        ##############################################################
        ##############################################################
        #main_list is made up of low prices and volumes
        #high_prices = is made up of high prices
        #print (main_list)
        ##############################################################
        ##############################################################
        ##############################################################

        for i in range(len(tmp_price_list)):
            tmp_list = []
            tmp_var_1 = tmp_price_list[i]
            tmp_var_2 = tmp_volume_list[i]
            if math.isnan(tmp_var_1):
                tmp_var_1 = 0
            if math.isnan(tmp_var_2):
                tmp_var_2 = 0
            tmp_list.append(float(tmp_var_1))
            tmp_list.append(float(tmp_var_2))
            main_list.append(tmp_list)

        for i in range(len(high_prices)):
            if math.isnan(high_prices[i]):
                high_prices[i] = 0

        main_list = np.asarray(main_list)
        high_prices = np.asarray(high_prices)

        PREDICT_FOR = quandl.get(QUAND_REF, collapse="daily")
        PREDICT_FOR_price_list = data['Low'].values.tolist()
        PREDICT_FOR_volume_list = data['Volume'].values.tolist()
        PREDICT_x = PREDICT_FOR_price_list[-1]
        PREDICT_y = PREDICT_FOR_volume_list[-1]

        print ("PREDICT_x : " + str(PREDICT_x))
        print ("PREDICT_y : " + str(PREDICT_y))

        # Initialize the model then train it on the data
        genius_regression_model = LinearRegression()
        genius_regression_model.fit(main_list,high_prices)
        # Predict the corresponding value of Y for X
        pred_ict = [PREDICT_x,PREDICT_y]
        pred_ict = np.asarray(pred_ict) #To Numpy Array, hacky but good!! 
        pred_ict = pred_ict.reshape(1, -1)
        price_prediction = genius_regression_model.predict(pred_ict)
        print ("PRICE PREDICTION FOR " + str(QUAND_REF) + str(price_prediction))

        score = genius_regression_model.score(main_list,high_prices)
        predictions = {'intercept': genius_regression_model.intercept_, 'coefficient': genius_regression_model.coef_,   'predicted_value': price_prediction, 'accuracy' : score}
        print ("-----------------DEBUG-----------------")
        print (score)
        print (predictions)
        print ("-----------------DEBUG-----------------")
     
        ##############################################################
        ##############################################################
        ###################QUANDL ENDS################################
        #################IGINDEX STUFF################################
        ##############################################################
        ##############################################################
        ##############################################################
        ##############################################################
        ##############################################################

        base_url = REAL_OR_NO_REAL + '/markets/' + epic_id
        auth_r = requests.get(base_url, headers=authenticated_headers)
        d = json.loads(auth_r.text)
        # print ("-----------------DEBUG-----------------")
        # print(auth_r.status_code)
        # print(auth_r.reason)
        # print (auth_r.text)
        # print ("-----------------DEBUG-----------------")
        current_price = d['snapshot']['bid']
        price_diff = current_price - price_prediction
        print ("Price Difference Away (Point's) : " + str(price_diff))
        ##############################################################
        ##############################################################
        ##############################################################
        #MUST NOTE :- IF THIS PRICE IS - THEN BUY!! IF THIS PRICE IS POSITIVE IT IS ALREADY ABOVE SO SELL!!!
        ##############################################################
        ##############################################################
        ##############################################################

        base_url = REAL_OR_NO_REAL + '/prices/'+ epic_id + '/HOUR/30'
        # Price resolution (MINUTE, MINUTE_2, MINUTE_3, MINUTE_5, MINUTE_10, MINUTE_15, MINUTE_30, HOUR, HOUR_2, HOUR_3, HOUR_4, DAY, WEEK, MONTH)
        auth_r = requests.get(base_url, headers=authenticated_headers)
        d = json.loads(auth_r.text)
        
        # print ("-----------------DEBUG-----------------")
        # print(auth_r.status_code)
        # print(auth_r.reason)
        # print (auth_r.text)
        # print ("-----------------DEBUG-----------------")
        
        for i in d['prices']:
            tmp_list = []
            high_price = i['highPrice'][price_compare]
            low_price = i['lowPrice'][price_compare]
            volume = i['lastTradedVolume']
            #---------------------------------
            tmp_list.append(float(low_price))
            tmp_list.append(float(volume))
            x.append(tmp_list)
            #x is Low Price and Volume
            y.append(float(high_price))
            #y = High Prices
        
        #Cut down on API Calls by using this again! 
        
        price_ranges = []
        closing_prices = []
        first_time_round_loop = True
        TR_prices = []


        for i in d['prices']:
            if first_time_round_loop == True:
                #First time round loop cannot get previous
                closePrice = i['closePrice'][price_compare]
                closing_prices.append(closePrice)
                high_price = i['highPrice'][price_compare]
                low_price = i['lowPrice'][price_compare]
                price_range = float(high_price - closePrice)
                price_ranges.append(price_range)
                first_time_round_loop = False
            else:
                prev_close = closing_prices[-1]
                ###############################
                closePrice = i['closePrice'][price_compare]
                closing_prices.append(closePrice)
                high_price = i['highPrice'][price_compare]
                low_price = i['lowPrice'][price_compare]
                price_range = float(high_price - closePrice)
                price_ranges.append(price_range)
                TR = max(high_price-low_price, abs(high_price-prev_close), abs(low_price-prev_close))
                #print (TR)
                TR_prices.append(TR)
                
             
        max_range = max(TR_prices)
        low_range = min(TR_prices)
        print ("stopDistance_value for " + str(epic_id) + " will bet set at " + str(int(max_range)))
        print ("limitDistance_value for " + str(epic_id) + " will bet set at " + str(int(low_range)))
        if low_range > 10:
            print ("!!DEBUG!! WARNING - Take Profit over high value, Might take a while for this trade!!")
            
     
        base_url = REAL_OR_NO_REAL + '/prices/'+ epic_id + '/DAY/1'
        # Price resolution (MINUTE, MINUTE_2, MINUTE_3, MINUTE_5, MINUTE_10, MINUTE_15, MINUTE_30, HOUR, HOUR_2, HOUR_3, HOUR_4, DAY, WEEK, MONTH)
        auth_r = requests.get(base_url, headers=authenticated_headers)
        d = json.loads(auth_r.text)
        
        #I only need this API call for real world values
        remaining_allowance = d['allowance']['remainingAllowance']
        reset_time = humanize_time(int(d['allowance']['allowanceExpiry']))
        total_allowance = humanize_time(int(d['allowance']['totalAllowance']))
                
        print ("-----------------DEBUG-----------------")
        print ("Remaining API Calls left : " + str(remaining_allowance))
        print ("Time to API Key reset : " + str(reset_time))
        print ("-----------------DEBUG-----------------")
   
        # print ("-----------------DEBUG-----------------")
        # print(auth_r.status_code)
        # print(auth_r.reason)
        # print (auth_r.text)
        # print ("-----------------DEBUG-----------------")

        for i in d['prices']:
            low_price = i['lowPrice'][price_compare]
            volume = i['lastTradedVolume']

        #####################################################################
        #########################PREDICTION CODE#############################
        #########################PREDICTION CODE#############################
        #########################PREDICTION CODE#############################
        #########################PREDICTION CODE#############################
        #########################PREDICTION CODE#############################
        #####################################################################
        
        x = np.asarray(x)
        y = np.asarray(y)
        # Initialize the model then train it on the data
        genius_regression_model = LinearRegression()
        genius_regression_model.fit(x,y)
        # Predict the corresponding value of Y for X
        pred_ict = [low_price,volume]
        pred_ict = np.asarray(pred_ict) #To Numpy Array, hacky but good!! 
        pred_ict = pred_ict.reshape(1, -1)
        price_prediction = genius_regression_model.predict(pred_ict)
        print ("PRICE PREDICTION FOR PRICE " + epic_id + " IS : " + str(price_prediction))


        score = genius_regression_model.score(x,y)
        predictions = {'intercept': genius_regression_model.intercept_, 'coefficient': genius_regression_model.coef_,   'predicted_value': price_prediction, 'accuracy' : score}
        print ("-----------------DEBUG-----------------")
        print (score)
        print (predictions)
        print ("-----------------DEBUG-----------------")
            
        price_diff = current_price - price_prediction
        limitDistance_value = int(low_range)
        #Fixing a weird bug, Where the prediction is 0. 
        #Fixing a weird bug, Where the prediction is 0.
        if int(limitDistance_value) == 0:
            limitDistance_value = "2"
            
        stopDistance_value = int(max_range) 
        #NOTE Sometimes IG Index want a massive stop loss for Guaranteed, Either don't use Guaranteed or "sell at market" with Artificial Stop loss
        #MUST NOTE :- IF THIS PRICE IS - i.e NOT HIT TARGET YET, CONVERSELY IF THIS PRICE IS POSITIVE IT IS ALREADY ABOVE PREDICTION!!!
        
        print ("TRUE GUARANTEED STOP LOSS DISTANCE WILL BE SET AT : " + str(stopDistance_value))
        print ("Price Difference Away (Point's) : " + str(price_diff))
                   
        ################################################################
        #########################ORDER CODE#############################
        #########################ORDER CODE#############################
        #########################ORDER CODE#############################
        #########################ORDER CODE#############################
        ################################################################
        
        ################################################################
        #############Predict Accuracy isn't that great. ################
        #############Predict Accuracy isn't that great. ################
        #############Predict Accuracy isn't that great. ################
        #############Predict Accuracy isn't that great. ################
        ################################################################
        Prediction_Wait_Timer = int(TIME_WAIT_MULTIPLIER) #Wait
        
        if float(current_price) > price_prediction:
            print ("!!DEBUG!! Current Price is OVER prediction")
            #limitDistance_value = "2"
        elif float(current_price) < price_prediction:
            print ("!!DEBUG!! Current Price is UNDER prediction")

        if float(score) < float(predict_accuracy):
            print ("!!DEBUG!! : " + str(datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")))
            DO_A_THING = False
            print ("!!DEBUG!! Prediction Wait Algo: " + str(datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")))
            systime.sleep(Prediction_Wait_Timer)
            print ("!!DEBUG!! Prediction Wait Algo: " + str(datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")))
            break
            
        sufficient_distance = limitDistance_value * -1
        #Otherwise here might have to change limitDistance_value to minus!!
        
        #Three things, Price difference is less than target, Accuracy is OK, Current Price is less than Price Prediction
        if price_diff < 0 and score > predict_accuracy and float(current_price) < float(price_prediction):
             DIRECTION_TO_TRADE = "BUY"
             DIRECTION_TO_CLOSE = "SELL"
             DIRECTION_TO_COMPARE = 'bid'
             DO_A_THING = True
        elif float(price_diff) > float(limitDistance_value) and score > predict_accuracy and float(current_price) > float(price_prediction):
            #!!!!Above Predicted Target!!!!
            #Tight limit (Take Profit)
            limitDistance_value = "2"
            DIRECTION_TO_TRADE = "SELL"
            DIRECTION_TO_CLOSE = "BUY"
            DIRECTION_TO_COMPARE = 'offer'
            DO_A_THING = True
        else:
            DO_A_THING = False
            print ("!!DEBUG!! NO CRITERIA!!: " + str(datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")))
            systime.sleep(Prediction_Wait_Timer)
            print ("!!DEBUG!! NO CRITERIA!! " + str(datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")))
            break
        

    if not DO_A_THING:
        #DO_A_THING NOT SET FOR WHATEVER REASON, GO BACK TO MAIN PROGRAM LOOP
        print ("-----------------DEBUG-----------------")
        print ("!!DEBUG!! AN ERROR OCCURED")
        print ("!!DEBUG!! Reminder, Check what the f*** is going on here")
        print ("!!DEBUG!! Most likely DO_A_THING Not Set!!")
        print ("-----------------DEBUG-----------------")
        continue
    
    #Hacky af due to low value produced. 
    #Hacky af due to low value produced. 
    #Hacky af due to low value produced. 
    stopDistance_value = "20"
    #Hacky af due to low value produced. 
    #Hacky af due to low value produced. 
    #Hacky af due to low value produced. 
    
    base_url = REAL_OR_NO_REAL + '/positions/otc'
    authenticated_headers = {'Content-Type':'application/json; charset=utf-8',
            'Accept':'application/json; charset=utf-8',
            'X-IG-API-KEY':API_KEY,
            'CST':CST_token,
            'X-SECURITY-TOKEN':x_sec_token}
            
    data = {"direction":DIRECTION_TO_TRADE,"epic": epic_id, "limitDistance":limitDistance_value, "orderType":orderType_value, "size":size_value,"expiry":expiry_value,"guaranteedStop":guaranteedStop_value,"currencyCode":currencyCode_value,"forceOpen":forceOpen_value,"stopDistance":stopDistance_value}
    r = requests.post(base_url, data=json.dumps(data), headers=authenticated_headers)
    
    print ("-----------------DEBUG-----------------")
    print(r.status_code)
    print(r.reason)
    print (r.text)
    print ("-----------------DEBUG-----------------")

    d = json.loads(r.text)
    deal_ref = d['dealReference']
    systime.sleep(2)
    # MAKE AN ORDER
    
    #CONFIRM MARKET ORDER
    base_url = REAL_OR_NO_REAL + '/confirms/'+ deal_ref
    auth_r = requests.get(base_url, headers=authenticated_headers)
    d = json.loads(auth_r.text)
    DEAL_ID = d['dealId']
    print("DEAL ID : " + str(d['dealId']))
    print(d['dealStatus'])
    print(d['reason'])
    
    #######################################################################################
    #This gets triggered if IG want a daft amount in your account for the margin, More than you specified initially. This happens sometimes... deal with it! 
    #This is fine, Whilst it is a bit hacky basically start over again.
    #######################################################################################
    if str(d['reason']) == "ATTACHED_ORDER_LEVEL_ERROR" or str(d['reason']) == "MINIMUM_ORDER_SIZE_ERROR" or str(d['reason']) == "INSUFFICIENT_FUNDS" or str(d['reason']) == "MARKET_OFFLINE" or str(d['reason']) == "MARKET_CLOSED_WITH_EDITS":
        print ("!!DEBUG!! Something went wrong, is the market even open? Have you got enough cash etc, Try again!!")
        continue
        
    previous_traded_epic_id = epic_id    
    # the trade will only break even once the price of the asset being traded has surpassed the sell price (for long trades) or buy price (for short trades). 
    ##########################################
    ##########READ IN INITIAL PROFIT##########
    ##########################################
        
    base_url = REAL_OR_NO_REAL + '/positions/'+ DEAL_ID
    auth_r = requests.get(base_url, headers=authenticated_headers)      
    d = json.loads(auth_r.text)
        
    print ("-----------------DEBUG-----------------")
    print(r.status_code)
    print(r.reason)
    print (r.text)
    print ("-----------------DEBUG-----------------")
    
    ##########################################
    ##########READ IN INITIAL PROFIT##########
    ##########################################
    
    if DIRECTION_TO_TRADE == "SELL":
        PROFIT_OR_LOSS = float(d['position']['openLevel']) - float(d['market'][DIRECTION_TO_COMPARE])
        PROFIT_OR_LOSS = PROFIT_OR_LOSS * float(size_value)
        print ("Deal Number : " + str(times_round_loop) + " Profit/Loss : " + str(PROFIT_OR_LOSS))
    else:
        PROFIT_OR_LOSS = float(d['market'][DIRECTION_TO_COMPARE] - float(d['position']['openLevel']))
        PROFIT_OR_LOSS = PROFIT_OR_LOSS * float(size_value)
        print ("Deal Number : " + str(times_round_loop) + " Profit/Loss : " + str(PROFIT_OR_LOSS))
     
    ##########################################
    ##########READ IN INITIAL PROFIT##########
    ##########################################
    
    ##########################################
    #####KEEP READING IN FOR PROFIT###########
    ##########################################
    try:
        #while PROFIT_OR_LOSS < float(limitDistance_value): 
        while PROFIT_OR_LOSS < float(limitDistance_value * int(size_value)) - 1: #Take something from the market, Before Take Profit.
            elapsed_time = round((time() - Start_loop_time), 1) 
            print ("******************************")
            print ("Order Time : " + str(humanize_time(elapsed_time)))
      
            base_url = REAL_OR_NO_REAL + '/positions/'+ DEAL_ID
            auth_r = requests.get(base_url, headers=authenticated_headers)      
            d = json.loads(auth_r.text)
            
            while not int(auth_r.status_code) == 200:
                if int(auth_r.status_code) == 400 or int(auth_r.status_code) == 404:
                    break
                    #This is a good thing!! It means that It cannot find the Deal ID, Your take profit has been hit. 
                    
                #Cannot read from API, Wait and try again
                #Give the Internet/IG 30s to sort it's shit out and try again
                systime.sleep(random.randint(1, TIME_WAIT_MULTIPLIER))
                print ("-----------------DEBUG-----------------")
                print ("HTTP API ERROR!! Please check your Internet connection and Try again...")
                print ("Check Ping and Latency between you and IG Index Servers")
                # print(auth_r.status_code)
                # print(auth_r.reason)
                # print (auth_r.text)
                print ("-----------------DEBUG-----------------")
                #Got some "basic" error checking after all
                base_url = REAL_OR_NO_REAL + '/positions/'+ DEAL_ID
                auth_r = requests.get(base_url, headers=authenticated_headers)      
                d = json.loads(auth_r.text)
            
            if DIRECTION_TO_TRADE == "SELL":
                PROFIT_OR_LOSS = float(d['position']['openLevel']) - float(d['market'][DIRECTION_TO_COMPARE])
                PROFIT_OR_LOSS = float(d['position']['openLevel']) - float(d['market'][DIRECTION_TO_COMPARE])
                PROFIT_OR_LOSS = float(PROFIT_OR_LOSS * float(size_value))
                print ("Deal Number : " + str(times_round_loop) + " Profit/Loss : " + str(PROFIT_OR_LOSS))
                systime.sleep(2) #Don't be too keen to read price
            else:
                PROFIT_OR_LOSS = float(d['market'][DIRECTION_TO_COMPARE] - float(d['position']['openLevel']))
                PROFIT_OR_LOSS = float(PROFIT_OR_LOSS * float(size_value))
                print ("Deal Number : " + str(times_round_loop) + " Profit/Loss : " + str(PROFIT_OR_LOSS))
                systime.sleep(2) #Don't be too keen to read price
                
            ARTIFICIAL_STOP_LOSS = int(max_range) * int(size_value)
            if ARTIFICIAL_STOP_LOSS > 100:
                print ("!!!!WARNING!!!! STOP LOSS MIGHT BE TOO HIGH :- Current Value is " + str(ARTIFICIAL_STOP_LOSS))
            ARTIFICIAL_STOP_LOSS = ARTIFICIAL_STOP_LOSS * -1 #Make Negative, DO NOT REMOVE!!
               
            if PROFIT_OR_LOSS < ARTIFICIAL_STOP_LOSS:
                #CLOSE TRADE/GTFO
                print ("!!!WARNING!!! POTENTIAL DIRECTION CHANGE!!")
                SIZE = size_value
                ORDER_TYPE = orderType_value
                base_url = REAL_OR_NO_REAL + '/positions/otc'
                data = {"dealId":DEAL_ID,"direction":DIRECTION_TO_CLOSE,"size":SIZE,"orderType":ORDER_TYPE}
                #authenticated_headers_delete IS HACKY AF WORK AROUND!! AS PER .... https://labs.ig.com/node/36
                authenticated_headers_delete = {'Content-Type':'application/json; charset=utf-8',
                'Accept':'application/json; charset=utf-8',
                'X-IG-API-KEY':API_KEY,
                'CST':CST_token,
                'X-SECURITY-TOKEN':x_sec_token,
                '_method':"DELETE"}
                auth_r = requests.post(base_url, data=json.dumps(data), headers=authenticated_headers_delete) 
                #DEBUG
                print(auth_r.status_code)
                print(auth_r.reason)
                print (auth_r.text)
                print ("!!DEBUG TIME!! Direction Change Wait: " + str(datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")))
                Prediction_Wait_Timer = 900 #15Mins
                systime.sleep(Prediction_Wait_Timer)
                
            if elapsed_time > 10800:
                print ("!!DEBUG!! WARNING: TRADE HAS BEEN OPEN OVER TIME")
                if float (PROFIT_OR_LOSS) > 0: #Any profit will do
                    print ("!!DEBUG!! TRADE OPEN OVER TIME AND IN PROFIT")
                    SIZE = size_value
                    ORDER_TYPE = orderType_value
                    base_url = REAL_OR_NO_REAL + '/positions/otc'
                    data = {"dealId":DEAL_ID,"direction":DIRECTION_TO_CLOSE,"size":SIZE,"orderType":ORDER_TYPE}
                    #authenticated_headers_delete IS HACKY AF WORK AROUND!! AS PER .... https://labs.ig.com/node/36
                    authenticated_headers_delete = {'Content-Type':'application/json; charset=utf-8',
                    'Accept':'application/json; charset=utf-8',
                    'X-IG-API-KEY':API_KEY,
                    'CST':CST_token,
                    'X-SECURITY-TOKEN':x_sec_token,
                    '_method':"DELETE"}
                    auth_r = requests.post(base_url, data=json.dumps(data), headers=authenticated_headers_delete) 
                    #DEBUG
                    print(auth_r.status_code)
                    print(auth_r.reason)
                    print (auth_r.text)
                    print ("!!DEBUG!! : TIME AND IN PROFIT :- CLOSED")
                    
          
            if elapsed_time > 18000:
                print ("!!DEBUG!! WARNING: TRADE HAS BEEN OPEN OVER 5 HOURS")
                if -10 <= float (PROFIT_OR_LOSS) <= 0.50:
                    print ("!!DEBUG!! TRADE OPEN OVER 5 HOURS, CUT LOSSES")
                    #ENABLE THIS CODE WHEN HAPPY WITH VALUES
                    ########################################
                    # SIZE = size_value
                    # ORDER_TYPE = orderType_value
                    # base_url = REAL_OR_NO_REAL + '/positions/otc'
                    # data = {"dealId":DEAL_ID,"direction":DIRECTION_TO_CLOSE,"size":SIZE,"orderType":ORDER_TYPE}
                    # #authenticated_headers_delete IS HACKY AF WORK AROUND!! AS PER .... https://labs.ig.com/node/36
                    # authenticated_headers_delete = {'Content-Type':'application/json; charset=utf-8',
                    # 'Accept':'application/json; charset=utf-8',
                    # 'X-IG-API-KEY':API_KEY,
                    # 'CST':CST_token,
                    # 'X-SECURITY-TOKEN':x_sec_token,
                    # '_method':"DELETE"}
                    # auth_r = requests.post(base_url, data=json.dumps(data), headers=authenticated_headers_delete) 
                    # #DEBUG
                    # print(auth_r.status_code)
                    # print(auth_r.reason)
                    # print (auth_r.text)
                    # print ("DEBUG : TIME AND IN PROFIT :- CLOSED")
            
            if float (PROFIT_OR_LOSS) > 4 and elapsed_time > 1800:
                #ENABLE THIS CODE WHEN HAPPY WITH VALUES
                ########################################
                SIZE = size_value
                ORDER_TYPE = orderType_value
                base_url = REAL_OR_NO_REAL + '/positions/otc'
                data = {"dealId":DEAL_ID,"direction":DIRECTION_TO_CLOSE,"size":SIZE,"orderType":ORDER_TYPE}
                #authenticated_headers_delete IS HACKY AF WORK AROUND!! AS PER .... https://labs.ig.com/node/36
                authenticated_headers_delete = {'Content-Type':'application/json; charset=utf-8',
                'Accept':'application/json; charset=utf-8',
                'X-IG-API-KEY':API_KEY,
                'CST':CST_token,
                'X-SECURITY-TOKEN':x_sec_token,
                '_method':"DELETE"}
                auth_r = requests.post(base_url, data=json.dumps(data), headers=authenticated_headers_delete) 
                #DEBUG
                print(auth_r.status_code)
                print(auth_r.reason)
                print (auth_r.text)
                print ("DEBUG : TIME AND IN PROFIT :- CLOSED")

                        
    except Exception as e:
        #print(e) #Yeah, I know now. 
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        print ("ERROR : ORDER MIGHT NOT BE OPEN FOR WHATEVER REASON")
        #WOAH CALM DOWN! WAIT .... STOP LOSS MIGHT HAVE BEEN HIT (Or take Profit)
        systime.sleep(random.randint(1, TIME_WAIT_MULTIPLIER))
        pass
    
        #systime.sleep(1)
            
    if PROFIT_OR_LOSS > 0:
        profitable_trade_count = int(profitable_trade_count) + 1
        print ("DEBUG : ASSUME PROFIT!! Profitable Trade Count " + str(profitable_trade_count))
        SIZE = size_value
        ORDER_TYPE = orderType_value
        
        base_url = REAL_OR_NO_REAL + '/positions/otc'
        data = {"dealId":DEAL_ID,"direction":DIRECTION_TO_CLOSE,"size":SIZE,"orderType":ORDER_TYPE}
        #authenticated_headers_delete IS HACKY AF WORK AROUND!! AS PER .... https://labs.ig.com/node/36
        authenticated_headers_delete = {'Content-Type':'application/json; charset=utf-8',
                'Accept':'application/json; charset=utf-8',
                'X-IG-API-KEY':API_KEY,
                'CST':CST_token,
                'X-SECURITY-TOKEN':x_sec_token,
                '_method':"DELETE"}
        
        auth_r = requests.post(base_url, data=json.dumps(data), headers=authenticated_headers_delete)   
        #CLOSE TRADE
        print(auth_r.status_code)
        print(auth_r.reason)
        print (auth_r.text)
        
        # #CONFIRM CLOSE - FUTURE
        # base_url = REAL_OR_NO_REAL + '/confirms/'+ deal_ref
        # auth_r = requests.get(base_url, headers=authenticated_headers)
        # d = json.loads(auth_r.text)
        # DEAL_ID = d['dealId']
        # print("DEAL ID : " + str(d['dealId']))
        # print(d['dealStatus'])
        # print(d['reason'])
        
        systime.sleep(random.randint(1, TIME_WAIT_MULTIPLIER)) #Obligatory Wait before doing next order
