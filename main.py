def main():
    balance = 0 # 보유금액 변수 지정 및 0으로 초기값을 준다.
    max_money = float('-inf') # 가장 큰 값을 저장하기 위한 변수를 음의 무한대로 초기화한다.
    min_money = float('inf') # 가장 작은 값을 저장하기 위한 변수를 양의 무한대로 초기화한다.

    while True: # 값이 True일 때까지 계속 반복한다.
        print("1 : 더하기 / 2 : 빼기 / 3 : 최대값 / 4 : 최소값 / 5 : 종료 / 6 : 도움") # 1은 더하기, 2는 빼기, 3은 최대값 출력, 4는 최소값 출력 5는 프로그램 종료, 6은 도움 출력
        print(f"현재 보유금액은 {balance}입니다.") # 보유금액을 먼저 출력한다.
        want = input("원하는 작업 번호를 선택하세요: ") # want변수를 지정하고 input을 이용해서 번호를 받는다.

        if want == '1': # want의 값이 1일 때 사용된다.
            money = float(input("금액을 입력하세요: ")) # money변수를 지정하고 float으로 실수형을 받고 input으로 money 변수에 값을 넣는다.
            balance += money  # 보유금액인 balance와 money를 더한다.
            max_money = max(max_money, money) # 입력받은 금액이 현재까지의 최대값보다 큰 경우 업데이트한다.
            min_money = min(min_money, money) # 입력받은 금액이 현재까지의 최소값보다 작은 경우 업데이트한다.
            print(f"현재 보유금액은 {balance}입니다.")  # 보유금액을 출력한다.
        elif want == '2': # want의 값이 2일 때 사용된다.
            money = float(input("금액을 입력하세요: "))  # money변수를 지정하고 float으로 실수형을 받고 input으로 money 변수에 값을 넣는다.
            if money > balance: # 입력받은 money의 값이 balance 즉 보유금액 보다 작을 경우를 뜻한다.
                print("잔액이 부족합니다.") # 보유금액이 마이너스가 될 수 없기 때문에 잔액이 부족하다고 뜬다.
            else: # 보유금액에서 입력받은 값을 뺄 수 있을 때
                balance -= money # 보유금액인 balance에서 입력받은 money를 뺀다.
                max_money = max(max_money, money) # 입력받은 금액이 현재까지의 최대값보다 큰 경우 업데이트한다.
                min_money = min(min_money, money) # 입력받은 금액이 현재까지의 최소값보다 작은 경우 업데이트한다.
                print(f"현재 보유금액은 {balance}입니다.")  # 보유금액을 출력한다.
        elif want == '3': # want의 값이 3일 때 사용된다.
            print(f"입력된 금액 중 가장 큰 값은 {max_money}입니다.")  # 가장 큰 값을 출력한다.
        elif want == '4': # want의 값이 4일 때 사용된다.
            print(f"입력된 금액 중 가장 작은 값은 {min_money}입니다.")  # 가장 작은 값을 출력한다.
        elif want == '5': # want의 값이 5일 때 사용된다.
            print("프로그램을 종료합니다.") # 프로그램을 종료합니다.가 출력된다.
            break  # 프로그램을 종료한다.
        elif want == '6':  # want의 값이 6일 때 사용된다.
            print("도움말: 프로그램은 다음과 같은 기능을 제공합니다.")  # 문장을 프린트한다.
            print("1 : 더하기 - 금액을 보유금액에 추가합니다.")  # 문장을 프린트한다.
            print("2 : 빼기 - 금액을 보유금액에서 차감합니다.")  # 문장을 프린트한다.
            print("3 : 최대값 - 입력된 금액 중 가장 큰 값을 출력한다..")  # 입력받은 가장 큰 금액을 출력한다.
            print("4 : 최소값 - 입력된 금액 중 가장 작은 값을 출력한다.")  # 입력받은 가장 작은 금액을 출력한다.
            print("5 : 종료 - 프로그램을 종료합니다.")  # 문장을 프린트한다.
            print("6 : 도움 - 이 도움말을 표시합니다.")  # 문장을 프린트한다.
        else:  # want의 값이 1,2,3,4,5,이가 아닌 다른 것일 경우에 작동한다.
            print("잘못된 선택입니다. 다시 시도하세요.")  # 프린트한다.

if __name__ == "__main__":
    main()
