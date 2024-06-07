# Basic Mathematical Typesetting

## Greek Letters

- $\alpha$ (alpha)
- $\beta$ (beta)
- $\gamma$ (gamma)
- $\delta$ (delta)
- $\epsilon$ (epsilon)
- $\zeta$ (zeta)
- $\eta$ (eta)
- $\theta$ (theta)
- $\lambda$ (lambda)
- $\mu$ (mu)
- $\pi$ (pi)
- $\rho$ (rho)
- $\sigma$ (sigma)
- $\tau$ (tau)
- $\phi$ (phi)
- $\chi$ (chi)
- $\psi$ (psi)
- $\omega$ (omega)

## Uppercase Greek Letters

- $\Gamma$ (Gamma)
- $\Delta$ (Delta)
- $\Theta$ (Theta)
- $\Lambda$ (Lambda)
- $\Xi$ (Xi)
- $\Pi$ (Pi)
- $\Sigma$ (Sigma)
- $\Upsilon$ (Upsilon)
- $\Phi$ (Phi)
- $\Psi$ (Psi)
- $\Omega$ (Omega)

## Subscripts and Superscripts

- $x_i$ (subscript)
- $x^2$ (superscript)
- $x_{ij}$ (nested subscript)
- $x^{2i}$ (nested superscript)

## Fractions and Radicals

- $\frac{1}{2}$ (fraction)
- $\frac{\pi}{2}$ (fraction with symbols)
- $\sqrt{2}$ (square root)
- $\sqrt[3]{8}$ (nth root)

## Summations and Integrals

- $\sum_{i=1}^{n} x_i$ (summation)
- $\int_{0}^{1} x\,dx$ (indefinite integral)
- $\iint_{D} f(x,y)\,dA$ (double integral)

## Vectors and Matrices

- $\vec{a}$ (vector)
- $\mathbf{A}$ (bold vector or matrix)
- $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ (matrix)

## Other Symbols

- $\infty$ (infinity)
- $\partial$ (partial derivative)
- $\nabla$ (nabla/del operator)
- $\equiv$ (identically equal to)
- $\approx$ (approximately equal to)
- $\therefore$ (therefore)
- $\because$ (because)
- $\pm$ (plus-minus)
- $\cdot$ (dot product)
- $\times$ (cross product)
- $\cup$ (union)
- $\cap$ (intersection)
- $\subseteq$ (subset or equal to)
- $\in$ (element of)
- $\notin$ (not an element of)
- $\exists$ (there exists)
- $\forall$ (for all)
- $\implies$ (implies)
- $\iff$ (if and only if)
- $\neg$ (negation)
- $\wedge$ (logical and)
- $\vee$ (logical or)
- $\mathbb{E}$
- $\mathcal{N}$
- $\sim$

This snippet covers the basic syntax for typesetting Greek letters (both lowercase and uppercase), subscripts and superscripts, fractions and radicals, summations and integrals, vectors and matrices, and various other mathematical symbols and operators commonly used in mathematical notation.

Note that these mathematical expressions are rendered using LaTeX syntax wrapped in dollar signs (`$`). For more advanced mathematical typesetting, you may need to refer to additional LaTeX documentation or resources.

# Tilde for Denoting Probability Distributions

## Examples

- $W_t \sim \mathcal{N}(0, \sigma^2 t)$ (Random variable $W_t$ follows a normal distribution with mean 0 and variance $\sigma^2 t$)
- $X \sim \text{Bernoulli}(p)$ (Random variable $X$ follows a Bernoulli distribution with parameter $p$)
- $Y \sim \text{Poisson}(\lambda)$ (Random variable $Y$ follows a Poisson distribution with rate parameter $\lambda$)
- $Z \sim \text{Exp}(\beta)$ (Random variable $Z$ follows an exponential distribution with rate parameter $\beta$)

## Explanation

In the context of probability and statistics, the tilde symbol (`~`) is used to denote that a random variable follows a particular probability distribution. The distribution is specified after the tilde symbol, along with any necessary parameters.

For example, in the expression `$W_t \sim \mathcal{N}(0, \sigma^2 t)$`, the random variable $W_t$ is said to follow a normal (Gaussian) distribution with a mean of 0 and a variance of $\sigma^2 t$.

