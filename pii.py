import os
from dotenv import load_dotenv
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
load_dotenv()
languaje_key = os.environ['LANGUAGE_KEY']
languaje_endpoint = os.environ['LANGUAJE_ENDPOINT']
#print(lenguaje_key)
#print(lenguaje_endpoint)
client=TextAnalyticsClient(languaje_endpoint, AzureKeyCredential(languaje_key))

def demo_pii_recognition(client):
    documents = ['El numero del empleado es 859-52-962', 
                 'mi nombre es Betsy', 
                 'Mi esposo se llama Douglas Falcón',
                 'Saludos es un texto']

    response = client.recognize_pii_entities(documents, language ="es" )
    result = [doc for doc in response if not doc.is_error]
    for doc in result:
        print("texto encontrado: {}".format(doc.redacted_text))
        for entity in doc.entities:
                print("\tEntidad:{}".format(entity.text))
                print("\tCategoria:{}".format(entity.category))
                print("\tVivel de confianza:{}".format(entity.confidence_score))
                print("\toffset:{}".format(entity.offset))
                print("\tlongitud:{}".format(entity.length))

        
demo_pii_recognition(client)