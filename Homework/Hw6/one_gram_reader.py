
'''
    This program is a module that reads csv files that contain data about English words over time.
    Author: Hoang Nhat Minh (220027) & Nguyen Chinh Quan (220066)
    Time: ~45 minutes
'''
import csv


# Read data about the given word over time csv file and return the years and count the count of the occurrence of the word.
def read_wfile(word, year_range, wfile):
    """ 
    Description: Read in the wfile provided and return two lists representing the counts and years for the word provided.
    Parameters:
        word: A string containing only upper and lower case letters
        year_range: A list of exactly two numbers. These specify the date range.
        wfile: A string giving the name of a one gram csv file
    Returns: 
        lstYears: List of all years that the word was used
        lstCounts: List of the word count during each year that the word appeared
    """
    with open(wfile, 'r') as file:
        data = csv.reader(file)
        lstYears = []
        lstCounts = []
        for row in data:
            rowData = row[0].split('\t')
            if (rowData[0] == word) & (int(rowData[1]) in range(year_range[0], year_range[1] + 1)):
                lstCounts.append(int(rowData[2]))
                lstYears.append(int(rowData[1]))
    return lstYears, lstCounts

# Read the total count of words in a given csv file.
def read_total_counts(tfile):
    """ 
    Description: Read in the tfile provided and return a dictionary of total word counts.
    Parameters:
        tfile: A string giving the filename of the total word counts file.
    Returns: 
        mapTotal_counts: dictionary of counts during each year
    """
    with open(tfile, 'r') as file:
        data = csv.reader(file)
        mapTotal_counts = {}
        for row in data:
            mapTotal_counts[int(row[0])] = int(row[1])
    return mapTotal_counts

if __name__ == "__main__":
    # years, counts = read_wfile('request', [2005, 2007], 'very_short.csv')
    # print(years, counts)
    total_counts = read_total_counts("total_counts.csv")
    print(total_counts[1525])
