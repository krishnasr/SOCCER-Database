
CREATE TABLE COUNTRY (Country_Name VARCHAR(20) NOT NULL, 
			Population DECIMAL(10,2), 
 			No_of_Worldcup_won INT, 
			Manager VARCHAR(20), 
			PRIMARY KEY (Country_Name));



CREATE TABLE PLAYERS (Player_id INT NOT NULL,  
			Name VARCHAR(40), 
			Fname VARCHAR(20), 
			Lname VARCHAR(35), 
			DOB DATE, 
			Country VARCHAR(20), 
			Height_cms INT, 
			Club VARCHAR(30), 
			Position VARCHAR(10), 
			Caps_for_Country INT, 
			IS_CAPTAIN BOOLEAN, 
			PRIMARY KEY( Player_id), 
			FOREIGN KEY (Country) REFERENCES COUNTRY(Country_Name) ON DELETE CASCADE ON UPDATE CASCADE);


CREATE TABLE MATCH_RESULTS ( Match_id INT NOT NULL, 
				Date_of_Match DATE, 
				Start_Time_Of_Match TIME, 
				Team1 VARCHAR(20), 
				Team2 VARCHAR(20), 
				Team1_score INT, 
 				Team2_score INT, 
				Stadium_Name VARCHAR(35), 
				Hosty_City VARCHAR(20), 
				PRIMARY KEY (Match_id), 
				FOREIGN KEY (Team1) REFERENCES COUNTRY ( Country_Name) ON DELETE CASCADE ON UPDATE CASCADE, 
				FOREIGN KEY (Team2) REFERENCES COUNTRY ( Country_Name) ON DELETE CASCADE ON UPDATE CASCADE);


CREATE TABLE PLAYER_CARDS ( Player_id INT NOT NULL, 
				Yellow_Cards INT, 
				Red_Cards INT, 
				PRIMARY KEY ( Player_id),
				FOREIGN KEY (Player_id) REFERENCES PLAYERS(Player_id) ON DELETE CASCADE ON UPDATE CASCADE);


CREATE TABLE PLAYER_ASSISTS_GOALS ( Player_id INT NOT NULL, 
					No_of_Matches INT, 
					Goals INT, 
					Assists INT, 
					Minutes_Played INT, 
					PRIMARY KEY (Player_id), 
					FOREIGN KEY (Player_id) REFERENCES PLAYERS(Player_id) ON DELETE CASCADE ON UPDATE CASCADE);
			