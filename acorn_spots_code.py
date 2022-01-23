import heapq
n, m = [int(i) for i in input().split()]
intervals = []
mini, maxi = 1000000000000000000, 0

for i in range(m): 
    x, y = [int(j) for j in input().split()]
    mini = min(x, mini)
    maxi = max(y, maxi)
    intervals.append((x, y))
intervals = sorted(intervals, key= lambda x: x[0])
print(intervals)

def does_work(i, n, test_d, start, maxi):
    num_bunnies = 0
    within_interval = True
    too_big = False
    ind = 0      
    while num_bunnies < n:
        print(start, ind, num_bunnies)
        if start > maxi:
            too_big = True
        if start<=i[ind][1] and start>=i[ind][0]: 
            num_bunnies+=1
            start+=test_d
        elif start<i[ind][1] and start<i[ind][0]: 
            within_interval=False
            num_bunnies+=1
            start+=test_d
        elif start>i[ind][1] and start>i[ind][0]:
            ind+=1
    print(start+test, ind)
    return too_big, within_interval

global_d = 0
def find_dist(n, intervals, test_d, low, high): 
    global global_d
    test_bool, test_result = does_work(intervals, n, 5, mini, maxi)
    print(test_bool, test_result)
    
    if test_result==n and test_bool: 
        test = global_d
        return
    elif test_result>n and test_bool: 
        test=(high+test)//2
        
    elif test_bool: 
        print('hi')
        test=(low+test)//2
    print(test)
    
find_dist(n, intervals, (mini+maxi)//2, mini, maxi)
print(global_d)
    
