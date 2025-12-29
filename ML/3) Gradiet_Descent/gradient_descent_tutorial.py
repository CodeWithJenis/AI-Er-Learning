import numpy as np

def gradient_descent(x, y):
    m_cur = b_cur = 0
    iterations = 10000
    learning_rate = 0.08
    n = len(x)
    for iteration in range(iterations):
        y_predicted = m_cur * x + b_cur
        md = -2/n *sum(x*(y-y_predicted))
        bd = -2/n *sum(y-y_predicted)
        m_cur = m_cur -learning_rate*md
        b_cur = b_cur -learning_rate*bd
        mse = 1/n*sum((y-y_predicted)**2)
        print("m={},b={},mse/cost={},i={}".format(m_cur, b_cur,mse,iteration+1))


x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])
gradient_descent(x, y)