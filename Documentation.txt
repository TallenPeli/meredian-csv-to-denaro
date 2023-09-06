----------------------------------------------------------------------------------
5 Groups:

Format : GROUPID;GROUPNAME;GROUPDESCRIPTION

1, 5;School Savings;Money saved for education (20%)
2, 2;Savings;Money that is saved for large purchases (15%)
3, 1;Free Spend;Money that I can freely spend (40%)
4, 3;Tithe;Money to donate (10%)
5, 4;Insurance;Money set aside for insurance (15%)
----------------------------------------------------------------------------------
Format (Readable): 

ID;M/D/YYYY;Name;Type;RepeatInterval;RepeatFrom;RepeatEndDate;Amount;RGBA;UseGroupColor;GroupID;GroupName;GroupDescription;GroupRGBA;Tags
----------------------------------------------------------------------------------
ID :
The Number of the transaction. This goes up by one every time

M/D/YYYY :
Month (one digit unless 2 required), Day (one digit unless 2 required), Year (YYYY)

Name :
Name of the transaction.

Type :
0 - income
1 - expense

RepeatInterval :
0 - Never
1 - Daily
2 - Weekly
7 - Biweekly
3 - Monthly
4 - Quarterly
5 - Yearly
6 - Biyearly

RepeatFrom :
Should be either an Id of source transaction or 0 if it's a source transaction or -1 if it's not repeat transaction.

RepeatEndDate : 
End date for repeat transaction, should be in English (US) format (MM/DD/YYYY). Leave it empty if it's not repeat transaction.

Amount : 
Transaction amount in English (US) format (123,456.78).

RGBA :
Transaction color, should be in rgb(R,G,B) format where R, G and B are integers in range between 0 and 255.

UseGroupColor : 
Whether a transaction should use group color: 0 — false, 1 — true.

GroupID :
Transaction's group Id. Ids start with 1. For ungrouped transaction it should be -1 (not 0, this is incorrect value for group Id).

GroupName :
Transaction's group name, should match group Id. It can contain any characters except semicolon. Leave it empty for ungrouped transaction, in any other cases it shouldn't be empty.

GroupDescription :
Transaction's group description, should match group Id. It can contain any characters except semicolon and can be empty. Leave it empty for ungrouped transaction.

GroupRGBA :
Group color, should be in rgb(R,G,B) format where R, G and B are integers in range between 0 and 255.

Tags :
Information about the transaction.

----------------------------------------------------------------------------------
