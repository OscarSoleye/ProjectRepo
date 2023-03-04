# ProjectRepo
This project displays the a webpage with 2 links that lead to 2 separate tables.
The Clubs Info table displays a database that shows a list of clubs with players born after the year 2000. The clubs name, stadium name and club id are displayed. 
The Players Data table shows information on the players name, player id, the club the player plays for, their nationality, date of birth and the position they play on the field. All information is accurate as of the 1st March,2023. 

The data was found on Kaggle and is based on the TransferMarkt datasets being scraped biweekly. (https://www.kaggle.com/datasets/davidcariboo/player-scores)

Flask is the framwework that was used to display the tables through templates. 

csv module was imported to assist in parsing the data from the csv files as there are more information from them but i only dsiplayed what i needed. 

SQLite3 was used to create and maange the databases created from the CSV files. 
