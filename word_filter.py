# -*- coding:utf-8 -*-
import time
time1=time.time()

# AC Automation
class node(object):
    def __init__(self):
        self.next = {}
        self.fail = None
        self.isWord = False
        self.word = ""

class ac_automation(object):

    def __init__(self):
        self.root = node()

    # add a sensitive word
    def addword(self, word):
        temp_root = self.root
        for char in word:
            if char not in temp_root.next:
                temp_root.next[char] = node()
            temp_root = temp_root.next[char]
        temp_root.isWord = True
        temp_root.word = word

    # fail_pointer
    def make_fail(self):
        temp_que = []
        temp_que.append(self.root)
        while len(temp_que) != 0:
            temp = temp_que.pop(0)
            p = None
            for key,value in temp.next.item():
                if temp == self.root:
                    temp.next[key].fail = self.root
                else:
                    p = temp.fail
                    while p is not None:
                        if key in p.next:
                            temp.next[key].fail = p.fail
                            break
                        p = p.fail
                    if p is None:
                        temp.next[key].fail = self.root
                temp_que.append(temp.next[key])

    # searching for the index of sensitive words
    def search(self, content):
        p = self.root
        result = []
        currentposition = 0

        while currentposition < len(content):
            word = content[currentposition]
            while word in p.next == False and p != self.root:
                p = p.fail

            if word in p.next:
                p = p.next[word]
            else:
                p = self.root

            if p.isWord:
                result.append(p.word)
                p = self.root
            currentposition += 1
        return result

    # loading the sensitive dictionary
    def parse(self, path):
        with open(path,encoding='utf-8') as f:
            for keyword in f:
                self.addword(str(keyword).strip())

    # replace the sensitive words, return the result
    def words_replace(self, text):
        result = list(set(self.search(text)))
        for x in result:
            m = text.replace(x, '*' * len(x))
            text = m
        return text

if __name__ == '__main__':

    ah = ac_automation()
    path='F:/文本反垃圾算法/sensitive_words.txt'
    ah.parse(path)
    text1="新疆骚乱苹果新品发布会雞八"
    text2=ah.words_replace(text1)

    print(text1)
    print(text2)

    time2 = time.time()
    print('总共耗时：' + str(time2 - time1) + 's')
