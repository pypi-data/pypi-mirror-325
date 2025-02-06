from flask import Flask, jsonify,request
from flask_cors import CORS
import logging
from pymongo import MongoClient
from langchain_openai import ChatOpenAI
from Fireflink_NLP import Agent,Browser, BrowserConfig
import asyncio
import uuid
from Fireflink_NLP import BrowserConfig
from Fireflink_NLP.browser.context import BrowserContext
# Basic configuration
import os
import copy
import json
import hvac
from dotenv import load_dotenv
import pandas as pd
load_dotenv()
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
app = Flask(__name__)

class Automation_NLP:
    def __init__(self):
        self.vault_URL = os.getenv('vault_URL')
        self.mongodb_URL = os.getenv('mongodb_URL')
        self.vault_path = os.getenv('vault_path')
        self.role_id = os.getenv('role_id')
        self.secret_id = os.getenv('secret_id')
        self.CAFile = os.getenv('CAFile')
        self.certificateKeyFile = os.getenv("certificateKeyFile")
        self.isOnprem = json.loads(os.getenv("isOnprem").lower())
        self.atc_collection_name=os.getenv("atc_collection_name")
        self.manual_step=""
        self.license_id=""
        self._id=""
        self.script_id=""
        self.project_Id=""
        self.script_name=""
        self.test_case_id=""
        self.prompt_id=""
        self.license_auth=""
        self.element_id=""
        if self.isOnprem == True:
            self.url = self.mongodb_URL
            logging.info(self.url)
        else:
            self.url = self.load_vault_url()
            logging.info(self.url)
        self.similarity_threshold = 1
        self.mongoClient = self.get_mongoClient_connection()
        app.logger.info(f"Class initialized successfully.")

    def load_vault_url(self):
        client = hvac.Client(url=self.vault_URL)
        client.auth.approle.login(
            role_id=self.role_id, secret_id=self.secret_id)
        try:
            secret_response = client.secrets.kv.v2.read_secret_version(
                path=self.vault_path, raise_on_deleted_version=True)
            mongodb_URL = secret_response['data']['data'][self.mongodb_URL]
            app.logger.info(f"Vault URL loaded successfully.")
            return mongodb_URL
        except Exception as e:
            app.logger.error(f"Error loading Vault URL: {e}")
            raise

    def get_mongoClient_connection(self):
        logging.info("Connecting to MongoDB")
        try:
            client = None
            if self.isOnprem == True:
                client = MongoClient(self.url)
            else:
                client = MongoClient(
                    self.url, tlsCAFile=self.CAFile, tlsCertificateKeyFile=self.certificateKeyFile)
            logging.info("Connected to MongoDB successfully")
            return client
        except Exception as e:
            logging.error(f"MongoDB connection error: {e}")
            raise
        
    def load_collection_for_saving(self,license_id):
        collection_prompt=self.mongoClient[license_id][self.atc_collection_name]
        return collection_prompt
    
    
    def open_browser(self):
        return {
                        "name": "OpenBrowser",
                        "type": "Group",
                        "nlpName": "OpenBrowser",
                        "executionOrder": 1,
                        "nlpId": "",
                        "stepInputs": [
                            {
                                "value": "MARK_THIS_STEP_AS_FAILED_AND_CONTINUE_SCRIPT_EXECUTION",
                                "name": "ifCheckPointIsFailed",
                                "type": "java.lang.String"
                            }
                        ],
                        "skip": False,
                        "returnType": "void",
                        "libraryId": "",
                        "stepGroupId": "",
                        "displayName": "OpenBrowser",
                        "defaultDisplayName": "OpenBrowser",
                        "stepId": "STP"+str(uuid.uuid4()),
                        "toolTip": "Open and Close Browser : OpenBrowser : Web",
                        "defaultToolTip": "Open and Close Browser : OpenBrowser : Web",
                        "hierarchy": 0,
                        "marginLeft": 0,
                        "mustExecute": False,
                        "isAfterBreakStep": False,
                        "isAfterContinueStep": False,
                        "imported": False,
                        "isDisabled": False
                    }
        
    def click_on_element(self,executionOrder,element,nlpId):
        print("---",element,"-----")
        return {
      "name": f"Click on {element.get("name")} {element.get("type")}",
      "type": "step",
      "nlpName": "Click",
      "executionOrder":executionOrder,
      "nlpId": nlpId,
      "passMessage": "Clicked on *elementName* *elementType*",
      "failMessage": "Failed to click on *elementName* *elementType* in *elementPage* page",
      "elementDetails": [
        {
          "executionOrder": 0,
          "name": element.get("name"),
          "type": element.get("type"),
          "locatorsCount": element.get("locatorsCount"),
          "locators": element.get("locators"),
          "folder": False,
          "elementId": element.get("elementId"),
          "commit": False,
          "publish": False,
          "newState": False,
          "activeStatus": False,
          "updatedStatus": False,
          "parentId": ""
        }
      ],
      "stepInputs": [
        {
          "value": element.get("name"),
          "name": "elementName",
          "type": "java.lang.String"
        },
        {
          "value": element.get("type"),
          "name": "elementType",
          "type": "java.lang.String"
        },
        {
          "value": "",
          "name": "element",
          "type": "org.openqa.selenium.WebElement",
          "reference": "ELEMENT",
          "locators": element.get("locators")
        },
        {
          "value": "MARK_THIS_STEP_AS_FAILED_AND_CONTINUE_SCRIPT_EXECUTION",
          "name": "ifCheckPointIsFailed",
          "type": "java.lang.String"
        }
      ],
      "skip": False,
      "returnType": "void",
      "displayName": f"Click on {element.get("name")} {element.get("type")}",
      "defaultDisplayName": "Click on *elementName* *elementType*",
      "stepId": f"STP{str(uuid.uuid4())}",
      "toolTip": f"Click on {element.get("name")} {element.get("type")}",
      "defaultToolTip": "Click on *elementName* *elementType* in *elementPage* page",
      "hierarchy": 0,
      "parentSpecialNlpId": "",
      "marginLeft": 0,
      "isIterationStep": True,
      "isAfterBreakStep": False,
      "isAfterContinueStep": False
    }    
    
    def maximize_browser(self):
        return {
                        "name": "Maximize browser window",
      "type": "step",
      "nlpName": "MaximizeBrowser",
      "executionOrder": 2,
      "nlpId": "NLP1199",## need to get from auth
      "passMessage": "Browser window is maximized",
      "failMessage": "Failed to maximize browser window",
      "stepInputs": [
        {
          "value": "MARK_THIS_STEP_AS_FAILED_AND_CONTINUE_SCRIPT_EXECUTION",
          "name": "ifCheckPointIsFailed",
          "type": "java.lang.String"
        }
      ],
      "skip": False,
      "returnType": "void",
      "displayName": "Maximize browser window",
      "defaultDisplayName": "Maximize browser window",
      "stepId": "STP84006M5D9H18M34S41M630R43",
      "toolTip": "Maximize browser window",
      "defaultToolTip": "Maximize browser window",
      "hierarchy": 0,
      "parentSpecialNlpId": "",
      "marginLeft": 0,
      "isIterationStep": True,
      "isAfterBreakStep": False,
      "isAfterContinueStep": False
                    }
        
        
    def enter_input_element(self,input,element,executionOrder,nlpId):
        return {
      "name": f"Enter {input} into {element.get("name")} {element.get("type")}",
      "type": "step",
      "nlpName": "SendKeys",
      "executionOrder": executionOrder,
      "nlpId": nlpId,
      "passMessage": "Entered *input* into *elementName* *elementType*",
      "failMessage": "Failed to enter *input* into *elementName* *elementType*",
      "elementDetails": [
        {
          "executionOrder": 0,
          "name": element.get("name"),
          "type": element.get("type"),
          "locatorsCount": element.get("locatorsCount"),
          "locators": element.get("locators"),
          "folder": False,
          "elementId": element.get("elementId"),
          "commit": False,
          "publish": False,
          "newState": False,
          "activeStatus": False,
          "updatedStatus": False,
          "parentId": ""
        }
      ],
      "stepInputs": [
        {
          "value": element.get("name"),
          "name": "elementName",
          "type": "java.lang.String"
        },
        {
          "value": element.get("type"),
          "name": "elementType",
          "type": "java.lang.String"
        },
        {
          "value": input,
          "name": "input",
          "type": "java.lang.String",
        },
        {
          "value": "",
          "name": "element",
          "type": "org.openqa.selenium.WebElement",
          "reference": "ELEMENT",
          "locators": element.get("locators")
        },
        {
          "value": "MARK_THIS_STEP_AS_FAILED_AND_CONTINUE_SCRIPT_EXECUTION",
          "name": "ifCheckPointIsFailed",
          "type": "java.lang.String"
        }
      ],
      "skip": False,
      "returnType": "void",
      "displayName": "Enter dtaa:dummy into search area textarea",
      "defaultDisplayName": "Enter *input* into *elementName* *elementType*",
      "stepId": f"STP{str(uuid.uuid4())}",
      "toolTip": f"Enter {input} into {element.get("name")} {element.get("type")}",
      "defaultToolTip": "Enter *input* into *elementName* *elementType* in *elementPage* page",
      "hierarchy": 0,
      "parentSpecialNlpId": "",
      "marginLeft": 0,
      "isIterationStep": True,
      "isAfterBreakStep": False,
      "isAfterContinueStep": False
    }
    
    def switch_tab(self,executionOrder,input,nlpId):
        return{
                "name": f"Switch to window if URL contains {input}",
                "type": "step",
                "nlpName": "SwitchToNewWindowIfUrlContainsString",
                "executionOrder": executionOrder,
                "nlpId": nlpId,
                "passMessage": "Switched to window where URL contains *url*",
                "failMessage": "Failed to switch to window with URL contains *url*",
                "stepReferenceInfo": {
                    "stepNumber": 0,
                    "name": "Capability",
                    "type": "GLOBAL",
                    "value": None,
                    "returnValue": None,
                    "masked": False,
                    "referenceId": None
                },
                "stepInputs": [
                    {
                        "value": input,
                        "name": "url",
                        "type": "java.lang.String",
                        "parameter": False
                    },
                    {
                        "value": "MARK_THIS_STEP_AS_FAILED_AND_CONTINUE_SCRIPT_EXECUTION",
                        "name": "ifCheckPointIsFailed",
                        "type": "java.lang.String",
                        "parameter": False
                    }
                ],
                "skip": False,
                "returnType": "String: currentWindow",
                "platform": "Web",
                "searchName": "Browser window : Switch to browser window if URL contains *url*",
                "displayName": f"Switch to window if URL contains {input}",
                "actualFailedResult": "N/A",
                "defaultDisplayName": "Switch to window if URL contains *url*",
                "stepId": f"STP{str(uuid.uuid4())}",
                "toolTip": f"Switch to window if URL contains {input}",
                "defaultToolTip": "Switch to window if URL contains *url*",
                "hierarchy": 0,
                "marginLeft": 0.0,
                "mustExecute": False,
                "imported": False,
                "isDisabled":False ,
                "isStepGroupStep": False,
                "isJDBCStep": False,
                "afterBreakStep": False,
                "afterContinueStep": False
            }
        
    def navigate_back(self,executionOrder,nlpId):
        return {
                "name": "Navigate to previous page in browser window",
                "type": "step",
                "nlpName": "NavigateBack",
                "executionOrder": executionOrder,
                "nlpId": nlpId,
                "passMessage": "Navigated to previous page in browser window",
                "failMessage": "Failed to navigate back to previous page in browser window",
                "stepInputs": [
                    {
                        "value": "MARK_THIS_STEP_AS_FAILED_AND_CONTINUE_SCRIPT_EXECUTION",
                        "name": "ifCheckPointIsFailed",
                        "type": "java.lang.String",
                        "parameter": False
                    }
                ],
                "skip": False,
                "returnType": "void",
                "platform": "Web",
                "searchName": "Browser window : Navigate back to previous page",
                "displayName": "Navigate to previous page in browser window",
                "actualFailedResult": "N/A",
                "defaultDisplayName": "Navigate to previous page in browser window",
                "stepId": f"STP{str(uuid.uuid4())}",
                "toolTip": "Navigate to previous page in browser window",
                "defaultToolTip": "Navigate to previous page in browser window",
                "hierarchy": 0,
                "marginLeft": 0.0,
                "mustExecute": False,
                "imported": False,
                "isDisabled": False,
                "isStepGroupStep": False,
                "isJDBCStep": False,
                "afterBreakStep": False,
                "afterContinueStep": False
            }
    
    
    def close_browser(self,executionOrder):
        return {
                "name": "Close Browser",
                "type": "Group",
                "nlpName": "Close Browser",
                "executionOrder": executionOrder,
                "nlpId": "",
                "stepInputs": [
                    {
                        "value": "MARK_THIS_STEP_AS_FAILED_AND_CONTINUE_SCRIPT_EXECUTION",
                        "name": "ifCheckPointIsFailed",
                        "type": "java.lang.String",
                        "parameter": False
                    }
                ],
                "skip": False,
                "returnType": "void",
                "libraryId": "",
                "stepGroupId": "",
                "displayName": "Close Browser",
                "defaultDisplayName": "Close Browser",
                "stepId": "STP3451725679170606",
                "toolTip": "Open and Close Browser : Close Browser : Web",
                "defaultToolTip": "Open and Close Browser : Close Browser : Web",
                "hierarchy": 0,
                "marginLeft": 0.0,
                "mustExecute": False,
                "imported": False,
                "isDisabled": False,
                "isStepGroupStep": False,
                "isJDBCStep": False,
                "afterBreakStep": False,
                "afterContinueStep": False
            }
    
    def navigate_to_url(self,url,executionOrder,nlpId):
        return {
                        "name": f"Navigate to URL {url}",
                        "type": "step",
                        "nlpName": "NavigateToURL",
                        "executionOrder": executionOrder,
                        "nlpId": nlpId,
                        "passMessage": "Navigated to URL *url*",
                        "failMessage": "Failed to navigate to URL *url*",
                        "stepInputs": [
                            {
                                "value": f"{url}",
                                "name": "url",
                                "type": "java.lang.String"
                            },
                            {
                                "value": "MARK_THIS_STEP_AS_FAILED_AND_CONTINUE_SCRIPT_EXECUTION",
                                "name": "ifCheckPointIsFailed",
                                "type": "java.lang.String"
                            }
                        ],
                        "skip": False,
                        "returnType": "void",
                        "platform": "Web",
                        "searchName": "Navigate to *url*",
                        "displayName": f"Navigate to URL {url}",
                        "actualFailedResult": "N/A",
                        "defaultDisplayName": "Navigate to URL *url*",
                        "stepId": "STP"+str(uuid.uuid4()),
                        "toolTip": f"Navigate to URL {url}",
                        "defaultToolTip": "Navigate to URL *url*",
                        "hierarchy": 0,
                        "marginLeft": 0,
                        "mustExecute": False,
                        "isAfterBreakStep": False,
                        "isAfterContinueStep": False,
                        "imported": False,
                        "isDisabled": False
            }
    
    
    def process_elements(self, data):
        for output in data:
            element_dict = {}
            elementname = None
            locators = []
            if not output.get("element"):
                continue
            for selector in output.get("element").get("selector"):
                _id=str(uuid.uuid4())
                output['element_ref']=_id
                locator = {
                    "value": selector.get("value")[0].get("value"),
                    "type": "static",
                    "name": selector.get("key"),
                    "status": "NOT_USED",
                    "isRecorded": "Y",
                    "priority": "",
                    "defaultAddedFirst": False,
                    "defaultAddedSecond": False
                }
                if str(selector.get("value")[0].get("key")).lower() == 'name':
                    elementname = selector.get("value")[0].get("value")

                locators.append(locator)
            if elementname is None:
                elementname =f"Ele{_id}"
            element_dict["locators"] = locators
            element_dict["elementName"] = elementname
            self.element_save(element_dict,_id)
        
            
            

    def element_save(self, element_dict: dict,_id):
        # Check if an element with the same name already exists in the database
        existing_element = self.mongoClient[self.license_id][os.getenv("collection")].find_one({"name": element_dict.get("elementName")})
        
        # Only proceed if the element does not already exist
        if existing_element:
            element_dict['elementName']=f"{element_dict.get("elementName")}-{str(uuid.uuid4())}"
         
        
        json = {
            "_id": _id,
            "executionOrder": 1,
            "hierarchy": 0,
            "name": element_dict.get("elementName"),
            "desc": "",
            "type": element_dict.get("type", "Link"),
            "locatorsCount": len(element_dict.get("locators")),
            "locators": element_dict.get("locators"),
            "isShared": "N",
            "isRecorded": "Y",
            "folder": False,
            "platform": "Web",
            "projectType": "Web",
            "projectId": element_dict.get("projectId", ""),
            "elementId": _id,
            "users": [""],
            "excludeUsers": [],
            "deleteUsers": [],
            "activeStatus": True,
            "updatedStatus": True,
            "imported": True,
            "createdBy": element_dict.get("createdBy", ""),
            "modifiedBy": element_dict.get("modifiedBy", ""),
            "createdByUname": element_dict.get("createdByUname", ""),
            "modifiedByUname": element_dict.get("modifiedByUname", ""),
            "createdOn": element_dict.get("createdOn", ""),
            "modifiedOn": element_dict.get("modifiedOn", ""),
            "state": "NEW",
            "path": element_dict.get("path", ""),
            "searchKey": element_dict.get("searchKey", ""),
            "parentId": element_dict.get("parentId", ""),
            "parentName": element_dict.get("parentName", ""),
            "version": "1.0",
        }

        self.mongoClient[self.license_id][os.getenv("collection")].insert_one(json)
        logging.info(f"Element with name {element_dict.get('elementName')} saved successfully.")


    def save_script_db(self,steps):
        collection=self.load_collection_for_saving(license_id=self.license_id)
        script_id=str(uuid.uuid4())
        document={
                    "_id": script_id,
                    "name": automation.script_name,
                    "scriptType": "Web",
                    "desc": "",
                    "type": "Script",
                    "testCaseType": "Automation",
                    "executionOrder": 0,
                    "stepCount": 0,
                    "hierarchy": 0,
                    "preConditionCount": 0,
                    "postConditionCount": 0,
                    "dependentScriptCount": 0,
                    "projectLabels": [],
                    "imported": False,
                    "assigneeCount": 0,
                    "projectId": automation.project_Id,
                    "authorizationInfo": {
                        "authType": "No Auth",
                        "parentId": "MOD1003",
                        "inherited": True
                    },
                    "prefix": "",
                    "pair": False,
                    "createdBy": "",
                    "modifiedBy": "",
                    "createdByUname": "",
                    "modifiedByUname": "",
                    "createdOn": "",
                    "modifiedOn": "",
                    "state": "",
                    "path": "",
                    "searchKey": "",
                    "parentId": "",
                    "parentName": "",
                    "version": "",
                    "_class": "",
                    "steps": steps
                }
        collection.insert_one(document)
        return script_id

    def clone_step(self,license_id, _id, execution_id):
        collection_name = os.getenv("atc_collection_name")
        document = self.mongoClient[license_id][collection_name].find_one({"_id": _id})
        if not document:  # Handle case where no document is found
            return {"error": "Document not found"}

        steps = document.get("steps", [])
        updated_steps = []
        cloned_step = None

        for step in steps:
            if step.get("executionOrder") == execution_id:
                cloned_step = copy.deepcopy(step)  # Properly clone the step
                cloned_step["executionOrder"] = step["executionOrder"] + 1
                cloned_step['stepId'] = f"STP{uuid.uuid4()}"
                updated_steps.append(step)  # Append original step
                updated_steps.append(cloned_step)  # Append cloned step
            elif step.get("executionOrder") > execution_id:
                step["executionOrder"] += 1  # Correct way to update execution order
                updated_steps.append(step)
            else:
                updated_steps.append(step)

        # Update the document with new steps
        self.mongoClient[self.license_id][collection_name].update_one(
            {"_id": _id},
            {"$set": {"steps": updated_steps}}
        )

        return {"success": True, "updated_steps_count": len(updated_steps)}

            
                

