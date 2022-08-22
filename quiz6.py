# Quiz 6) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 체중 : 각 개인의 키에 적당한 체충

# (성별에 따른 공식)
# 남자 : 키(m) X 키(m) X 22
# 여자 : 키(m) X 키(m) X 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
#     * 함수명 : std_weight
#     * 전달값 : 키(height), 성별(gender)

# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

# def std_weight(height, gender):
#     if gender == "남자":
#         print("키 {0}cm 남자의 표준 체중은 {1:.2f}kg 입니다.".format(height, height*height*22/10000))
#     elif gender == "여자":
#         print("키 {0}cm 여자의 표준 체중은 {1:.2f}kg 입니다.".format(height, height*height*21/10000))
#     else:
#         print("성별을 다시 입력해주세요.")

# std_weight(175, "남자")
# std_weight(150, "여자")

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    elif gender == "여자":
        return height * height * 21
    else:
        print("성별을 다시 입력해주세요.")

height = 175
gender = "남자"
# weight = std_weight(height / 100, gender)
# print("키 {0}cm {1}의 표준 체중은 {2:.2f}kg 입니다.".format(height, gender, weight))

weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

