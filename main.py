#3-misol
class Harorat:
    @staticmethod
    def c_dan_f(c):
        return c * 9 / 5 + 32

    @staticmethod
    def f_dan_c(f):
        return round((f - 32) * 5 / 9, 1)

print("25 C =", Harorat.c_dan_f(25), "F")
print("100 F =", Harorat.f_dan_c(100), "C")
print("0 C =", Harorat.c_dan_f(0), "F")
