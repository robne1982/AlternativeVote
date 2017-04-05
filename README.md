Very basic code to calculate the results of an AV vote. 

## Input

Please supply a csv file that looks like 

|VoteChoice|PersonA|PersonB|PersonC|
| --- |--- |--- |--- |
|DonaldTrump|2|3||
|Obama|1||1|
|GeorgeBush|3|2||
|DavidCameron|4||2|
|TonyBlair|5|1||

At the moment you need to save this somewhere and then change the hardcoded file path on line 4 the python code.

## Usage

Run the python code. Out is written to the console.

## Output

```
============================================================================================
Before round 1 there are 5 candidates 
 and we have 3 goats voting
============================================================================================
============================================================================================
 ROUND 1
 --------------------------------
The votes are 
DonaldTrump : 0
Obama : 2
GeorgeBush : 0
DavidCameron : 0
TonyBlair : 1
 --------------------------------
Therefore there are 3 removals
DonaldTrump
GeorgeBush
DavidCameron
 --------------------------------
The new vote list is as follows
['Obama', 1, '', '1']
['TonyBlair', '5', 1, '']
 --------------------------------
============================================================================================
 ROUND 2
 --------------------------------
The votes are 
Obama : 2
TonyBlair : 1
 --------------------------------
Therefore there are 1 removals
TonyBlair
 --------------------------------
The new vote list is as follows
['Obama', 1, '', '1']
 --------------------------------
============================================================================================
 The winner is declared : Obama
============================================================================================
```
