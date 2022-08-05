\c olympics

INSERT into Country values('India',100,156,'1350Million','Neeraj');
INSERT into Country values('USA',101,201,'1150Million','Michael');
INSERT into Country values('China',102,176,'1550Million','Xiao');
INSERT into Country values('Japan',103,196,'150Million','Minamoto');
INSERT into Country values('SriLanka',104,190,'850Million','Kushal');
INSERT into Country values('SouthKorea',105,287,'900Million','Kim');
INSERT into Country values('HongKong',106,67,'50Million','Jong');
INSERT into Country values('Taiwan',107,42,'350Million','Jinping');
INSERT into Country values('Australia',108,125,'750Million','Imran');


INSERT into Athlete values('PV','Sindhu','100','F',25,170.3,57.5,98765);
INSERT into Athlete values('Neeraj','Chopra','101','M',23,180.5,67.5,98764);
INSERT into Athlete values('Lovlina','Borgohain','102','F',26,171.3,55.5,98763);
INSERT into Athlete values('Milka','Singh','103','M',45,180.3,67.5,98762);
INSERT into Athlete values('PT','Usha','104','F',28,176.3,53.5,98761);
INSERT into Athlete values('Ravi','Dahiya','105','M',32,167.3,71.5,98760);
INSERT into Athlete values('Sushil','Kumar','106','M',45,187.3,77.3,98759);
INSERT into Athlete values('Suchith','Shankar','107','M',31,177.9,59.8,98758);
INSERT into Athlete values('Aarav','Bindra','108','M',30,167.9,59.8,98757);
INSERT into Athlete values('Virat','Singh','109','M',39,178.9,59.8,98756);
INSERT into Athlete values('Neerav','Paswan','110','M',29,179.9,59.8,98755);


INSERT into Sport values('Badminton','10','Individual');
INSERT into Sport values('Cricket','11','Team');
INSERT into Sport values('Javelin','12','Individual');
INSERT into Sport values('Hockey','13','Team');
INSERT into Sport values('BasketBall','14','Team');
INSERT into Sport values('BaseBall','15','Team');
INSERT into Sport values('FootBall','16','Team');
INSERT into Sport values('Boxing','17','Individual');
INSERT into Sport values('Wrestling','18','Individual');
INSERT into Sport values('Golf','19','Individual');


INSERT into SportActivity values('Badminton',1,4);
INSERT into SportActivity values('Badminton',2,6);
INSERT into SportActivity values('Cricket',3,2);
INSERT into SportActivity values('Cricket',4,2);
INSERT into SportActivity values('Cricket',5,2);
INSERT into SportActivity values('Javelin',6,15);
INSERT into SportActivity values('Javelin',7,14);
INSERT into SportActivity values('Hockey',8,4);
INSERT into SportActivity values('BasketBall',9,5);
INSERT into SportActivity values('Wrestling',10,16);
INSERT into SportActivity values('Golf',11,20);


INSERT into Schedule values('Badminton',10,38.3,'2021-07-15','13:00:00','14:00:00');
INSERT into Schedule values('Javelin',12,30,'2021-07-14','12:00:00','13:00:00');
INSERT into Schedule values('Cricket',11,42,'2021-07-13','14:00:00','15:00:00');
INSERT into Schedule values('BasketBall',14,50,'2021-07-12','15:00:00','16:00:00');
INSERT into Schedule values('BaseBall',15,32,'2021-07-11','10:00:00','11:00:00');
INSERT into Schedule values('Hockey',13,100,'2021-07-10','13:00:00','14:00:00');
INSERT into Schedule values('Wrestling',18,38.3,'2021-07-09','10:00:00','11:00:00');
INSERT into Schedule values('Golf',19,45,'2021-07-08','09:00:00','10:00:00');
INSERT into Schedule values('FootBall',16,38,'2021-07-07','11:00:00','12:00:00');
INSERT into Schedule values('Boxing',17,15,'2021-07-06','13:00:00','14:00:00');


