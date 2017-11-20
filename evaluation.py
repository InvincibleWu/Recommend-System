import RecommenderSystem as rcst
import matplotlib.pyplot as plt


def test_for_naiveCF_u1_to_u5(k1, k2, out_put_path, out_put_graph_path):

	base_path_list = ['ml-100k/u1.base', 'ml-100k/u2.base', 'ml-100k/u3.base', 'ml-100k/u4.base', 'ml-100k/u5.base']
	test_path_list = ['ml-100k/u1.test', 'ml-100k/u2.test', 'ml-100k/u3.test', 'ml-100k/u4.test', 'ml-100k/u5.test']
	f = open(out_put_path, 'w')
	f = open(out_put_path, 'a')
	mean_rmse_list = []
	for k in range(k1, k2 + 1):
		sum_rmse = 0
		# print('***********************************************************')
		# print('Test for k = {}:'. format(k))
		f.write('***********************************************************\n')
		str_test = 'Test for k = ' + str(k) + ':' + '\n'
		f.write(str_test)
		for i in range(5):
			rs = rcst.Recommender_System(base_path_list[i], test_path_list[i], k)
			r = rs.calculate_NaiveCF_rmse()

			str_res = '\tuse u' + str(i+1) + '.base and u' + str(i+1) + '.test :\t' + str(r) + '\n'
			f.write(str_res)
			sum_rmse += r
		mean_rmse = sum_rmse/5
		# print('root mean square error: ', mean_rmse)
		str_rmse = 'mean of root mean square error: ' + str(mean_rmse) + '\n'
		f.write(str_rmse)
		mean_rmse_list.append(mean_rmse)
	
	# find optimal k
	minima = 10
	min_k = 0
	for i in range(k2 - k1 + 1):
		if mean_rmse_list[i] < minima:
			min_k = i+k1
			minima = mean_rmse_list[i]
	f.write('optimal value of k: ' + str(min_k) + '\n')
	f.write('rmse with optimal k: ' + str(minima) + '\n')
	f.close()
	# print(min_k)
	# print(minima)

	# plot
	k_list = [i for i in range(k1, k2 + 1)]
	plt.plot(k_list, mean_rmse_list)
	# plt.show()
	plt.xlabel('K')
	plt.ylabel('Mean of RMSE')

	plt.savefig(out_put_graph_path)
	plt.close()

def test_for_user_user_u1_to_u5(k1, k2, out_put_path, out_put_graph_path):
 	
	base_path_list = ['ml-100k/u1.base', 'ml-100k/u2.base', 'ml-100k/u3.base', 'ml-100k/u4.base', 'ml-100k/u5.base']
	test_path_list = ['ml-100k/u1.test', 'ml-100k/u2.test', 'ml-100k/u3.test', 'ml-100k/u4.test', 'ml-100k/u5.test']
	f = open(out_put_path, 'w')
	f = open(out_put_path, 'a')
	mean_rmse_list = []
	for k in range(k1, k2 + 1):
		sum_rmse = 0
		# print('***********************************************************')
		# print('Test for k = {}:'. format(k))
		f.write('***********************************************************\n')
		str_test = 'Test for k = ' + str(k) + ':' + '\n'
		f.write(str_test)
		for i in range(5):
			rs = rcst.Recommender_System(base_path_list[i], test_path_list[i], k)
			r = rs.calculate_user_user_rmse()

			str_res = '\tuse u' + str(i+1) + '.base and u' + str(i+1) + '.test :\t' + str(r) + '\n'
			f.write(str_res)
			sum_rmse += r
		mean_rmse = sum_rmse/5
		# print('root mean square error: ', mean_rmse)
		str_rmse = 'mean of root mean square error: ' + str(mean_rmse) + '\n'
		f.write(str_rmse)
		mean_rmse_list.append(mean_rmse)
	
	# find optimal k
	minima = 10
	min_k = 0
	for i in range(k2 - k1 + 1):
		if mean_rmse_list[i] < minima:
			min_k = i+k1
			minima = mean_rmse_list[i]
	f.write('optimal value of k: ' + str(min_k) + '\n')
	f.write('rmse with optimal k: ' + str(minima) + '\n')
	f.close()
	# print(min_k)
	# print(minima)

	# plot
	k_list = [i for i in range(k1, k2 + 1)]
	plt.plot(k_list, mean_rmse_list)
	# plt.show()
	plt.xlabel('K')
	plt.ylabel('Mean of RMSE')

	plt.savefig(out_put_graph_path)
	plt.close()
