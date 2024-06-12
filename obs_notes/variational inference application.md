The negative sign is not normally present in the standard definition of the KL divergence. In most literature, the KL divergence is defined as:

$$D_{KL}(q(x_0) || p_\theta(x_0)) = \int q(x_0) \log\left(\frac{q(x_0)}{p_\theta(x_0)}\right) dx_0$$

However, in the context of the diffusion model and the variational upper bound $\bar{L}$, the authors have introduced a negative sign in the definition of the KL divergence. Let's rewrite the explanation, making this fact explicit.

Why the negative sign?

The authors of the diffusion model paper have introduced a negative sign in their definition of the KL divergence, which differs from the standard definition. They define the KL divergence as:

$$D_{KL}(q(x_0) || p_\theta(x_0)) = -\int q(x_0) \log\left(\frac{p_\theta(x_0)}{q(x_0)}\right) dx_0$$

This modification to the standard definition is intentional and serves a specific purpose in the context of the variational upper bound $\bar{L}$ used in the diffusion model:

$$\bar{L} = -\mathbb{E}_q\left[\log \frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}\right]$$

The authors introduce this upper bound as a surrogate objective to minimize instead of directly maximizing the log-likelihood $\log p_\theta(x_0)$, which is often intractable to compute or optimize directly.

The negative sign in the modified definition of the KL divergence and the upper bound $\bar{L}$ serves two important purposes:

1. Variational inference: In variational inference, the goal is to maximize a lower bound (ELBO) on the log-likelihood or, equivalently, minimize an upper bound. By introducing a negative sign in the definition of the KL divergence and $\bar{L}$, the authors cast the problem as a minimization problem, which is consistent with the variational inference framework.

2. Consistency with the objective function: The negative sign ensures that the subsequent derivations and the resulting KL divergence terms appear with a positive sign in the final expression of the upper bound. This consistency is important for the interpretation and optimization of the objective function.

To understand the relationship between the true log-likelihood and the upper bound $\bar{L}$, we can use Jensen's inequality:

$$\log p_\theta(x_0) = \log \int p_\theta(x_{0:T}) dx_{1:T} \geq \mathbb{E}_q\left[\log \frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}\right] = -\bar{L}$$

The inequality holds because the log function is concave. By minimizing $\bar{L}$, we are effectively maximizing a lower bound on the log-likelihood $\log p_\theta(x_0)$. This approach allows for tractable optimization of the model parameters while indirectly maximizing the log-likelihood.

In summary, the authors of the diffusion model paper have intentionally introduced a negative sign in their definition of the KL divergence, which differs from the standard definition. This modification, along with the negative sign in the variational upper bound $\bar{L}$, serves the purpose of casting the optimization problem as a minimization problem, maintaining consistency with the variational inference framework, and ensuring that the resulting KL divergence terms appear with a positive sign in the final objective function. By minimizing the upper bound $\bar{L}$, the authors indirectly maximize the log-likelihood of the data, which is the ultimate goal of the diffusion model.