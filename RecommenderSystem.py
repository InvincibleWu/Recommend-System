import pandas as pd
import numpy as np
import operator
import datetime
from sklearn.metrics import mean_squared_error
import warnings

class Recommender_System:
    # base_name = ''
    # test_name = ''
    # user_num = 943
    # movie_num = 1682
    # rating_matrix = np.zeros((movie_num,user_num))
    # base_data = None
    # test_data = None
    # similarity_movie = None
    # mean_of_movie = []
    # mean_of_user = []
    # mean_of_user_movie = 0
    # k_similarity = 0
    
    def __init__(self, base_path, test_path, k):
        self.user_num = 943
        self.movie_num = 1682
        self.rating_matrix = np.zeros((self.movie_num,self.user_num))
        self.k_similarity = k
        self.base_name = base_path
        self.test_name = test_path
        # read data into dataframe
        r_cols = ['userId', 'movieId', 'rating', 'timestamp']
        # print('load base data')
        self.base_data = pd.read_csv(self.base_name, sep='\t', names=r_cols, encoding='latin-1')
        # print('load test data')
        self.test_data = pd.read_csv(self.test_name, sep='\t', names=r_cols, encoding='latin-1')
        # transform into rating CF table
        # rating_matrix = np.zeros(( max(base_data.movieId), base_data.userId.unique().shape[0]))
        for row in self.base_data.itertuples():
            self.rating_matrix[row[2]-1, row[1]-1] = row[3]
        self.similarity_movie = self.rating_matrix.dot(self.rating_matrix.T) + 1e-9
        norms = np.array([np.sqrt(np.diagonal(self.similarity_movie))])
        self.similarity_movie = ( self.similarity_movie / (norms * norms.T) )
        self.getMean()
    
    def calculate_rmse(self):
        warnings.filterwarnings('ignore')
        predict_dictionary = {}
        predict_results = []
        real_results = []
        # print('----start to testing----')
        # print(datetime.datetime.now())
        for row in self.test_data.itertuples():
            movie_id, user_id, real_value = row[2]-1, row[1]-1, row[3]
            real_results.append(real_value)
            predict_r = self.getRatingWithBaseline(user_id, movie_id, self.k_similarity)
            predict_results.append(predict_r)

        # print('----end of testing----')  
        # print(datetime.datetime.now())
        # print('rmse result is')
        # print(np.sqrt(mean_squared_error(np.array(predict_results), np.array(real_results))))
        output = np.sqrt(mean_squared_error(np.array(predict_results), np.array(real_results)))
        
        # print(items)
        # items.sort()
        # rand_list = [[key, value] for key, value in items]

        return output
 


    def getMean(self):
        
        #cal movie mean 
        self.mean_of_movie = self.rating_matrix.sum(1)/(self.rating_matrix != 0).sum(1)
        #cal user mean
        self.mean_of_user = self.rating_matrix.sum(0)/(self.rating_matrix != 0).sum(0)
        #cal all mean
        self.mean_of_user_movie = np.mean(self.rating_matrix[self.rating_matrix != 0])
        #replace nan into mean_of_user_movie
        self.mean_of_movie = np.where(np.isnan(self.mean_of_movie), self.mean_of_user_movie, self.mean_of_movie)
        self.mean_of_user = np.where(np.isnan(self.mean_of_user), self.mean_of_user_movie, self.mean_of_user)
           

    def getRatingWithBaseline(self, user_index, item_idx, topk):
        #get baseline matrix
        baseline = []
        baseline = self.mean_of_movie + self.mean_of_user[user_index] - self.mean_of_user_movie
        #get all movie index that current user has alread rated
        nonzero_item_idx = np.nonzero(self.rating_matrix.T[user_index])[0]
        #find top k similar movies
        temp_topk = {}
        for n0 in nonzero_item_idx:
            temp_topk[n0] = self.similarity_movie[item_idx, n0]
        sorted_topk_results = sorted(temp_topk.items(), key=operator.itemgetter(1), reverse=True)[:topk]
        topk_idx = []
        for t1,t2 in sorted_topk_results:
            topk_idx.append(t1)
            
        predict_results = (self.rating_matrix[topk_idx,user_index] - \
                           baseline[topk_idx]).dot(self.similarity_movie[item_idx, topk_idx])\
                    / sum(self.similarity_movie[item_idx, topk_idx]) + baseline[item_idx] 
        if predict_results > 5: predict_results = 5
        if predict_results < 1: predict_results = 1
        # item_with_predict = {item_idx:predict_results}
        return predict_results

    def getRatingOfUserUser(self, user_index, item_idx, topk):
        #get baseline matrix
        baseline = []
        baseline = self.mean_of_user + self.mean_of_movie[user_index] - self.mean_of_user_movie
        #get all movie index that current user has alread rated
        nonzero_item_idx = np.nonzero(self.rating_matrix[item_idx])[0]
        #find top k similar movies
        temp_topk = {}
        for n0 in nonzero_item_idx:
            temp_topk[n0] = self.similarity_movie[n0, user_index]
        sorted_topk_results = sorted(temp_topk.items(), key=operator.itemgetter(1), reverse=True)[:topk]
        topk_idx = []
        for t1,t2 in sorted_topk_results:
            topk_idx.append(t1)

        predict_results = (self.rating_matrix[item_idx,topk_idx] - \
                           baseline[topk_idx]).dot(self.similarity_movie[topk_idx, user_index])\
                    / sum(self.similarity_movie[topk_idx, user_index]) + baseline[user_index] 
        if predict_results > 5: predict_results = 5
        if predict_results < 1: predict_results = 1
        if np.isnan(predict_results): predict_results = baseline[user_index]    
        return predict_results
        
    def calculate_user_user_rmse(self):
            warnings.filterwarnings('ignore')
            predict_dictionary = {}
            predict_results = []
            real_results = []
            # print('----start to testing----')
            # print(datetime.datetime.now())
            for row in self.test_data.itertuples():
                movie_id, user_id, real_value = row[2]-1, row[1]-1, row[3]
                real_results.append(real_value)
                predict_r = self.getRatingOfUserUser(user_id, movie_id, self.k_similarity)
                predict_results.append(predict_r)

            output = np.sqrt(mean_squared_error(np.array(predict_results), np.array(real_results)))
            
            return output    
        
    def getRatingOfNaiveCF(self, user_index, item_idx, topk):
        #get baseline matrix
        #baseline = []
        #baseline = self.mean_of_movie + self.mean_of_user[user_index] - self.mean_of_user_movie
        #get all movie index that current user has alread rated
        nonzero_item_idx = np.nonzero(self.rating_matrix.T[user_index])[0]
        #find top k similar movies
        temp_topk = {}
        for n0 in nonzero_item_idx:
            temp_topk[n0] = self.similarity_movie[item_idx, n0]
        sorted_topk_results = sorted(temp_topk.items(), key=operator.itemgetter(1), reverse=True)[:topk]
        topk_idx = []
        for t1,t2 in sorted_topk_results:
            topk_idx.append(t1)

        predict_results = (self.rating_matrix[topk_idx,user_index]  \
                          ).dot(self.similarity_movie[item_idx, topk_idx])\
                    / sum(self.similarity_movie[item_idx, topk_idx])
        #if predict_results > 5: predict_results = 5
        #if predict_results < 1: predict_results = 1
        # item_with_predict = {item_idx:predict_results}
        return predict_results
        
    def calculate_NaiveCF_rmse(self):
            warnings.filterwarnings('ignore')
            predict_dictionary = {}
            predict_results = []
            real_results = []
            # print('----start to testing----')
            # print(datetime.datetime.now())
            for row in self.test_data.itertuples():
                movie_id, user_id, real_value = row[2]-1, row[1]-1, row[3]
                real_results.append(real_value)
                predict_r = self.getRatingOfNaiveCF(user_id, movie_id, self.k_similarity)
                predict_results.append(predict_r)

            output = np.sqrt(mean_squared_error(np.array(predict_results), np.array(real_results)))
            
            return output    
    def get_unseen_movieID_list(self, uid):
        movie_id_list = [i for i in range(1, 1683)]
        for row in self.base_data.itertuples():
            if row[1] == uid:
                movie_id_list.remove(row[2])
        return movie_id_list

    def recommend_top_k_movies(self, user_id, k):
        warnings.filterwarnings('ignore')
        
        
        unseen_list = self.get_unseen_movieID_list(user_id)
        predict_dictionary = {}
        for movie_id in unseen_list:
            try:
                predict_r = self.getRatingWithBaseline(user_id, movie_id, 20)
                predict_dictionary.update({movie_id:predict_r})
            except Exception:
                continue
        items=predict_dictionary.items()

        sortitems = [[v[1],v[0]] for v in items]

        sortitems.sort(reverse = True)

        sortitems = sortitems[:k]

        name_dict = {}
        f = pd.read_csv('ml-100k/u.item', sep='|', encoding='latin-1')
        for line in f.itertuples():
            name_dict.update({line[1]: line[2]})
        for item in sortitems:
            item.append(name_dict[item[1]])
        sortitems = [[v[1], v[0], v[2]] for v in sortitems]
        print('Movie ID\tMovie Rate (predict)\tMovie Name')
        for line in sortitems:
            print(line[0], '\t\t', round(line[1], 3), '\t\t\t', line[2])
        return sortitems

