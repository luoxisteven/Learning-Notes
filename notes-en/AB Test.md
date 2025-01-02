# A/B Test

An A/B test is a method of comparing two or more options to determine which one performs better. This is typically done by comparing changes in a specific metric.

## A/B Test Process

1. **Define the Experiment's Objective**:
   - Whether the new feature or project aims to improve return, profit, ROI, conversion rate, etc.
   - A key metric needs to be selected to determine which feature or project performs better.

2. **Hypothesis Testing**:
   - Propose the null hypothesis and alternative hypothesis.

3. **Set the Significance Level**:
   - Define the significance level and determine the minimum acceptable threshold.

4. **Determine Sample Size and Experiment Duration**:
   - Calculate the required sample size and set the experiment's duration.

5. **Calculate Results**:
   - Analyze the results to determine whether the null hypothesis should be rejected and conclude which option is better.

## Possible Reasons for A/B Test Failures

1. **Novelty Effect**:
   - Initially, customers may show interest in a new feature, but as time progresses, their interest wanes, and the effect may no longer be significant.

2. **Insufficient Sample Size**:
   - If the sample size is too small, the test results may be inaccurate or inconclusive.

3. **External Factors**:
   - External events like floods, earthquakes, or policy changes can affect the experiment's results.
   - Since comparison experiments are sometimes not run simultaneously, events happening during different time periods may indirectly impact the results.

## Statistical Principles in A/B Testing

- **Hypothesis Testing**: Hypothesis testing is used to determine the significance of experimental results and decide whether to reject the null hypothesis.

## How Long Should an A/B Test Run to Meet Significance Requirements? How to Evaluate?

The duration of an A/B test mainly depends on the following factors:
1. **Sample Size**:
   - The larger the sample size, the easier it is to observe significant differences. The required sample size needs to be estimated using a sample size calculation formula (explained later).

2. **Baseline Conversion Rate**:
   - Before the experiment starts, the current conversion rate must be known, which will serve as a baseline to determine if the new option shows significant improvement.

3. **Expected Improvement**:
   - Estimate how much improvement the new option will bring compared to the current one. The smaller the expected improvement, the larger the sample size required.

4. **Significance Level and Test Power**:
   - The significance level is usually set to 5% (i.e., 95% confidence), and the test power is usually set to 80%. The significance level affects the precision required in calculating the sample size.

## Evaluating the Duration of A/B Tests

To assess the duration of an experiment:
- Determine the required **total sample size**.
- Estimate the **daily traffic** and assess how many days it will take to gather the necessary sample.

For example:
- If the calculated sample size is 5000 people, and 1000 people participate in the experiment daily, the test will require at least 5 days to complete.

## How to Determine A/B Test Sample Size?

The sample size calculation formula is usually based on the following parameters:
- **Baseline Conversion Rate (p1)**: The conversion rate before the experiment.
- **Minimum Detectable Effect (MDE)**: The minimum expected improvement in conversion rate with the new option.
- **Significance Level (Alpha)**: Typically set at 0.05 (5%).
- **Statistical Power (Beta)**: Typically set at 0.80 (80%).

The sample size formula is:

$$
n = \frac{{Z_{\alpha/2}^2 \cdot p_1 (1 - p_1) + Z_{\beta}^2 \cdot p_2 (1 - p_2)}}{{(p_1 - p_2)^2}}
$$

- $p_1$ is the baseline conversion rate.
- $p_2$ is the expected conversion rate after the improvement.
- $Z_{\alpha/2}$ is the Z-score corresponding to the significance level (1.96 for a 95% confidence level).
- $Z_{\beta}$ is the Z-score corresponding to the statistical power (0.84 for 80% power).

## Sample Size Calculation for Two Proportions

The formula for calculating the sample size $ N $ is:

$$
N = \frac{{\left( Z_{\alpha/2} + Z_{\beta} \right)^2 \cdot \sigma^2}}{{\delta^2}} \approx \frac{{8 \cdot \sigma^2}}{{\delta^2}}
$$

Where:
- $ \alpha = 0.05 $, $ Z_{\alpha/2} = 1.96 $ (for a 95% confidence level)
- $ \beta = 0.2 $, $ Z_{\beta} = 0.84 $ (for 80% power)
- $ \sigma $ is the standard deviation of the sample
- $ \delta $ is the minimal detectable difference between the two proportions

### General Case:

- Significance level: $ \alpha = 0.05 $, $ Z_{\alpha/2} = 1.96 $
- Statistical power: $ \beta = 0.2 $, $ Z_{\beta} = 0.84 $
- $ \sigma $ represents the standard deviation, and $ \delta $ is the minimum difference between the groups.


## Principles for Traffic Allocation in A/B Tests

1. **Randomness**:
   - The allocation of different experimental groups should be as random as possible to avoid systematic bias.

2. **Independence**:
   - Ensure that the user experience in each experimental group is independent, preventing any cross-group influence.

3. **Equivalence**:
   - The sample sizes in each group should be as similar as possible to ensure comparability of the results.

4. **Consistency**:
   - Ensure that the same user is consistently assigned to the same experimental group throughout the entire experiment to avoid interference from group-switching.

## How to Solve the Problem of Insufficient Traffic

To address the problem of insufficient traffic, A/B tests can use a **Multi-Armed Bandit (MAB)** approach, with the **Upper Confidence Bound (UCB)** algorithm being a common method.

- **Multi-Armed Bandit (MAB)**:
   - This is a strategy that dynamically adjusts resource allocation through exploration and exploitation in uncertain environments. It allocates more traffic to the better-performing options, thus improving the use of traffic.

- **UCB Algorithm**:
   - The UCB algorithm continuously evaluates the performance of each experimental group and assigns more traffic to better-performing groups while maintaining some level of exploration to discover potentially better options.

## What is an AA Test?

- **AA Test**: An A/B test conducted without introducing any new features or changes, using the same group or bucket of data to check for significant differences.
  
- **Purpose**: The AA test aims to verify that there are no significant differences in the data collection or traffic allocation logic. If an AA test shows significant differences, it suggests that there may be issues with data collection or the experiment's traffic allocation, requiring correction or data re-collection.

- **Expected Result**: The expected result of an AA test is **no significant difference**, meaning the two groups should show similar results.
