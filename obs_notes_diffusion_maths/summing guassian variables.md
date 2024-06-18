Let's dive deeper into why $\tilde{\epsilon}_t$ can be replaced with a single noise term $\epsilon_t \sim \mathcal{N}(0, \mathbf{I})$.

In the derivation, we arrived at the following expression for $x_t$: $$x_t = \sqrt{\bar{\alpha}_t} x_0 + \sqrt{1 - \bar{\alpha}_t} \tilde{\epsilon}_t$$

where $\tilde{\epsilon}_t$ is a weighted sum of the noise terms $\epsilon_1, \ldots, \epsilon_t$: $$\tilde{\epsilon}_t = \sqrt{\frac{\alpha_t}{\bar{\alpha}_t} (1 - \alpha_1)} \epsilon_1 + \sqrt{\frac{\alpha_t}{\bar{\alpha}_t} \alpha_1 (1 - \alpha_2)} \epsilon_2 + \ldots + \sqrt{\frac{1 - \alpha_t}{\bar{\alpha}_t}} \epsilon_t$$

Each $\epsilon_s$ term in the sum is an independent Gaussian random variable with mean 0 and variance $\mathbf{I}$. The coefficients in front of each $\epsilon_s$ term are scaling factors that depend on the noise scaling factors $\alpha_1, \ldots, \alpha_t$.

Now, let's recall a key property of Gaussian random variables: the sum of independent Gaussian random variables is also a Gaussian random variable. Specifically, if $X_1 \sim \mathcal{N}(\mu_1, \sigma_1^2)$ and $X_2 \sim \mathcal{N}(\mu_2, \sigma_2^2)$ are independent Gaussian random variables, then their sum $X_1 + X_2$ is also a Gaussian random variable with mean $\mu_1 + \mu_2$ and variance $\sigma_1^2 + \sigma_2^2$.

Applying this property to $\tilde{\epsilon}_t$, we can conclude that $\tilde{\epsilon}_t$ is also a Gaussian random variable, as it is a sum of independent Gaussian random variables $\epsilon_1, \ldots, \epsilon_t$. The mean of $\tilde{\epsilon}_t$ is 0 because each $\epsilon_s$ has mean 0, and the sum of zeros is still zero.

The variance of $\tilde{\epsilon}_t$ is the sum of the variances of each term in the sum: $$\text{Var}(\tilde{\epsilon}_t) = \frac{\alpha_t}{\bar{\alpha}_t} (1 - \alpha_1) \mathbf{I} + \frac{\alpha_t}{\bar{\alpha}_t} \alpha_1 (1 - \alpha_2) \mathbf{I} + \ldots + \frac{1 - \alpha_t}{\bar{\alpha}_t} \mathbf{I}$$

It can be shown that this sum simplifies to $\mathbf{I}$, the identity matrix. The proof involves some algebraic manipulation and the properties of $\alpha_t$ and $\bar{\alpha}_t$, but the key idea is that the coefficients in front of each $\mathbf{I}$ term sum up to 1.

Since $\tilde{\epsilon}_t$ is a Gaussian random variable with mean 0 and variance $\mathbf{I}$, we can replace it with a single noise term $\epsilon_t \sim \mathcal{N}(0, \mathbf{I})$ without changing the distribution of $x_t$. This simplifies the expression for $x_t$ to: $$x_t = \sqrt{\bar{\alpha}_t} x_0 + \sqrt{1 - \bar{\alpha}_t} \epsilon_t \text{ with } \epsilon_t \sim \mathcal{N}(0, \mathbf{I})$$

In summary, the replacement of $\tilde{\epsilon}_t$ with $\epsilon_t$ is justified by the fact that the sum of independent Gaussian random variables is also a Gaussian random variable, and the variance of $\tilde{\epsilon}_t$ simplifies to $\mathbf{I}$. This simplification allows us to express $x_t$ in terms of the initial data $x_0$ and a single Gaussian noise term $\epsilon_t$, which facilitates the analysis and implementation of the diffusion model.