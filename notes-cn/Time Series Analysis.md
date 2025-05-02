# Time Series Analysis 时间序列分析

https://www.kaggle.com/code/iamleonie/time-series-interpreting-acf-and-pacf/notebook

## ARMA

ARMA 是 **AutoRegressive Moving Average（自回归滑动平均）** 的缩写，是一种用于建模和预测**平稳时间序列数据**的统计模型。

### 1. 自回归部分（AR）

表示当前值与过去若干个值相关：

$$
X_t = \phi_1 X_{t-1} + \phi_2 X_{t-2} + \dots + \phi_p X_{t-p} + \varepsilon_t
$$

- $\phi_1$, $\dots$, $\phi_p$：自回归系数  
- $\varepsilon_t$：白噪声


### 2. 滑动平均部分（MA）

表示当前值与过去若干个误差项（噪声）相关：

$$
X_t = \varepsilon_t + \theta_1 \varepsilon_{t-1} + \theta_2 \varepsilon_{t-2} + \dots + \theta_q \varepsilon_{t-q}
$$

- $\theta_1$, $\dots$, $\theta_q$：滑动平均系数


### 3. 综合 ARMA(p, q) 模型

$$
X_t = \phi_1 X_{t-1} + \dots + \phi_p X_{t-p} + \varepsilon_t + \theta_1 \varepsilon_{t-1} + \dots + \theta_q \varepsilon_{t-q}
$$

## ACF 和 PACF

在构建 ARMA/ARIMA 等时间序列模型前，我们通常使用 ACF 和 PACF 来识别时间序列的结构（例如选择 AR 或 MA 的阶数）。

### ACF（AutoCorrelation Function，自相关函数）

- 描述：度量序列当前值与其过去值之间的**线性相关性**。
- 给定时间滞后 $ k $，ACF 计算 $ X_t $ 与 $ X_{t-k} $ 的相关系数：

$$
\rho_k = \frac{\mathrm{Cov}(X_t, X_{t-k})}{\sqrt{\mathrm{Var}(X_t)\mathrm{Var}(X_{t-k})}} = \frac{\mathbb{E}[(X_t - \mu)(X_{t-k} - \mu)]}{\sigma^2}
$$

- 样本估计版本为：

$$
\hat{\rho}_k = \frac{\sum_{t=k+1}^{T}(X_t - \bar{X})(X_{t-k} - \bar{X})}{\sum_{t=1}^{T}(X_t - \bar{X})^2}
$$

- 图像：**ACF 图**展示每个滞后 $ k $ 的自相关系数。

**用途：**
- ACF 在某个滞后后**快速截尾** → 可能是 **MA(q)** 模型。
- ACF **缓慢衰减** → 可能是 **AR** 或 **ARMA** 模型。


### PACF（Partial AutoCorrelation Function，偏自相关函数）

- 描述：度量在排除所有较小滞后项（如 $ X_{t-1}, ..., X_{t-k+1} $）的影响后，$ X_t $ 与 $ X_{t-k} $ 的**直接线性关系**。
- 可通过对下列回归模型中 $ X_{t-k} $ 的系数估计来计算 PACF（第 $ k $ 阶）：

$$
X_t = \phi_{k1} X_{t-1} + \phi_{k2} X_{t-2} + \cdots + \phi_{kk} X_{t-k} + \epsilon_t
$$

其中：  
- $ \phi_{kk} $ 就是 PACF 在滞后 $ k $ 的值。

**用途：**
- PACF 在某个滞后后**快速截尾** → 可能是 **AR(p)** 模型。
- PACF **缓慢衰减** → 可能是 **MA** 或 **ARMA** 模型。


### ACF vs PACF 对比与模型识别

| 模型类型 | ACF 表现           | PACF 表现           |
|----------|--------------------|---------------------|
| AR(p)    | 渐进衰减           | **截尾于 lag p**     |
| MA(q)    | **截尾于 lag q**   | 渐进衰减             |
| ARMA(p,q)| 渐进衰减           | 渐进衰减             |


- 结合 ACF 和 PACF 图像模式，判断使用 AR、MA、或 ARMA 模型的合适阶数。


### 拖尾和截尾
在时间序列分析中，ARMA（AutoRegressive Moving Average，自回归滑动平均）模型的"拖尾"和"截尾"分别指的是自相关函数（ACF）和偏自相关函数（PACF）的特征表现。判断时间序列是否适合AR、MA或ARMA模型，可以通过观察ACF和PACF的拖尾和截尾特征来确定模型的阶数。

> 拖尾：始终有非零取值，不会在大于某阶后就快速趋近于0（而是在0附近波动），可简单理解为无论如何都不会为0，而是在某阶之后在0附近随机变化。

> 截尾：在大于某阶(k)后快速趋于0为k阶截尾，可简单理解为从某阶之后直接就变为0。

| 模型        | 自相关图    | 偏自相关图    |
|-------------|-------------|--------------|
| AR(p)       | 拖尾       | p阶截尾      |
| MA(q)       | q阶截尾    | 拖尾         |
| ARMA(p, q)  | 拖尾       | 拖尾         |
| 模型不适合   | 截尾       | 截尾         |

#### 1. 拖尾和截尾的定义
- **截尾（Cutoff）**：指的是自相关函数或偏自相关函数在某个滞后阶数之后突然迅速衰减为零，表现为在该滞后阶数之后ACF或PACF的值接近零。
- **拖尾（Tailing Off）**：指的是自相关函数或偏自相关函数的值缓慢衰减，且没有明显的截断点，表现为随着滞后阶数的增加，ACF或PACF逐渐接近零。

#### 2. 不同模型的拖尾和截尾特征
- **AR(p)模型**：
  - PACF截尾在阶数 $ p $ 处，即在第 $ p $ 阶之后，PACF接近零。
  - ACF表现为拖尾，即随着滞后阶数的增加逐渐衰减接近零。
- **MA(q)模型**：
  - ACF在阶数 $ q $ 处截尾，即在第 $ q $ 阶之后，ACF接近零。
  - PACF表现为拖尾，即随着滞后阶数的增加逐渐衰减接近零。
- **ARMA(p, q)模型**：
  - ACF和PACF均表现为拖尾，即自相关和偏自相关都逐渐衰减。

#### 3. 判断模型阶数的方法
通过分析时间序列的ACF和PACF图可以初步判断模型类型：
1. **绘制自相关函数（ACF）和偏自相关函数（PACF）图**。
2. **观察ACF和PACF的截尾和拖尾情况**，参考上述特征：
   - 若ACF截尾而PACF拖尾，建议使用MA模型。
   - 若PACF截尾而ACF拖尾，建议使用AR模型。
   - 若ACF和PACF均拖尾，建议使用ARMA模型。

这种判断方法是非正式的，选定模型后通常还需使用AIC或BIC等信息准则来进一步确认模型的适合度和阶数，以确保模型的解释力和预测效果。
