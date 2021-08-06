CREATE TABLE myData (
	fullName text,
	email text,
	slackUsername text,
	biostack text,
-- project update
	twitterHandle text,
	hammingDist int);

INSERT INTO myData 
VALUES ('Abdulafiz Musa', 'musaabdulafiz@gmail.com', '@Abdulafiz', 'Data science', '@Abdulafiz_O', 0);

SELECT CONCAT(fullName, ',', email, ',', slackUsername,',', biostack, ',', twitterHandle, ',', hammingDist)
	AS 	"myDetails" FROM myData

