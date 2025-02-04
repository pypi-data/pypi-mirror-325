import os
import json
import requests
from .log_keeper import *


# def reg_no_ml_options(data):
#     credPath = input("Enter registered credential file path: ")
#     if os.path.exists(credPath):
#         f = open(credPath)
#         creds = json.load(f)
#         print(creds)
#     else:
#         print("Credential file path invalid.")
#         exit()
        
#     registerOption = input("Enter 0 to register model and upload datasets to Azure ML workspace.\nEnter 1 to register model to Azure ML.\nEnter 2 to upload datasets to Azure ML workspace. : ")
#     if int(registerOption) == 0 or int(registerOption) == 2:
#         datasetUploadPath = input("Enter dataset upload path: ")
#     else:
#         datasetUploadPath = None
#     data.update({"credId": json.dumps(creds), "registerOption": int(registerOption), "datasetUploadPath": datasetUploadPath})       
#     return data

# def fetch_no_ml_options(data):
#     credPath = input("Enter registered credential file path: ")
#     if os.path.exists(credPath):
#         f = open(credPath)
#         creds = json.load(f)
#         print(creds)
#     else:
#         print("Credential file path invalid.")
#         exit()
    
#     fetch_list = []
#     fetchOption = input("Enter 0 to fetch model and upload datasets from Azure ML workspace.\nEnter 1 to fetch model from Azure ML.\nEnter 2 to fetch datasets from Azure ML workspace. : ")

#     if fetchOption == 0:
#         fetch_list.append(["Model", "Datasets"])
#     elif fetchOption == 1:
#         fetch_list.append(["Model"])
#     else:
#         fetch_list.append(["Datasets"])

#     if int(fetchOption) == 0 or int(fetchOption) == 2:
#         dataPath = input("Enter dataset path: ")
#     else:
#         dataPath = None
#     data.update({"credId": json.dumps(creds), "fetchOption": fetch_list, "dataPath": dataPath})       
#     return data

def reg_ml(data, ml_options):
    datasetUploadPath = ml_options.get("datasetUploadPath", None)
    try:
        if os.path.exists(ml_options.get("credPath",None)):
                    f = open(ml_options.get("credPath",None))
                    creds = json.load(f)
                    print(creds)
        else:
            print("Credential file path invalid.")
            exit()
        data.update({"amlCred": json.dumps(creds), "datasetUploadPath": datasetUploadPath})
    except Exception as e:
        logger.error(str(e))
    return data

def fetch_ml(data, ml_options):
    dataPath = ml_options.get("dataPath", None)
    try:
        if os.path.exists(ml_options.get("credPath",None)):
                    f = open(ml_options.get("credPath",None))
                    creds = json.load(f)
                    print(creds)
        else:
            print("Credential file path invalid.")
            exit()
        data.update({"amlCred": json.dumps(creds), "dataPath": dataPath})
    except Exception as e:
        logger.error(str(e))
    return data

def model_request(url, kwargs, data, ml_options, files):
    insertionType = data.get("datasetinsertionType", None)
    try:
        if insertionType == "Manual":
            if ml_options:
                data = reg_ml(data, ml_options)
            else:
                data = data
            model = requests.post(url, data=data, files=files, headers=kwargs['headers'])
        elif insertionType == "AzureML":
            data = fetch_ml(data, ml_options)
            data.update(files)
            model = requests.post(url, data=data, headers=kwargs['headers'])
        elif insertionType == "MLFlow":
            dataset_field_keys = ['training_dataset', 'test_dataset', 'pred_dataset', 'actual_dataset', 'model_file_path']
            list(map(data.pop, dataset_field_keys))
            data.update(files)
            model = requests.post(url, data=data, headers=kwargs['headers'])
        else:
            data.update({"datasetinsertionType":"Manual"})
            model = requests.post(url, data=data, files=files, headers=kwargs['headers'])
    except Exception as e:
        logger.error(str(e))
    return model
    