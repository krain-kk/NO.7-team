class Checkout:
    def __init__(self):
        # 学生折扣比例 10%
        self.student_discount_rate = 0.10

    def calculate_student_discount(self, total_amount: float, is_student: bool) -> float:
        """
        计算折扣后金额
        :param total_amount: 原始总价
        :param is_student: 是否是符合条件的学生客户
        :return: 折扣后应付金额
        """
        if is_student:
            discount = total_amount * self.student_discount_rate
            final_amount = total_amount - discount
        else:
            final_amount = total_amount
        return final_amount

    def checkout(self, items: list, is_student: bool) -> dict:
        """
        结账主函数
        :param items: 商品价格列表
        :param is_student: 是否学生
        :return: 结账结果字典
        """
        subtotal = sum(items)
        final_price = self.calculate_student_discount(subtotal, is_student)
        return {
            "subtotal": round(subtotal, 2),
            "is_student": is_student,
            "discount_rate": self.student_discount_rate if is_student else 0.0,
            "final_price": round(final_price, 2)
        }


# 测试代码：学生 和 非学生两种场景
if __name__ == "__main__":
    checkout_system = Checkout()

    # 测试1：学生客户
    items1 = [99, 50.5, 20]
    result_student = checkout_system.checkout(items1, is_student=True)
    print("=== 学生客户结账 ===")
    print(result_student)

    # 测试2：非学生客户
    items2 = [99, 50.5, 20]
    result_normal = checkout_system.checkout(items2, is_student=False)
    print("\n=== 普通客户结账 ===")
    print(result_normal)
