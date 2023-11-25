def monthly_payment_plan(principle, interest, year):
    r = (interest / 12) / 100
    m = year * 12
    return ((1 + r) ** m * principle * r) / ((1 + r) ** m - 1)

print('자유은행 대출 상관금 계산 서비스에 오심을 환영합니다.')
principle = int(input('대출원금이 얼마인가요? (백만원 이상) '))
interest = float(input('연 이자율은 몇 %인가요? (0.0~9.9) '))
year = int(input('상환기간은 몇 년인가요? '))

result = monthly_payment_plan(principle, interest, year)

print('대출 상관금 내역을 알려드리겠습니다')
print('대출원금: ' + str(principle) + ' 원')
print('연 이자율 ' + str(interest) + ' 매월 ' + str(int(result)) +' 원씩 지불하셔야 합니다')
print('상환 완료시까지 총 상환금액은 ' + str(int(result * year * 12)) + ' 원입니다')
print('\n')
print('저희 자유은행은 항상 여러분과 함께 합니다')
print('또 들려주세요.')