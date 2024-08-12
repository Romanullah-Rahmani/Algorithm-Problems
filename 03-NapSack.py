def knapSack(W, wt, val): 
    # W: The maximum weight capacity of the knapsack
    # wt: A list of weights for each item
    # val: A list of values for each item

    n = len(val)  # Number of items
    # Create a 2D table to store the maximum value that can be achieved with a given weight capacity
    table = [[0 for x in range(W + 1)] for _ in range(n + 1)] 
 
    # Iterate over all items
    for i in range(n + 1): 
        # Iterate over all capacities from 0 to W
        for j in range(W + 1): 
            if i == 0 or j == 0: 
                # Base case: If there are no items or the capacity is 0, the maximum value is 0
                table[i][j] = 0
            elif wt[i-1] <= j: 
                # If the weight of the current item is less than or equal to the capacity
                # Consider the maximum value of either including the item or excluding it
                table[i][j] = max(val[i-1] + table[i-1][j-wt[i-1]],  table[i-1][j]) 
            else: 
                # If the weight of the current item is more than the capacity, exclude it
                table[i][j] = table[i-1][j] 
                
    return table[n][W]  # The maximum value that can be achieved with the given weight capacity
 
# Example values
val = [55, 200, 150, 200]  # Values of the items
wt = [2, 3, 3, 4]  # Weights of the items
W = 8  # Maximum weight capacity of the knapsack
 
# Print the result of the knapSack function
print(knapSack(W, wt, val))






























# def knapSack(W, wt, val): 
#     n=len(val)
#     table = [[0 for x in range(W + 1)] for x in range(n + 1)] 
 
#     for i in range(n + 1): 
#         for j in range(W + 1): 
#             if i == 0 or j == 0: 
#                 table[i][j] = 0
#             elif wt[i-1] <= j: 
#                 table[i][j] = max(val[i-1] + table[i-1][j-wt[i-1]],  table[i-1][j]) 
#             else: 
#                 table[i][j] = table[i-1][j] 
   
#     return table[n][W] 
 
# val = [50,100,150,200]
# wt = [8,16,32,40]
# W = 64
 
# print(knapSack(W, wt, val))