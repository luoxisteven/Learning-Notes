# Time Series Analysis

## Tailing Off and Cutoff

In time series analysis, "tailing off" and "cutoff" in ARMA (AutoRegressive Moving Average) models refer to the characteristics of the Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF). Determining whether a time series is suitable for AR, MA, or ARMA models can be done by observing the tailing off and cutoff features of the ACF and PACF to determine the model's order.

> **Tailing Off**: Always has non-zero values and does not rapidly approach zero after a certain lag (but fluctuates around zero). It can be simply understood as never being zero regardless of the lag order, but fluctuating randomly near zero after a certain lag.

> **Cutoff**: Rapidly approaches zero after a certain lag \( k \). It can be simply understood as becoming zero directly after a certain lag \( k \).

| Model        | ACF         | PACF        |
|--------------|-------------|-------------|
| AR(p)        | Tailing Off | Cutoff at p |
| MA(q)        | Cutoff at q | Tailing Off |
| ARMA(p, q)   | Tailing Off | Tailing Off |
| Not Suitable | Cutoff      | Cutoff      |

### 1. Definitions of Tailing Off and Cutoff

- **Cutoff**: Refers to the autocorrelation function or partial autocorrelation function rapidly decaying to zero after a certain lag order. This is manifested as ACF or PACF values approaching zero after that lag.

- **Tailing Off**: Refers to the autocorrelation function or partial autocorrelation function gradually decaying without a clear cutoff point. This means that as the lag order increases, the ACF or PACF gradually approaches zero.

### 2. Tailing Off and Cutoff Characteristics of Different Models

- **AR(p) Model**:
  - **PACF** cuts off at lag \( p \), meaning that after the \( p \)-th lag, the PACF approaches zero.
  - **ACF** exhibits tailing off, gradually decaying towards zero as the lag increases.

- **MA(q) Model**:
  - **ACF** cuts off at lag \( q \), meaning that after the \( q \)-th lag, the ACF approaches zero.
  - **PACF** exhibits tailing off, gradually decaying towards zero as the lag increases.

- **ARMA(p, q) Model**:
  - Both **ACF** and **PACF** exhibit tailing off, meaning that autocorrelations and partial autocorrelations gradually decay.

### 3. Methods to Determine Model Order

By analyzing the ACF and PACF plots of a time series, one can preliminarily determine the type of model:

1. **Plot the Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF)**.

2. **Observe the cutoff and tailing off characteristics of ACF and PACF**, referencing the features described above:
   - If **ACF cuts off** and **PACF tails off**, it is recommended to use an **MA** model.
   - If **PACF cuts off** and **ACF tails off**, it is recommended to use an **AR** model.
   - If both **ACF and PACF tail off**, it is recommended to use an **ARMA** model.

This method is informal; after selecting a model, information criteria such as AIC (Akaike Information Criterion) or BIC (Bayesian Information Criterion) are usually used to further confirm the model's suitability and order. This ensures the model's explanatory power and forecasting performance.

