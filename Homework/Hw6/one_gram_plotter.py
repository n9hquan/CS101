    This is a program that plot words data on a graph base on their relative frequency over time.
    Author: Hoang Nhat Minh (220027) & Nguyen Chinh Quan (220066)
    Time: ~45 minutes
'''

import matplotlib.pyplot as plt

import one_gram_reader


# Return normalized counts of a word by dividing the count from the total word count of each year
def normalize_counts(years, counts, total):
    """ 
    Description: Return the normalized word count.
    Parameters:
        years: A list of years, same as provided by one gram reader.read wfile
        counts: A list of counts, same as provided by one gram reader.read wfile
        total: A dictionary of counts during each year, same as provided by one_gram_reader.read_total_counts
    Returns: 
        lstNormalizedCounts: A normalized version of counts
    """
    lstNormalizedCounts = []
    for i in range(len(years)):
        lstNormalizedCounts.append(counts[i]/total[years[i]])
    return lstNormalizedCounts

# Plot the relative frequency of each word in the given words list
def plot_words(words, year_range, wfile, tfile):
    """ 
    Description: Plot the relative popularity of words over time.
    Parameters:
        words: A list of words
        year_range: A list of two integers
        wfile: Name of the word csv file
        tfile: Name of the totals csv file
    Returns: 
        Creates a plot figure.
    """
    fig = plt.figure()
    for word in words:
        years, counts = one_gram_reader.read_wfile(word, year_range, wfile)
        total = one_gram_reader.read_total_counts(tfile)
        normalized_counts = normalize_counts(years, counts, total)

        plt.plot(years, normalized_counts)
  
    plt.grid(visible=True, linestyle='dotted')
    plt.xlabel('Year')
    plt.ylabel('Relative frequency')
    plt.legend(words)
    plt.axis([year_range[0], year_range[1], 0, 0.00016])
    plt.show()

if __name__ == "__main__":
    # years, counts = one_gram_reader.read_wfile("request", [2000, 2010], "very_short.csv")
    # total = one_gram_reader.read_total_counts("total_counts.csv")
    # print(years)
    # first_observed_year = years[0]
    # print(first_observed_year)
    # print(counts[0])
    # print(total[first_observed_year])
    
    # normalized_counts = normalize_counts(years, counts, total)
    # print(normalized_counts[0])
    plot_words(["horse", "fish", "dog"], [1800, 2000], "all_words.csv", "total_counts.csv")
