import easygui

#문장 입력 받기 : enterbox 사용
sentence = easygui.enterbox("Write a sentence.")
easygui.msgbox('You wrote " {} " '.format(sentence))

#단어 분리 : split 함수 사용
word = sentence.split(" ")

#단어 선택 : choicebox 사용
result = easygui.choicebox("Choose your word to study", choices = word)

#결과들은 msgbox로 출력 (단, 여기서 출력 시, %s 를 사용할 것)
easygui.msgbox("Today's Word : %s"%result)
