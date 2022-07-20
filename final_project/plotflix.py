import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/netflix_clean.csv')

# verify dataframe is as expected
print(data.info())

# create a class with multiple data viz functions for later use
class plotflix:
    """ A class to generate various visualizations using the exported clean Netflix dataset. """
    # initialize the class with the x and y axes used in the visualizations
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def barplot(x, height):
        # create bar plot
        plt.bar(x, height)
        # adjust x axis label for clarity
        plt.xticks(rotation=90)
        # display created viz
        plot = plt.show()

        return plot

    def lineplot(x, y):
        # create line plot
        plt.plot(x, y)
        # display created viz
        plot = plt.show()

        return plot


# define a main function to test class attributes in plotflix
def main():
    # group data by ratings and type of content
    grouped_ratings = data.groupby(['type', 'rating']).size().reset_index(name='count')
            
    # number of titles by rating
    plotflix.barplot(x=grouped_ratings['rating'], height=grouped_ratings['count'])

    # group data by release year and content type
    temp = data.groupby(['release_year']).size().reset_index(name='count')
    # Content type frequency by content type
    plotflix.lineplot(x=temp['release_year'], y=temp['count'])

main()
