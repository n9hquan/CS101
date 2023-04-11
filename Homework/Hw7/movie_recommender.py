"""
This program contains one major function called recommend_movies() and 4 smaller functions in the major function.

Author: Nguyen Dac Minh Phu, Nguyen Chinh Quan
Time spent: 4 hours
"""
def recommend_movies():
    """
    Description: This function uses the user's preferences in choosing movies
                 to give new movie recommendations for the input user.
    Parameter: none
    Return:
        movies_recommended: a list of new movie recommendations
    """

    def find_data():
        """
        Description: This function gets the database of user recommendations
        by reading a given file named 'ratings.txt'.
        Parameter: none
        Return:
            ratings: the database of all users
        """
        
        with open("ratings.txt", 'r') as data:
            ratings = []
            for user in range(AMOUNT_OF_USERS):
                ratings.append({})
            for line in data:
                title = ""
                values = line.split()
                for i in range(1, len(values)-2):
                    title += values[i] + " "
                title = title + values[len(values)-2]
                ratings[int(values[0])][title] = int(values[-1])
            return ratings
    
    def define_preference_vector():
        """
        Description: This function computes the preference vector of the user who is going to be recommended.
        Parameter: none
        Return:
            preference_vector: a dictionary mapping strings (representing movie titles)
                               to integers (representing the user’s rating for that movie)
        """
        preference_vector = {}
    
        print("*** Welcome to the movie recommender engine ***")
        title = input("Please enter the title of a movie: ")
        while title != "":
            rating = input("Please enter your rating for the movie: ")
            if rating not in MOVIE_RATING:
                print("Sorry -- only permitted values are -5, -3, 1, 3, or 5.")
                rating = input("Please enter your rating for the movie: ")
            else:
                preference_vector[title] = int(rating)
            title = input("Please enter the title of a movie: ")
        return preference_vector

    def find_nearest_neighbor():
        """
        Description: This function finds the nearest neighbor of the user using the dot product.
        Parameter: none
        Return:
            nearest_neighbor: the nearest neighbor of the user
            dot_product_dict: a dictionary of the dot product
        """
        dot_product_dict = {}
        dot_product_list = []
        for user in range(len(ratings)):
            product = 0
            for movie in preference_vector:
                if movie in ratings[user]:
                    product += preference_vector[movie]*ratings[user][movie]
            dot_product_dict[user] = product
            dot_product_list.append(product)
        nearest_neighbor = max(dot_product_list)
        return nearest_neighbor, dot_product_dict

    def listing_recommendation():
        """
        Description: This function lists new movie recommendations for the user using the
                     given database of movie ratings, preference vector, and dot product.
        Parameter: none
        Return:
            movies_recommended: a list of new movie recommendations
        """
        movies_recommended = []
        user_id = []
        for user in dot_product_dict:
            if dot_product_dict[user] == nearest_neighbor:
                user_id.append(user)
        neighbor_id = min(user_id)
        for akey in ratings[neighbor_id]:
            if akey not in preference_vector and ratings[neighbor_id][akey] == 5:
                movies_recommended.append(akey)
        return movies_recommended

    try:
        AMOUNT_OF_USERS = 943
        MOVIE_RATING = {"-5": "Hated it", "-3": "Disliked it",
                                "1": "Meh", "3": "Liked it", "5": "Loved it"}
        ratings = find_data()
        preference_vector = define_preference_vector()
        nearest_neighbor, dot_product_dict = find_nearest_neighbor()
        movies_recommended = listing_recommendation()
        return movies_recommended
    except FileNotFoundError:
        return []
