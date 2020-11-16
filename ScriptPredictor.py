# Alex Johnson
#
# Script Predictor
#
# Input Scripts should have their genre listed on the first line of the .txt file.

import sys
import os
from sklearn import tree

ARTICLE_LIST = ['the', 'a', 'an' ]
PREPOSITION_LIST = ['at', 'by', 'for', 'from', 'in', 'of', 'to', 'as', 'like']
PRONOUN_LIST = ['he', 'him', 'his', 'she', 'her', "her's", 'they', 'them', "their's"]
genres = {'Action':0, 'Adventure':1, 'Animation':2, 'Biography':3, 'Comedy':4, 'Crime':5, 'Documentary':6, 'Drama':7, 'Family':8, 'Fantasy':9, 'Film-Noir':10, 'History':11, 'Horror':12, 'Music':13, 'Musical':14, 'Mystery':15, 'Romance':16, 'Sci-Fi':17, 'Short':18, 'Sport':19, 'Thriller':20, 'War':21, 'Western':22}


class Film:
	def __init__(self, title, genres, data):
		self.title = title
		self.genres = genres
		self.data = data
	
	def __eq__(self, other):
		return self.title == other.title

	def __repr__(self):
		return(title)

#Creates a data set based on the given file path, input is a folder of scripts
def populateFilms(path):
	films = [] 

	for root, dir, files in os.walk(path):
		for file in files:
			filename, extension = os.path.splitext(file)
			if extension == '.txt':
				film = getScriptData(file)				
				films.append(film)
	return films
	
#parses a Script
def getScriptData(fileName):
	#set the temporary title
	tempTitle = filename
	fin = open(fileName,'r')
			
	#set the temporary genres
	first_line = fin.readline()
	tempGenres = first_line.split()
	tempGenres = [genres[item] for item in tempGenres]
			
	#get the word data
	lines1 = fin.readlines()
	lines2 = []
	for lines in lines1:
		lines = lines.split()
		lines2.append(lines)
	fin.close()
			
	#filter out certain words
	for x in lines2:
		for i in range(x.length()):
			x[i] = x[i].lower()
		x = [item for item in x if item not in ARTICLE_LIST]
		x = [item for item in x if item not in PREPOSITION_LIST]
		x = [item for item in x if item not in PRONOUN_LIST]
				
	#make a dictionary of words and their count
	words = {}
	for line in lines2:
		for word in line:
			if word in words:
				current = words[word]
				words[word] = current + 1
			else:
				words[word] = 1
	data = []
	word_list = []
	word_counts = []			
	for word in words:
		word_list.append(word)
		word_counts.append(words[word])
	data = [word_list, word_counts]

	tempData = data
			
	#make film object
	tempFilm = Film(tempTitle, tempGenres, tempData)
	return tempFilm
	
def main():
	path = sys.argv[1]
	films_list = populateFilms(path)
	
	genres = [film.genres for film in films_list]
	features = data
	
	
	clf = tree.DecisionTreeClassifier()
	clf = clf.fit(features, genres)
	
	predictScript = sys.argv[2]
	predictFilm = getScriptData(predictScript)
	
	clf.predict(predictFilm.data)
	
if __name__ == "__main__":
	main()
	
	
	
	