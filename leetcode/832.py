class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        arr = []

        for i in range(len(image)):

            poc = []
            a = image[i][::-1]

            for j in a:

                if j == 0:
                    poc.append(1)

                else:
                    poc.append(0)

            arr.append(poc)

        return arr