Other common examples include:
- `$X \sim \text{Bernoulli}(p)$`: $X$ follows a Bernoulli distribution with parameter $p$
- `$Y \sim \text{Poisson}(\lambda)$`: $Y$ follows a Poisson distribution with rate parameter $\lambda$
- `$Z \sim \text{Exp}(\beta)$`: $Z$ follows an exponential distribution with rate parameter $\beta$

The tilde symbol (`~`) is a concise and widely accepted notation for specifying the probability distribution of a random variable in mathematical expressions and equations.

When encountered in this context, the tilde should be read as "is distributed as" or "follows the distribution of." For example, `$W_t \sim \mathcal{N}(0, \sigma^2 t)$` can be read as "W_t is distributed as a normal distribution with mean 0 and variance sigma-squared times t."
# Diffusion and Deep Learning

## Introduction

Diffusion models and deep learning have emerged as powerful tools in various domains, including computer vision, natural language processing, and generative modeling. This document explores the fundamental concepts and mathematical foundations underlying these techniques.

## Notation

Throughout this document, we will use the following notation:

- $\mathbf{x}$ represents an input vector or data sample
- $\mathbf{y}$ represents the corresponding target or output
- $\mathbf{W}$, $\mathbf{b}$ represent weight matrices and bias vectors, respectively
- $\sigma(\cdot)$ denotes the activation function (e.g., ReLU, sigmoid, tanh)
- $\odot$ represents element-wise multiplication (Hadamard product)
- $\otimes$ represents the convolution operation
- $\mathcal{N}(\mu, \Sigma)$ represents the multivariate normal distribution with mean $\mu$ and covariance $\Sigma$

## Deep Learning

Deep learning models, such as convolutional neural networks (CNNs) and recurrent neural networks (RNNs), are powerful function approximators capable of learning complex mappings from data. The fundamental building block of these models is the artificial neuron, which computes a weighted sum of inputs and applies a non-linear activation function:

$$
\mathbf{z} = \sigma(\mathbf{W}^T\mathbf{x} + \mathbf{b})
$$

These neurons are stacked and combined in various architectures to form deep neural networks, which can learn hierarchical representations of data.

## Diffusion Models

Diffusion models are a class of generative models that operate by gradually adding noise to data samples and then learning to reverse the diffusion process, effectively generating new samples from the learned data distribution.

The forward diffusion process is defined as:

$$
q(\mathbf{x}_t | \mathbf{x}_{t-1}) = \mathcal{N}(\mathbf{x}_t; \sqrt{1 - \beta_t}\mathbf{x}_{t-1}, \beta_t\mathbf{I})
$$

where $\beta_t$ is a noise schedule that controls the amount of noise added at each step.

The reverse process, known as the denoising diffusion process, is learned by a neural network $\epsilon_\theta(\mathbf{x}_t, t)$ that predicts the noise added at each step:

$$
\mathbf{x}_{t-1} = \frac{1}{\sqrt{1 - \beta_t}}(\mathbf{x}_t - \frac{\beta_t}{\sqrt{1 - \bar{\alpha}_t}}\epsilon_\theta(\mathbf{x}_t, t)) + \sigma_t\mathbf{z}
$$

Here, $\bar{\alpha}_t = \prod_{i=1}^t (1 - \beta_i)$, and $\sigma_t$ is a variance term.

## Conclusion

This document provided an overview of deep learning and diffusion models, introducing the key notation, concepts, and mathematical foundations. For more detailed information and practical applications, refer to the relevant literature and resources.

# Diffusion and Deep Learning

## Deep Learning Architectures

### Convolutional Neural Networks (CNNs)

CNNs are widely used in computer vision tasks and are particularly effective for processing grid-like data such as images. They employ convolutional layers that apply learnable filters to the input, capturing local patterns and spatial correlations.

$$
\mathbf{y} = \mathbf{W} \otimes \mathbf{x} + \mathbf{b}
$$

Here, $\mathbf{W}$ represents the convolutional kernel, $\otimes$ denotes the convolution operation, and $\mathbf{b}$ is the bias vector.

### Recurrent Neural Networks (RNNs)

RNNs are designed to process sequential data, such as text or time series. They maintain an internal state that captures information from previous inputs, allowing them to model dependencies in the data.

