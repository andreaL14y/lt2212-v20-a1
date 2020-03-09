# LT2212 V20 Assignment 1

This program deals with the manipulation of textual data, especially within the structure of dataframes. 

First some helper functions are implemented. 
1. get_files to extract all files within two input folders
2. get_words creates a list of words occuring in the input file
3. get_word_couns takes a list of words and creates a dictionary containing a list of unique words and their number of occurances in the initial list

#### Part 1: The function takes two folders and an integer as input and creates a dataframe. The multiindex consists of the article/file name of every file in the input folders and the folder where it was found. 
For each word occuring at least once in any text a column is created. The integer value in cell C_ij derives the total occurence of word j in article i.

#### Part 2: The 10 most used words (in total) of the dataframe from part 1 are taken. A bar chart is created that illustrates how often the each word is used within each of the input folders.

#### Part 3: The values within the cells of the dataframe of Part 1 are transformed via the raw count version of term frequency. The function creates a new dataframe out of the dataframe from part 1.

#### Part 4: As in part 2 the output of part 3 is illustrated. The tf-idf transformation of the Dataframe values squeezes down the value of very frequent used words such that the weight of words, which do not mediate any content but are naturally often used (such as articles 'a'/'the' or propositions 'in') are considered less "important" while rarer words get an higher weight. 
This allows (more likely) to get the most important words considering the content of the articles. 
As it can be seen in the second plot there is still appearing words like 'the' due to its very high fequency (however on 3rd not on first place) but also words like 'min', 'oil' or 'tonnes', that allow conclusions/suggestions about the topics of the articles. 
