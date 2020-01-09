from src.collect_data import *
from src.oauth import *
from src.rest_api import *

# Call code
if __name__ == '__main__': 
    
    # collect data 
    tags=['#openbanking','#apifirst','#devops','#cloudfirst','#microservices','#apigateway','#oauth', '#swagger','#raml','#openapis']
    
    print('\nCollecting twitter data...\n')
    
    for hashtags in tags:
         pdatabase = CollectData(100, -1, hashtags)
         pdatabase.get_tweets()  
         
    # run REST API
    app.run(debug=True)

# Test post one tweet 
#api.update_status("OI!")