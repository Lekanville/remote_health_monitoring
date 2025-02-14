import argparse
from pathlib import Path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import requests
import json
import pandas as pd


parser = argparse.ArgumentParser(description="Preprocessing the data")
parser.add_argument("-i", "--start", type=str, required=True, help="The start time ns timestamp")
parser.add_argument("-j", "--end", type=str, required=True, help="The end time in ns timestamp")

#1. Scopes Definition
SCOPES = ["https://www.googleapis.com/auth/fitness.heart_rate.read",
          "https://www.googleapis.com/auth/fitness.blood_pressure.read"]

#2. Access Grant and Security
def getData(start, end):
    creds = None
    
    time_frame = start+"-"+end
    
    if Path("token.json").exists():
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

#3. Data Pipelining 
    with build("fitness", "v1", credentials=creds) as service:        
    #       response1 = service.users().dataSources().datasets().get(userId='me', dataSourceId="derived:com.google.heart_rate.bpm:com.google.android.gms:merge_heart_rate_bpm",
    #                                             datasetId="1682925670000000000-1704039842000000000").execute()
                                                         
            
    #       response2 = service.users().dataSources().datasets().get(userId='me', dataSourceId="derived:com.google.blood_pressure:com.google.android.gms:merged", 
    #                                              datasetId="1682925670000000000-1704039842000000000").execute()
            response1 = service.users().dataSources().datasets().get(
                userId='me', dataSourceId="derived:com.google.heart_rate.bpm:com.google.android.gms:merge_heart_rate_bpm",
                                                  datasetId=time_frame
            ).execute()
                                                         
            response2 = service.users().dataSources().datasets().get(
                userId='me', dataSourceId="derived:com.google.blood_pressure:com.google.android.gms:merged", 
                                                   datasetId=time_frame
            ).execute()
            res1 = pd.DataFrame(response1)
            res2 = pd.DataFrame(response2) 
            return (res1, res2)

#4. Data Endpoint and Preprocessing
def main(start, end):
    response_1, response_2 = getData(start, end)
    
    df_1 = pd.json_normalize(response_1['point'])
    df_1['BPM'] = df_1["value"].apply(lambda x: x[0]['fpVal'])
    df_1['Date_Time'] = df_1['startTimeNanos'].apply(lambda x: x[0:10])
    df_1['Date_Time'] = pd.to_datetime(df_1['Date_Time'],unit='s')
    df_1['Date'] = df_1['Date_Time'].dt.date
    df_1['Time'] = df_1['Date_Time'].dt.time
    grouped_1 = df_1.groupby("Date").agg(BPM_Min = ("BPM", "min"), BPM_Max = ("BPM", "max"), BPM_Avg = ("BPM", "mean")).round(0)
    
    df_2 = pd.json_normalize(response_2['point'])
    df_2['Systolic'] = df_2["value"].apply(lambda x: x[0]['fpVal'])
    df_2['Diastolic'] = df_2["value"].apply(lambda x: x[1]['fpVal'])
    df_2['Date_Time'] = df_2['startTimeNanos'].apply(lambda x: x[0:10])
    df_2['Date_Time'] = pd.to_datetime(df_2['Date_Time'],unit='s')
    df_2['Date'] = df_2['Date_Time'].dt.date
    df_2['Time'] = df_2['Date_Time'].dt.time
    df_2.drop(['Date_Time'], axis = 1, inplace = True)
    #return (df_2)
    #return (df_1, df_2, grouped_1)
    print(df_1.head())
    print(df_2.head())
    return (df_1, df_2)

if __name__ == "__main__":
    args = parser.parse_args()
    main(args.start, args.end)
