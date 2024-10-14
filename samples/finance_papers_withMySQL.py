import pymysql

# 데이터베이스 연결 설정
conn = pymysql.connect(
    host='python_mysql_mysql',  # 컨테이너 이름 또는 IP 주소
    user='cocolabhub',
    password='cocolabhub',
    db='python_mysql',  # 데이터베이스 이름
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with conn.cursor() as cursor:
        # 질문 데이터
        questions = [
            {
                "question": "정기 예금의 주요 특징은 무엇인가요?",
                "options": ["A. 높은 유동성", "B. 고정 금리", "C. 만기 기간 없음", "D. 높은 위험"],
                
            },
            {
                "question": "다음 중 정부가 발행하는 증권 유형은 무엇인가요?",
                "options": ["A. 국채", "B. 회사채", "C. 뮤추얼 펀드", "D. 정기 예금"],
                
            },
            {
                "question": "대출에서 APR은 무엇의 약자인가요?",
                "options": ["A. 연이율", "B. 평균 지급률", "C. 누적 지급 비율", "D. 연간 지급 비율"],
                
            },
            {
                "question": "다음 중 가장 안전한 투자 옵션은 무엇인가요?",
                "options": ["A. 주식", "B. 채권", "C. 저축 계좌", "D. 부동산"],
                
            },
            {
                "question": "복리의 주요 이점은 무엇인가요?",
                "options": ["A. 세금 절감", "B. 빠른 자산 축적", "C. 유동성 증가", "D. 고정 금리"],
                
            }
        ]

        # RESPONDENTS 테이블에 응답자 정보 삽입
        sql = "INSERT INTO RESPONDENTS (RESPONDENT_NO) VALUES (%s), (%s)"
        cursor.execute(sql, ('정지호', '정진겸'))
        conn.commit()

        # QUESTIONS 테이블에 질문 정보 삽입
        for i, q in enumerate(questions):
            sql = "INSERT INTO QUESTIONS (question_no, question_content) VALUES (%s, %s)"
            cursor.execute(sql, (f'Q{i+1}', q['question']))
        conn.commit()

        # REPLIES 테이블에 답변 정보 삽입
        replies = [
            ('R1', 'Q1', '정지호', 'B'),
            ('R2', 'Q2', '정지호', 'A'),
            ('R3', 'Q3', '정지호', 'A'),
            ('R4', 'Q4', '정지호', 'C'),
            ('R5', 'Q1', '정진겸', 'D'),
            ('R6', 'Q2', '정진겸', 'A'),
            ('R7', 'Q3', '정진겸', 'A'),
            ('R8', 'Q4', '정진겸', 'D'),
            ('R9', 'Q5', '정진겸', 'D')
        ]
        sql = "INSERT INTO REPLIES (replies_no, question_no, respondent_no, answer) VALUES (%s, %s, %s, %s)"
        cursor.executemany(sql, replies)
        conn.commit()

finally:
    conn.close()
    