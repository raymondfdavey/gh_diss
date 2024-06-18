
Forward: 
$q(x_t|x_{t-1}) = \mathcal{N}(x_t; \sqrt{1 - \beta_t} x_{t-1}, \beta_t \mathbf{I})$
Backward:
$p_\theta(x_{t-1}|x_{t}) = \mathcal{N}(x_{t-1}; \mu_\theta(x_t, t), \Sigma_\theta(x_t, t)$
and
$p_\theta(x_{t-1}|x_t) \approx q(x_{t-1}|x_t)$ where $q(x_{t-1}|x_t)$ is the true reverse diffusion dist.

$\mu_\theta(x_t, t),\text{ and } \Sigma_\theta(x_t, t)$ are FUNCTIONS PARAMETERISED BY $\theta$ TO BE LEARNED BY THE NN

Certainly! Let's focus on the relationship between the true reverse transition probability $q(x_{t-1}|x_t)$ and the approximated parameterized probability distribution $p_\theta(x_{t-1}|x_t)$.

In the diffusion process, the forward transition probability $q(x_t|x_{t-1})$ is known and defined by the Gaussian noise addition process. However, the true reverse transition probability $q(x_{t-1}|x_t)$, which describes the probability of transitioning from a noisy state $x_t$ to a less noisy state $x_{t-1}$, is unknown.

The goal is to learn a model that approximates this true reverse transition probability. This is where the parameterized probability distribution $p_\theta(x_{t-1}|x_t)$ comes into play. The subscript $\theta$ indicates that this distribution is parameterized by learnable parameters $\theta$, which are typically the weights of a neural network.

The parameterized probability distribution $p_\theta(x_{t-1}|x_t)$ is designed to approximate the true reverse transition probability $q(x_{t-1}|x_t)$. In other words, we want to learn the parameters $\theta$ such that $p_\theta(x_{t-1}|x_t)$ is as close as possible to $q(x_{t-1}|x_t)$.

Mathematically, this approximation can be expressed as:

$$p_\theta(x_{t-1}|x_t) \approx q(x_{t-1}|x_t)$$

The approximation is achieved by minimizing a suitable divergence or distance measure between the two distributions. In the case of diffusion models, the Kullback-Leibler (KL) divergence is commonly used.

The KL divergence between $q(x_{t-1}|x_t)$ and $p_\theta(x_{t-1}|x_t)$ is defined as:

$$D_{KL}(q(x_{t-1}|x_t) || p_\theta(x_{t-1}|x_t)) = \mathbb{E}_{q(x_{t-1}|x_t)}\left[\log \frac{q(x_{t-1}|x_t)}{p_\theta(x_{t-1}|x_t)}\right]$$

By minimizing the KL divergence, we encourage the parameterized distribution $p_\theta(x_{t-1}|x_t)$ to be as close as possible to the true reverse transition probability $q(x_{t-1}|x_t)$.

In practice, the parameterized distribution $p_\theta(x_{t-1}|x_t)$ is often chosen to be a Gaussian distribution with learnable mean and variance parameters. The neural network takes the noisy state $x_t$ as input and outputs the parameters of the Gaussian distribution.

During training, the model learns to predict the parameters of the Gaussian distribution that best approximate the true reverse transition probability. This is done by minimizing the variational lower bound on the negative log-likelihood, as discussed in the previous answer.

By learning the parameters $\theta$ of the parameterized distribution $p_\theta(x_{t-1}|x_t)$, the model effectively learns to approximate the true reverse transition probability $q(x_{t-1}|x_t)$. This allows the model to generate clean samples by starting from random noise and iteratively applying the learned reverse transitions.

In summary, the parameterized probability distribution $p_\theta(x_{t-1}|x_t)$ is introduced to approximate the true reverse transition probability $q(x_{t-1}|x_t)$. By minimizing a suitable divergence measure, such as the KL divergence, the model learns the parameters $\theta$ that make $p_\theta(x_{t-1}|x_t)$ as close as possible to $q(x_{t-1}|x_t)$. This approximation enables the model to learn the reverse process and generate clean samples from noisy inputs.

***
Sure! Let's rewrite and explain the section you mentioned, which focuses on the reverse process, the parameterized probability distribution, and the loss function.

As we described in the previous subsection, our goal is to learn the reverse process of the forward diffusion process, which is expected to go from the simple Gaussian noise distribution back to the original complex data distribution. We want to learn a model that can generate clean samples by starting from random noise and gradually denoising it.

$p_\theta(x_{t-1}|x_{t}) = \mathcal{N}(x_{t-1}; \mu_\theta(x_t, t), \Sigma_\theta(x_t, t)$

To achieve this, we introduce a parameterized probability distribution $p_\theta(x_{t-1}|x_t)$, which represents the reverse process. The subscript $\theta$ indicates that this distribution is parameterized by learnable parameters $\theta$, which are typically the weights of a neural network.

The reverse process is also modeled as a Markov chain, but in the opposite direction of the forward process. It starts from the final noise sample $x_T$ and progressively denoises it to obtain the clean sample $x_0$. The parameterized probability distribution $p_\theta(x_{t-1}|x_t)$ defines the transition probabilities between consecutive states in the reverse process.

Since the reverse process is a Markov chain, we can express the probability of a complete reverse trajectory $x_{T:0}$ as the product of the transition probabilities as we saw in the latter parts of [[3 Mathematics of Diffusion]]:

$$p_\theta(x_{T:0}) = p(x_T) \prod_{t=1}^T p_\theta(x_{t-1}|x_t)$$

Here, $p(x_T)$ represents the prior distribution of the final noise sample, which is typically chosen to be a simple Gaussian distribution.

The goal is to learn the parameters $\theta$ of the reverse process model $p_\theta(x_{t-1}|x_t)$ so that the generated samples from the reverse process closely resemble the clean samples from the original data distribution.

***
LOSS
Let's dive deeper into the loss function, its derivation, and how it drives the optimization of the parameters in the diffusion model.

Note on [[Expected Value Subscript Notation]]

The goal of the diffusion model is to learn the reverse process that can generate clean samples from random noise. To achieve this, we need to define a loss function that measures the discrepancy between the generated samples and the real samples from the training data.

The authors propose to use the negative log-likelihood (NLL) of the clean samples under the reverse process model as the loss function:

$$L = \mathbb{E}_{x_0 \sim q(x_0)}[-\log p_\theta(x_0)]$$

Here, $x_0$ represents the clean samples from the training data, and $q(x_0)$ is the true data distribution. The term $p_\theta(x_0)$ represents the probability of generating the clean sample $x_0$ using the reverse process model parameterized by $\theta$.

Minimizing the negative log-likelihood encourages the reverse process model to assign high probability to the clean samples from the training data. In other words, it drives the model to generate samples that are similar to the real samples.

However, directly optimizing this loss function is challenging because it involves computing the marginal probability $p_\theta(x_0)$, which requires integrating over all possible reverse trajectories:

$$p_\theta(x_0) = \int p_\theta(x_{0:T}) dx_{1:T}$$

This integral is intractable to compute in practice, especially for high-dimensional data.

To overcome this challenge, the authors introduce a variational lower bound on the negative log-likelihood. They start by applying the Jensen's inequality, which states that for a concave function $f$ (in this case, the negative logarithm) and a random variable $X$:

$$f(\mathbb{E}[X]) \geq \mathbb{E}[f(X)]$$

Applying Jensen's inequality to the negative log-likelihood, we get:

$$-\log p_\theta(x_0) = -\log \mathbb{E}_{q(x_{1:T}|x_0)}\left[\frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}\right] \leq \mathbb{E}_{q(x_{1:T}|x_0)}\left[-\log \frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}\right]$$

