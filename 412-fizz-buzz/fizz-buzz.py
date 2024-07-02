class Solution(object):
    def fizzBuzz(self, n):
        List=[]
        for n in range(1,n+1):
            if n%3==0 and n%5==0:
                List.append('FizzBuzz')
            elif n%3==0:
                List.append('Fizz')
            elif n%5==0:
                 List.append('Buzz')
            else:
                List.append(str(n))
        return List
        