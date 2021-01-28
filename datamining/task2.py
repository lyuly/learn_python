import numpy as np
from sklearn.datasets import load_iris

dataset = load_iris() # 或者自己下载数据再加载
X = dataset.data
y = dataset.target
print(dataset.DESCR) # 打印下载数据集介绍
n_samples, n_festures = X.shape

# 计算平均值
attribute_means = X.mean(axis=0)
assert attribute_means.shape == (n_festures,)
X_d = np.array(X >= attribute_means, dtype='int')

# 划分训练集和测试集
from sklearn.model_selection import train_test_split

# 设置随机数种子以便复现书里的内容
random_state = 14

X_train, X_test, y_train, y_test = train_test_split(X_d, y, random_state=random_state)
print("训练集数据有 {} 条".format(y_train.shape))
print("测试集数据有 {} 条".format(y_test.shape))

from collections import defaultdict
from operator import itemgetter

def train(X, y_true, feature):
    # 1.一些等下要用的变量（数据的形状如上）
    n_samples, n_festures = X.shape
    assert 0 <= feature < n_festures
    values = set(X[:,feature])
    predictors = dict()
    errors = []

    # 2.算法（对照上面的算法流程）
    # 已经给定特征feature, 作为函数参数传过来了
    for current_value in values:
        # For 该特征对应的真值（即植物是哪一类）
        most_frequent_class, error = train_feature_value(X, y_true, feature, current_value)
        # 预测值：基于该特征预测的次数最多的类，即在所有样本里该特征10次有6次预测了A类，那我们对所有样本都预测为A类

        predictors[current_value] = most_frequent_class
        errors.append(error)
        # 计算预测值与真值的误差

    total_error = sum(errors)
    # 对上面计算的误差求和
    # python里求和函数sum([1, 2, 3] == 1 + 2 + 3 == 6)

    return predictors, total_error

def train_feature_value(X, y_true, feature, value):
    # 预测值：基于该特征预测的次数最多的类，即在所有样本里该特征10次有6次预测了A类，那我们对所有样本都预测为A类
    # 我们需要一个字典型变量在每个变量预测正确的次数
    class_counts = defaultdict(int)
    # 对每个二元组（类别，真值）迭代计数
    for sample, y in zip(X, y_true):
        if sample[feature] == value:
            class_counts[y] += 1
    # 现在选被预测最多的类别，需要排序（我们认为被预测最多的类别是正确的）
    sorted_class_counts = sorted(class_counts.items(), key=itemgetter(1), reverse=True)
    most_frequent_class = sorted_class_counts[0][0]
    # 误差定义为分类“错误”的次数，这里“错误”指样本中没有分类为我们预测的值，即样本的真实类别不是“被预测最多的类别”
    n_samples = X.shape[1]
    error = sum([class_count for class_value, class_count in class_counts.items()
                if class_value != most_frequent_class])
    return most_frequent_class, error

# For 给定的每个特征，计算所有预测值（这里 for 写到 list 里面是 python 的语法糖）
all_predictors = {variable: train(X_train, y_train, variable) for variable in range(X_train.shape[1])}
errors = {variable: error for variable, (mapping, error) in all_predictors.items()}
# 现在选择最佳模型并保存为 "model"
# 按误差排序
best_variable, best_error = sorted(errors.items(), key=itemgetter(1))[0]
print("最佳模型基于第 {0} 个变量， 误差为 {1:.2f}".format(best_variable, best_error))

# 选最好的模型，也就是误差最小的模型
model = {'variable': best_variable,
         'predictor': all_predictors[best_variable][0]}
print(model)

def predict(X_test, model):
    variable = model['variable']
    predictor = model['predictor']
    y_predicted = np.array([predictor[int(sample[variable])] for sample in X_test])
    return y_predicted

y_predicted = predict(X_test, model)
print(y_predicted)
accuracy = np.mean(y_predicted == y_test) * 100
print("在测试集上的准确率 {:.1f}%".format(accuracy))
from sklearn.metrics import classification_report
print(classification_report(y_test, y_predicted))