Here, $q(x_{1:T}|x_0)$ represents the forward diffusion process conditioned on the clean sample $x_0$. It defines the distribution of the noisy samples $x_{1:T}$ generated by applying the forward diffusion process to $x_0$.

The variational lower bound on the right-hand side of the inequality provides a tractable objective that can be optimized. It involves an expectation over the forward diffusion process, which can be estimated using Monte Carlo sampling.

By minimizing the variational lower bound, we are effectively maximizing a lower bound on the log-likelihood of the clean samples under the reverse process model. This drives the model to generate samples that are more likely to be clean samples from the training data.

The training objective becomes:

$$\min_\theta \mathbb{E}_{x_0 \sim q(x_0)} \mathbb{E}_{q(x_{1:T}|x_0)}\left[-\log \frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}\right]$$

To optimize this objective, we use stochastic gradient descent (SGD) or its variants. The gradients of the objective with respect to the parameters $\theta$ are computed using backpropagation through the reverse process model.

During each training iteration, we sample a mini-batch of clean samples $x_0$ from the training data. For each clean sample, we generate a random forward trajectory $x_{1:T}$ by applying the forward diffusion process. We then compute the log-likelihood ratio $-\log \frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}$ for each trajectory and average them to estimate the expectation.

The gradients of the average log-likelihood ratio with respect to the parameters $\theta$ are computed using backpropagation. These gradients indicate how the parameters should be updated to minimize the objective and improve the reverse process model.

