from matplotlib import pyplot


class AniPlot():
    def __init__(self, shape=(1, 1), threeDIndexes=[], pause=0.0001):
        self.pause = pause
        self.plt = pyplot
        self.plt.close()  # clf() # 清图  cla() # 清坐标轴 close() # 关窗口
        self.plt.ion()  # interactive mode on
        self.plt.show()

        self.fig = self.plt.figure()

        self.axis_list = []
        if (shape != None) and len(shape) == 2:
            (x, y) = shape
            index = 0
            for i in range(x):
                for j in range(y):
                    index += 1

                    if (threeDIndexes.__contains__(index)):
                        self.axis_list.append(self.fig.add_subplot(x, y, index, projection='3d'))
                    else:
                        self.axis_list.append(self.fig.add_subplot(x, y, index))

    def plot(self):
        return self.plt

    def figure(self):
        return self.fig

    def axis(self, index):
        return self.axis_list[index]

    def axises(self):
        return self.axis_list

    def scatter(self, axis=0, *args, **kwargs):
        try:
            self.axis_list[axis].scatter(*args, **kwargs)
            self.plt.pause(self.pause)
        except Exception as err:
            print(err)

    def plot_surface(self, axis=0, *args, **kwargs):
        try:
            self.axis_list[axis].plot_surface(*args, **kwargs)
        except Exception as err:
            print(err)
