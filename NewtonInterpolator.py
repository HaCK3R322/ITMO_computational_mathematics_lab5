import math


class WrongData(Exception):
    pass


class NewtonInterpolator:
    @staticmethod
    def interpolate_divided_differences(x_values, y_values, x):
        raise WrongData("Sorry, but this program cannot interpolate by Newton polynom with divided differences yet.")

    @staticmethod
    def delta(values, value_pos, power):
        if power == 0:
            return values[value_pos]
        else:
            return NewtonInterpolator.delta(values, value_pos + 1, power - 1) \
                   - NewtonInterpolator.delta(values, value_pos, power - 1)

    @staticmethod
    def get_t(t0, power, direct=True):
        answer = 1
        if power == 0:
            return answer
        else:
            if direct:
                for i in range(1, power + 1):
                    answer *= t0 - i + 1
                return answer
            else:
                for i in range(power, 0, -1):
                    answer *= t0 + i - 1
                return answer

    @staticmethod
    def direct_interpolation(x_values, y_values, x):
        index_of_x_before = 0
        for i in range(len(x_values)):
            if x >= x_values[i]:
                index_of_x_before = i
            else:
                break
        n = len(x_values)
        h = x_values[1] - x_values[0]
        t = (x - x_values[index_of_x_before]) / h
        answer = y_values[index_of_x_before]
        power = 1
        for i in range(index_of_x_before, n - 1):  # if len(xarr) == 7, -> i ... 6
            answer += NewtonInterpolator.get_t(t, power) \
                      * NewtonInterpolator.delta(y_values, index_of_x_before, power) \
                      / math.factorial(power)
            power += 1
        return answer

    @staticmethod
    def back_interpolation(x_values, y_values, x):
        h = x_values[1] - x_values[0]
        n = len(x_values)
        t = (x - x_values[n - 1]) / h

        answer = NewtonInterpolator.delta(y_values, n - 1, 0)
        for i in range(1, n):
            answer += NewtonInterpolator.get_t(t, i, False) \
                      * NewtonInterpolator.delta(y_values, n - i - 1, i) \
                      / math.factorial(i)
        return answer

    @staticmethod
    def interpolate_finite_differences(x_values, y_values, x):
        mid_index = len(x_values) // 2
        mid = x_values[mid_index]
        if x < mid:
            return NewtonInterpolator.direct_interpolation(x_values, y_values, x)
        else:
            return NewtonInterpolator.back_interpolation(x_values, y_values, x)

    @staticmethod
    def interpolate(x_values, y_values, x):
        if not (x_values[0] <= x <= x_values[len(x_values) - 1]):
            raise WrongData("Sowwy but this progwam cannot extwapolate (>.>;;) OwO")

        if len(x_values) < 2:
            raise WrongData("Not enough data")

        return NewtonInterpolator.interpolate_finite_differences(x_values, y_values, x)

    @staticmethod
    def calculate_interpolations(x_values, y_values, interpolation_nodes):
        interpolated_y_values = []
        for i in range(len(interpolation_nodes)):
            interpolated_y = NewtonInterpolator.interpolate(x_values, y_values, interpolation_nodes[i])
            interpolated_y_values.append(interpolated_y)
        return interpolated_y_values