By iteratively updating the parameters using the gradients, the model learns to generate samples that are more likely to be clean samples from the training data. The optimization process drives the reverse process model to assign higher probability to the clean samples and lower probability to the noisy samples.

As the training progresses, the reverse process model becomes better at generating clean samples from random noise. The learned parameters $\theta$ capture the statistical properties and patterns of the training data, allowing the model to generate realistic and diverse samples.

It's worth noting that the variational lower bound is a tractable approximation to the true negative log-likelihood. It provides a way to optimize the reverse process model without the need to explicitly compute the intractable marginal probability $p_\theta(x_0)$.

In practice, the expectation over the forward diffusion process is estimated using Monte Carlo sampling. For each clean sample $x_0$, we generate a random forward trajectory $x_{1:T}$ and use it to compute the log-likelihood ratio. The average of these log-likelihood ratios serves as an unbiased estimate of the expectation.

The choice of the variational lower bound as the training objective is motivated by the fact that it is a tractable approximation to the true negative log-likelihood. It allows us to optimize the reverse process model efficiently using stochastic gradient descent and backpropagation.

By minimizing the variational lower bound, the model learns to generate samples that are more likely to be clean samples from the training data. The optimization process adjusts the parameters $\theta$ to maximize the log-likelihood of the clean samples under the reverse process model.

In summary, the loss function in diffusion models is based on the negative log-likelihood of the clean samples under the reverse process model. To make the optimization tractable, a variational lower bound is introduced using Jensen's inequality. The training objective becomes the minimization of the variational lower bound, which is estimated using Monte Carlo sampling and optimized using stochastic gradient descent. By minimizing this objective, the model learns to generate clean samples from random noise, capturing the statistical properties and patterns of the training data. The optimization process drives the reverse process model to assign higher probability to the clean samples, leading to the generation of realistic and diverse samples.

***
LOSSSSSSSSSSSS questions from here

To train the reverse process model, we need to define a loss function that measures the difference between the generated samples and the real samples. The loss function is typically chosen to be the negative log-likelihood (NLL) of the clean samples under the reverse process model:

$$L = \mathbb{E}_{x_0 \sim q(x_0)}[-\log p_\theta(x_0)]$$

This loss function encourages the reverse process model to assign high probability to the clean samples from the real data distribution.

However, directly optimizing this loss function is challenging because it involves marginalizing over all possible reverse trajectories. To make the optimization tractable, the authors introduce a variational lower bound on the negative log-likelihood:

$$-\log p_\theta(x_0) \leq \mathbb{E}_{q(x_{1:T}|x_0)}\left[-\log \frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}\right]$$

This lower bound is obtained by applying Jensen's inequality and using the fact that the KL divergence is non-negative. The term $q(x_{1:T}|x_0)$ represents the forward diffusion process conditioned on the clean sample $x_0$.

The variational lower bound provides a surrogate objective that can be optimized more easily. By minimizing this lower bound, we are effectively maximizing the log-likelihood of the clean samples under the reverse process model.

