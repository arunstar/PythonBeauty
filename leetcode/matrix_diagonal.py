import collections

def findDiagonalOrder(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        # matrix = [ [1,2,3],
        #             [4,5,6],
        #               [7,8,9]]

        # [ [0,1,2]
        #   [0,1,2]
        #   [0,1,2]
        # ]

        # # op = [1,4,2,7,5,3,8,6,9]

        result = [ ]
        dd = collections.defaultdict(list)
        print(dd)
        if not matrix: return result
        # Step 1: Numbers are grouped by the diagonals.
        # Numbers in same diagonal have same value of row+col
        for i in range(0, len(matrix)):
            print("+"*30)
            for j in range(0, len(matrix[i])):
                print(i,j,1)
                print(matrix[i][j])
                dd[i+j+1].append(matrix[i][j]) # starting indices from 1, hence i+j+1.
        print(dd)
        # Step 2: Place diagonals in the result list.
        # But remember to reverse numbers in odd diagonals.
        for k in sorted(dd.keys()):
            if k%2==1: dd[k].reverse()
            result += dd[k]
        print("Done ************************")
        return result

mat = [ ['a','b','c'],
        ['d','e','f'],
        ['g','h','i']]
# op = [1, 2, 4, 7, 5, 3, 6, 8, 9]
print(findDiagonalOrder(mat))