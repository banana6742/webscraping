import numpy as np
TwoD = np.array([[2,3,8],[3,4,6],[2,4,6]])
print(TwoD)
print(TwoD[0][0])
print(TwoD[2][1])
print(TwoD[2,2])

print(TwoD[:2])
print(TwoD[:2,0:1])

print('-'*50)

new = np.arange(0,10)
# 0~5まで出す
slice_of_array=new[0:6]
print(slice_of_array)

# 0~5まで99に変更
slice_of_array[:]=99
print(slice_of_array)

new2 = new.copy()
print(new2)


lohit=np.arange(1,11)
print(lohit)

bool_arr=lohit>4
print(bool_arr)

lohit[bool_arr]
    
arr = np.arange(25)
ranarr=np.random.randint(0,50,10)
print(ranarr)
print(arr)
print(arr[arr<5])

from numpy.random import randint
# 3~22までランダムに出す
print(randint(3,22))

# 40個の行列、4行10列
arr_2d=np.arange(40).reshape(4,10)
print(arr_2d)

print('-'*50)

import numpy as np
# 1行の4足演算
new_array = np.arange(0,11)
print(new_array)
print(new_array+new_array)
print(new_array-new_array)
print(new_array*new_array)
print(new_array/new_array)

new=new/12
print(new)


new_array=np.arange(1,10)
new=new_array+new_array
print(new)
n=new/10
print(n)
print('-'*50)


# 2次元の行列計算
import numpy as np
TwoD = np.array([[2,3,8],[3,4,6],[2,4,6]])
print(TwoD)
print(TwoD[0][0])
print(TwoD[2][1])
print(TwoD[2,2])

print(TwoD[:2])
print(TwoD[:2,0:1])

print('-'*50)



new = np.arange(0,10)
slice_of_array=new[0:6]
print(slice_of_array)

slice_of_array[:]=99
print(slice_of_array)

new2 = new.copy()
print(new2)

lohit=np.arange(1,11)
print(lohit)

# 4より大きい数のTF確認
bool_arr=lohit>4
print(bool_arr)




lohit[bool_arr]


arr = np.arange(25)
ranarr=np.random.randint(0,50,10)
ranarr
print('ranarr: ', ranarr)
print(arr)




print('-'*50)
arr[arr<5]

#3~22の数字をランダムに出す
from numpy.random import randint
randint(3,22)

# 40個の数字の4行10列表示
arr_2d=np.arange(40).reshape(4,10)
arr_2d

print('-'*50)

import numpy as np
# 1行の配列同士の四則演算
new_array = np.arange(0,11)
print(new_array)
print(new_array+new_array)
print(new_array-new_array)
print(new_array*new_array)
print(new_array/new_array)
new=new_array+1000
print(new)

new = new_array*10
new

new=new/12
new

new_array=np.arange(1,10)
new=new_array+new_array
new
n=new/10
n

ok=np.arange(3,10)
ok

np.sqrt(ok)
print('np.sqrt(ok): ', np.sqrt(ok))
np.max(ok)
print('np.max(ok: ', np.max(ok)
np.min(ok)
print('np.min(ok: ', np.min(ok)
np.sin(ok)
print('np.sin(ok): ', np.sin(ok))
np.log(ok)
print('np.log(ok): ', np.log(ok))


log_number=np.arange(4,10)
print(np.log(log_number))



n=np.zeros(10)
print(n)

print(n+5)

print(np.ones(10)*5)

N= (np.arange(100).reshape(10,10)+1)/100
print(N)

print(np.arange(1,101).reshape(10,10)/100)

# ０～１の数字を20等分して計算
print(np.linspace(0,1,20))
# 10～50の数字を並べる
print(np.arange(10,51))

# 3行3列の計算
print(np.arange(9).reshape(3,3))

ok=np.eye(3)
print(ok)


print('np.random.rand(): ', np.random.rand())
# 0~50の数字を200等分して計算
np.linspace(0,50,200)
print('np.linspace(0,50,200): ', np.linspace(0,50,200))
# 正規分布を25個適当に配列
np.random.randn(25)
print('np.random.randn(25): ', np.random.randn(25))

# 10～50の数字を2個おきに配列、偶数の数字の配列、奇数の場合は＋１
np.arange(10,51,2)
print('np.arange(10,51,2): ', np.arange(10,51,2))

# 5行5列の25個の数字を配列
n = np.arange(25).reshape(5,5)+1
print(n)

np.arange(1,26).reshape(5,5)
print('np.arange(1,26).reshape(5,5):\n ', np.arange(1,26).reshape(5,5))


print('-'*70)
print(n[2:,1:])

np.sum(np.arange(1,26).reshape(5,5))
print('np.sum(np.arange(1,26).reshape(5,5)): ', np.sum(np.arange(1,26).reshape(5,5)))

print(n[4:5])

print(n[3:5])






np.array([[12,13,14,15],[17,18,19,20],[22,23,24,25]])

#行列から抽出
np.array(n[0:3,1:2])
print('np.array(n[0:3,1:2]): ', np.array(n[0:3,1:2]))




np.sqrt(52)
print('np.sqrt(52): ', np.sqrt(52))

ｘ