At this stage, the training objective becomes:

$$\min_\theta \mathbb{E}_{x_0 \sim q(x_0)} \mathbb{E}_{q(x_{1:T}|x_0)}\left[-\log \frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}\right]$$

This objective can be optimized using stochastic gradient descent or other optimization techniques.

The key ideas in this section are:
1. The reverse process is modeled by a parameterized probability distribution $p_\theta(x_{t-1}|x_t)$, which defines the transition probabilities between consecutive states in the reverse direction.
2. The goal is to learn the parameters $\theta$ of the reverse process model so that the generated samples closely resemble the clean samples from the real data distribution.
3. The negative log-likelihood (NLL) of the clean samples under the reverse process model is used as the loss function.
4. To make the optimization tractable, a variational lower bound on the NLL is introduced, which provides a surrogate objective that can be optimized more easily.

I hope this explanation clarifies the concepts introduced in this section. Let me know if you have any further questions!
***
ALL:

As we described in the previous subsection, our goal is to learn the reverse process of the forward diffusion process, which is expected to go from the simple Gaussian noise distribution back to the original complex data distribution. We want to learn a model that can generate clean samples by starting from random noise and gradually denoising it.

To achieve this, we introduce a parameterized probability distribution $p_\theta(x_{t-1}|x_t)$, which represents the reverse process. The subscript $\theta$ indicates that this distribution is parameterized by learnable parameters $\theta$, which are typically the weights of a neural network.

The reverse process is modeled as a Markov chain, similar to the forward process, but in the opposite direction. It starts from the final noise sample $x_T$ and progressively denoises it to obtain the clean sample $x_0$. The parameterized probability distribution $p_\theta(x_{t-1}|x_t)$ defines the transition probabilities between consecutive states in the reverse process.

In the diffusion process, the forward transition probability $q(x_t|x_{t-1})$ is known and defined by the Gaussian noise addition process. However, the true reverse transition probability $q(x_{t-1}|x_t)$, which describes the probability of transitioning from a noisy state $x_t$ to a less noisy state $x_{t-1}$, is unknown. The parameterized probability distribution $p_\theta(x_{t-1}|x_t)$ is introduced to approximate this true reverse transition probability.

Mathematically, we want to learn the parameters $\theta$ such that $p_\theta(x_{t-1}|x_t)$ is as close as possible to $q(x_{t-1}|x_t)$. This approximation is often achieved by minimizing a suitable divergence or distance measure between the two distributions, such as the Kullback-Leibler (KL) divergence.

Since the reverse process is modeled as a Markov chain, we can express the probability of a complete reverse trajectory $x_{T:0}$ as the product of the transition probabilities:

$$p_\theta(x_{T:0}) = p(x_T) \prod_{t=1}^T p_\theta(x_{t-1}|x_t)$$

Here, $p(x_T)$ represents the prior distribution of the final noise sample, which is typically chosen to be a simple Gaussian distribution.

The notation $x_{T:0}$ represents the sequence of states in the reverse process, starting from the final noise sample $x_T$ and going back to the clean sample $x_0$. The probability of this reverse trajectory is the product of the prior probability $p(x_T)$ and the transition probabilities $p_\theta(x_{t-1}|x_t)$ at each step.

The goal is to learn the parameters $\theta$ of the reverse process model $p_\theta(x_{t-1}|x_t)$ so that the generated samples from the reverse process closely resemble the clean samples from the original data distribution.

To train the reverse process model, we need to define a loss function that measures the difference between the generated samples and the real samples. The loss function is typically chosen to be the negative log-likelihood (NLL) of the clean samples under the reverse process model:

$$L = \mathbb{E}_{x_0 \sim q(x_0)}[-\log p_\theta(x_0)]$$

This loss function encourages the reverse process model to assign high probability to the clean samples from the real data distribution. The expectation $\mathbb{E}_{x_0 \sim q(x_0)}$ denotes that we are averaging the negative log-likelihood over the clean samples $x_0$ drawn from the true data distribution $q(x_0)$.

