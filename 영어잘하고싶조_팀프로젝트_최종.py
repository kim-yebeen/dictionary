import random
import os
import pprint
import turtle as t
import time

# 영어 -> 뜻 확인할 시험에 필요한 단어 리스트
words_dict1 = {'resume' : '이력서',
               'opening' : '공석,개장',
               'applicant' : '지원자,신청자',
               'requirement' : '필요조건,요건',
               'meet' : '만족시키다',
               'qualified' : '자격 있는,적격의',
               'candidate' : '후보자,지원자',
               'confidence' : '확신,신임',
               'highly' : '매우,대단히',
               'professional' : '직업의,전문가',
               'interview' : '면접',
               'hire' : '고용하다',
               'training' : '교육,훈련',
               'reference' : '추천서',
               'position' : '두다,일자리',
               'achievement' : '성취,달성',
               'impressed' : '인상 깊게 생각하는,감명을 받은',
               'excellent' : '훌륭한,탁월한',
               'eligible' : '자격이 있는,적격의',
               'identify' : '알아보다,확인하다',
               'associate' : '관련시키다',
               'condition' : '조건',
               'employment' : '고용',
               'lack' : '~이 없다',
               'managerial' : '관리의',
               'diligent' : '성실한',
               'familiar' : '익숙한,친숙한',
               'proficiency' : '숙달,능숙',
               'prospective' : '장래의,미래의',
               'appeal' : '관심을 끌다,매력적이다',
               'specialize' : '~을 전공하다,전문적으로 다루다',
               'apprehensive' : '걱정하는,염려하는',
               'consultant' : '고문,컨설턴트',
               'entitle' : '자격을 주다',
               'degree' : '학위',
               'payroll' : '임금 대장,급료 명부',
               'recruit' : '모집하다',
               'certification' : '증명서,증명',
               'occupation' : '직업',
               'wage' : '임금,급료'
                }

my_dict = {}

# 뜻 -> 영어 확인할 시험에 필요한 단어 리스트
words_dict2 = {'이력서' : 'resume',
               '공석,개장' : 'opening',
               '지원자, 신청자' : 'applicant',
               '필요조건,요건' : 'requirement',
               '만족시키다' : 'meet',
               '자격 있는,적격의' : 'qualified',
               '후보자,지원자' : 'candidate',
               '확신,자신' : 'confidence',
               '매우,대단히' : 'highly',
               '직업의,전문가' : 'professional',
               '면접' : 'interview',
               '고용하다' : 'hire',
               '교육,훈련' : 'training',
               '추천서' : 'reference',
               '두다,일자리': 'position',
               '성취,달성' : 'achievement',
               '인상 깊게 생각하는,감명을 받은' : 'impressed',
               '훌륭한,탁월한' : 'excellent',
               '자격이 있는,적격의' : 'eligible',
               '알아보다' : 'identify',
               '관련시키다' : 'associate',
               '조건' : 'condition',
               '고용' : 'employment',
               '~이 없다' : 'lack',
               '관리의' : 'managerial',
               '성실한' : 'diligent',
               '익숙한,친숙한' : 'familiar',
               '숙달,능숙' : 'proficiency',
               '장래의,미래의' : 'prospective',
               '관심을 끌다,매력적이다' : 'appeal',
               '~을 전공하다,전문적으로 다루다' : 'specialize',
               '걱정하는,염려하는' : 'apprehensive',
               '고문,컨설턴트' : 'consultant',
               '자격을 주다' : 'entitle',
               '학위' : 'degree',
               '임금 대장,급료 명부' : 'payroll',
               '모집하다' : 'recruit',
               '증명서,증명' : 'certification',
               '직업' : 'occupation',
               '임금,급료' : 'wage'
               }

