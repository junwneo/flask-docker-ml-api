# ATE Estimation Report

## 📘 Description of Data

This dataset contains simulated observations from 20 corporations, each with:

- A **stakeholder engagement score** (Y)
- A **binary treatment indicator** (W) indicating participation in a carbon offset program
- **Annual sustainability spending** in \$1,000s (X)

---

## 🧠 Regression Model

We estimate:

\[
Y_i = \alpha + \tau W_i + \beta X_i + \varepsilon_i
\]

---

## 📊 Results

- **Intercept (α):** 95.966  
- **Average Treatment Effect (τ):** −9.106  
- **Effect of Spending (β):** 1.515  

---
# Answer

## (b) Estimated ATE (τ̂) and Its Statistical Significance

We estimate the causal effect of participation in a **carbon offset program** on a corporation’s **stakeholder engagement score**, controlling for **annual sustainability spending**.

Using a linear regression model of the form:

\[
Y_i = \alpha + \tau W_i + \beta X_i + \varepsilon_i
\]

we obtain the following estimates:

- **Intercept (α):** 95.966
- **Average Treatment Effect (τ̂):** −9.106
- **Coefficient for Spending (β):** 1.515

**Estimated Average Treatment Effect (τ̂):**  
The regression analysis estimates the ATE to be **−9.106**, indicating that **participation in the carbon offset program is associated with a decrease of approximately 9.1 points** in the stakeholder engagement score, after controlling for annual spending on sustainability initiatives.

**Statistical Significance:**  
This effect is **statistically significant at the 1% level** (*p* < 0.001), with a **95% confidence interval of [−13.44, −4.77]**. This suggests that the negative association between treatment and engagement is unlikely due to chance, even when accounting for differences in sustainability spending across corporations.

The coefficient for **sustainability spending (X)** is also **statistically significant** (*p* < 0.01), with a **positive estimate of 1.515**, confirming that **increased investment in sustainability is associated with higher engagement scores**.

---

## (c) Assumptions Required for a Causal Interpretation of τ̂

To interpret \( \hat{\tau} \) as a **causal effect** (i.e., the true impact of carbon offset program participation on engagement), the following assumptions must hold:

1. **Unconfoundedness (Ignorability):**  
   Given the observed covariate \( X \) (annual sustainability spending), the assignment to treatment (W) is assumed to be independent of potential outcomes. This means there are no **unobserved confounders** that influence both a company’s decision to participate and its engagement score. Violation of this assumption would bias the ATE estimate.

2. **Positivity (Overlap):**  
   Every corporation has a **non-zero probability** of receiving either the treatment or control condition for any value of \( X \). Without overlap, it becomes impossible to estimate the counterfactual outcomes for some groups.

3. **SUTVA (Stable Unit Treatment Value Assumption):**  
   Each corporation’s outcome is affected **only by its own treatment status**, and there are no spillover effects. Also, the treatment (participation in the carbon offset program) is assumed to have **a single, consistent version** across all corporations.

If these assumptions are satisfied, the estimated coefficient \( \hat{\tau} \) represents the **Average Treatment Effect (ATE)** of participating in the carbon offset program on stakeholder engagement scores.

---