INSERT into Facility values('RedPlanet',200,'Tokyo',25);
INSERT into Facility values('Aman',201,'Hokaido',32);
INSERT into Facility values('HostelEast21',202,'Tokyo',56);
INSERT into Facility values('TokyoPrince',203,'Hokaido',16);
INSERT into Facility values('RoyalParkHotel',204,'Tokyo',87);
INSERT into Facility values('TokyoBay',205,'Tokyo',22);
INSERT into Facility values('SarkuraCross',206,'Hokaido',29);
INSERT into Facility values('TheGateHotel',207,'Tokyo',75);


INSERT into Transportation values('Bus',200,500,25);
INSERT into Transportation values('Car',201,501,32);
INSERT into Transportation values('Car',202,502,56);
INSERT into Transportation values('Bus',203,503,16);
INSERT into Transportation values('Taxi',204,504,87);
INSERT into Transportation values('Car',205,505,22);
INSERT into Transportation values('Taxi',206,506,29);
INSERT into Transportation values('Bus',207,507,75);


INSERT into SupportStaff values('Alex',600,'M','Physio');
INSERT into SupportStaff values('Theodore',601,'F','Host');
INSERT into SupportStaff values('Yamato',602,'M','Organiser');
INSERT into SupportStaff values('Joy',603,'M','Physio');
INSERT into SupportStaff values('Tabata',604,'M','Host');
INSERT into SupportStaff values('Inata',605,'F','Cameraman');
INSERT into SupportStaff values('Michael',606,'M','Commentator');
INSERT into SupportStaff values('Elizabeth',607,'F','Maintainence');


INSERT into Coach values('Chaitanya','Sharma',700,'M',100,'Badminton',12340);
INSERT into Coach values('Tarpan','Roy',701,'M',101,'Javelin',12341);
INSERT into Coach values('Hemanth','Hegde',702,'M',102,'Boxing',12342);
INSERT into Coach values('Lohith','Kumar',703,'M',103,'Hockey',12343);
INSERT into Coach values('Nihal','Jadhav',704,'M',104,'BaseBall',12344);
INSERT into Coach values('Pranjal','Kumar',705,'M',105,'Wrestling',12345);
INSERT into Coach values('Deepti','Yadav',706,'F',106,'Golf',12346);
INSERT into Coach values('Divya','Sharma',707,'F',107,'FootBall',12347);
INSERT into Coach values('Anjali','Kumar',708,'F',108,'BasketBall',12348);

INSERT into OlympicEvent values('Japan',2021,'Summer','Tokyo','Kanto');

INSERT into Win values(10,100,'Silver');
INSERT into Win values(11,101,'Gold');
INSERT into Win values(12,102,'Bronze');
INSERT into Win values(13,103,'Silver');
INSERT into Win values(14,104,'Bronze');
INSERT into Win values(15,105,'Bronze');
INSERT into Win values(16,106,'Gold');


INSERT into Participates values(1,100,2,'Won');
INSERT into Participates values(2,101,1,'Won');
INSERT into Participates values(3,102,3,'Won');
INSERT into Participates values(4,103,2,'Won');
INSERT into Participates values(5,104,3,'Won');
INSERT into Participates values(6,105,3,'Won');
INSERT into Participates values(7,106,1,'Won');
INSERT into Participates values(8,107,0,'Lost');
INSERT into Participates values(9,108,0,'Lost');
INSERT into Participates values(10,109,0,'Lost');

INSERT into is_Scheduled values('13:00:00','2021-07-12',200,500);
INSERT into is_Scheduled values('12:00:00','2021-07-11',201,501);
INSERT into is_Scheduled values('11:00:00','2021-07-12',202,502);
INSERT into is_Scheduled values('10:00:00','2021-07-11',203,503);
INSERT into is_Scheduled values('09:00:00','2021-07-10',204,504);
INSERT into is_Scheduled values('11:00:00','2021-07-13',205,505);
INSERT into is_Scheduled values('12:00:00','2021-07-14',206,506);
INSERT into is_Scheduled values('13:00:00','2021-07-11',207,507);


INSERT into PhoneNo values(600,987654321);
INSERT into PhoneNo values(601,987654320);
INSERT into PhoneNo values(602,987654322);
INSERT into PhoneNo values(603,987654323);
INSERT into PhoneNo values(604,987654324);
INSERT into PhoneNo values(605,987654325);
INSERT into PhoneNo values(606,987654326);
INSERT into PhoneNo values(607,987654327);
