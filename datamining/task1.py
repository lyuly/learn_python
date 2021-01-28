# 引入库
import numpy as np
from operator import itemgetter

# 准备数据

# 创造随机生成的数据
X = np.zeros((100, 5), dtype='bool')
for i in range(X.shape[0]):
    if np.random.random() < 0.3:
        # A bread winner
        X[i][0] = 1
        if np.random.random() < 0.5:
            # Who likes milk
            X[i][1] = 1
        if np.random.random() < 0.2:
            # Who likes cheese
            X[i][2] = 1
        if np.random.random() < 0.25:
            # Who likes apples
            X[i][3] = 1
        if np.random.random() < 0.5:
            # Who likes bananas
            X[i][4] = 1
    else:
        # Not a bread winner
        if np.random.random() < 0.5:
            # Who like milk
            X[i][1] = 1
            if np.random.random() < 0.2:
                # Who like cheese
                X[i][2] = 1
            if np.random.random() < 0.25:
                # Who like apples
                X[i][3] = 1
            if np.random.random() < 0.5:
                # Who likes bananas
                X[i][4] = 1
        else:
            if np.random.random() < 0.8:
                # Who likes cheese
                X[i][2] = 1
            if np.random.random() < 0.6:
                # Who likes apples
                X[i][3] = 1
            if np.random.random() < 0.7:
                # Who likes bananas
                X[i][4] = 1
    if X[i].sum() == 0:
        X[i][4] = 1 # must buy something, so gets bananas
np.savetxt("./data/affinity_dataset.txt", X, fmt='%d') # 保存

# 读取数据
dataset_filename = "./data/affinity_dataset.txt"
X = np.loadtxt(dataset_filename) # 加载数据
n_samples, n_features = X.shape
print(X.shape)
print(X[:5])

features = ["bread", "milk", "cheese", "apples", "bananas"]

num_apple_purchases = 0 # 计数
for sample in X:
    if sample[3] == 1: # 记录买Apples的有多少人
        num_apple_purchases += 1
print("买苹果的有{0}人".format(num_apple_purchases))

rule_valid = 0
rule_invalid = 0
for sample in X:
    if sample[3] == 1: # 买了苹果
        if sample[4] ==1 : # 又买了香蕉
            rule_valid += 1
        else:# 不买香蕉的
            rule_invalid += 1
print("买了苹果又买香蕉的有{0}人".format(rule_valid))
print("买了苹果不买香蕉的有{0}人".format(rule_invalid))

# 计算支持度support和置信度confidence
support = rule_valid # 支持度是符合“买了苹果又买香蕉”这个规则的人数
confidence = rule_valid / num_apple_purchases
print("支持度support = {0} 置信度confidence = {1:.3f}.".format(support, confidence))
# 置信度的百分比形式
print("置信度confidence的百分比形式为 {0:.1f}%.".format(100 * confidence))

from collections import defaultdict
# 上面“买了苹果又买香蕉”是一种情况，现在把所有可能的情况都做一遍
valid_rules = defaultdict(int)
invalid_rules = defaultdict(int)
num_occurences = defaultdict(int)

for sample in X:
    for premise in range(n_features):
        if sample[premise] == 0: continue
        # 先买premise, premise代表一种食物，记做X
        num_occurences[premise] += 1
        for conclusion in range(n_features):
            if premise == conclusion:
                continue # 跳过买X又买X的情况
            if sample[conclusion] == 1: # 又买了conclusion, conclusion代表一种食物，记做Y
                valid_rules[(premise, conclusion)] += 1 # 买X买Y
            else:
                invalid_rules[(premise, conclusion)] += 1 # 买X没买Y
support = valid_rules
confidence = defaultdict(float)
for premise, conclusion in valid_rules.keys():
    confidence[(premise, conclusion)] = valid_rules[(premise, conclusion)] / num_occurences[premise]

for premise, conclusion in confidence:
    premise_name = features[premise]
    conclusion_name = features[conclusion]
    print("Rule: 买了{0}, 又买{1}".format(premise_name, conclusion_name))
    print(" - 置信度Confidence: {0:.3f}".format(confidence[(premise, conclusion)]))
    print(" -  支持度Suport: {0}".format(support[(premise, conclusion)]))
    print("")

# 封装一下方便使用
def print_rule(premise, conclusion, support, confidence, features):
    premise_name = features[premise]
    conclusion_name = features[conclusion]
    print("Rule: 买了{0}, 又买{1}".format(premise_name, conclusion_name))
    print(" - 置信度Confidence: {0:.3f}".format(confidence[(premise, conclusion)]))
    print(" - 支持度Support: {0}".format(support[(premise, conclusion)]))
    print("")

premise = 1
conclusion = 3
print_rule(premise, conclusion, support, confidence, features)

# 按支持度support排序
from pprint import pprint
pprint(list(support.items()))

sorted_confidence = sorted(confidence.items(), key=itemgetter(1), reverse=True)
for index in range(5): # 打印前5个
    print("Rule #{0}".format(index + 1))
    (premise, conclusion) = sorted_confidence[index][0]
    print_rule(premise, conclusion, support, confidence, features)
