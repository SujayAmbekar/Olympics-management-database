drop database olympics;
create database olympics;

\c olympics


CREATE TABLE Country
 (	Name VARCHAR(15) NOT NULL,
	CountryID CHAR(5) NOT NULL, 
	NumberOfParticipants INT NOT NULL,
	Population VARCHAR(30),
	Representative VARCHAR(30) NOT NULL,
	PRIMARY KEY (CountryID)
 );


CREATE TABLE Athlete
 (	FirstName VARCHAR(15) NOT NULL,
	LastName VARCHAR(15) NOT NULL,
	PlayerID CHAR(6) NOT NULL, 
	Gender CHAR(1) NOT NULL,
	Age INT NOT NULL,
	Height DECIMAL NOT NULL,
	Weight DECIMAL NOT NULL,
	PassportNo INT NOT NULL,
	PRIMARY KEY (PlayerID)
 );

CREATE TABLE Sport
 (	SportName VARCHAR(20) NOT NULL UNIQUE,
	SportID CHAR(5) NOT NULL, 	
	TypeOfSport VARCHAR(10),
	PRIMARY KEY (SportID)
 );

CREATE TABLE SportActivity
 (	SportName VARCHAR(20) NOT NULL,
	ActivityNo INT NOT NULL, 	
	NumberOfParticipants INT NOT NULL,
	PRIMARY KEY (ActivityNo),
	FOREIGN KEY (SportName) REFERENCES Sport(SportName) 
 );

CREATE TABLE Schedule
 (	SportName VARCHAR(20) NOT NULL,
	SportID CHAR(5) NOT NULL, 	
	Duration DECIMAL NOT NULL,
	Date DATE NOT NULL,
	StartTime TIME NOT NULL,
	EndTime TIME NOT NULL,
	PRIMARY KEY (SportID),	
	FOREIGN KEY (SportName) REFERENCES Sport(SportName)
 );

CREATE TABLE Facility
 (	Name VARCHAR(20) NOT NULL,
	FacilityID CHAR(5) NOT NULL, 	
	Location VARCHAR(20) NOT NULL,
	Capacity INT NOT NULL,
	PRIMARY KEY (FacilityID)	
 );

CREATE TABLE Transportation
 (	Type VARCHAR(10) NOT NULL,
	FacilityID CHAR(5) NOT NULL, 
	TransportID CHAR(5) NOT NULL, 		
	Capacity INT NOT NULL,
	PRIMARY KEY (TransportID),
	FOREIGN KEY (FacilityID) REFERENCES Facility(FacilityID)	
 );

CREATE TABLE SupportStaff
 (	Name VARCHAR(20) NOT NULL,			
	StaffID CHAR(5) NOT NULL,
	Gender CHAR(1) NOT NULL,
	Role VARCHAR(20) NOT NULL, 
	PRIMARY KEY (StaffID)	
 );

CREATE TABLE Coach
 (	FirstName VARCHAR(15) NOT NULL,
	LastName VARCHAR(15) NOT NULL,	
	CoachID CHAR(5) NOT NULL,
	Gender CHAR(1) NOT NULL,
	PlayerID VARCHAR(6) NOT NULL, 
	Sport VARCHAR(20) NOT NULL,
	PassportNo INT NOT NULL,
	PRIMARY KEY (CoachID),
	FOREIGN KEY (PlayerID) REFERENCES Athlete(PlayerID),
	FOREIGN KEY (Sport) REFERENCES Sport(SportName) 	
 );

CREATE TABLE OlympicEvent
 (	CountryName VARCHAR(15) NOT NULL,
	Year INT NOT NULL,
	Season VARCHAR(6) NOT NULL,
	City VARCHAR(10) NOT NULL, 
	State VARCHAR(10) NOT NULL,
	PRIMARY KEY (CountryName)	
 );

CREATE TABLE Win
 (	SportID CHAR(5) NOT NULL,
	PlayerID CHAR(6) NOT NULL,	
	Medal VARCHAR(6) NOT NULL,
	PRIMARY KEY (SportID,PlayerID),
	FOREIGN KEY (PlayerID) REFERENCES Athlete(PlayerID), 
	FOREIGN KEY (SportID) REFERENCES Sport(SportID)
 );

CREATE TABLE Participates
 (	ActivityNo INT NOT NULL,
	PlayerID CHAR(6) NOT NULL,	
	Rank INT NOT NULL,
	Result VARCHAR(6),
	PRIMARY KEY (PlayerID,ActivityNo),
	FOREIGN KEY (PlayerID) REFERENCES Athlete(PlayerID),
	FOREIGN KEY (ActivityNo) REFERENCES SportActivity(ActivityNo) 
 );


CREATE TABLE is_Scheduled
 (	Time TIME NOT NULL,
	Date DATE NOT NULL,	
	FacilityID CHAR(5) NOT NULL,
	TransportID CHAR(5) NOT NULL,
	PRIMARY KEY (FacilityID,TransportID),
	FOREIGN KEY (TransportID) REFERENCES Transportation(TransportID) 
 );

CREATE TABLE PhoneNo
 (	StaffID CHAR(5) NOT NULL,
	Phone BIGINT NOT NULL,	
	PRIMARY KEY (StaffID,Phone),
	FOREIGN KEY (StaffID) REFERENCES SupportStaff(StaffID) 
 );
