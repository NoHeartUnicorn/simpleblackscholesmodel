import math
from scipy.stats import norm

S = float(input("Enter the value for Current Asset Price: "))
K = float(input("Enter the value for Strike Price: "))
T = float(input("Enter the value for Time to Expiration: "))
r = float(input("Enter the value of the Risk-Free Rate: "))
v = float(input("Enter the value for Volatility: "))

d1 = (math.log(S/K) + (r + 0.5 * v**2)*T ) / (v * math.sqrt(T))
d2 = d1 - (v * math.sqrt(T))

C = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
P = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

print('The value of d1 is: ', round(d1, 4))
print('The value of d2 is: ', round(d2, 4))
print('The price of the call option is: $', round(C, 2))
print('The price of the put option is: $', round(P, 2))