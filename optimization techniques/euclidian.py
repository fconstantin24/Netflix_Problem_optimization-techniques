import time
from scipy import spatial
import numpy as np
import scipy.optimize as spo


users = [{}, {}, {}, {}, {}, {}]

# [[3.0  5.0  2.0  5.0  5.0  5.0]
#  [2.0  4.0  1.0  5.0  3.0  5.0]
#  [2.0  3.0  1.0  5.0  1.0  4.0]
#  [2.0  2.0  4.0  5.0  4.0  4.0]
#  [5.0  4.0  1.0  5.0  2.0  5.0]
#  [1.0  2.0  3.0  5.0  4.0  4.0]]

# [[3. 4. 2. 5. 5. 5.]
#  [2. 4. 1. 5. 3. 5.]
#  [2. 4. 3. 5. 1. 5.]
#  [2. 2. 4. 5. 4. 4.]
#  [5. 4. 3. 5. 2. 5.]
#  [1. 2. 3. 5. 4. 4.]]




def compute_user_similarity(x):
    ratings = [[3.0, 0.0, 2.0, 0.0, 5.0, 0.0],
               [2.0, 4.0, 1.0, 0.0, 3.0, 5.0],
               [2.0, 0.0, 0.0, 5.0, 1.0, 0.0],
               [2.0, 2.0, 4.0, 0.0, 0.0, 4.0],
               [5.0, 0.0, 0.0, 0.0, 2.0, 0.0],
               [1.0, 0.0, 3.0, 5.0, 4.0, 0.0]]
    ratings = np.array(ratings)
    for movie1 in range(0, 6):
        for movie2 in range(0, 6):
            if movie1 != movie2:
                res = []
                for user in range(0, 6):
                    result_per_user = []
                    if ratings[user][movie1] != 0 and ratings[user][movie2] != 0:
                        for out_user in range(user+1, 6):
                            if ratings[out_user][movie1] != 0 and ratings[out_user][movie2] != 0:
                                similarity = {out_user: spatial.distance.cosine([ratings[user][movie1],
                                                                                 ratings[user][movie2]],
                                                                                [ratings[out_user][movie1],
                                                                                 ratings[out_user][movie2]])}
                                result_per_user.append(similarity)
                    res.append(result_per_user)

                for i in range(0, 6):
                    if len(res[i]) != 0:
                        for j in range(len(res[i])):
                            for key, value in res[i][j].items():
                                users[i][key] = value
                                users[key][i] = value

    for i in range(0, 6):
        users[i] = dict(sorted(users[i].items(), key=lambda item: item[1]))

    for i in range(0, 6):
        for j in range(0, 6):
            if ratings[i][j] == 0:
                for key, value in users[i].items():
                    if ratings[key][j] != 0:
                        ratings[i][j] = ratings[key][j]
                        break
    print(ratings)
    return ratings


if __name__ == '__main__':
    r0 = [[3.0, 4.0, 2.0, 5.0, 5.0, 5.0],
          [2.0, 4.0, 1.0, 5.0, 3.0, 5.0],
          [2.0, 3.0, 2.0, 5.0, 1.0, 4.0],
          [2.0, 2.0, 4.0, 5.0, 4.0, 4.0],
          [5.0, 4.0, 1.0, 5.0, 2.0, 5.0],
          [1.0, 2.0, 3.0, 5.0, 4.0, 4.0]]
    r0 = np.array(r0)
    result = spo.minimize(compute_user_similarity, r0)
    print(result.ratings)
