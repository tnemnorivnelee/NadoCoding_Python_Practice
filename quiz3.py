# Quiz 3) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

# ex) http://naver.com
# 규칙 1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성 (nav51!)

site = "http://naver.com"

# rule1 = site[-9:]
rule1 = site.replace("http://", "")

firstDot = rule1.index(".")

rule2 = rule1[:firstDot]

thirdString = rule2[:3]

stringLen = len(rule2)

eCount = rule2.count("e")

rule3 = thirdString + str(stringLen) + str(eCount) + "!"

print(rule3)