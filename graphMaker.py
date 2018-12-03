import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


class graphMaker:

    def __init__(self, runtime, costs, qualities):

        self.runtime = runtime
        self.costs = costs
        self.qualities = qualities


    def graph1(self):

        # dataSets = [[1.1, 1.2, 1.4, 2, 3, 5, 5.2], [2, 3, 5, 6, 2, 4, 2, 1, 2.3, 6.8, 6.9, 9]]
        qua = [1,2]
        for q in qua:
            index = np.where(self.costs > q)[0]
            data = self.runtime[index]
            sns.distplot(data, hist_kws={"histtype": "step", "linewidth": 1, "alpha": 1, "cumulative": True}, kde=False,
                         label="quality="+str(q))
        plt.legend()
        plt.show()


if __name__ == '__main__':

    print(1)
