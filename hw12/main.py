import re

#Task 1
text = "Rbbbbr, rBbBr, rBBRR, rbbr."
pattern = r'[Rr]b+r'
matches = re.findall(pattern, text)
print(matches)


#Task 2
def validate_credit_card(card_number):
    pattern = r'\d{4}-\d{4}-\d{4}-\d{4}'
    if re.search(pattern, card_number):
        return True
    else:
        return False

card_number = "1234-5678-9101-116"
if validate_credit_card(card_number):
    print(f'Card number {card_number} is valid')
else:
    print(f'Card number {card_number} is not valid')


#Task 3
def validate_mail(mail):
    pattern = r'^[\w._-]+@[\w.-]+\.[a-zA-Z]{2,}$'
    if re.search(pattern, mail):
        return True
    else:
        return False

mail = "example_123@e-mail.com"
if validate_mail(mail):
    print(f'Mail {mail} is valid')
else:
    print(f'Mail{mail} is not valid')


#Task 4
def validate_login(login):
    pattern = r'^\w{2,10}$'
    if re.search(pattern, login):
        return True
    else:
        return False

login = "abcd1234"
if validate_login(login):
    print(f'Login {login} is valid')
else:
    print(f'Login {login} is not valid')