async def run_agent():
    context = BrowserContext(browser=Browser(BrowserConfig(headless=False)))
    token = os.getenv("OpenAIkey")
    agent = Agent(
        task=automation.manual_step,
        use_vision=False,
        llm=ChatOpenAI(model="gpt-4o-mini", api_key=token),
        browser_context=context
    )
    steps=[]
    result = await agent.run()
    await context.browser.close() 
    output=agent.resultstep# Ensure the browser is closed properly
    automation.process_elements(output)
    steps.append(automation.open_browser())
    steps.append(automation.maximize_browser())
    for index,obj in enumerate(output,start=3):
        if obj['nlpName']=="NavigateToURL":
            nlpid=automation.mongoClient[automation.license_auth]["nlps"].find_one({ "nlpName":obj['nlpName'],"platform": "Web" })
            steps.append(automation.navigate_to_url(url=obj['input'],executionOrder=index,nlpId=nlpid.get("_id")))
        if obj['nlpName']=="Click":
            nlpid=automation.mongoClient[automation.license_auth]["nlps"].find_one({ "nlpName":obj['nlpName'],"platform": "Web" })
            element=automation.mongoClient[automation.license_id]["aiElement"].find_one({"_id":obj['element_ref']})
            steps.append(automation.click_on_element(element=element,executionOrder=index,nlpId=nlpid.get("_id")))
        if obj['nlpName']=="SendKeys":
            nlpid=automation.mongoClient[automation.license_auth]["nlps"].find_one({ "nlpName":obj['nlpName'],"platform": "Web" })
            element=automation.mongoClient[automation.license_id]["aiElement"].find_one({"_id":obj['element_ref']})
            steps.append(automation.enter_input_element(input=obj['input'],element=element,executionOrder=index,nlpId=nlpid.get("_id")))
        if obj['nlpName']=='SwitchToNewWindowIfUrlContainsString':
            nlpid=automation.mongoClient[automation.license_auth]["nlps"].find_one({ "nlpName":obj['nlpName'],"platform": "Web" })
            steps.append(automation.switch_tab(input=obj['input'],executionOrder=index,nlpId=nlpid.get("_id")))
        if obj['nlpName']=="NavigateBack":
            nlpid=automation.mongoClient[automation.license_auth]["nlps"].find_one({ "nlpName":obj['nlpName'],"platform": "Web" })
            steps.append(automation.navigate_back(executionOrder=index,nlpId=nlpid.get("_id")))
    steps.append(automation.close_browser(executionOrder=len(output)+3))
    script_id=automation.save_script_db(steps=steps)
    
    return  automation.mongoClient[automation.license_id]["ai_atc_script"].find_one({"_id":script_id})




