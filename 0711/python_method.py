# string
ex_str = "Hi I'm jiyoung, I'm a frontend developer"

# --------------------------------------------- #

# find/index
find_str = ex_str.find('jiyoung')
index_str = ex_str.index('jiyoung')
print(find_str,index_str)
find_str = ex_str.find('piro')
# index_str = ex_str.index('piro')
print(find_str) # find는 없는 값을 찾을 시 -1를 반환. 차이 알고 find 사용하기!
# print(index_str) # index는 없는 값을 찾을 시 substring not found 에러 뜸.

# index함수를 죽어도 쓰고 싶으면 아래와 같이 예외처리해줄 수 있다.
try:
    index_str = ex_str.index('piro')
    print(index_str)
except Exception as e:
    index_str = -1
    print(index_str,e) #예외처리할때는 이렇게 error 프린트해주는 것이 좋다

# --------------------------------------------- #

# split
splitted_list = ex_str.split(" ")
print(splitted_list)

# --------------------------------------------- #

# join
joined_str = '-'.join(splitted_list)
print(joined_str)

# --------------------------------------------- #

# replace
replaced_str = ex_str.replace("jiyoung","piro")
print(replaced_str)

# --------------------------------------------- #

# strip
text = "                    data       data           "
print(text.strip()) # 안쪽 공백은 유지됨. 안쪽까지 없애고 싶다면?
print(text.replace(" ",""))

# --------------------------------------------- #

# f string(파이썬 3.6부터). .format()보다 f string 활용할 것!
print(f'{text} 입니다')

name="지영"
job="프론트엔드"
age=25

# 안녕하세요. 개발자 한지영입니다. 라고 출력하고 싶다면?(f string 추가)
print("안녕하세요 {} 개발자 {} 입니다.".format(job,name))
print("안녕하세요 {job} 개발자 {name}입니다.".format(name=name, job=job))
print(f'안녕하세요 {job} 개발자 {name}입니다.') #편리!

# --------------------------------------------- #

# extend - 원본 데이터가 변형됨에 주의!
list1 = [1,2,3]
list2 = [4,5]
list1.extend(list2)
print(list1)
list3 = list1.extend(list2)
print(list3) #list3은 list1을 조작하는 것일뿐 return값은 없다. 따라서 list3=None.

# --------------------------------------------- #

# 딕셔너리
ex_dic = {
    "name":"jiyoung",
    "age":23,
    "job":"developer"
}

ex_dic["address"] = "잠실" #딕셔너리에 없는 키값쌍 추가
ex_keys = list(ex_dic.keys()) #반환값이 리스트가 아님을 주의. 리스트로 변환을 해야 사용 가능
print(ex_keys)

ex_values = list(ex_dic.values())
print(ex_values)

ex_items = list(ex_dic.items())
print(tuple(ex_items)) #tuple이 list보다 메모리 등 면에서 좋다

# --------------------------------------------- #

# lambda
# 익명함수 -> 함수인데 이름이 없다.
# 함수 호출 방법 -> 이름을 쓰고 인자를 준다.
# 사용 시기 : 간단한 함수 or 인라인에 사용할 때
# 그러나 람다 사용은 비추 -> 가독성이 떨어짐

print((lambda x, y:x+y)(1,2))

#x: <- 람다함수가 파라미터를 하나만 받는 경우 x, y: <- 파라미터 두개받는 경우
# : 뒤에는 리턴값. 여기서는 x+y
# (lambda x, y:x+y) <-여기가 함수의 선언
# (1,2) <-여기가 함수의 실행

# 해석
def sum(x, y):
    return(x+y)
print(sum(1,2)) #이것을 축약해서 쓴게 람다함수식

# --------------------------------------------- #

# map
# map -> list -> func(item) -> result_list
# map(function,list) - map은 list의 요소들을 순회하며 function에 넣어 수행한다.
# 이 function의 수행결과를 반환해 주는 것이 map. map object로 반환되기 때문에 list()로 감싸줘야함.

numbers = [1,2,3,4,5]
ex_map_1 = list(map(str, numbers))
print("map 1",ex_map_1)

ex_map_2 = list(map(lambda number:number+10,numbers)) #lambda + map 조합
print("map 2",ex_map_2)

# --------------------------------------------- #

# filter #map은 item개수와 인자의 개수가 동일. filter는 인자의 개수를 바꿀 수 있음. 대신 값은 못바꿈.

target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(n):
    return True if n % 2 == 0 else False

result = filter(is_even, target)

print(list(result))