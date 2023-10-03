class ErrorClass:
    class IllegalArgumentException(Exception):
        def __init__(self, msg = "올바른 연산식이 아닙니다."):
            self.msg = msg
            super().__init__(self.msg)

    class CannotCalculate(Exception):
        def __init__(self, msg = "계산할 수 없는 오류"):
            self.msg = msg
            super().__init__(self.msg)

    class VoidFormula(Exception):
        def __init__(self, msg = "수식이 비어있습니다."):
            self.msg = msg
            super().__init__(self.msg)

    class IncorrectOperator(Exception):
        def __init__(self, msg = "올바른 연산자가 아닙니다."):
            self.msg = msg
            super().__init__(self.msg)

    class IncorrectOperand(Exception):
        def __init__(self, msg = "해당 숫자로는 식 계산 불가능"):
            self.msg = msg
            super().__init__(self.msg)