# LT2212 V20 Assignment 1

Unfortunately the program I wrote is not compareable with the required structure as I defined the Dataframes of PART 1 and 3 globally and used its multiindex-structure for the plots. 
As I don't know how strict the deadline is and I was not able to adjust everything in time I just uploaded this version and hope that I'll have the chance to formulate the tasks as function within the next days. 

Considering the question of PART 4: 
The tf-idf transformation of the Dataframe values squeezes down the value of very frequent used words such that the weight of words, which do not mediate any content but are naturally often used (such as articles 'a'/'the' or propositions 'in') are considered less "important" while rarer words get an higher weight. 
This allows (more likely) to get the most important words considering the topics of the articles. 
As it can be seen in the second plot there is still appearing words like 'the' due to its very high fequency (however on 3rd not on first place) but also words like 'min', 'oil' or 'tonnes', that allow conclusions/suggestions about the topics of the articles. 
