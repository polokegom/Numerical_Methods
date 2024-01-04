def newtonRaphson(num, intervals) : 
    val = num 
    count = 0
    isFound =False
    
    while (not isFound) :
        count += 1
        root = 0.5 * (val + (num / val)) 
        isFound = (abs(root - val) < intervals)
        val = root
    return root 
 
if __name__ == "__main__" : 
    print(newtonRaphson(144, 0.1)) 