def test_for_item_item_u1_to_u5(k1, k2, out_put_path, out_put_graph_path):
	base_path_list = ['ml-100k/u1.base', 'ml-100k/u2.base', 'ml-100k/u3.base', 'ml-100k/u4.base', 'ml-100k/u5.base']
	test_path_list = ['ml-100k/u1.test', 'ml-100k/u2.test', 'ml-100k/u3.test', 'ml-100k/u4.test', 'ml-100k/u5.test']
	f = open(out_put_path, 'w')
	f = open(out_put_path, 'a')
	mean_rmse_list = []
	for k in range(k1, k2 + 1):
		sum_rmse = 0
		# print('***********************************************************')
		# print('Test for k = {}:'. format(k))
		f.write('***********************************************************\n')
		str_test = 'Test for k = ' + str(k) + ':' + '\n'
		f.write(str_test)
		for i in range(5):
			rs = rcst.Recommender_System(base_path_list[i], test_path_list[i], k)
			r = rs.calculate_rmse()

			str_res = '\tuse u' + str(i+1) + '.base and u' + str(i+1) + '.test :\t' + str(r) + '\n'
			f.write(str_res)
			sum_rmse += r
		mean_rmse = sum_rmse/5
		# print('root mean square error: ', mean_rmse)
		str_rmse = 'mean of root mean square error: ' + str(mean_rmse) + '\n'
		f.write(str_rmse)
		mean_rmse_list.append(mean_rmse)
	
	# find optimal k
	minima = 10
	min_k = 0
	for i in range(k2 - k1 + 1):
		if mean_rmse_list[i] < minima:
			min_k = i+k1
			minima = mean_rmse_list[i]
	f.write('optimal value of k: ' + str(min_k) + '\n')
	f.write('rmse with optimal k: ' + str(minima) + '\n')
	f.close()
	# print(min_k)
	# print(minima)

	# plot
	k_list = [i for i in range(k1, k2 + 1)]
	plt.plot(k_list, mean_rmse_list)
	# plt.show()
	plt.xlabel('K')
	plt.ylabel('Mean of RMSE')

	plt.savefig(out_put_graph_path)
	plt.close()

def test_for_naiveCF_uaub(k1, k2, out_put_path, out_put_graph_path):
	base_path_list = ['ml-100k/ua.base', 'ml-100k/ub.base']
	test_path_list = ['ml-100k/ua.test', 'ml-100k/ub.test']
	f = open(out_put_path, 'w')
	f = open(out_put_path, 'a')
	mean_rmse_list = []
	for k in range(k1, k2 + 1):
		sum_rmse = 0
		# print('***********************************************************')
		# print('Test for k = {}:'. format(k))
		f.write('***********************************************************\n')
		str_test = 'Test for k = ' + str(k) + ':' + '\n'
		f.write(str_test)
		for i in range(2):
			rs = rcst.Recommender_System(base_path_list[i], test_path_list[i], k)
			r = rs.calculate_NaiveCF_rmse()
			#r = mu.main(base_path_list[i], test_path_list[i], k)
			# print('\tuse u{}.base and u{}.test :\t{}'.format(i+1, i+1, r))
			if i == 0:
				str_res = '\tuse ua.base and ua.test :\t' + str(r) + '\n'
			else:
				str_res = '\tuse ub.base and ub.test :\t' + str(r) + '\n'
			f.write(str_res)
			sum_rmse += r
		mean_rmse = sum_rmse/2
		# print('root mean square error: ', mean_rmse)
		str_rmse = 'mean of root mean square error: ' + str(mean_rmse) + '\n'
		f.write(str_rmse)
		mean_rmse_list.append(mean_rmse)
	
	# find optimal k
	minima = 10
	min_k = 0
	for i in range(k2 - k1 + 1):
		if mean_rmse_list[i] < minima:
			min_k = i+k1
			minima = mean_rmse_list[i]
	f.write('optimal value of k: ' + str(min_k) + '\n')
	f.write('rmse with optimal k: ' + str(minima) + '\n')
	f.close()
	# print(min_k)
	# print(minima)

	# plot
	k_list = [i for i in range(k1, k2 + 1)]
	plt.plot(k_list, mean_rmse_list)
	# plt.show()
	plt.xlabel('K')
	plt.ylabel('Mean of RMSE')

	plt.savefig(out_put_graph_path)
	plt.close()
	