while True:                                   #while문을 이용하여 반복
    user_choose = input('원하시는 번호를 입력하세요 1) Eating English(터틀게임)  2) 뜻 맞추기  3) 영단어 맞추기  4) 나만의 단어장  5) 종료: ')
    print()
    os.system('cls')                          # 앞선 화면 지우기
    if user_choose == '1':                    # 1번을 입력했을 경우 -> turtle로 단어 학습
        
        playing = False  # 현재 게임이 플레이중인지 확인
        word = {'resume' : '이력서',
               'opening' : '공석,개장',
               'applicant' : '지원자,신청자',
               'requirement' : '필요조건,요건',
               'meet' : '만족시키다',
               'qualified' : '자격 있는,적격의',
               'candidate' : '후보자,지원자',
               'confidence' : '확신,신임',
               'highly' : '매우,대단히',
               'professional' : '직업의,전문가',
               'interview' : '면접',
               'hire' : '고용하다',
               'training' : '교육,훈련',
               'reference' : '추천서',
               'position' : '두다,일자리',
               'achievement' : '성취,달성',
               'impressed' : '인상 깊게 생각하는,감명을 받은',
               'excellent' : '훌륭한,탁월한',
               'eligible' : '자격이 있는,적격의',
               'identify' : '알아보다,확인하다',
               'associate' : '관련시키다',
               'condition' : '조건',
               'employment' : '고용',
               'lack' : '~이 없다',
               'managerial' : '관리의',
               'diligent' : '성실한',
               'familiar' : '익숙한,친숙한',
               'proficiency' : '숙달,능숙',
               'prospective' : '장래의,미래의',
               'appeal' : '관심을 끌다,매력적이다',
               'specialize' : '~을 전공하다,전문적으로 다루다',
               'apprehensive' : '걱정하는,염려하는',
               'consultant' : '고문,컨설턴트',
               'entitle' : '자격을 주다',
               'degree' : '학위',
               'payroll' : '임금 대장,급료 명부',
               'recruit' : '모집하다',
               'certification' : '증명서,증명',
               'occupation' : '직업',
               'wage' : '임금,급료'}

        ts = t.Turtle()  # 먹이(초록 동그라미)
        ts.shape("circle")
        ts.color("green")
        ts.speed(0)
        ts.up()
        ts.goto(0, -200)


        def turn_right():  # 오른쪽으로 방향을 바꿈
            t.setheading(0)


        def turn_up():  # 위로 방향을 바꿉니다.
            t.setheading(90)


        def turn_left():  # 왼쪽으로 방향을 바꿉니다.
            t.setheading(180)


        def turn_down():  # 아래로 방향을 바꿉니다.
            t.setheading(270)


        def start():  # 게임을 시작하는 함수
            global playing

            if playing == False:
                playing = True
                t.clear()  # 메시지를 지웁니다.
                play()


        def play():  # 게임을 실제로 플레이하는 함수
            global playing
            t.forward(10)  # 주인공 거북이 10만큼 앞으로 이동합니다.

                
            if t.distance(ts) < 12:  # 주인공과 먹이의 거리가 12보다 작으면(가까우면)
                
                itemlist = word.items()

                t.write(word.popitem(), font=("",10 , "bold"))  # 의미를 화면에 표시합니다.
                
                star_x = random.randint(-220, 220)
                star_y = random.randint(-220, 220)
                ts.goto(star_x, star_y)  # 먹이를 다른 곳으로 옮깁니다.

            
                
            if playing:
                t.ontimer(play, 100)  # 게임 플레이 중이면 0.1초 후

                # play 함수를 실행합니다.

        def blank():
            global playing
            message("화면 정리","\n계속하고 싶으시다면 \n메세지 창이 사라진 뒤에 space를 누르세요 \n종료를 원하시면 마우스를 클릭하세요,")
            playing = False
            time.sleep(3)
            t.clear()
            
           
        def message(m1, m2):  # 메시지를 화면에 표시하는 함수
            t.clear()
            t.goto(0, 100)
            t.write(m1, False, "center", ("", 20))
            t.goto(0, -100)
            t.write(m2, False, "center", ("", 15))
            t.home()


        t.title("Eating English")
        t.setup(600, 600)
        t.bgcolor("orange")
        t.shape("turtle")  # 거북이 모양의 커서를 사용합니다.
        t.speed(0)  # 거북이 속도를 설정합니다.
        t.up()
        t.color("white")
        t.onkeypress(turn_right, "Right")  # →를 누르면 turn_right 함수를 실행합니다.
        t.onkeypress(turn_up, "Up")
        t.onkeypress(turn_left, "Left")
        t.onkeypress(turn_down, "Down")
        t.onkeypress(start, "space")
        t.onkeypress(blank,"Escape")
        t.listen()  # 거북이 그래픽 창이 키보드 입력을 받도록 합니다.
        message("Word Turtle Run", "[Space]를 누르면 시작됩니다.\n 화면 정리를 원하시면 Esc를 누르세요. \n종료를 원하시면 마우스를 클릭하세요.")
        t.exitonclick()
        
        
    elif user_choose == '2':                      # 2번을 입력했을 경우 영어 -> 뜻 시험 출력
        if len(words_dict1) == 0:
            print('학습이 완료되었습니다')
        else:
            print('단어시험을 시작합니다. (두 개의 뜻을 알고 있다면 뜻 사이에 \",\" 를 입력하세요.)')
            print('-' * 78)

            words1 = []                       # 빈 리스트 생성

            #빈 words1 리스트에 영단어 추가
            for word1 in words_dict1:
                words1.append(word1)

            random.shuffle(words1)             # 리스트 항목 섞기

           
            #words1 리스트 내 단어갯수만큼 랜덤퀴즈 반복
            for i in range(0, len(words1)):
                q1 = words1[i]
                user_input1 =  str(input('{} 영단어의 뜻을 입력하세요 >> '.format(q1)))
                english1 = words_dict1[q1].split(',')
                english2 = words_dict1[q1]

                #정답 및 오답 입력에 따른 문구 출력
                
                #뜻을 하나만 입력했을 경우도 정답처리
                if user_input1 in english1:
                    print('\033[33m'+"정답입니다."+'\033[0m')
                    print()
                    # 맞았다면 나만의 단어장에 저장된 단어 제외
                    del(words_dict1[q1])
                    if my_dict.get(q1):
                        del(my_dict[q1])
                        
                #뜻 전체를 입력했을 경우 정답처리
                elif user_input1 == english2 :
                    print('\033[33m'+"정답입니다."+'\033[0m')
                    print()
                    # 맞았다면 나만의 단어장에 저장된 단어 제외
                    del(words_dict1[q1])
                    if my_dict.get(q1):
                        del(my_dict[q1])
                    
                else: 
                    print('\033[31m' + '틀렸습니다.'+ '\033[0m')
                    print('정답은 {} 입니다.'.format(english1))
                    print()
                    # 나만의 단어장에 틀린 영단어 저장
                    if (q1 in my_dict)==False:
                        my_dict[q1]=words_dict1[q1]
                    
                                 
            print('모든 문제를 다 풀었습니다.')
            print('-'*50)
            print('단어시험을 종료합니다. 수고하셨습니다.')

    elif user_choose == '3':                       # 3번 입력했을 경우 뜻 -> 영어 시험 출력
        if len(words_dict2)==0:
            print('학습이 완료되었습니다')
        else:
            print('단어시험을 시작합니다. ')
            print('-' * 78)

            words2  = []

            for word2 in words_dict2:
                words2.append(word2)

            random.shuffle(words2)                # 리스트 항목 섞기

            for i in range(0, len(words2)):
                q2 = words2[i]
                user_input2 =  str(input("'{}' 라는 뜻을 가진 영단어를 입력하세요 >> ".format(q2)))
                english2 = words_dict2[q2].split(',')

                if user_input2 in english2 :
                    print('\033[33m'+"정답입니다."+'\033[0m')
                    print()
                    # 맞았다면 나만의 단어장에 저장된 단어 제외
                    del(words_dict2[q2])
                    if (user_input2 in my_dict)==True:
                        del my_dict[user_input2]
                        
                else: 
                    print('\033[31m' + '틀렸습니다.'+ '\033[0m')
                    print("정답은 {} 입니다.".format(english2))
                    print()
                    # 나만의 단어장에 틀린 영단어 저장
                    if (words_dict2[q2] in my_dict) == False:
                        my_dict[words_dict2[q2]] = q2
                                       
            print("모든 문제를 다 풀었습니다.")
            print("-"*50)
            print("단어시험을 종료합니다.수고하셨습니다.")

    elif user_choose == '4':                            # 4번 입력했을 경우 나만의 단어장 출력
        print('[나만의 단어장]')
        
        pprint.pprint(my_dict)
        print()

    elif user_choose == '5':                            # 5번 입력했을 경우 종료
        break

    else:                                               # 다른 번호를 입력했을 경우 다시 입력받기
        print("다시 입력하세요.")
        print()
        continue
    
