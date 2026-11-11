def apply_student_discount(total, is_student):
    if is_student:
        return total * 0.90
    return total

if __name__ == "__main__":
    print(apply_student_discount(100, True))   #学生，输出90
    print(apply_student_discount(100, False))  #非学生，输出100
