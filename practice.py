# weather = input("오늘 날씨는 어때요? ")

# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("오늘은 준비물이 필요없어요")

# temp = int(input("기온은 어때요? "))

# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_no in range(1, 6): # 1,2,3,4,5
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]

# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다".format(customer))

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요".format(customer, index))
#     index += -1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다")

# customer = "아이언맨"
# index = 0
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")
    
# absent = [2, 5] # 결석
# no_book = [7] # 책이 없음

# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업은 여기까지. {0}은 교무실로 따라와!".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

students = [1,2,3,4,5]
print(students)

students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)
