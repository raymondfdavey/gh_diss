
$$X_t = √(1 - β_t) X_{t-1} + √β_t ε_t$$

The  choice of $\sqrt{1 - \beta_t}$ and $\sqrt{\beta_t}$ is likely due to mathematical convenience as it allows for a clean decomposition of the process into a shrinking deterministic component ($\sqrt{1 - \beta_t}X_{t-1}$) and an additive Gaussian noise component ($\sqrt{\beta_t}\epsilon_t$).

Additionally, the parametrization using $\beta_t \in (0, 1)$ allows for a simple control over the trade-off between preserving the previous value ($\sqrt{1 - \beta_t}X_{t-1}$) and adding Gaussian noise ($\sqrt{\beta_t}\epsilon_t$). As $\beta_t$ increases, more noise is added, and as $\beta_t$ decreases, more of the previous value is preserved.
***
In terms of the dirty maths

The goal here is to demonstrate that the discretized diffusion process $X_t = \sqrt{1 - \beta_t}X_{t-1} + \sqrt{\beta_t}\epsilon_t$ converges to a standard Gaussian distribution as the number of steps $T$ goes to infinity, regardless of the initial value $X_0$ - which is the ckaim.

Let's start with the equation for $X_T$:

$X_T = \sqrt{1 - \beta_T}X_{T-1} + \sqrt{\beta_T}\epsilon_T$

We can expand this by substituting the expression for $X_{T-1}$:

$$X_T = \sqrt{1 - \beta_T}(\sqrt{1 - \beta_{T-1}}X_{T-2} + \sqrt{\beta_{T-1}}\epsilon_{T-1}) + \sqrt{\beta_T}\epsilon_T$$
which expands to 
     $$X_T = \sqrt{1 - \beta_T}\sqrt{1 - \beta_{T-1}}X_{T-2} + \sqrt{1 - \beta_T}\sqrt{\beta_{T-1}}\epsilon_{T-1} + \sqrt{\beta_T}\epsilon_T$$

We can continue this expansion for all $X_{T-2}$ steps:

$$X_T = \sqrt{1 - \beta_T}\sqrt{1 - \beta_{T-1}}\sqrt{1 - \beta_{T-2}}X_{T-3} + \sqrt{1 - \beta_T}\sqrt{1 - \beta_{T-1}}\sqrt{\beta_{T-2}}\epsilon_{T-2} + \sqrt{1 - \beta_T}\sqrt{\beta_{T-1}}\epsilon_{T-1} + \sqrt{\beta_T}\epsilon_T$$

which could go on for all T minus' and so simplifies to (where $X_0 == X_{T-N}$):

$X_T= \left(\prod_{t=1}^T \sqrt{1 - \beta_t}\right)X_0 + \sum_{t=1}^T\left(\prod_{s=t+1}^T \sqrt{1 - \beta_s}\right)\sqrt{\beta_t}\epsilon_t$

Now, let's look at the two terms separately:

1) The first term: $\left(\prod_{t=1}^T \sqrt{1 - \beta_t}\right)X_0$
   - This term represents the contribution of the initial value $X_0$ to the final value $X_T$.
   - As $T$ gets large, this term will converge to zero because $\sqrt{1 - \beta_t} < 1$ for all $t$, so the product of many such terms will become very small.

2) The second term: $\sum_{t=1}^T\left(\prod_{s=t+1}^T \sqrt{1 - \beta_s}\right)\sqrt{\beta_t}\epsilon_t$
   - This term represents the sum of the Gaussian noise added at each step, weighted by the product of the drift coefficients from that step onwards.
   - Each $\epsilon_t$ is an independent standard Gaussian random variable, so this sum is itself a Gaussian random variable.
   - The variance of this Gaussian is the sum of the variances of each term: $\sum_{t=1}^T\beta_t\left(\prod_{s=t+1}^T (1 - \beta_s)\right)$
   - As $T$ gets large, this variance converges to 1, because $\sum_{t=1}^T\beta_t \rightarrow 1$ (this is an assumption they make, and it's reasonable if the $\beta_t$ are chosen appropriately).

Therefore, as $T \rightarrow \infty$, the first term goes to zero, and the second term becomes a standard Gaussian random variable with mean 0 and variance 1. This means that regardless of the initial value $X_0$, the discretized diffusion process converges to a standard Gaussian distribution in the limit of many steps.

This demonstration justifies the use of the square root coefficients $\sqrt{1 - \beta_t}$ and $\sqrt{\beta_t}$ in the discretized diffusion process, as they lead to the desired convergence to a standard Gaussian distribution.

Let me know if any part of this explanation needs further clarification!
***
Yes, this explanation does cover the justification for the use of square roots in the coefficients of the discretized diffusion process. Let me summarize the key points:

1) The use of square roots in the coefficients $\sqrt{1 - \beta_t}$ and $\sqrt{\beta_t}$ allows for a clean separation of the process into a deterministic drift term and a stochastic diffusion term.

2) The drift term $\sqrt{1 - \beta_t}X_{t-1}$ is designed to shrink the contribution of the previous value $X_{t-1}$ over time. The square root ensures that $\sqrt{1 - \beta_t} < 1$, so the product of many such terms converges to zero as $T \rightarrow \infty$. This is what causes the process to forget its initial value $X_0$.

3) The diffusion term $\sqrt{\beta_t}\epsilon_t$ is designed to add Gaussian noise at each step. The square root here ensures that the sum of the variances of these noise terms converges to 1 as $T \rightarrow \infty$, under the assumption that $\sum_{t=1}^T\beta_t \rightarrow 1$. This is what causes the process to converge to a standard Gaussian distribution.

4) Without the square roots, it would be more difficult to ensure these convergence properties. For example, if we used $\beta_t$ instead of $\sqrt{\beta_t}$ in the diffusion term, the sum of the variances would converge to something other than 1, and we would not get a standard Gaussian in the limit.

So the use of square roots in the coefficients is a clever mathematical trick that ensures the desired convergence properties of the discretized diffusion process: forgetting the initial value and converging to a standard Gaussian distribution. The informal demonstration in the paper relies on these square roots to derive the limit behavior of the process as $T \rightarrow \infty$.