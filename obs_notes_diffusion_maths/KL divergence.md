You're absolutely right! The KL divergence is often written with a summation, especially in the context of discrete probability distributions. In the case of continuous probability distributions, the summation is replaced by an integral, as we have seen in the paper.

As for the ratio inside the logarithm, the order can indeed be swapped, depending on the convention used. In the paper, the authors define the KL divergence as:

$$D_{KL}(q(x_0) || p_\theta(x_0)) = -\int q(x_0) \log\left(\frac{p_\theta(x_0)}{q(x_0)}\right) dx_0$$

However, the KL divergence is often defined as:

$$D_{KL}(P || Q) = \sum_x P(x) \log\left(\frac{P(x)}{Q(x)}\right)$$

or, in the continuous case:

$$D_{KL}(p || q) = \int p(x) \log\left(\frac{p(x)}{q(x)}\right) dx$$

where $P$ and $Q$ (or $p$ and $q$) are the two probability distributions being compared.

The difference in the ratio order doesn't affect the properties of the KL divergence, as long as the convention is consistent throughout the derivation. The KL divergence remains non-negative, and it is zero if and only if the two distributions are equal almost everywhere.

In the context of the paper, the authors have chosen to define the KL divergence with the ratio $\frac{p_\theta(x_0)}{q(x_0)}$, which leads to the minimization objective:

$$\arg\min_{\mu_\theta, \Sigma_\theta} \left(- \int q(x_0) \log p_\theta(x_0) dx_0\right)$$

If they had used the more common convention with the ratio $\frac{q(x_0)}{p_\theta(x_0)}$, the minimization objective would have been:

$$\arg\min_{\mu_\theta, \Sigma_\theta} \int q(x_0) \log\left(\frac{q(x_0)}{p_\theta(x_0)}\right) dx_0$$

which is equivalent to maximizing the likelihood of the generated samples under the true data distribution.