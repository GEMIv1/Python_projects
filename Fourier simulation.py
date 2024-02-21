import numpy as np
import matplotlib.pyplot as plt 

figure = plt.figure(figsize=(8, 4.125))



l = np.pi

x = np.linspace(-1, 1 ,500)
y = x #f(X)

a_0= 1/l * np.trapz(y, x ,dx=1/100)

y_fourier = np.zeros(len(x))+a_0/2

for n in range(1, 100):

    error = np.sqrt(np.trapz(np.abs(np.add(y_fourier,-y))**2,x,dx=1/100))


    figure.clear()
    axis=figure.subplots()
    axis.plot(x,y_fourier,color='black',label='Fourier Approximation')
    axis.plot(x,y,'--',color='red',label='Periodic function')
    axis.set_title(f'Evaluation f(x) = x with fourier having: {n} terms.\n Mean squared error{error}.')
    axis.set_xlabel('x')
    axis.set_ylabel('f(x) - Using Fourier.')
    plt.xlim(1.2*min(x),1.2*max(x))
    plt.ylim(1.2*min(y),1.2*max(y))
    plt.grid()
    plt.legend()
    plt.draw()
    plt.pause(0.09)


    a_n = 1/l * np.trapz(y*np.cos(np.pi * n * x/l), x ,dx=1/100)
    b_n = 1/l * np.trapz(y*np.sin(np.pi * n * x/l), x ,dx=1/100)
    fourier_term = a_n * np.cos(np.pi * n * x/l) + b_n* np.sin(np.pi * n * x/l)
    y_fourier = np.add(fourier_term,y_fourier)

plt.show()



