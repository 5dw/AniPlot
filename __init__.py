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

    def get_plot(self):
        return self.plt

    def get_figure(self):
        return self.fig

    def get_axis(self, index):
        try:
            axis = self.axis_list[index]
            return axis
        except Exception as err:
            print(err)

    def axises(self):
        return self.axis_list

    def plot(self, axis=0, *args, **kwargs):
        try:
            self.axis_list[axis].plot(*args, **kwargs)
        except Exception as err:
            print(err)

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

    def plot_date(self, axis=0, *args, **kwargs):
            try:
                self.axis_list[axis].plot_date(*args, **kwargs)
            except Exception as err:
                print(err)
    def step(self, axis=0, *args, **kwargs):
            try:
                self.axis_list[axis].step(*args, **kwargs)
            except Exception as err:
                print(err)
    def loglog(self, axis=0, *args, **kwargs):
            try:
                self.axis_list[axis].loglog(*args, **kwargs)
            except Exception as err:
                print(err)
    def semilogx(self, axis=0, *args, **kwargs):
            try:
                self.axis_list[axis].semilogx(*args, **kwargs)
            except Exception as err:
                print(err)
    def semilogy(self, axis=0, *args, **kwargs):
            try:
                self.axis_list[axis].semilogy(*args, **kwargs)
            except Exception as err:
                print(err)
    def fill_between(self, axis=0, *args, **kwargs):
            try:
                self.axis_list[axis].fill_between(*args, **kwargs)
            except Exception as err:
                print(err)
    def fill_betweenx(self, axis=0, *args, **kwargs):
            try:
                self.axis_list[axis].fill_betweenx(*args, **kwargs)
            except Exception as err:
                print(err)
    def bar(self, axis=0, *args, **kwargs):
            try:
                self.axis_list[axis].bar(*args, **kwargs)
            except Exception as err:
                print(err)
    def barh(self, axis=0, *args, **kwargs):
            try:
                self.axis_list[axis].barh(*args, **kwargs)
            except Exception as err:
                print(err)
    def stem(self, axis=0, *args, **kwargs):
            try:
                self.axis_list[axis].stem(*args, **kwargs)
            except Exception as err:
                print(err)
    def eventplot(self, axis=0, *args, **kwargs):
            try:
                self.axis_list[axis].eventplot(*args, **kwargs)
            except Exception as err:
                print(err)
    def pie(self, axis=0, *args, **kwargs):
            try:
                self.axis_list[axis].pie(*args, **kwargs)
            except Exception as err:
                print(err)
    def stackplot(self, axis=0, *args, **kwargs):
            try:
                self.axis_list[axis].stackplot(*args, **kwargs)
            except Exception as err:
                print(err)
    def broken_barh(self, axis=0, *args, **kwargs):
            try:
                self.axis_list[axis].broken_barh(*args, **kwargs)
            except Exception as err:
                print(err)
    def vlines(self, axis=0, *args, **kwargs):
            try:
                self.axis_list[axis].vlines(*args, **kwargs)
            except Exception as err:
                print(err)
    def hlines(self, axis=0, *args, **kwargs):
            try:
                self.axis_list[axis].hlines(*args, **kwargs)
            except Exception as err:
                print(err)
    def fill(self, axis=0, *args, **kwargs):
            try:
                self.axis_list[axis].fill(*args, **kwargs)
            except Exception as err:
                print(err)
