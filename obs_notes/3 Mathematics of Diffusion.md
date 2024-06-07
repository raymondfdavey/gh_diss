It is more accurate when describing the discrete diffusion process as a 'Markov chain wityh guassian transition probability kernel'

Sure, let's start with the first few equations in the "Mathematics of diffusion models" section.

"Let's denote $x_0$ a data from a distribution we want to sample from and $q(x_0)$ the distribution itself."

- $x_0$ represents a single data point sampled from the original data distribution that we aim to model.
- $q(x_0)$ denotes the true data distribution itself, from which $x_0$ is sampled.

"We define the forward process with gaussian transition probability (the diffusion kernel) as follows:
$q(x_t|x_{t-1}) = \mathcal{N}(x_t; \sqrt{1 - \beta_t} x_{t-1}, \beta_t \mathbf{I})$"

- This equation defines the forward diffusion process, which is a Markov chain with [[Gaussian transition probabilities]].
- $q(x_t|x_{t-1})$ represents the conditional probability distribution of $x_t$ given $x_{t-1}$, where $t$ is the timestep index.
- The forward process gradually adds Gaussian noise to the data at each step, transforming it from the original distribution $q(x_0)$ to a simple isotropic Gaussian distribution.
- The transition probability is modeled as a Gaussian distribution $\mathcal{N}(x_t; \sqrt{1 - \beta_t} x_{t-1}, \beta_t \mathbf{I})$, where:
  - The mean is given by $\sqrt{1 - \beta_t} x_{t-1}$, which is a scaled version of the previous timestep's data $x_{t-1}$. The scaling factor $\sqrt{1 - \beta_t}$ controls the amount of noise added at each step.
  - The covariance matrix is a diagonal matrix with $\beta_t$ on the diagonal, denoted as $\beta_t \mathbf{I}$. This means that the noise added at each step is isotropic (i.e., independent and identically distributed along each dimension).

"We can also write: $x_t = \sqrt{1-\beta_t} x_{t-1} + \sqrt{\beta_t}\epsilon_t \text{ with } \epsilon_t \sim \mathcal{N}(0, \mathbf{I})$"

- This equation provides an alternative way to express the forward diffusion process.
- Instead of directly specifying the transition probability distribution, it describes how to generate $x_t$ from $x_{t-1}$ using a deterministic scaling term $\sqrt{1-\beta_t} x_{t-1}$ and a stochastic Gaussian noise term $\sqrt{\beta_t}\epsilon_t$.
- $\epsilon_t$ is a standard Gaussian noise vector sampled from $\mathcal{N}(0, \mathbf{I})$, where $\mathbf{I}$ is the identity matrix.
- The scaling factor $\sqrt{1-\beta_t}$ controls the amount of the previous timestep's data $x_{t-1}$ that is preserved, while $\sqrt{\beta_t}$ controls the magnitude of the Gaussian noise added.

These equations lay the foundation for the forward diffusion process, which gradually corrupts the data by adding Gaussian noise at each step. The amount of noise added is controlled by the parameter $\beta_t$, which can be chosen to ensure a smooth transition from the original data distribution to a simple isotropic Gaussian distribution over the course of the diffusion process.

In the subsequent equations, the authors will build upon this forward process to define the reverse process and the training objective for the diffusion model. We'll go through those equations step by step as well to ensure a clear understanding.
