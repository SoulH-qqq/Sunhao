
def gradiern_descent(square,room,price,alpha,theta0,theta1,theta2,max_iter):
    """线性回归，梯度下降算法
    :param square: 训练集种的自变量
    :param room: 训练集种的自变量
	:param price: 训练集种的因变量
	:param theta0,theta1,theta2: 待求的权值
	:param alpha: 学习速率
	:param max_iter: 最大迭代次数
    """

    deviation=1
    iter=0
    while deviation>0.0001 and iter<max_iter:
        deviation=0
        sigma0=0
        sigma1=0
        sigma2=0
        for i in range(len(square)):
            h=theta0+theta1*square[i]+theta2*room[i]
            sigma0=sigma0+(h-price[i])
            sigma1=sigma1+(h-price[i])*square[i]
            sigma2=sigma2+(h-price[i])*room[i]
        theta0=theta0-alpha*sigma0/len(square)
        theta1=theta1-alpha*sigma1/len(square)
        theta2=theta2-alpha*sigma2/len(room)
        #计算误差
        for i in range(len(square)):
            deviation=deviation+(theta0+theta1*square[i]+theta2*room[i]-price[i])**2
        iter=iter+1
    return theta0,theta1,theta2,iter

square=[1.0,2.0,3.0,4.0]
room=[1.0,2.0,3.0,4.0]
price=[2.0,3.0,4.0,5.0]
alpha=0.1
theta0=0
theta1=0
theta2=0
max_iter=5000
restheta0,restheta1,restheta2,iters=gradiern_descent(square,room,price,alpha,theta0,theta1,theta2,max_iter)
print("theta0:",restheta0)
print("theta1:",restheta1)
print("theta2:",restheta2)
print("iters:",iters)

sq=input()
ro=input()
corprice=restheta0+restheta1*float(sq)+restheta2*float(ro)
print(corprice)