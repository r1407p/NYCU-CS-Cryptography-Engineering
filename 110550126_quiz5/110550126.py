ori = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1]
def list_to_poly(li):
   ans = ""
   if li[0]:
      ans =" + 1"
   for i in range(1, len(li)):
      if li[i]==1:
         ans+=" + x^"
         ans+=str(i)
   ans = ans[3:]
   return ans

def mix_poly(A,B):
   if len(A)<len(B):
      A,B = B,A
   for i in range(len(B)):
      A[i]^=B[i]
   return A
def BM(ori):
   C = [1]
   B = [1]
   l = 0
   n = 0
   m = -1
   N = len(ori)
   for i in range(N):

      d = ori[i]
      for j in range(1,l+1):
         d ^= C[j]*ori[i-j]
      if d == 0:         
         continue
      T = C.copy()
      shift = i-m
      C = mix_poly(C, [0]*shift+B)
      if l <= int(i/2):
         l = i+1-l
         m = i
         B = T.copy()
   return C
if __name__ == "__main__":
   ans = BM(ori)
   poly = list_to_poly(ans)
   print(f'The input sequence is  {str(ori)}')
   print(f'Its characteristic polynomial is {poly}')
   print(f'and linear span is {len(ans)-1}')
   
    

