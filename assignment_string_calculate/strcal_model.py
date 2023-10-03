from strcal_ErrorClass import ErrorClass

class CalculatorModel:
    def __init__(self):
        self.expression = ""

    def expression_setting(self, expression): # 입력 받은 식 캡슐화 작업
        self.expression = expression

    @staticmethod
    def calculate(input_calculation):
        if not input_calculation:
            raise ErrorClass.VoidFormula # 식을 입력하지 않음
        """
        # 이렇게 작성할 수도 있다는 걸 알지만 eval은 지양하라고 배워서 다르게 작성했습니다.
        try:
            result = eval(self.expression)
            return result
        except:
            raise ErrorClass.IncorrectOperator
        """

        operator = []
        operand = []

        elements = input_calculation.split()
        for element in elements:
            if element.isdigit() or (elements[0] == '-' and element[1:].isdigit()): # 숫자인지 확인
                operand.append(float(element)) # 피연산자 받기
            elif element in ['+', '-', '*', '/']:
                while( # 계산 순서 정해주기
                    operator
                    and operator[-1] in ['+', '-']
                    and (element in ['*', '/'] or element == operator[-1])
                ):
                    operand.append(operator.pop())
                operator.append(element)
            else:
                raise ErrorClass.IncorrectOperator

            stack = []
            # 계산 준비, 계산
            for element in operand:
                if isinstance(element, float):
                    stack.append(element)
                else:
                    if len(stack) < 2:
                        raise ErrorClass.IllegalArgumentException

                num_b = stack.pop()
                num_a = stack.pop()

                if element == '+':
                    stack.append(num_a+num_b)
                elif element == '-':
                    stack.append(num_a-num_b)
                elif element == '*':
                    stack.append(num_a*num_b)
                elif element == '/':
                    if num_b == 0:
                        raise ErrorClass.IncorrectOperand
                    stack.append(num_a/num_b)

            if len(stack) == 1:
                return stack[0]
            elif len(stack) != 1: # else를 안 쓰려고 노력
                raise ErrorClass.IllegalArgumentException

        """
        # 해당 코드는 입력 받은 식이 float로 변환 시키면서 오류가 났습니다. 어떻게 고칠지 고민 중입니다...
        result = float(input_calculation[0])
        operator = None # 초기 연산자 변수 none으로 선언

        for number in input_calculation[1:]: # 연산자 기준으로 분리한 숫자만큼 반복문 돌리기
            if number in ['+','-','*','/']: # 연산자 분리
                operator = number
            else:
                operand = float(number) # 피연산자 처리
                if operator == "+":
                    result += operand
                elif operator == '-':
                    result -= operand
                elif operator == '*':
                    result *= operand
                elif operator == '/':
                    result /= operand
                else:
                    raise ErrorClass.IncorrectOperator # 잘못된 연산자 오류
        return str(result)
        """

    def check_calculate(self): # 연산식 맞는지 확인
        try:
            # numbers = self.numberize(self.expression)
            results = self.check_calculate()
            return results
        except ValueError:
            raise ErrorClass.IllegalArgumentException

    def numberize(self, expression): # 입력받은 문자열 수식을 공백을 기준으로 숫자 분리
        return expression.split()
