class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        WhereAreOnes = []
        for i in range(len(boxes)):
            if boxes[i] == '1':
                WhereAreOnes.append(i)
        answers = [0]*len(boxes)
        for i in range(len(answers)):
            minOper = 0
            for n in WhereAreOnes:
                minOper += abs(n-i)
            answers[i] = minOper
        return answers