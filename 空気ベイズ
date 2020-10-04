import nagisa
import collections
import numpy as np

text1 = "水を含んだ湿った空気が流れてくる"
text2 = "時代を漂う湿った空気が読みとれる"

doc = nagisa.tagging(text1 + text2)
def tokenize_jp(doc):
    doc = nagisa.tagging(doc)
    return doc.words
text1 = (tokenize_jp(text1))
text2 = (tokenize_jp(text2))

count_air1 = 426
count_air2 = 455
percent_air1 = count_air1 / (count_air1 + count_air2)
percent_air2 = count_air2 / (count_air1 + count_air2)

c1 = collections.Counter(湿っ=52,  水=34,流れ=11, 感じ=14, 時代=6, 漂う=5,読み=2)
c2 = collections.Counter(湿っ=1,  水=3,流れ=22, 感じ=34, 時代=32, 漂う=33,読み=89)

text1_c1_probability = 1
text1_c2_probability = 1

for word in text1:
    word_in_c1 = c1[word]
    word_in_c2 = c2[word]
    text1_c1_probability *= (word_in_c1 + 1) / (count_air1 + len(c1))
    text1_c2_probability *= (word_in_c2 + 1) / (count_air2 + len(c2))
    
    
text1_final_c1 = c1_probability * percent_air1
text1_final_c2 = c2_probability * percent_air2

if text1_final_c1 > text1_final_c2:
    print("The word 空気 has the first meaning in the first text")
else:
    print("The word 空気 has the second meaning in the first text")
    
text2_c1_probability = 1
text2_c2_probability = 1

for word in text2:
    word_in_c1 = c1[word]
    word_in_c2 = c2[word]
    text2_c1_probability *= (word_in_c1 + 1) / (count_air1 + len(c1))
    text2_c2_probability *= (word_in_c2 + 1) / (count_air2 + len(c2))
    
    
text2_final_c1 = text2_c1_probability * percent_air1
text2_final_c2 = text2_c2_probability * percent_air2

if text2_final_c1 > text2_final_c2:
    print("The word 空気 has the first meaning in the first text")
else:
    print("The word 空気 has the second meaning in the first text")
    

