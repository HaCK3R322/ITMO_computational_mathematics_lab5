class LagrangeInterpolator:
    @staticmethod
    def interpolate(x_values, y_values, x):
        n = len(x_values)
        isum = 0
        for i in range(n):
            jmul = 1
            for j in range(n):
                if i != j:
                    jmul *= (x - x_values[j]) / (x_values[i] - x_values[j])
            isum += y_values[i] * jmul
        return isum

    @staticmethod
    def calculate_interpolations(x_values, y_values, x_values_to_interpolate):
        interpolated_yarr = []
        for i in range(len(x_values_to_interpolate)):
            interpolated_yarr.append(LagrangeInterpolator.interpolate(x_values,
                                                                      y_values,
                                                                      x_values_to_interpolate[i]))
        return interpolated_yarr