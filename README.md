# Python Flask REST API and JavaScript Chart Visualizer

### Connection to Local MongoDB (Requires MongoDB installation. Please see nonDB branch to run a demo on Fannie Mae computer):

To run locally:
 
  -Download zip file
  
  -Configure Local DB:
    -Move the dump folder to your MongoDB bin directorY
    -If you already have a dump folder, merge the two folders
    
    Run this command:  mongorestore
    
  -Open another command prompt and run:  mongod
  
  -Open another command prompt and run:  mongo

 
 -Open another command prompt and cd into templates folder
    
  -Install dependencies: 
      
        pip install Flask flask_pymongo pymongo flask_cors
  
  
  -Run app.py to launch server 
  
  
  -Open chart.html in a browser
  
  <br>
  
  ### Current Progress:
  -Connected to Local MongoDB
  
  -Current DB contains the following documents:
  
  
  
  -A simple proof of concept for two different models on Delinquency: By Year and by FICO. 
  <br>
  -Can switch between the two using drop-down menu
  
  
  
