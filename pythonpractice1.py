
def is_palindrome(x):
    if test_case == test_case2:
        print("회문입니다.")
    else:
        print("회문이 아닙니다.")

test_case = list(input())
test_case2 = list(reversed(test_case))
is_palindrome(test_case)



def prime_number(a):
    is_prime_number = True
    for i in range(2,a):
        if a % i == 0:
            is_prime_number = False
            break
    return is_prime_number

test_case = int(input())
prime_number(test_case)




def my_point(x):
    combo_score = 0
    current_score = 0
    for ox in x:
        if ox == "o":
            combo_score += 1
        else:
            combo_score = 0
        current_score += combo_score
    return current_score

test_case = int(input())
for i in range(test_case):
    ox_quiz = input()
    print(my_point(ox_quiz))


def is_game(user1,user2):
    if user1 == user2:
        return "draw"
    if user1 == "rock":
        if user2 == "sci":
            return "user1 win"
        elif user2 == "paper":
            return "user2 win"
    if user1 == "sci":
        if user2 == "rock":
            return "user2 win"
        elif user2 == "paper":
            return "user1 win"
    if user1 == "paper":
        if user2 == "rock":
            return "user1 win"
        elif user2 == "sci":
            return "user2 win"

user1 = input()
user2 = input()
print(is_game(user1, user2))



def fib(x):
    a, b = 1, 1
    if x == 1 or x == 2:
        return 1
    for i in range(1,x+1):
        a, b = b, a + b
        return a

fibo = int(input())