# Route to execute the agent task
@app.route('/run-agent', methods=['POST'])
def run_agent_endpoint():
    data=request.get_json()
    automation.manual_step=data.get("manualSteps")
    automation.project_Id=data.get("project_Id")
    license_id=data.get("license_id")
    automation.script_name=data.get("script_name")
    automation.prompt_id=data.get("prompt_id")
    automation.test_case_id=data.get("test_case_id")
    automation._id=f"ELE{str(uuid.uuid4())}"
    env = os.getenv('PROFILE')
    if env:
        automation.license_id = f"optimize_{env}_{license_id}"
        automation.license_auth=f"optimize_{env}_auth"
    else:
        automation.license_id = f"optimize_{license_id}"
        automation.license_auth=f"optimize_auth"
    result = asyncio.run(run_agent())
    print(result)
    return jsonify({"Ouptut":result})
        

@app.route('/clone', methods=['POST'])
def clone():
    data=request.get_json()
    _id=data.get("_id")
    execution_id=data.get("execution_id")
    license_id=data.get("license_id")
    env = os.getenv('PROFILE')
    if env:
        automation.license_id = f"optimize_{env}_{license_id}"
        automation.license_auth=f"optimize_{env}_auth"
    else:
        automation.license_id = f"optimize_{license_id}"
        automation.license_auth=f"optimize_auth"
    result=automation.clone_step(license_id=automation.license_id,_id=_id,execution_id=execution_id)
    return jsonify({"Ouptut":result})
# Health check endpoint
@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "API is running!"})
automation=Automation_NLP()
# Run the Flask app
if __name__ == '__main__':
    app.run(host="0.0.0.0")
