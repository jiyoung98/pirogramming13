word = input()

croatias = ("c=","c-","dz=","d-","lj","nj","s=","z=")

for croatia in croatias:
    word = word.replace(croatia, "0") #replace는 자체를 변환하는게 아니라 변환시킨 새로운 문자열을 반환

print(len(word))