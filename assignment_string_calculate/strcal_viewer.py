from strcal_ErrorClass import ErrorClass

class CalculatorView:
    def get_user_input(self):
        formula = input("계산할 식을 입력하세요: ")
        return formula

    def show_result(self, result):
        print(f"결과: {result}")

    def calculate_error(self, message):
        return ErrorClass.CannotCalculate
