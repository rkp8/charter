# Python Flask REST API and JavaScript Chart Visualizer


<img width="500" height="500" alt="Screen Shot 2021-06-27 at 7 52 57 PM" src="https://user-images.githubusercontent.com/60204834/123563192-53b42500-d781-11eb-9ca0-3ee20c1480a8.png">


 -A simple proof of concept for two different models on Delinquency: By Year and by FICO. 
  <br>
  -Can switch between the two using drop-down menu


  ### DB Connection Info:
  -Connected to Local MongoDB:   
  
    client = MongoClient('mongodb://localhost:27017')
  
  -Current DB contains the following 2 documents:
  
    { "_id" : ObjectId("60d8c78d1cb1bd5f83331898"), "predicted" : [ 3, 5, 6, 7, 8 ], "name" : "Delinquency", "actual" : [ 4, 6, 5, 12, 7 ], "xlabel" : "Year", "xvalues" : [ 2005, 2006, 2007, 2008, 2009 ] }
    
   <br>

    { "_id" : ObjectId("60d8c7ba1cb1bd5f83331899"), "actual" : [ 7, 6, 4, 5, 3 ], "name" : "Delinquency", "predicted" : [ 9, 8, 6, 4, 2 ], "xlabel" : "FICO", "xvalues" : [ 100, 300, 500, 700, 900 ] }
  
  
### (Requires MongoDB installation. Please see nonDB branch to run a demo on Fannie Mae computer):

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
 
