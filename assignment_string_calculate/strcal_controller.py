from strcal_model import CalculatorModel
from strcal_viewer import CalculatorView
from strcal_ErrorClass import ErrorClass

class CalculatorController:
    def __init__(self):
        self.model = CalculatorModel()  # 모델 초기화
        self.view = CalculatorView()    # 뷰 초기화

    def run(self):
        while True:
            user_input = self.view.get_user_input() # 사용자로부터 수식 입력 받기
            if user_input == 'quit':
                break # 실행 중인 코드 나갈려면 quit 입력

            try:
                self.model.expression_setting(user_input) # 모델에 입력한 수식 넣기
                result = self.model.check_calculate()  # 모델에서 계산 수행
                self.view.show_result(result)             # 계산 결과 뷰에서 수행
            except ValueError:
                raise ErrorClass.CannotCalculate

if __name__ == "__main__":
    controller = CalculatorController()
    controller.run()
