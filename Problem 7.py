'''
You are given few sentences as a list (Python list of sentences).
Take a query string as an input from the user. You have to pull out the sentences matching this query inputted
by the user in decreasing order of relevance after converting every word in the query and the sentence to lowercase.
Most relevant sentence is the one with the maximum number of matching words with the query.

Sentences = [“This is good”, “python is good”, “python is not python snake”]

Input:
Please input your query string

“Python is”

Output:
3 results found:

1.      python is not python snake

2.      python is good

3.      This is good
'''
# my_list = ['this is good', 'python is easy to learn', 'python is interpreted language', 'english is most spoken language',
#            'python is a conputer language and python is also a snake', 'language is medium to connect people']


# def query(str1):
#     for string in my_list:
#         if str1 in string:
#             # print(f'{} result found.')
#             print(string)
#         elif str1 not in string:
#             print('Sorry!, Result not found')
        


# if __name__ == "__main__":
#     str1 = input('What do you want to search?\n')
#     str1 = str1.lower()
#     query(str1)

'''
You are given few sentences as a list (Python list of sentences). Take a query string as an input from the user. You have to pull out the sentences matching this query inputted by the user in decreasing order of relevance after converting every word in the query and the sentence to lowercase. Most relevant sentence is the one with the maximum number of matching words with the query. 
Sentences = [“This is good”, “python is good”, “python is not python snake”]

Input:
Please input your query string
“Python is”

Output:
3 results found:
1.	python is not python snake
2.	python is good
3.	This is good
'''


def mathingWords(sentence1, sentence2):
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.strip().split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2}")
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == "__main__":
    # mathingWords("This is good", "python is good")
    sentences = ["python is a good", "this is snake",
                 "harry is a good boy", "Subscribe to code with harry"]

    query = input("Please enter the query string\n")
    scores = [mathingWords(query, sentence) for sentence in sentences]
    # print(scores)
    sortedSentScore = [sentScore for sentScore in sorted(
        zip(scores, sentences), reverse=True) if sentScore[0] !=0 ]
    # print(sortedSentScore)

    print(f"{len(sortedSentScore)} results found!")
    for score, item in sortedSentScore:
        print(f" \"{item}\": with a score of {score}")


