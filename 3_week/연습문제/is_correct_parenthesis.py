# Q. 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻이다. 예를 들어
# ()() 또는 (())() 는 올바르다.
# )()( 또는 (()( 는 올바르지 않다.
# 이 때, '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 True 를 반환하고 아니라면 False 를 반환하시오.

"(())()" # True
"(((("   # False

#내풀이
#스택을 이용
#스택에 ( 만 집어넣을 수 있도록 하고 ) 이 나오면 스택에서 ( 을 pop 함.
#이때 아무것도 없는 스택에 ) 이 들어오면 그 즉시 False
#배열이 끝난 후 스택에 아무것도 남아있지 않으면 True
def is_correct_parenthesis_1(string):
    # 구현해보세요!
    stack = []
    for chr in string:
        if chr == '(':
            stack.append(chr)
        elif chr == ')':
            if stack:
                stack.pop()
            else:
                return False

    if stack:
        return False

    return True


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis_1("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis_1(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis_1("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis_1("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis_1("((())"))