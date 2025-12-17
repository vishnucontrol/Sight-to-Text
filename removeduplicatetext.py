
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import spacy 
import spacy.cli

import tensorflow_hub as hub


#---------------------------------------------------------------------------------------------------------
#Using tensor flow

#---------------------------------------------------------------------------------------------------------

embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
from scipy.spatial import distance
"""
embeddings = embed([
    "the person wear red T-shirt",
    "this person is walking",
    "the boy wear red T-shirt"
    ])

print(embeddings)

from scipy.spatial import distance
print(1 - distance.cosine(embeddings[0], embeddings[1]))
print(1 - distance.cosine(embeddings[0], embeddings[2]))
print(1 - distance.cosine(embeddings[1], embeddings[2]))"""

my_file = open("text.txt", "r")
data = my_file.read()
sentences= data.split("\n")
sentences.pop(-1)
#print(sentences)
my_file.close()


def reducesimilarities(sentence_list,count):
    if(count>len(sentence_list)):
        return sentence_list,-1
    else:
        reduced_sentences=[]
        for i in range(count):
            reduced_sentences.append(sentence_list[i])
        #print("before",reduced_sentences)
        embeddings = embed(sentence_list)
        #print(sentence_list[count-1],sentence_list[count])
        for i in range(count,len(sentence_list)):
            val=1-distance.cosine(embeddings[count-1], embeddings[i])
            if(val<0.85):
                reduced_sentences.append(sentence_list[i])
        #print("after",reduced_sentences)
        return reduced_sentences,count+1




count=1
reduced_sentences=list(sentences)
while(count!=-1):
    print("epoch : ",count)
    reduced_sentences,count=reducesimilarities(reduced_sentences,count)
print(reduced_sentences)


with open ('text.txt1', 'w') as file:  
    for line_1 in reduced_sentences:  
        file.writelines(line_1)
        file.write('\n') 





#---------------------------------------------------------------------------------------------------------
#SPACY --cant download the model

#---------------------------------------------------------------------------------------------------------

"""
#import en_core_web_lg
#spacy.cli.download("en_core_web_lg")

#nlp=spacy.load("en_core_web_lg")

def reducesimilarities(sentence_list,count):
    if(count>len(sentence_list)):
        return sentence_list,-1
    else:
        reduced_sentences=[]
        for i in range(count):
            reduced_sentences.append(sentence_list[i])
        #sentence_vecs=model.encode(sentence_list)
        #print("reduced sentences : ",reduced_sentences)
        #print("sentence_vecs :" ,sentence_vecs)
        #similarity=cosine_similarity([sentence_vecs[count]],sentence_vecs[count:])[0]
        #print("similarity : ",similarity)
        sentence1=nlp(sentence_list[count])
        for i in range(count+1,len(sentence_list)):
            sentence2=nlp(sentence_list[i])
            similarity=sentence1.similarity(sentence2)
            if(similarity<0.80):
                reduced_sentences.append(sentence_list[i])
        #print("len reduced string : ",len(reduced_sentences))
        return reduced_sentences,count+1


my_file = open("text.txt", "r")
data = my_file.read()
sentences= data.split("\n")
sentences.pop(-1)
#print(sentences)
my_file.close()

count=0
reduced_sentences=list(sentences)
while(count!=-1):
    print("epoch : ",count)
    reduced_sentences,count=reducesimilarities(reduced_sentences,count)
print(reduced_sentences)

with open ('text.txt1', 'w') as file:  
    for line_1 in reduced_sentences:  
        file.writelines(line_1)
        file.write('\n') 

"""















#---------------------------------------------------------------------------------------------------------
#BERT

#---------------------------------------------------------------------------------------------------------
""""
def reducesimilarities(sentence_list,count):
    if(count>len(sentence_list)):
        return sentence_list,-1
    else:
        reduced_sentences=[]
        for i in range(count):
            reduced_sentences.append(sentence_list[i])
        sentence_vecs=model.encode(sentence_list)
        #print("reduced sentences : ",reduced_sentences)
        #print("sentence_vecs :" ,sentence_vecs)
        similarity=cosine_similarity([sentence_vecs[count]],sentence_vecs[count:])[0]
        #print("similarity : ",similarity)
        for i in range(len(similarity)-1):
            if(similarity[i]<0.85):
                reduced_sentences.append(sentence_list[i+count])
        #print("len reduced string : ",len(reduced_sentences))
        return reduced_sentences,count+1

my_file = open("text.txt", "r")
data = my_file.read()
sentences= data.split("\n")
sentences.pop(-1)
#print(sentences)
my_file.close()

modelname="bert-base-nli-mean-tokens"
model=SentenceTransformer(modelname)

count=1
reduced_sentences=list(sentences)
while(count!=-1):
    print("epoch : ",count)
    reduced_sentences,count=reducesimilarities(reduced_sentences,count)
print(reduced_sentences)

#print(reduced_sentences)
with open ('text.txt1', 'w') as file:  
    for line_1 in reduced_sentences:  
        file.writelines(line_1)
        file.write('\n')   
"""