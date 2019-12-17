# -*- coding:utf-8 -*-
import time
import os
import pickle

# AC Automation
class node(object):
    def __init__(self):
        self.next = {}
        self.backlink = None
        self.ending = False
        self.word = ""

class AC_automation(object):
    def __init__(self):
        self.root = node()
        self.root.word = "THEROOT"

    # add a word
    def addword(self, word):
        if len(word) == 0 or len(word) > 8:
            return
        if len(word) == 1:
            print(word)
        tmp_root = self.root
        for char in word:
            if char not in tmp_root.next:
                tmp_root.next[char] = node()
            tmp_root = tmp_root.next[char]
        tmp_root.word = word
        tmp_root.ending = True

    # back link pointer
    def make_backlink(self):
        tmp_q = []
        tmp_q.append(self.root)
        while len(tmp_q) != 0:
            tmp = tmp_q.pop(0)
            p = False
            for key,value in tmp.next.items():
                #print(key)
                if tmp == self.root:
                    tmp.next[key].backlink = self.root
                else:
                    p = tmp.backlink
                    while p:
                        if key in p.next:
                            #tmp.next[key].backlink = p.backlink
                            tmp.next[key].backlink = p.next[key]
                            if p.next[key].ending:
                                tmp.next[key].ending = True
                            break
                        p = p.backlink
                    if not p:
                        tmp.next[key].backlink = self.root
                tmp_q.append(tmp.next[key])

    # searching for the index of sensitive words
    def search(self, content):
        p = self.root
        print(p.word, self.root.word)
        result = []
        curpos = 0

        while curpos < len(content):
            word = content[curpos]
            #print("DEBUG1", p.word)
            while (word not in (p.next)) and (p.word != "THEROOT"):
                #print("DEBUG2", word)
                p = p.backlink

            if word in p.next:
                p = p.next[word]
            else:
                p = self.root

            if p.ending:
                while p.word == "":
                    p = p.backlink
                result.append(p.word)
                print(p.word)
                p = self.root
            curpos += 1
        return result

    # replace the sensitive words, return the result
    def words_replace(self, text):
        result = list(set(self.search(text)))
        for x in result:
            m = text.replace(x, '*' * len(x))
            text = m
        return text

if __name__ == '__main__':

    the_filter = AC_automation()
    with open('../words.pkl', 'rb') as f:
        wordlist = pickle.load(f)
    for w in wordlist:
        #print(w)
        the_filter.addword(w)
    text1="鷄和谐清华帮陈云新疆网易云音乐"
    text2=the_filter.words_replace(text1)

    print(text1)
    print(text2)
