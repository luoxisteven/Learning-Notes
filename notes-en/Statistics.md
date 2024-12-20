# Statistics

## Table of Contents
- [Type I and Type II Errors](#type-i-and-type-ii-errors)
- [Significance Level, Statistical Power, and P-Value](#significance-level-statistical-power-and-p-value)
- [Confidence Intervals](#confidence-intervals)
- [Analysis of Variance (ANOVA)](#analysis-of-variance-anova)
- [One-Tailed and Two-Tailed Tests](#one-tailed-and-two-tailed-tests)
- [Simpson's Paradox](#simpsons-paradox)
- [Hypothesis Testing](#hypothesis-testing)
- [Parameter Estimation](#parameter-estimation)
- [Common Statistical Tests](#common-statistical-tests)
- [Law of Large Numbers and Central Limit Theorem](#law-of-large-numbers-and-central-limit-theorem)
- [Statistics and Sampling Distributions](#statistics-and-sampling-distributions)
  - [Chi-Square Distribution](#chi-square-distribution)
  - [T-Distribution](#t-distribution)
  - [F-Distribution](#f-distribution)

## Type I and Type II Errors

- **Type I Error (False Positive)**: Incorrectly rejecting a true null hypothesis.  
  **Example**: Suppose an innocent person is accused of a crime. Here, the null hypothesis is "the person is innocent." If the court mistakenly convicts the innocent person, a Type I error has occurred.

- **Type II Error (False Negative)**: Failing to reject a false null hypothesis.  
  **Example**: If the defendant is actually guilty but the court finds them not guilty, a Type II error has occurred.

----
#### Which is More Severe: Type I or Type II Error?

Generally, a Type I error (false positive) is considered more severe. In statistics, the null hypothesis is what we aim to reject, so we set the significance level α to be relatively small to reduce the probability of committing a Type I error. A common α value is 0.05, meaning we accept a 5% probability of making a Type I error.

However, in certain scenarios, such as cancer screening, a Type II error (false negative) may be more severe. If the test fails to identify existing cancer (false negative), the patient might miss the optimal treatment window. Therefore, the severity depends on the specific application context and requires careful consideration.

## Significance Level, Statistical Power, and P-Value

- **Significance Level (α)**: The threshold probability that researchers are willing to accept for committing a Type I error (false positive). A common α value is 0.05, indicating a willingness to accept a 5% probability of incorrectly rejecting the null hypothesis.

- **Statistical Power (1-β)**: The probability of correctly rejecting the null hypothesis (detecting an actual effect), representing the ability to avoid committing a Type II error (false negative). Higher statistical power increases the likelihood of detecting a true effect.

- **P-Value**: The probability of observing the current data results assuming the null hypothesis is true. The smaller the P-value, the less likely the observed results are under the null hypothesis, thus increasing our inclination to reject the null hypothesis.

## Confidence Intervals

- **Confidence Interval**: Used to estimate the range within which a population parameter lies. In interval estimation, the confidence interval represents the possible range of the population parameter inferred from the sample data. A 95% confidence interval is commonly used, meaning we are 95% confident that the population parameter falls within this interval.

## Different Types of Testing Methods

- **t-Test**: Used to compare the means of two samples to determine if there is a significant difference, suitable when the population variance is unknown or the sample size is small.

- **z-Test**: Also used to compare the means of two samples but applicable when the sample size is large or the population variance is known.

- **Chi-Square Test**: Used for testing the independence of categorical data or goodness of fit. The independence test checks whether two variables are independent, while the goodness of fit test determines if the observed distribution of categorical variables matches the expected distribution.

- **F-Test**: Primarily used to test whether the variances of two or more groups are significantly different, commonly applied in Analysis of Variance (ANOVA) to analyze whether the means of multiple samples are significantly different.

## Analysis of Variance (ANOVA)

**ANOVA (Analysis of Variance)** is used to determine whether there are significant differences among the means of multiple samples. By comparing between-group variability and within-group variability, ANOVA determines if the group means are significantly different. The F-statistic calculated in ANOVA is given by:

$$
F = \frac{MSB}{MSE}
$$

where MSB represents the mean square between groups, and MSE represents the mean square within groups.

## One-Tailed and Two-Tailed Tests

- **One-Tailed Test**: Used when the hypothesis has a directional prediction, testing whether the effect is significant in one direction. For example, if a researcher wants to verify that a new method is better than the old one, a one-tailed test is used.

- **Two-Tailed Test**: Used to verify whether there is a difference between two variables without considering the direction. When researchers are only concerned with whether a difference exists, a two-tailed test is employed.

- **One-Tailed Test**: Used to detect if the effect is moving in a single hypothesized direction.  
- **Two-Tailed Test**: Used to detect if there is a difference between two variables, regardless of direction.

## Simpson's Paradox

**Simpson's Paradox** refers to a situation where, under certain conditions, separate analysis of two groups of data may both satisfy a particular property, but when the data are combined, the opposite conclusion is reached. This means that separate and combined analyses can lead to contradictory conclusions.

### Example

Suppose two doctors, Doctor A and Doctor B, treat two groups of patients in a hospital. When calculating the treatment success rates for each doctor separately within each group, Doctor A may have a higher success rate. However, when all patients are combined, the overall success rate might show that Doctor B has a higher success rate. This illustrates Simpson's Paradox.

### How to Avoid Simpson's Paradox?

1. **Hierarchical Analysis**:
   - Perform stratified analysis by grouping data based on important variables such as gender, age group, etc., instead of simply aggregating all data. Stratification can more clearly reveal the relationships between variables and avoid misleading results caused by data aggregation.

2. **Detailed Segmentation**:
   - Analyze data by subdividing based on the context and actual conditions. Handle and analyze each subset individually to ensure that important information is not lost due to data aggregation.

3. **Sample Size and Quality**:
   - Ensure that each subgroup has a sufficiently large sample size and high sample quality. Insufficient sample sizes may lead to statistical inaccuracies, and sample selection bias may result in misleading analysis outcomes.

## Hypothesis Testing
- [Hypothesis Testing (Zhihu)](https://zhuanlan.zhihu.com/p/86178674?utm_psn=1743869140127977472)
- Standard Normal Distribution, also known as the z-distribution

**Hypothesis Testing** is the process of making inferences about a population parameter by proposing a hypothesis value and using sample information to determine whether the hypothesis holds.

- **Null Hypothesis (H₀)**: Typically the hypothesis we aim to reject, such as the equality of two group means.
- **Alternative Hypothesis (H₁)**: Complementary to the null hypothesis, suggesting that the two group means are not equal.

### Type I and Type II Errors in Hypothesis Testing:
- **Type I Error (False Positive)**: The null hypothesis is actually true but is incorrectly rejected.
- **Type II Error (False Negative)**: The null hypothesis is actually false but fails to be rejected.

### Significance Level and P-Value
- **Significance Level (α)**: The threshold probability for accepting the risk of committing a Type I error. A common α value is 0.05.
- **P-Value**: The probability of observing the current results assuming the null hypothesis is true. A smaller P-value indicates a higher inclination to reject the null hypothesis.

## Parameter Estimation

**Parameter Estimation** is used to infer population parameters from sample data and is divided into two methods:
1. **Point Estimation**: Directly estimates the population parameter using a sample statistic (e.g., mean).
2. **Interval Estimation**: Constructs an interval within a given confidence level to estimate the population parameter. For example, a 95% confidence interval implies there is a 95% probability that the population parameter lies within this interval.
 ![alt text](<img-en/parameter-estimation.jpg>)
 - Note: When the variance is unknown, a normal distribution can be used even with large samples.
 
 $$
 z = \frac{(x - μ)}{σ}
 $$

### Confidence Intervals
- [Confidence Intervals CSDN](https://blog.csdn.net/Anne033/article/details/109739681?ops_request_misc=&request_id=&biz_id=102&utm_term=%E7%BD%AE%E4%BF%A1%E5%8C%BA%E9%97%B4&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0-109739681.142^v99^pc_search_result_base2&spm=1018.2226.3001.4187)

- **Confidence Interval**: A range of values derived from sample data used to estimate a population parameter.
- **Confidence Level**: The probability that the confidence interval contains the true population parameter. A common confidence level is 95%.
  
A confidence interval means that if we were to draw different samples and construct confidence intervals from each, a certain percentage (e.g., 95%) of those intervals would contain the true population parameter (e.g., population mean).

## Law of Large Numbers and Central Limit Theorem

### Law of Large Numbers
- **Weak Law of Large Numbers**: As the sample size increases, the sample mean converges in probability to the population mean.
- **Strong Law of Large Numbers**: As the sample size increases, the sample mean almost surely converges to the population mean.

### Central Limit Theorem
- [Central Limit Theorem (Zhihu)](https://zhuanlan.zhihu.com/p/259280292)
- When samples are independent and identically distributed (i.i.d.), regardless of the original distribution, as the sample size n becomes sufficiently large, the "sample mean" approaches the population mean, and the sample variance approaches the population variance divided by the sample size.

The Central Limit Theorem emphasizes the distribution of the sample mean, and the samples should follow the original distribution. This means that the probability density function of the sample mean will always follow a normal distribution.

## Common Statistical Tests

### t-Test and z-Test
- **t-Test**: Used when the sample size is small or the population variance is unknown. The t-distribution has heavier tails compared to the normal distribution, making it better suited for handling extreme values in small samples.
- **z-Test**: Used for large samples or when the population variance is known.

### Chi-Square Test
- **Chi-Square Test of Independence**: Used to determine if there is a significant association between two categorical variables.
- **Chi-Square Goodness of Fit Test**: Used to determine if the observed frequencies of categorical variables match the expected frequencies.

### F-Test
- **F-Test**: Used to compare the variances of two or more groups, typically applied in Analysis of Variance (ANOVA).

## Statistics and Sampling Distributions
- [Various Distributions (Zhihu)](https://www.zhihu.com/question/365697476/answer/3316448243)
- According to statistical conventions, $n \geq 30$ is considered a large sample, and $n < 30$ is a small sample.

### Chi-Square Distribution
- When the sum of the squares of multiple normal random variables follows a distribution with n degrees of freedom, it is called a Chi-Square distribution, commonly used for variance testing.

$$
X = \sum_{i=1}^{n} \frac{(o_i - e_i)^2}{e_i}
$$

This is the **Chi-Square Distribution** statistic formula, where:
- $o_i$ is the observed value,
- $e_i$ is the expected value,
- $n$ is the total number of observations.

According to this formula, the Chi-Square statistic $X$ calculates the sum of the squared differences between observed and expected values divided by the expected values.

Under certain conditions, the Chi-Square statistic $X$ follows a Chi-Square distribution with $n$ degrees of freedom. This distribution is used to test the goodness of fit or independence of categorical data.

----
### T-Distribution

#### Relationship Between Normal Distribution and t-Distribution

- Let X follow a standard normal distribution $(0,1)$, and Y follow a Chi-Square distribution with n degrees of freedom.
- Then:

$$ 
t = \frac{X}{\sqrt{Y/n}} 
$$ 

follows a t-distribution with n degrees of freedom.

- When the degrees of freedom for the t-distribution are sufficiently large, the t-distribution approximates the standard normal distribution $N(0,1)$.

#### Sampling Distribution of a Single Normal Population
- Applicable for both large and small samples.
- This method is used to determine whether there is a significant difference between the sample mean and the population mean.
- **Example**

    Suppose an educational researcher wants to evaluate the impact of a new teaching method on students' mathematics scores. The researcher knows from historical data that the school's overall mean math score is 70 (population mean $\mu = 70$, and the score distribution is approximately normal). The researcher selects 30 students, applies the new teaching method, and tests their math scores after the experiment.

    For small samples or when the population variance is unknown, the t-distribution is used for statistical testing. The formula is as follows:

    $$
    \frac{\bar{x} - \mu}{\frac{s}{\sqrt{n}}} \sim t(n-1)
    $$

    where:
    - $\bar{x}$ is the sample mean,
    - $\mu$ is the population mean,
    - $s$ is the sample standard deviation,
    - $n$ is the sample size,
    - The statistic follows a t-distribution with $(n - 1)$ degrees of freedom.

#### Two-Sample t-Test for Significant Differences Between Means

#### Formula 1: Calculation of t-Statistic

$$
\frac{{(\bar{x} - \bar{y}) - (\mu_1 - \mu_2)}}{{S_w \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}} \sim t(n_1 + n_2 - 2)
$$

where:
- $\bar{x}$ and $\bar{y}$ are the sample means of the two groups
- $\mu_1$ and $\mu_2$ are the hypothesized population means (usually assumed to be 0)
- $S_w$ is the pooled sample variance
- $n_1$ and $n_2$ are the sample sizes of the two groups
- $t(n_1 + n_2 - 2)$ is the t-distribution with $(n_1 + n_2 - 2)$ degrees of freedom

#### Formula 2: Calculation of Pooled Sample Variance

$$
S_w^2 = \frac{{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}}{{n_1 + n_2 - 2}}
$$

where:
- $s_1^2$ and $s_2^2$ are the sample variances of the two groups
- $n_1$ and $n_2$ are the sample sizes of the two groups

#### Example

Suppose a nutrition researcher wants to compare the effectiveness of two different diet plans on weight loss. The researcher randomly divides 60 participants who wish to lose weight into two groups, with 30 people in each group. The first group follows Diet Plan A, and the second group follows Diet Plan B.

(Note: Here, Welch's t-test is used, which does not assume equal population variances.)

#### Welch's t-Test (Does Not Assume Equal Population Variances)

#### Formula

$$
t = \frac{{x_1 - x_2}}{{\sqrt{\frac{{s_1^2}}{{n_1}} + \frac{{s_2^2}}{{n_2}}}}}
$$

#### Calculation of Degrees of Freedom

The degrees of freedom for Welch's t-test are calculated using the following formula:

$$
df = \frac{{\left( \frac{{s_1^2}}{{n_1}} + \frac{{s_2^2}}{{n_2}} \right)^2}}{{\frac{{\left( \frac{{s_1^2}}{{n_1}} \right)^2}}{{n_1 - 1}} + \frac{{\left( \frac{{s_2^2}}{{n_2}} \right)^2}}{{n_2 - 1}}}}
$$

where:
- $x_1$ and $x_2$ are the sample means of the two groups
- $s_1^2$ and $s_2^2$ are the sample variances of the two groups
- $n_1$ and $n_2$ are the sample sizes of the two groups
- $df$ is the degrees of freedom

#### Note
- **t-Distribution**: Compared to the normal distribution, the t-distribution has heavier tails, meaning it can better handle the additional variability introduced by small sample sizes.

- The t-distribution is used when the population variance is unknown and the sample size is small. As the degrees of freedom increase, the t-distribution approaches the standard normal distribution.
- **Why use the t-Distribution when the Variance is Unknown or Sample Size is Small?**

    In statistics, when the population variance is unknown or the sample size is small, the **t-distribution** is used instead of the standard normal distribution for two main reasons:
    1. **Heavier Tails**:
       - The t-distribution has heavier tails compared to the standard normal distribution. Heavier tails mean that extreme values are more likely in the t-distribution than in the normal distribution. When the sample size is small and the population variance is unknown, the variability in the data may be larger, and the t-distribution better reflects the probability of extreme values.
       
    2. **Effect of Degrees of Freedom**:
       - The shape of the t-distribution is influenced by the **degrees of freedom**, which are directly related to the sample size. The larger the degrees of freedom, the more the t-distribution resembles the normal distribution. As the sample size increases, the tails of the t-distribution become thinner, gradually approaching the standard normal distribution. Therefore, as the sample size grows, the difference between the t-distribution and the standard normal distribution diminishes.

----
### F-Distribution
- When the ratio of two Chi-Square distributions follows an F-distribution, it is commonly used in Analysis of Variance (ANOVA) and regression analysis.
  
  When random variables $Y$ and $Z$ follow Chi-Square distributions with degrees of freedom $m$ and $n$ respectively, define the variable:

$$
X = \frac{(Y / m)}{(Z / n)}
$$

- Then $X$ follows an F-distribution with the first degree of freedom $m$ and the second degree of freedom $n$.
