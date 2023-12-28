# cleaning text
#   1) create a text file and take text from it
#   2) convert the letter into lowercase ('Apple' is not equal to 'apple')
#   3) Remove punctuations like .,!? etc.

import string
from collections import Counter
from nltk import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

text = open('read.txt', encoding='utf-8').read()
# thông thường theo mã hóa utf-8
lower_text = text.lower()
# Str1: Specifies the list of characters that need to be replace.
# Str2: Specifies the list of characters with which the characters need to be replace.
# Str3: Specifies the list of characters that needs to be deleted.

clean_text = lower_text.translate(str.maketrans(' ', ' ', string.punctuation))
#splitting punctuations
tokenized_words = word_tokenize(clean_text, "english")
#print(clean_text)
#print(tokenized_words)
# stop word là những từ không thêm bất kỳ ý nghĩa gì vào câu, có thể bị loại bỏ

#removing stopwords
final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

#NLP emtion alorithm
# 1) Check if the word in the final word list is also present in emotion.txt
# 2) If word is present -> Add the emotion to emotion_list
# 3) Finally count each emotion in emotion list
#print(final_words) #list được rút gọn (loại trừ các từ stop_word)
emotion_list =[]
with open('emotion.txt','r') as file:
    for line in file:
        clean_line = line.replace('\n','').replace("'","").replace(',','').strip()
        #xử lý dữ liệu từng dòng trong emotion.txt
        #print(clean_line)
        word, emotion = clean_line.split(':')
        #phía trước: được lưu trữ với word
        #phía sau: được lưu trữ với emotion
        #print("Word:"+ word+ " "+ "Emotion"+emotion)

        if word in final_words:
            emotion_list.append(emotion)
print(emotion_list)
#đếm các emotion trong emotion list xuất hiện bao nhiêu lần trong list
counter_emtion = Counter(emotion_list)
print(counter_emtion)


fig , ax1 = plt.subplots()
ax1.bar(counter_emtion.keys(),counter_emtion.values())
#.keys() tương ứng với trục x, values() tương ứng với trục y
fig.autofmt_xdate()
plt.show()