import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "계산기"
        self.setWindowTitle(self.title)
        self.init_ui()

    def init_ui(self):
        '''
             issue #2
                1. Equation, Solution 삭제 및 하나의 LineEdit로 바꾸기
                2. 4칙연산 버튼 위치 변경하기
                3. 기존 계산기에 없는 항목(버튼)들 추가하기
                4. 모든 버튼들은 QGridLayout을 활용하여 구현
        '''
        # 2.4
        main_layout = QGridLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_equation_solution = QGridLayout()
        layout_operation1 = QGridLayout()
        layout_operation = QGridLayout()
        layout_number = QGridLayout()

        # 2.1 Equation, Solution 삭제 및 하나의 LineEdit로 바꾸기
        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        layout_equation_solution = QGridLayout()

        equation = QLabel()
        solution = QLineEdit()

        # solution.textChanged.connect(equation.setText)

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_equation_solution.addWidget(equation)
        layout_equation_solution.addWidget(solution)

        # 2.2 4칙연산 버튼 위치 변경하기
        ### 사칙연산 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_equal = QPushButton("=")

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))

        ### 사칙연산 버튼을 layout_operation 레이아웃에 추가
        layout_operation.addWidget(button_product, 0, 0)
        layout_operation.addWidget(button_minus, 1, 0)
        layout_operation.addWidget(button_plus, 2, 0 )
        layout_operation.addWidget(button_equal, 3, 0)

        # 4.3 기존 계산기에 없는 항목(버튼)들 추가하기
        button_rest = QPushButton("%")
        button_clear = QPushButton("C")
        button_c_entry = QPushButton("CE")
        button_backspace = QPushButton("Backspace")

        button_reciprocal = QPushButton("1/x") # 역수
        button_square = QPushButton("x²") # 제곱
        button_squ_root = QPushButton("²√x") # 제곱근
        button_division = QPushButton("/")

        ### 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))

        ### layout_clear_equal 레이아웃에 추가
        layout_operation1.addWidget(button_rest, 0, 0)
        layout_operation1.addWidget(button_c_entry, 0, 1)
        layout_operation1.addWidget(button_clear, 0, 2)
        layout_operation1.addWidget(button_backspace, 0, 3)
        layout_operation1.addWidget(button_reciprocal, 1, 0)
        layout_operation1.addWidget(button_square, 1, 1)
        layout_operation1.addWidget(button_squ_root, 1, 2)
        layout_operation1.addWidget(button_division, 1, 3)

        layout_operation1.addLayout(layout_operation, 2, 3, 1, 1)
        layout_operation1.addLayout(layout_number, 2, 0, 1, 3)

        ### 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                x,y = divmod(number-1, 3)
                layout_number.addWidget(number_button_dict[number], x, y)
            elif number==0:
                layout_number.addWidget(number_button_dict[number], 3, 1)

        ### 소숫점 버튼과 00 버튼을 입력하고 시그널 설정
        button_reverse = QPushButton("+/-")
        button_reverse.clicked.connect(lambda state, num = "00": self.number_button_clicked(num))
        layout_number.addWidget(button_reverse, 3, 0)

        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_number.addWidget(button_dot, 3, 2)

        # layout_number.addLayout(layout_operation, 1, 3)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution, 0, 0)
        main_layout.addLayout(layout_operation1, 1, 0)
        # main_layout.addLayout(layout_operation, 1, 0)
        # main_layout.addLayout(layout_number, 3, 0)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.equation.text()
        equation += operation
        self.equation.setText(equation)

    def button_equal_clicked(self):
        equation = self.equation.text()
        solution = eval(equation)
        self.solution.setText(str(solution))

    def button_clear_clicked(self):
        self.equation.setText("")
        self.solution.setText("")

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
