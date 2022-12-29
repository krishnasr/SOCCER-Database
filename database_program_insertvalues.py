import pandas as pd
file_country = pd.read_csv(r'C:\Users\Krishna S R\Desktop\Country.csv',index_col=False,delimiter=',',header=None)  
file_country.head()
file_players = pd.read_csv(r'C:\Users\Krishna S R\Desktop\Players.csv',index_col=False,delimiter=',',header=None)
file_players.head()
file_match_results = pd.read_csv(r'C:\Users\Krishna S R\Desktop\Match_results.csv',index_col=False,delimiter=',',header=None)
file_match_results.head()
file_player_cards = pd.read_csv(r'C:\Users\Krishna S R\Desktop\Player_Cards.csv',index_col=False,delimiter=',',header=None)
file_player_cards.head()
file_player_assists_goals = pd.read_csv(r'C:\Users\Krishna S R\Desktop\Player_Assists_Goals.csv',index_col=False,delimiter=',',header=None)
file_player_assists_goals.head()
import mysql.connector as mesql
from mysql.connector import Error
try:
    connet=mesql.connect(host="acadmysqldb001p.uta.edu",user="kxs0344",password="Scarenage@0512")
    if connet.is_connected():
        cursor=connet.cursor()
        print("Database is connected")
        cursor.execute("USE kxs0344;")
        cursor.execute("DROP TABLE IF EXISTS PLAYER_ASSISTS_GOALS ;")
        cursor.execute("DROP TABLE IF EXISTS PLAYER_CARDS ;")
        cursor.execute("DROP TABLE IF EXISTS MATCH_RESULTS ;")
        cursor.execute("DROP TABLE IF EXISTS PLAYERS;")
        cursor.execute("DROP TABLE IF EXISTS COUNTRY;")
        print("Creating table COUNTRY...")
        cursor.execute("CREATE TABLE COUNTRY (Country_Name VARCHAR(20) NOT NULL, Population DECIMAL(10,2), No_of_Worldcup_won INT, Manager VARCHAR(20), PRIMARY KEY (Country_Name));")
        print("Table COUNTRY created..")
        for i, row in file_country.iterrows():
            cursor.execute(f"INSERT INTO COUNTRY VALUES ({row[0]},{row[1]},{row[2]},{row[3]});")
            print("value for country inserted")
            connet.commit()
        print("Creating table PLAYERS...")
        cursor.execute("CREATE TABLE PLAYERS (Player_id INT NOT NULL,  Name VARCHAR(40), Fname VARCHAR(20), Lname VARCHAR(35), DOB DATE NOT NULL, Country VARCHAR(20), Height_cms INT, Club VARCHAR(30), Position VARCHAR(15), Caps_for_Country INT, IS_CAPTAIN BOOLEAN, PRIMARY KEY( Player_id), FOREIGN KEY (Country) REFERENCES COUNTRY(Country_Name) ON DELETE CASCADE ON UPDATE CASCADE);")
        print("Table PLAYERS created..")
        for i, row in file_players.iterrows():
            cursor.execute(f"INSERT INTO PLAYERS VALUES ({row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]},{row[8]},{row[9]},{row[10]});")
            print("value for players inserted")
            connet.commit()
        print("Creating table MATCH_RESULTS...")
        cursor.execute("CREATE TABLE MATCH_RESULTS ( Match_id INT NOT NULL, Date_of_Match DATE, Start_Time_Of_Match TIME, Team1 VARCHAR(20), Team2 VARCHAR(20), Team1_score INT, Team2_score INT, Stadium_Name VARCHAR(35), Hosty_City VARCHAR(20), PRIMARY KEY (Match_id), FOREIGN KEY (Team1) REFERENCES COUNTRY ( Country_Name) ON DELETE CASCADE ON UPDATE CASCADE, FOREIGN KEY (Team2) REFERENCES COUNTRY ( Country_Name) ON DELETE CASCADE ON UPDATE CASCADE);")
        print("Table MATCH_RESULTS created..")
        for i, row in file_match_results.iterrows():
            cursor.execute(f"INSERT INTO MATCH_RESULTS VALUES ({row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]},{row[8]});")
            print("value for match_results inserted")
            connet.commit()
        print("Creating table PLAYER_CARDS...")
        cursor.execute("CREATE TABLE PLAYER_CARDS ( Player_id INT NOT NULL, Yellow_Cards INT, Red_Cards INT, PRIMARY KEY ( Player_id),FOREIGN KEY (Player_id) REFERENCES PLAYERS(Player_id) ON DELETE CASCADE ON UPDATE CASCADE);")
        print("Table PLAYER_CARDS created..")
        for i, row in file_player_cards.iterrows():
            cursor.execute(f"INSERT INTO PLAYER_CARDS VALUES ({row[0]},{row[1]},{row[2]});")
            print("value for player_cards inserted")
            connet.commit()
        print("Creating table PLAYER_ASSISTS_GOALS...")
        cursor.execute("CREATE TABLE PLAYER_ASSISTS_GOALS ( Player_id INT NOT NULL, No_of_Matches INT, Goals INT, Assists INT, Minutes_Played INT, PRIMARY KEY (Player_id), FOREIGN KEY (Player_id) REFERENCES PLAYERS(Player_id) ON DELETE CASCADE ON UPDATE CASCADE);")
        print("Table PLAYER_ASSISTS_GOALS created..")
        for i, row in file_player_assists_goals.iterrows():
            cursor.execute(f"INSERT INTO PLAYER_ASSISTS_GOALS VALUES ({row[0]},{row[1]},{row[2]},{row[3]},{row[4]});")
            print("value for player_assists_goals inserted")
            connet.commit()

except Error as err:
    print("Error while connecting to mysql",err)
