class Solution(object):
    def rotate(self, arr, d):
        n=len(arr)
        k= d % n
        if len(arr)==1:
            arr.reverse()
            return arr
        arr.reverse()
        i=0
        j=k-1
        while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        
        i=k
        j=n-1
        while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            j-=1
            i+=1
        return arr