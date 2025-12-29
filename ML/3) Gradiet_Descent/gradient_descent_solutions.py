from statistics import linear_regression

import numpy as np
import pandas as pd
from sklearn import linear_model
import math

def gradient_descent(x,y):
    learning_rate = 0.0002
    m_cur = b_cur = 0
    n = len(x)
    iterations = 1000000
    cost_previous = 0
    for i in range(iterations):
        y_predicted = m_cur * x + b_cur
        cost_cur = 1/n * sum((y-y_predicted)**2)
        md = -2/n * sum(x*(y-y_predicted))
        bd = -2/n * sum(y-y_predicted)
        m_cur = m_cur - learning_rate*md
        b_cur = b_cur - learning_rate*bd
        iterations += 1
        if(math.isclose(cost_previous,cost_cur,rel_tol=1e-20,abs_tol=0.00)):
                break
        cost_previous = cost_cur
        print(f"m_cur: {m_cur}, b_cur: {b_cur}, mse: {cost_cur}, iterations: {i}")
    return m_cur,b_cur

def linear_regression(x,y):
    reg = linear_model.LinearRegression()
    reg.fit(x.reshape(-1,1),y)
    return reg.coef_,reg.intercept_

if __name__ == '__main__':
    df = pd.read_csv(r"D:\Carrer\AI\AI Er Learning\ML\3) Gradiet_Descent\data\test_scores.csv")
    x = np.array(df['math'])
    y = np.array(df['cs'])
    m,b = gradient_descent(x,y)
    print(f"Using gradient descent: \n m:{m} b:{b}")
    m_sklearn,b_sklearn = linear_regression(x,y)
    print(f"Using linear regression: \n m_sklearn:{m_sklearn} b_sklearn:{b_sklearn}")