def test_for_user_user_uaub(k1, k2, out_put_path, out_put_graph_path):
	base_path_list = ['ml-100k/ua.base', 'ml-100k/ub.base']
	test_path_list = ['ml-100k/ua.test', 'ml-100k/ub.test']
	f = open(out_put_path, 'w')
	f = open(out_put_path, 'a')
	mean_rmse_list = []
	for k in range(k1, k2 + 1):
		sum_rmse = 0
		# print('***********************************************************')
		# print('Test for k = {}:'. format(k))
		f.write('***********************************************************\n')
		str_test = 'Test for k = ' + str(k) + ':' + '\n'
		f.write(str_test)
		for i in range(2):
			rs = rcst.Recommender_System(base_path_list[i], test_path_list[i], k)
			r = rs.calculate_user_user_rmse()
			#r = mu.main(base_path_list[i], test_path_list[i], k)
			# print('\tuse u{}.base and u{}.test :\t{}'.format(i+1, i+1, r))
			if i == 0:
				str_res = '\tuse ua.base and ua.test :\t' + str(r) + '\n'
			else:
				str_res = '\tuse ub.base and ub.test :\t' + str(r) + '\n'
			f.write(str_res)
			sum_rmse += r
		mean_rmse = sum_rmse/2
		# print('root mean square error: ', mean_rmse)
		str_rmse = 'mean of root mean square error: ' + str(mean_rmse) + '\n'
		f.write(str_rmse)
		mean_rmse_list.append(mean_rmse)
	
	# find optimal k
	minima = 10
	min_k = 0
	for i in range(k2 - k1 + 1):
		if mean_rmse_list[i] < minima:
			min_k = i+k1
			minima = mean_rmse_list[i]
	f.write('optimal value of k: ' + str(min_k) + '\n')
	f.write('rmse with optimal k: ' + str(minima) + '\n')
	f.close()
	# print(min_k)
	# print(minima)

	# plot
	k_list = [i for i in range(k1, k2 + 1)]
	plt.plot(k_list, mean_rmse_list)
	# plt.show()
	plt.xlabel('K')
	plt.ylabel('Mean of RMSE')

	plt.savefig(out_put_graph_path)
	plt.close()
def test_for_item_item_uaub(k1, k2, out_put_path, out_put_graph_path):
	base_path_list = ['ml-100k/ua.base', 'ml-100k/ub.base']
	test_path_list = ['ml-100k/ua.test', 'ml-100k/ub.test']
	f = open(out_put_path, 'w')
	mean_rmse_list = []
	f = open(out_put_path, 'a')
	for k in range(k1, k2 + 1):
		sum_rmse = 0
		# print('***********************************************************')
		# print('Test for k = {}:'. format(k))
		f.write('***********************************************************\n')
		str_test = 'Test for k = ' + str(k) + ':' + '\n'
		f.write(str_test)
		for i in range(2):
			rs = rcst.Recommender_System(base_path_list[i], test_path_list[i], k)
			r = rs.calculate_rmse()
			#r = mi.main(base_path_list[i], test_path_list[i], k)
			# print('\tuse u{}.base and u{}.test :\t{}'.format(i+1, i+1, r))
			if i == 0:
				str_res = '\tuse ua.base and ua.test :\t' + str(r) + '\n'
			else:
				str_res = '\tuse ub.base and ub.test :\t' + str(r) + '\n'
			f.write(str_res)
			sum_rmse += r
		mean_rmse = sum_rmse/2
		# print('root mean square error: ', mean_rmse)
		str_rmse = 'mean of root mean square error: ' + str(mean_rmse) + '\n'
		f.write(str_rmse)
		mean_rmse_list.append(mean_rmse)
	
	# find optimal k
	minima = 10
	min_k = 0
	for i in range(k2 - k1 + 1):
		if mean_rmse_list[i] < minima:
			min_k = i+k1
			minima = mean_rmse_list[i]
	f.write('optimal value of k: ' + str(min_k) + '\n')
	f.write('rmse with optimal k: ' + str(minima) + '\n')
	f.close()
	# print(min_k)
	# print(minima)

	# plot
	k_list = [i for i in range(k1, k2 + 1)]
	plt.plot(k_list, mean_rmse_list)
	# plt.show()
	plt.xlabel('K')
	plt.ylabel('Mean of RMSE')

	plt.savefig(out_put_graph_path)
	plt.close()
