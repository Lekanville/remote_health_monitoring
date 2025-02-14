# Remote Vital Signs Monitoring Using Smart Devices
Feasibility, Accuracy, and Implications for Health Status Prediction

## Prerequisites 

#### Conda (required)

## Setup

```bash
#Clone the Repo (use https if necessary)
git@github.com:MRCIEU/bbt_research.git
cd remote_health_monitoring

#Create the Conda Environment
conda env create -f environment.yml
conda activate health_monitor_env

#Add module directory to python path
cd code
pwd
export PYTHONPATH=$PYTHONPATH:pwd
cd ..
```
## General
Our codes for remote access of health vital signs from GoogleFit API are uploaded into this repository. Additionally, we added our codes for comparing the remote data with a clinical device (sphygmomanometer) data.

To access data from GoogleFit API, create a Google account to access Google cloud services. Afterward;
1. Create a new project form the Google cloud console
2. From the navigation menu or the quick access menu, click "APIs and Services"
3. Select credentials, create credentials and then OAuth client ID.
4. Select application type and give the credential a name
5. Click create and download the JSON file
6. Save the credentials (credentials.json) in the root folder of the project

You can get more information here [https://support.google.com/googleapi/answer/6158862?hl=en]

## GoogleFit data access
If accessing this for the first time, you would be asked to verify your identity, afterwards a token will be created. If accessing after the token as expired, delete the token file and create a new one
by verifying your identity. 
To run this script, do the following;
1. Specify the start of the period to get in nanoseconds
2. Specify the end of the period to get in nanoseconds

Afterwards, run the following in the terminal
```bash
python -m code/get_fit_data -i start -j end
```

## Comparing data obtained with a those obtained from a clinical device
This python script preprocesses the remote and clinical data for both users with and without health conditions. It then analyses the differences in the mean readings of boths groups.
To run this script, do the following;
1. Specify the remote dataset
2. Specify the clinical dataset

run
```bash
python -m code/process -i data/remote_data.csv -j data/clinical_data.csv  
```

## Data
Due to privacy issues, we could not upload out data here. However, you can contact us if you wish to work with our datasets

## Potential issues
1. 'invalid_grant: Token has been expired or revoked.'
If you get this error, it means your access token has expired. Delete the token.json file, run  scrip again and allow google access. Another token.json file will be created for your from your credentails.

If you encounter any other bug, please report it in the bug section

## Citation
If you find our work useful, please cite -
Ranti FAMUTIMI, Olalekan AWONIRAN, Olufemi OYELAMI, O. OLABIYI, Olumide ADELEKE (2024). Remote Vital Signs Monitoring Using Smart Devices: Feasibility, Accuracy, and Implications for Health Status Prediction. Virtual Reality & Intelligent Hardware
