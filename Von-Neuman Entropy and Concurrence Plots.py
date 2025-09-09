#!/usr/bin/env python
# coding: utf-8

# In[66]:


import matplotlib.pyplot as plt
from numpy import *

list_values = [0.00001, 0.1, 0.2, 0.5, 1]


def single_entropy(x, i):
    term1 = -cos(i * x)**2 * log2(cos(i * x)**2)
    term2 = -sin(i * x)**2 * log2(sin(i * x)**2)
    return term1 + term2

vectorized_entropy = vectorize(single_entropy)

t_values = linspace(0, 5 * pi, 2000)

plt.figure(figsize=(10, 6))

for i in list_values:
    y_values = vectorized_entropy(t_values, i)
    plt.plot(t_values, y_values, label=f'J={i}')

plt.title('Entropy Function for Different Coupling Strength Values')
plt.xlabel('Time')
plt.ylabel('Von-Neumann Entropy Value')
plt.legend()
plt.grid(True)
plt.show()


# In[67]:


import matplotlib.pyplot as plt
from numpy import *

list_values = [2,5,10,50,100]

def single_entropy(x, i):
    term1 = -cos(i * x)**2 * log2(cos(i * x)**2)
    term2 = -sin(i * x)**2 * log2(sin(i * x)**2)
    return term1 + term2

vectorized_entropy = vectorize(single_entropy)

t_values = linspace(0, 0.01*  pi, 2000)

plt.figure(figsize=(10, 6))

for i in list_values:
    y_values = vectorized_entropy(t_values, i)
    plt.plot(t_values, y_values, label=f'J={i}')

plt.title('Entropy Function for Different Coupling Strength Values')
plt.xlabel('Time')
plt.ylabel('Von-Neumann Entropy Value')
plt.legend()
plt.grid(True)
plt.show()


# In[68]:


import matplotlib.pyplot as plt
from numpy import *


list_values = [0, 0.1, 0.2, 1]


def single_concurrence(x, i):
   
    term1 = abs(sin(2*i * x))
    return term1 


vectorized_concurrence = vectorize(single_concurrence)

t_values = linspace(0, 4 * pi, 2000)

plt.figure(figsize=(10, 6))


for i in list_values:
    y_values = vectorized_concurrence(t_values, i)
    plt.plot(t_values, y_values, label=f'J={i}')

plt.title('Concurrence Function for Different Coupling Strength Values')
plt.xlabel('Time')
plt.ylabel('Concurrence Value')
plt.legend()
plt.grid(True)
plt.show()


# In[69]:


import matplotlib.pyplot as plt
from numpy import *

list_values = [2, 5, 10, 50, 100]

def single_concurrence(x, i):
    term1 = abs(sin(2*i * x))
    return term1 

vectorized_concurrence = vectorize(single_concurrence)

t_values = linspace(0, 0.05 * pi, 2000)

plt.figure(figsize=(10, 6))

for i in list_values:
    y_values = vectorized_concurrence(t_values, i)
    plt.plot(t_values, y_values, label=f'J={i}')

plt.title('Concurrence Function for Different Coupling Strength Values')
plt.xlabel('Time')
plt.ylabel('Concurrence Value')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




