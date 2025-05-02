# Finance

| 参数 | 抽样分布 | 置信区间 |
|------|----------|----------|
| $\mu$，$\sigma^2$ 已知 | $\dfrac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim N(0,1)$ | $\left[\bar{X} - \dfrac{\sigma}{\sqrt{n}} z_{\alpha/2},\ \bar{X} + \dfrac{\sigma}{\sqrt{n}} z_{\alpha/2} \right]$ |
| $\mu$，$\sigma^2$ 未知 | $\dfrac{\bar{X} - \mu}{S / \sqrt{n}} \sim t(n-1)$ | $\left[\bar{X} - \dfrac{S}{\sqrt{n}} t_{\alpha/2}(n-1),\ \bar{X} + \dfrac{S}{\sqrt{n}} t_{\alpha/2}(n-1) \right]$ |
| $\sigma^2$ | $\dfrac{(n - 1) S^2}{\sigma^2} \sim \chi^2(n - 1)$ | $\left[\dfrac{(n - 1) S^2}{\chi^2_{1 - \alpha/2}},\ \dfrac{(n - 1) S^2}{\chi^2_{\alpha/2}} \right]$ |
| $\mu_1 - \mu_2$ <br> ($\sigma_1^2,\ \sigma_2^2$ 已知) | $\dfrac{(\bar{X} - \bar{Y}) - (\mu_1 - \mu_2)}{\sqrt{\dfrac{\sigma_1^2}{n} + \dfrac{\sigma_2^2}{m}}} \sim N(0,1)$ | $\left[(\bar{X} - \bar{Y}) \pm z_{\alpha/2} \sqrt{\dfrac{\sigma_1^2}{n} + \dfrac{\sigma_2^2}{m}} \right]$ |
| $\mu_1 - \mu_2$ <br> ($\sigma_1^2 = \sigma_2^2 = \sigma^2$ 未知) | $\dfrac{(\bar{X} - \bar{Y}) - (\mu_1 - \mu_2)}{S_w \sqrt{1/n + 1/m}} \sim t(n + m - 2)$ | $\left[(\bar{X} - \bar{Y}) \pm t_{\alpha/2}(n + m - 2) S_w \sqrt{\dfrac{1}{n} + \dfrac{1}{m}} \right]$ |
| $\dfrac{\sigma_1^2}{\sigma_2^2}$ | $\dfrac{S_1^2 / \sigma_1^2}{S_2^2 / \sigma_2^2} \sim F(n - 1,\ m - 1)$ | $\left[\dfrac{S_1^2}{S_2^2 F_{1 - \alpha/2}(n - 1,\ m - 1)},\ \dfrac{S_1^2}{S_2^2 F_{\alpha/2}(n - 1,\ m - 1)} \right]$ |
