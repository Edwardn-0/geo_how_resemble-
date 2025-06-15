import numpy as np
#티킨터로 입력 이미지를 만들어서 입력하면 유사도 비교해주는 기능 추가

#저장된 이미지
Number_1 = np.array([-1, 1, -1,
                     -1, 1, -1,
                     -1, 1, -1])

Number_0 = np.array([-1, 1, -1,
                     1, -1, 1, 
                     -1, 1, -1])

#입력 이미지
input_Num = np.array([1, 1, -1, 
                      -1, 1, -1,
                      -1, 1, -1])

#내적 계산
def calc(image):
    result = 0
    for i in range(9):
        if image[i] == input_Num[i]:
            add = np.abs(image[i])*np.abs(input_Num[i])*1
            result += add
        elif image[i] != input_Num[i]:
            dele = np.abs(image[i])*np.abs(input_Num[i])*(-1)
            result += dele
    return result

input_1 = calc(Number_1)
input_0 = calc(Number_0)

#유사도 비교 후 출력
if input_1 > input_0:
    print(f'숫자 1과 더 유사합니다 ({input_1}>{input_0})')
elif input_1 < input_0:
    print(f'숫자 0과 더 유사합니다 ({input_1}<{input_0})')
else:
    print(f'숫자 1, 0 모두와 유사합니다 ({input_1}={input_0})')