import pickle
import ItemItemCollaborativeFiltering as icf
import ItemItemCollaborativeFiltering as icf
import findWeight
import get_features_by_movie_id as gf
import numpy as np
from sklearn import linear_model as lm
import pandas as pd

icf1 = icf.ItemItemCollaborativeFiltering('ml-100k/u1.base','ml-100k/u.user','ml-100k/u.item')
data = pickle.load(open('ml-100k-split/movie_features.txt', 'rb'))

#*****************************************
#             content-based 
#*****************************************

##########################################
#             1.item profile
##########################################
def getItemProfile(movie_id,movies_features):
    return movies_features[movie_id]

def getAllItemProfile():
    movies_features = {}
    all_movies_features = pickle.load(open('ml-100k/movie_features.txt', 'rb'))
    for one_movie_feature in all_movies_features:
        movie_feature = []
        for f in one_movie_feature:
            if f != '|':
                movie_feature.append(f)
        movies_features[int(movie_feature[0])] =  movie_feature[1:]
    return movies_features
def findSimilarInArray(list1, list2):
    for l1 in list1:
        for l2 in list2:
            if l1 == l2:
                return 1
    return 0
def findSimilarMovies(movie_id,movies_features):
    similar_movies = {}
    high_similarity_movies = []
    item_profile = getItemProfile(movie_id,movies_features)
    for movieid in movies_features:
        similar_array = []
        if movieid != movie_id:
            rate = 0
            if item_profile[0] == movies_features[movieid][0]:
                similar_array.append(1)
                rate = rate + 1
            else:
                similar_array.append(0)
            if findSimilarInArray(item_profile[1], movies_features[movieid][1]) == 1:
                similar_array.append(1)
                rate = rate + 1
            else:
                similar_array.append(0)
            if findSimilarInArray(item_profile[2], movies_features[movieid][2]) == 1:
                similar_array.append(1)
                rate = rate + 1
            else:
                similar_array.append(0)
            if findSimilarInArray(item_profile[3], movies_features[movieid][3]) == 1:
                similar_array.append(1)
                rate = rate + 1
            else:
                similar_array.append(0)
            if findSimilarInArray(item_profile[4], movies_features[movieid][4]) == 1:
                similar_array.append(1)
                rate = rate + 1
            else:
                similar_array.append(0)
            if rate >= 3:
                high_similarity_movies.append(movieid)
            similar_array.append(rate)
        similar_movies[movieid] = similar_array
    return high_similarity_movies, similar_movies
#2.person profile
def intersectionLists(sLiked_movies):
    lists_map = {}
    dupli_list = []
    for ls in sLiked_movies:
        for l in ls:
            if l in lists_map:
                lists_map[l] = lists_map[l] + 1
            else:
                lists_map[l] = 1
    for i in lists_map:
        if lists_map[i] > 1:
            dupli_list.append(i)
    return dupli_list
            
    
def findLikedMoviesFeatures(user_id,movies_features):
    Liked_movies = icf1.getLikedMovie(user_id)
    sLiked_movies = []
    for liked_movie in Liked_movies:
        high_similarity_movies, similar_movies = findSimilarMovies(liked_movie+1,movies_features)
        sLiked_movies.append(high_similarity_movies)
    return intersectionLists(sLiked_movies)

def content_based_recommend(user_id):
    movies_features = getAllItemProfile()
    liked_movies_id = findLikedMoviesFeatures(user_id,movies_features)
    name_dict = {}
    f = pd.read_csv('ml-100k/u.item', sep='|', encoding='latin-1')
    for line in f.itertuples():
        name_dict.update({line[1]: line[2]})
    print('Movies recommend to user (content-based) :')
    print('****************************')
    for mid in liked_movies_id:
        print(name_dict[mid])
    print('****************************')