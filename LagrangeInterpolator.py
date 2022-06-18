class LagrangeInterpolator:
    @staticmethod
    def interpolate(x_values, y_values, x):
        n = len(x_values)
        answer = 0
        for i in range(n):
            mult = 1
            for j in range(n):
                if i != j:
                    mult *= (x - x_values[j]) / (x_values[i] - x_values[j])
            answer += y_values[i] * mult
        return answer

    @staticmethod
    def calculate_interpolations(x_values, y_values, x_values_to_interpolate):
        interpolated_yarr = []
        for i in range(len(x_values_to_interpolate)):
            interpolated_yarr.append(LagrangeInterpolator.interpolate(x_values,
                                                                      y_values,
                                                                      x_values_to_interpolate[i]))
        return interpolated_yarr
