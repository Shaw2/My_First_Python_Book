### 1번 문제
# guest_file = 'guest.txt'
#
# with open(guest_file, 'w') as file_object:
#     name = input('사용자 이름을 입력하세요 : ')
#     file_object.write(name)

### 2번 문제
# book_file = 'guest_book2.txt'
#
# while True:
#     name = input('방명록에 이름을 남겨보세요 : ')
#     print('방문을 환영합니다~ :)')
#     with open(book_file, 'a') as file_object:
#         file_object.write(name+'\n')

### 3번 문제
survey_file = 'survey_file.txt'

while True:
    reason = input('당신은 프로그래밍을 왜 좋아하시나요?')
    with open(survey_file, 'a') as file_object:
        file_object.write(reason+'\n')