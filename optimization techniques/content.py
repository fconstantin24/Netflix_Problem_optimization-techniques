import numpy as np
import time

users = [[3.0, 4.0, 2.0, 1.0],
         [2.0, 4.0, 1.0, 4.0],
         [2.0, 3.0, 4.0, 5.0],
         [2.0, 1.0, 4.0, 1.0],
         [5.0, 5.0, 1.0, 1.0],
         [1.0, 1.0, 3.0, 1.0]]

movies = [[1.0, 1.0, 5.0, 1.0, 1.0, 5.0],
          [5.0, 4.0, 5.0, 4.0, 5.0, 5.0],
          [4.0, 5.0, 2.0, 3.0, 2.0, 1.0],
          [2.0, 1.0, 2.0, 5.0, 1.0, 1.0]]

names = ["Maria", "Gigel", "Ana", "Dana", "Matei", "Alex"]
genre = ["comedie", "actiune", "drama", "horror"]
titles = ["Avatar", "Titanic", "American Pie", "Conjuring", "Deadpool", "Matrix"]

start_time = time.time()
ratings = np.dot(users, movies) / 20
for i in range(len(ratings)):
    for j in range(len(ratings[i])):
        ratings[i][j] = round(ratings[i][j], 2)

print(time.time() - start_time)
print(ratings)

for i in range(len(ratings)):
    for j in range(len(ratings[i])):
        print(names[i] + " a dat nota " + str(ratings[i][j]) + " filmului " + titles[j])