However, directly optimizing this loss function is challenging because it involves marginalizing over all possible reverse trajectories. To make the optimization tractable, the authors introduce a variational lower bound on the negative log-likelihood:

$$-\log p_\theta(x_0) \leq \mathbb{E}_{q(x_{1:T}|x_0)}\left[-\log \frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}\right]$$

This lower bound is obtained by applying Jensen's inequality and using the fact that the KL divergence is non-negative. The term $q(x_{1:T}|x_0)$ represents the forward diffusion process conditioned on the clean sample $x_0$.

Jensen's inequality is a fundamental result in probability theory that relates the value of a convex function of an expectation to the expectation of the convex function. In this case, the negative logarithm is a convex function, and applying Jensen's inequality allows us to obtain a lower bound on the negative log-likelihood.

The variational lower bound provides a surrogate objective that can be optimized more easily. By minimizing this lower bound, we are effectively maximizing the log-likelihood of the clean samples under the reverse process model.

At this stage, the training objective becomes:

$$\min_\theta \mathbb{E}_{x_0 \sim q(x_0)} \mathbb{E}_{q(x_{1:T}|x_0)}\left[-\log \frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}\right]$$

This objective can be optimized using stochastic gradient descent or other optimization techniques. The notation $\min_\theta$ denotes that we are minimizing the objective with respect to the parameters $\theta$ of the reverse process model.

The expectation $\mathbb{E}_{x_0 \sim q(x_0)}$ indicates that we are averaging over the clean samples $x_0$ drawn from the true data distribution $q(x_0)$. The inner expectation $\mathbb{E}_{q(x_{1:T}|x_0)}$ denotes that, for each clean sample $x_0$, we are averaging over the possible forward trajectories $x_{1:T}$ conditioned on $x_0$.

The term $-\log \frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}$ inside the expectation is the negative log-likelihood ratio between the reverse process probability $p_\theta(x_{0:T})$ and the forward process probability $q(x_{1:T}|x_0)$. Minimizing this term encourages the reverse process model to assign high probability to the clean samples and their corresponding forward trajectories.

By optimizing this variational lower bound, the model learns the parameters $\theta$ of the reverse process model $p_\theta(x_{t-1}|x_t)$ that best approximate the true reverse transition probabilities $q(x_{t-1}|x_t)$. This allows the model to generate clean samples by starting from random noise and iteratively applying the learned reverse transitions.

It's important to note that the variational lower bound is a tractable approximation to the true negative log-likelihood. It provides a way to optimize the reverse process model without the need to explicitly compute the intractable marginal likelihood $p_\theta(x_0)$.

In practice, the expectation over the forward trajectories $q(x_{1:T}|x_0)$ is estimated using Monte Carlo sampling. This means that, for each clean sample $x_0$, we generate random forward trajectories by applying the forward diffusion process and use these samples to estimate the expectation.

The optimization of the variational lower bound is typically done using stochastic gradient descent (SGD) or its variants. The gradients of the objective with respect to the parameters $\theta$ are computed using backpropagation through the reverse process model.

During training, the model learns to generate clean samples by iteratively denoising the random noise samples. At each step, the model takes a noisy sample $x_t$ and predicts the parameters of the Gaussian distribution $p_\theta(x_{t-1}|x_t)$ that approximate the true reverse transition probability. By sampling from this predicted distribution, the model generates a slightly denoised sample $x_{t-1}$. This process is repeated until the model generates a clean sample $x_0$.

Once the model is trained, it can be used to generate new samples by starting from random noise and applying the learned reverse process. The generated samples are expected to resemble the clean samples from the original data distribution.

In summary, the reverse process in diffusion models is learned by introducing a parameterized probability distribution $p_\theta(x_{t-1}|x_t)$ that approximates the true reverse transition probabilities. The training objective is formulated as a variational lower bound on the negative log-likelihood of the clean samples. By optimizing this objective using stochastic gradient descent and Monte Carlo sampling, the model learns to generate clean samples by iteratively denoising random noise. The learned reverse process model can then be used to generate new samples that resemble the original data distribution.
***
