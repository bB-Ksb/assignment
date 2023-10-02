import random


# 에러 다루는 class
class ErrorClass:
    class LowMovementError(Exception):  # 입력한 이동 횟수 적은 경우
        def __init__(self, message="이동 횟수는 1 이상이어야 합니다."):
            self.message = message
            super().__init__(self.message)  # 이렇게 작성하는 게 맞는지? 싶습니다... 부모 class 상속을 위해 super.__init__사용

    class NoWinner(Exception):  # 승리자가 없는 경우
        def __init__(self, message="승리한 자동차가 없습니다."):
            self.message = message
            super().__init__(self.message)



class Car:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    # 나아가는 횟수 랜덤으로 정하는 메서드
    def move(self):
        random_value = random.randint(0, 9)
        if random_value >= 4:
            self.distance += 1

    @staticmethod
    def get_valid_car_names(self):
        while True:
            car_names_input = input("경주할 자동차 이름을 입력하세요 (이름은 쉼표(,)로 구분):\n")
            car_names_list = car_names_input.split(',')  # 쉼표로 구분

            valid_names = []  # 유효 이름
            invalid_names = []  # 무효 이름

            for car_name in car_names_list:
                car_name = car_name.strip()
                if len(car_name) <= 5:
                    valid_names.append(car_name)
                else:
                    invalid_names.append(car_name)

            if len(invalid_names) != 0:
                for name in invalid_names:
                    print(f"유효하지 않은 자동차 이름: {name} (5자 이상 규칙 미준수)")
                continue

            if valid_names:
                return valid_names  # 유효한 자동차 이름 return

# main 사용 익숙해지기
def main():
    try:
        car_names = Car("").get_valid_car_names()  # 유효한 자동차 이름 출력

        # 게임 횟수 정하기
        how_much_car_play = int(input(f"시도할 회수는 몇 회인가요?\n"))
        if how_much_car_play <= 0:
            raise ErrorClass.LowMovementError()

        cars = []  # 가져온 자동차 이름 요소마다 풀어주기
        for name in car_names:
            car = Car(name)
            cars.append(car)

        # 게임 시작
        for play_game in range(how_much_car_play):
            for car in cars:  # 자동차 각각에 대해서
                car.move()  # 랜덤 값만큼 자동차 움직이기
                print(f"{car.name}: {'-' * car.distance}")
            print()  # 각 이동 사이에 빈 줄 출력

        # 승리 조건 작성하기
        max_distance = 0
        for car in cars:
            if car.distance > max_distance:
                max_distance = car.distance
        winner_cars = []  # 승리 자동차 리스트
        for car in cars:
            if car.distance == max_distance:
                winner_cars.append(car.name)

        # 마지막 경기 결과
        print("\n경주 결과:")
        for car in cars:
            print(f"{car.name}: {'-' * car.distance}")

        if winner_cars:
            print("\n우승자: ", end="")
            for won_car in range(len(winner_cars)):
                if won_car > 0:
                    print(", ", end="")
                print(winner_cars[won_car], end="")
            print()
        elif not winner_cars:  # else 사용 최대한 지양
            raise ErrorClass.NoWinner()

    except TypeError:
        print(f"입력 에러 발생")


if __name__ == "__main__":
    main()
