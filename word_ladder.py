class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        #Input: beginWord = "hit", endWord = "cog", 
        #wordList = ["hot","dot","dog","lot","log","cog"]
        new_list = []
        new_list.append(beginWord)

        str_1 = ""
        counter = 0

        if endWord not in wordList:
            return 0
        else:

            for word in wordList:
                str_1 = word
                if len(str_1) == len(beginWord):
                    for i in range(1, len(beginWord) + 1):
                        if str_1[i:i+1] == beginWord[i:i+1]:
                            counter += 0
                        else:
                            counter += 1

                    if counter < 2:
                        new_list.append(str_1)
                        beginWord = str_1
                else:
                    counter = 2

            new_list.append(endWord)
            print(new_list)
                


S1 = Solution()
# S1.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])

