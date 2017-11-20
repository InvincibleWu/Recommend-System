# Recommend-System

This program contains two recommender ststem:
1. ItemCF-BaseLine Recommender System: improve item-item collaborative filtering model by adding a baseline
2. Content-based Recommender System: extract movies who has similiar features with the user like's
And also some evaluation programs.

# Dataset
* use ml-100k from MovieLen (older dataset)
* u1 to u5 are training and testing data for random cases from u.data
* ua and ub are training and testing data for few information

# Run 
To run this program, need to load training and testing dataset first by using following commands:
>>cd files/ml-100k 
	or cd ml-100k (if you already in "/files" directory)
>>chmod +x allbut.pl
>>chmod +x mku.sh
>>./mku.sh

After run mku.sh, all test datasets we need will appear in the files/ml-100k directory.



# Part I ItemCF-BaseLine Recommender System
1. RecommenderSystem.py
	* main program of implementation Recommender system

	Example for Recommender:
		# perform Recommender system to recommend 10 movies for user 5
		run code:
		import RecommenderSystem as R
		example = R.Recommender_System('ml-100k/u1.base', 'ml-100k/u1.test', 20)
		example.recommend_top_k_movies(5, 10)

2. evaluation.py
	* use to test the accuracy of the result
	* 6 function for testing:

	test_for_user_user_u1_to_u5(k1, k2, txt_output_path, png_output_path)
	test_for_user_user_uaub(k1, k2, txt_output_path, png_output_path)
	test_for_NaiveCF_u1_to_u5(k1, k2, txt_output_path, png_output_path)
	test_for_NaiveCF_uaub(k1, k2, txt_output_path, png_output_path)
	test_for_item_item_u1_to_u5(k1, k2, txt_output_path, png_output_path)
	test_for_item_item_uaub(k1, k2, txt_output_path, png_output_path)

	where k1 and k2 are the range for value of k pass to calculate the similarity.
	txt_output_path, png_output_path are the output file path

  2.1 Evaluating User-User Collaborative Filtering
	  * for dataset u1 to u5:
		  run code:
			  import evaluation
			  evaluation.test_for_user_user_u1_to_u5(10, 30, 'results/test_for_useruser_u1u5.txt', 'results/test_for_useruser_u1u5.png')
		  result files:
			  results/test_for_useruser_u1u5.txt
			  results/test_for_useruser_u1u5.png
	* for dataset ua and ub:
		run code:
			import evaluation
			evaluation.test_for_user_user_uaub(10, 30, 'results/test_for_useruser_uaub.txt', 'results/test_for_useruser_uaub.png')
		result files:
			results/test_for_useruser_uaub.txt
			results/test_for_useruser_uaub.png

2.2 Evaluating Naive Item-Item Collaborative Filtering
	* for dataset u1 to u5:
		run code:
			import evaluation
			evaluation.test_for_NaiveCF_u1_to_u5(10, 30, 'results/test_for_naive_u1u5.txt', 'results/test_for_naive_u1u5.png')
		result files:
			results/test_for_naive_u1u5.txt
			results/test_for_naive_u1u5.png
	* for dataset ua and ub:
		run code:
			import evaluation
			evaluation.test_for_NaiveCF_uaub(10, 30, 'results/test_for_naive_uaub.txt', 'results/test_for_naive_uaub.png')
		result files:
			results/test_for_naive_uaub.txt
			results/test_for_naive_uaub.png
	
2.3 Evaluating Item-Item Collaborative Filtering with BaseLine (Our Final System)
	* for dataset u1 to u5:
		run code:
			import evaluation
			evaluation.test_for_item_item_u1_to_u5(10, 30, 'results/test_for_itembaseline_u1u5.txt', 'results/test_for_itembaseline_u1u5.png')
		result files:
			results/test_for_itembaseline_u1u5.txt
			results/test_for_itembaseline_u1u5.png
	* for dataset ua and ub:
		run code:
			import evaluation
			evaluation.test_for_item_item_uaub(10, 30, 'results/test_for_itembaseline_uaub.txt', 'results/test_for_itembaseline_uaub.png')
		result files:
			results/test_for_itembaseline_uaub.txt
			results/test_for_itembaseline_uaub.png
	


# Part II Content-Based Recommender System

1. get_movie_features.py
	* Get movie features from website and database(u.item)
	* visit database to get decade, genres, url from u.item dataset
	* visit url of each movie and find directors, writters and stars information from the html code.
	* this program runs lots of time and we have saved the information in file "result/movie_features.txt"
	  by using pickle, so you DON'T NEED TO RUN the following code to save time.

	
	run code:
		import get_movie_features as gmf
		gmf.read_data_from_item_file('ml-100k-split/u.item', 'ml-100k-split/movie_features.txt')
	result file:
		result/movie_features.txt

	/*********************************************************************************************/
	* if you want to load the features file, just using the following command:
	run code:
		import pickle
		k = pickle.load(open('ml-100k-split/movie_features.txt', 'rb'))
	/*********************************************************************************************/


2. content_based.py
	* perform Recommender by similarity of movie features
	run code:
		# recommend for user 5
		import content_based
		content_based.content_based_recommend(5)