$$
\mathbf{h}_t = \phi(\mathbf{W}_h\mathbf{h}_{t-1} + \mathbf{W}_x\mathbf{x}_t + \mathbf{b}_h)
$$
$$
\mathbf{y}_t = \mathbf{W}_y\mathbf{h}_t + \mathbf{b}_y
$$

Here, $\mathbf{h}_t$ is the hidden state at time step $t$, $\phi$ is the activation function, and $\mathbf{W}_h$, $\mathbf{W}_x$, $\mathbf{W}_y$, $\mathbf{b}_h$, and $\mathbf{b}_y$ are learnable parameters.

## Diffusion Models

### Diffusion Probabilistic Models

Diffusion models are based on the principle of gradually adding noise to data samples and learning to reverse the diffusion process. This is accomplished by learning a sequence of conditional distributions:

$$
q(\mathbf{x}_{0:T}) = q(\mathbf{x}_0)\prod_{t=1}^T q(\mathbf{x}_t | \mathbf{x}_{t-1})
$$

where $\mathbf{x}_0$ represents the original data sample, and $\mathbf{x}_T$ is the final noisy sample.

### Denoising Diffusion Probabilistic Models (DDPMs)

DDPMs learn the reverse process by training a neural network $\epsilon_\theta(\mathbf{x}_t, t)$ to predict the noise added at each step:

$$
\mathbf{x}_{t-1} = \frac{1}{\sqrt{\alpha_t}}(\mathbf{x}_t - \frac{1 - \alpha_t}{\sqrt{1 - \bar{\alpha}_t}}\epsilon_\theta(\mathbf{x}_t, t)) + \sigma_t\mathbf{z}
$$

Here, $\alpha_t = 1 - \beta_t$, $\bar{\alpha}_t = \prod_{i=1}^t \alpha_i$, and $\sigma_t$ is a variance term.

### Score-Based Models

Score-based models learn the gradient of the data distribution $\nabla_\mathbf{x} \log p(\mathbf{x})$, which is known as the score function. This allows for efficient sampling and generation of new data samples.

$$
\mathbf{x}_{t-1} = \mathbf{x}_t + \frac{\beta_t}{2}\nabla_\mathbf{x} \log p(\mathbf{x}_t) + \sqrt{\beta_t}\mathbf{z}_t
$$

Here, $\mathbf{z}_t \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ is a Gaussian noise vector.

## Training and Optimization

### Loss Functions

Deep learning models are typically trained by minimizing a loss function that measures the discrepancy between the model's predictions and the ground truth. Common loss functions include:

- Mean Squared Error (MSE): $\mathcal{L}_{MSE} = \frac{1}{N}\sum_{i=1}^N (\mathbf{y}_i - \hat{\mathbf{y}}_i)^2$
- Cross-Entropy Loss: $\mathcal{L}_{CE} = -\frac{1}{N}\sum_{i=1}^N \sum_{j=1}^C y_{ij}\log(\hat{y}_{ij})$

### Optimization Algorithms

Gradient-based optimization algorithms are used to update the model parameters and minimize the loss function. Popular choices include:

- Stochastic Gradient Descent (SGD): $\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla_\mathbf{w} \mathcal{L}(\mathbf{w}_t)$
- Adam: $\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \frac{\hat{\mathbf{m}}_t}{\sqrt{\hat{\mathbf{v}}_t + \epsilon}}$

Here, $\eta$ is the learning rate, $\hat{\mathbf{m}}_t$ and $\hat{\mathbf{v}}_t$ are the bias-corrected first and second moment estimates, and $\epsilon$ is a small constant for numerical stability.

## Evaluation Metrics

Assessing the performance of deep learning and diffusion models often involves various evaluation metrics, such as:

- Accuracy, Precision, Recall, F1-Score (classification tasks)
- Mean Squared Error (MSE), Peak Signal-to-Noise Ratio (PSNR) (regression tasks)
- Fréchet Inception Distance (FID), Kernel Inception Distance (KID) (generative models)
- Perplexity, BLEU score (language models and machine translation)

This extended snippet covers additional concepts and mathematical notation related to deep learning architectures (CNNs and RNNs), diffusion probabilistic models, denoising diffusion probabilistic models, score-based models, loss functions, optimization algorithms, and evaluation metrics. It provides a more comprehensive overview of the key components and principles involved in diffusion and deep learning.