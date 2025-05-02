# Time Series Analysis

https://www.kaggle.com/code/iamleonie/time-series-interpreting-acf-and-pacf/notebook

## ACF and PACF

Before building ARMA/ARIMA models, we typically use ACF and PACF to identify the structure of the time series (e.g., selecting the order of AR or MA).

### ACF (AutoCorrelation Function)

- **Description**: Measures the **linear correlation** between the current value and its past values.
- For a time lag $k$, ACF calculates the correlation coefficient between $X_t$ and $X_{t-k}$:

$$
\rho_k = \frac{\mathrm{Cov}(X_t, X_{t-k})}{\sqrt{\mathrm{Var}(X_t)\mathrm{Var}(X_{t-k})}} = \frac{\mathbb{E}[(X_t - \mu)(X_{t-k} - \mu)]}{\sigma^2}
$$

- The sample estimate is:

$$
\hat{\rho}_k = \frac{\sum_{t=k+1}^{T}(X_t - \bar{X})(X_{t-k} - \bar{X})}{\sum_{t=1}^{T}(X_t - \bar{X})^2}
$$

- **Graph**: The **ACF plot** shows the autocorrelation coefficients for each lag $k$.

**Usage:**
- ACF **cuts off quickly** after a certain lag → Likely an **MA(q)** model.
- ACF **decays slowly** → Likely an **AR** or **ARMA** model.

### PACF (Partial AutoCorrelation Function)

- **Description**: Measures the **direct linear relationship** between $X_t$ and $X_{t-k}$ after removing the effects of all smaller lags (e.g., $X_{t-1}, ..., X_{t-k+1}$).
- PACF at lag $k$ can be calculated as the coefficient of $X_{t-k}$ in the following regression model:

$$
X_t = \phi_{k1} X_{t-1} + \phi_{k2} X_{t-2} + \cdots + \phi_{kk} X_{t-k} + \epsilon_t
$$

Where:  
- $ \phi_{kk} $ is the PACF value at lag $k$.

**Usage:**
- PACF **cuts off quickly** after a certain lag → Likely an **AR(p)** model.
- PACF **decays slowly** → Likely an **MA** or **ARMA** model.

### ACF vs PACF Comparison and Model Identification

| Model Type | ACF Behavior       | PACF Behavior       |
|------------|--------------------|---------------------|
| AR(p)      | Gradual decay      | **Cuts off at lag p** |
| MA(q)      | **Cuts off at lag q** | Gradual decay       |
| ARMA(p,q)  | Gradual decay      | Gradual decay       |

- Use the patterns in ACF and PACF plots to determine the appropriate order for AR, MA, or ARMA models.

### Tailing Off and Cutoff

In time series analysis, the "tailing off" and "cutoff" behaviors of ACF and PACF are used to determine whether a time series is suitable for AR, MA, or ARMA models. These behaviors help identify the model order.

> **Tailing Off**: ACF or PACF values do not quickly approach zero after a certain lag but instead fluctuate around zero. This indicates no clear cutoff and suggests a gradual decay.

> **Cutoff**: ACF or PACF values quickly approach zero after a certain lag (e.g., lag $k$). This indicates a clear cutoff at lag $k$.

| Model       | ACF Behavior | PACF Behavior |
|-------------|--------------|---------------|
| AR(p)       | Tailing off  | Cuts off at lag p |
| MA(q)       | Cuts off at lag q | Tailing off  |
| ARMA(p, q)  | Tailing off  | Tailing off   |
| Not Suitable| Cuts off     | Cuts off      |

#### 1. Definitions of Tailing Off and Cutoff
- **Cutoff**: Refers to when ACF or PACF values quickly decay to zero after a certain lag. This is observed as ACF or PACF values becoming negligible beyond a specific lag.
- **Tailing Off**: Refers to when ACF or PACF values decay slowly without a clear cutoff point, gradually approaching zero as the lag increases.

#### 2. Characteristics of Different Models
- **AR(p) Model**:
  - PACF cuts off at lag $p$, meaning PACF values become negligible beyond lag $p$.
  - ACF tails off, gradually decaying to zero as lag increases.
- **MA(q) Model**:
  - ACF cuts off at lag $q$, meaning ACF values become negligible beyond lag $q$.
  - PACF tails off, gradually decaying to zero as lag increases.
- **ARMA(p, q) Model**:
  - Both ACF and PACF tail off, gradually decaying to zero.

#### 3. Steps to Determine Model Order
1. **Plot ACF and PACF** for the time series.
2. **Observe the cutoff and tailing off behaviors** in ACF and PACF:
   - If ACF cuts off and PACF tails off, consider an MA model.
   - If PACF cuts off and ACF tails off, consider an AR model.
   - If both ACF and PACF tail off, consider an ARMA model.

This method is informal. After selecting a model, use criteria like AIC or BIC to confirm the model's suitability and order, ensuring good interpretability and predictive performance.