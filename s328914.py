import numpy as np
# All numpy's mathematical functions can be used in formulas
# see: https://numpy.org/doc/stable/reference/routines.math.html

def f1(x: np.ndarray) -> np.ndarray: 
    return np.sin(x[0])

def f2(x: np.ndarray) -> np.ndarray:
    return (((x[0] / (((x[0] / np.exp(x[0])) / np.exp(x[0])) * np.exp(x[2]))) - (np.exp(x[2]) * ((((np.exp(x[0]) -
                np.exp(x[2])) / np.exp(x[0])) - (np.exp(x[2]) * (x[0] / np.exp(x[0])))) - ((x[0] / np.exp(x[0])) - 
                    (np.exp(x[2]) * (np.exp(x[0]) - np.exp(x[2]))))))) - (np.exp(x[2]) * ((x[1] - ((x[0] / np.exp(x[0])) *
                        np.exp(x[2]))) - ((x[0] / np.exp(x[0])) - (np.exp(x[2]) * (np.exp(x[0]) - np.exp(x[2])))))))

def f3(x: np.ndarray) -> np.ndarray:
    return (((((((((((np.log(0.7479720658146718) - x[1]) - x[1]) - (x[1] + (x[1] + (x[1] + x[2])))) - x[1]) - x[1]) - x[1]) - x[1]) - x[1]) - x[1]) - (x[1] + (x[1] + x[2]))) - ((x[1] + x[2]) + x[1]))

def f4(x: np.ndarray) -> np.ndarray: 
    return ((np.cos(2.7118426536302964) - (np.cos(np.log(-1.6048844614869529)) - (np.cos(x[1]) - (2.7118426536302964 - -2.7478447580991294))))
            - (np.cos(np.log(-1.6048844614869529)) - ((np.cos(x[1]) - (np.cos(2.7118426536302964) - (np.cos(x[1]) - (2.7118426536302964 - -2.7478447580991294)))) 
                - (np.cos(np.log(-1.6048844614869529)) - ((np.cos(-1.6048844614869529) - (np.cos(np.log(-1.6048844614869529)) - ((np.cos(x[1]) - (np.cos(-1.6048844614869529) 
                    - (np.cos(x[1]) - (2.7118426536302964 - -2.7478447580991294)))) - (np.cos((np.cos(-1.6048844614869529) - (np.cos(np.log(-1.6048844614869529)) - (np.cos(x[1]) - (1.3464165493217628 - 1.3464165493217628))))) - ((np.cos(-1.6048844614869529) - (np.cos(np.log(-1.6048844614869529)) - (np.cos(x[1]) - (1.3464165493217628 - 1.3464165493217628)))) - (2.7118426536302964 - 1.3464165493217628)))))) - (2.7118426536302964 - 0.31949730548264466))))))

def f5(x: np.ndarray) -> np.ndarray:
    return (x[1] / 0.24705147919260284)

def f6(x: np.ndarray) -> np.ndarray:
    return (((-2.7488142240095725 / 4.8008749887592685) + (x[1] + x[1])) - x[0])

def f7(x: np.ndarray) -> np.ndarray:
    return np.exp((x[1] + (x[0] * x[1])))

def f8(x: np.ndarray) -> np.ndarray:
    return ((np.cos(-4.804226154565837) * ((((np.cos(-4.804226154565837) * ((np.exp(x[5]) - x[5]) + np.cos(np.exp(np.log(-4.804226154565837))))) - x[5]) - x[5]) + np.log(-4.804226154565837))) * (np.exp(x[5]) + x[5]))
