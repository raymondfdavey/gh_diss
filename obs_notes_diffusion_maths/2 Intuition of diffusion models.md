diffusion process: $$dX_t = a(X_t, t)dt + \sigma(X_t, t)dW_t $$

Which can end up being such that 
$$X_{t+1} = aX_t + b*\mathcal{N}(0, 1)$$

but then we often see in the literature:

$$X_t = √(1 - β_t) X_{t-1} + √β_t * ε_t$$

Where $\epsilon_t \sim \mathcal{N}(0, 1)$ is a standard normal random variable. 

So wtf is all this?

Well it is basically a way of paramaterising the diffusion process such that the process will progressively destroy any relevant information. Indeed, any diffusion with a "shrinking" drift coefficient (|a|<1) and a non-null diffusion coefficient will progressively turn data from any complex distribution into data from a simple isotropic gaussian noise (gaussian whose covariance matrix is diagonal, meaning that all dimensions are independent gaussians)."

What this means is that if we set up the drift coefficient $a(X_t, t)$ to be less than 1 in absolute value, and the diffusion coefficient $σ(X_t, t$) to be non-zero, the diffusion process defined by $dX_t = a(X_t, t)dt + σ(X_t, t)dW_t$ will have the effect of gradually destroying the initial distribution of $X_0$ and converging towards a simple isotropic Gaussian distribution over time.

When we see the example
$$X_t = √(1 - β_t) X_{t-1} + √β_t ε_t$$

where $ε_t$ is a standard Gaussian random variable. Then regardless of the initial value $X_0$, this process will converge to a Gaussian distribution as $t$ increases.

In this common form (especially in diffusion for deep learning)
- $β_t$ controls the trade-off between keeping information from the previous step ($√(1 - β_t) X_{t-1}$) and adding new Gaussian noise ($√β_t ε_t$)
- $ε_t$ is a Gaussian random variable
- So basically the $\sqrt{1-\beta_t}X_{t-1}$ term and $\sqrt{\beta_t} \epsilon_t$ terms mean that the value of $\beta_t$ determines the extent of $X_t$ and $\epsilon_t$ that are passed onto the next t

This discretized equation approximates the continuous SDE $$dX_t = a(X_t, t)dt + σ(X_t, t)dW_t$$ over small time intervals $dt$, with the drift $a(X_t, t)$ approximated by $√(1 - β_t)$ and the diffusion $σ(X_t, t)$ approximated by $√β_t.$

In doing this they have parametrized the drift and diffusion coefficients as:

$$a(X_t, t) = \sqrt{1 - \beta_t}X_t$$
$$\sigma(X_t, t)dW_t = \sqrt{\beta_t}\epsilon_t$$

Where $\epsilon_t \sim \mathcal{N}(0, 1)$ is a standard normal random variable, and $dW_t$ represents the increment of the Wiener process.

in this case $\beta_t \in (0, 1)$ controls the trade-off between preserving the previous value ($\sqrt{1 - \beta_t}X_t$) and adding Gaussian noise ($\sqrt{\beta_t}Z_t$).

WHY THOUGH?

***
The paper does not provide a detailed explanation for why they choose to parametrize the drift and diffusion coefficients as $a(X_t, t) = \sqrt{1 - \beta_t}X_t$ and $\sigma(X_t, t) = \sqrt{\beta_t}$, where $\beta_t \in (0, 1)$. Let me try to give a more thorough explanation for this parametrization:

The key idea is that they want the discretized diffusion process to gradually destroy the relevant information in the data $X_t$ and converge to a simple isotropic Gaussian distribution as $t \rightarrow \infty$. To achieve this, they need the drift coefficient $a(X_t, t)$ to be "shrinking" (i.e., $|a(X_t, t)| < 1$) and the diffusion coefficient $\sigma(X_t, t)$ to be non-zero.

1. The drift coefficient $a(X_t, t) = \sqrt{1 - \beta_t}$:
    - Since $\beta_t \in (0, 1)$, we have $0 < \sqrt{1 - \beta_t} < 1$, satisfying the shrinking drift condition.
    - This shrinking drift ensures that the process gradually forgets its initial value $X_0$ over time.
2. The diffusion coefficient $\sigma(X_t, t) = \sqrt{\beta_t}$:
    - Since $\beta_t \in (0, 1)$, we have $\sqrt{\beta_t} > 0$, satisfying the non-zero diffusion condition.
    - This non-zero diffusion ensures that Gaussian noise is added at each step, gradually making the process converge to a Gaussian distribution.

The [[specific choice of using square roots]] $\sqrt{1 - \beta_t}$ and $\sqrt{\beta_t}$ is likely due to mathematical convenience shown in the linked doc.

But ultimately, what this setup does is ensure that the diffusion process set up like this regardless of the $\beta$ vaue will go towards a $\mathcal{N}(0, 1)$ with mean of 0 and variance of 1

***
The key points are:
1) Setting $|a| = \sqrt{1 - \beta_t} < 1$ makes the drift "shrinking", driving $X_t$ towards 0.
2) Setting $\sigma = \sqrt{\beta_t} \neq 0$ introduces Gaussian noise at each step.

This combination of shrinking drift and non-zero diffusion causes the process to gradually forget its initial value $X_0$ and converge to an isotropic Gaussian distribution as $t \rightarrow \infty$.
***
The specific discretized form used in diffusion models simplifies to:
$$
X_{t+1} = \sqrt{1 - \beta_t} X_t + \sqrt{\beta_t} \epsilon_t
$$
where $\epsilon_t \sim \mathcal{N}(0, I)$.

This equation implies that at each step, the process retains a fraction of the previous state $\sqrt{1 - \beta_t} X_t$ while adding some Gaussian noise $\sqrt{\beta_t} \epsilon_t$.

### Key Points

- **Progressive Destruction of Information**: Over many steps, the process 
$$
X_{t+1} = \sqrt{1 - \beta_t} X_t + \sqrt{\beta_t} \epsilon_t
$$
gradually transforms data $X_t$ into Gaussian noise.

- **Reversibility**: The aim is to learn the reverse of this process, starting from Gaussian noise and reconstructing the original data by progressively reducing the noise.
***

"So far, we know that we can use a diffusion to go from a complex distribution to a simple isotropic gaussian noise. From what we discussed at the beginning of this article, one could outline that we are much more interested in the reverse process: going from the simple distribution to the complex one."

The authors have established that a forward diffusion process can transform data from a complex distribution into a simple isotropic Gaussian distribution. However, for generative modeling, we are more interested in the reverse process, which starts from the simple Gaussian distribution and gradually generates samples from the complex target distribution.

"On top of that, going from complex to simple distribution is not that hard as we could simply randomly project any point of the complex distribution into the simple distribution as we know how to sample from this last one."

The authors note that transforming data from a complex distribution to a simple one is relatively easy. We could simply sample random points from the simple distribution and assign them to the points in the complex distribution. This is because we know how to sample from the simple distribution (e.g., a Gaussian).

"So what is really the point of using a diffusion here? The simple answer is that it gives us a progressive and structured way to go from our complex distribution to an isotropic gaussian noise that will ease the learning of the reverse process."

The key idea is that using a diffusion process provides a gradual and structured way to transform the complex distribution into a simple one. This structured approach makes it easier to learn the reverse process, which generates samples from the simple distribution back to the complex one. The intermediate steps of the diffusion process provide a guide for the reverse process.

"And this the important point here: intermediate steps are the strength diffusion model rely on."

The authors emphasize that the intermediate steps of the diffusion process are crucial for the success of diffusion models. These steps provide a gradual transition from the complex distribution to the simple one, which can be leveraged during the learning of the reverse process.

"At this point one could have indeed observed that despite the fact it is done progressively, diffusion process ultimately take any data point from the initial complex distribution and turns it into a random point from the simple distribution. So, in the end, as we can go from complex to simple distribution in one shot, why bothering with intermediate steps? Instead of learning a multistep reverse process, why not learning a single big reverse process that would be the unrolled version of the multistep process? Can't we even consider that it would be exactly the same?"

The authors raise a potential question: since the diffusion process ultimately transforms any point from the complex distribution into a random point in the simple distribution, why not learn a single-step reverse process instead of a multi-step one? They consider whether learning a single "unrolled" reverse process would be equivalent to learning the multi-step reverse process.

"If one could be tempted to hold this reasoning, truth is that breaking down the process into intermediate steps brings two things. First, all the reverse steps are not completely different from each others, meaning that in practice we don't have to learn a fully different model for each reverse step but instead a common model that simply takes the step as a parameter to adjust its behaviour. It drastically reduces the size of the model to be learned. Second, on top of having much more parameters to be learned, a one shot unrolled version is much harder to train as it needs to go from pure noise to final high quality data, making the task and gradient descent learning much more complicated. At the opposite, a progressive model do not need to handle the whole complexity at once and can first introduce coarse information at the early stages before adding progressively finer and finer information. Intermediate steps can in some sense also be seen as a way to guide the training process to make it easier."

The authors counter the idea of learning a single-step reverse process by highlighting two advantages of using intermediate steps:

1. The reverse steps are not entirely different from each other, which means that a single model can be learned for all reverse steps, with the step number as a parameter to adjust its behavior. This significantly reduces the size of the model compared to learning separate models for each step.

2. Learning a single-step "unrolled" reverse process is much harder because it needs to go from pure noise to high-quality data in one shot. This makes the training process and gradient descent optimization more challenging. In contrast, a progressive multi-step model can introduce coarse information in the early stages and gradually add finer details, making the learning process more manageable. The intermediate steps guide the training process and make it easier.

"The obvious downside of DPMs is that sampling requires multiple steps, meaning that the generative process will be longer than it is for GANs or VAEs, as these kind of models require a single pass. This fundamental difference raises many questions. Assuming an equivalent number of parameters, is it completely fair to compare DPMs outputs with GANs and VAEs outputs when the first one make several passes (and, so, takes more time) ? How much sense does it make to try to distillate DMPs if their strength come from the progressive nature of their generative process? We won't answer these questions here, but they are, for sure, interesting ones to think about."

The authors acknowledge that a drawback of diffusion models is that the sampling process requires multiple steps, making it slower compared to generative models like GANs or VAEs, which generate samples in a single pass. They raise questions about the fairness of comparing the outputs of diffusion models with those of GANs and VAEs, given the difference in the number of steps and computation time. They also question whether it makes sense to distill diffusion models into single-step models, as the progressive nature of the generative process is a key strength of diffusion models. While they don't provide definitive answers to these questions, they highlight them as interesting points for consideration.
***
timestep as paramater:
Certainly! Let's dive deeper into this concept of using a common model for all reverse steps and passing the timestep as a parameter.

In the context of diffusion models, the reverse process involves multiple steps that gradually transform the noisy data back into the original data distribution. Each step in this process can be seen as a denoising operation, where the model takes the noisy data at step t and attempts to remove some of the noise to produce a slightly cleaner version of the data.

Now, instead of learning separate models for each reverse step, the authors suggest using a single model that is shared across all steps. This common model takes two inputs: the noisy data at the current step and the timestep itself. By conditioning the model on the timestep, it can learn to behave differently depending on the stage of the reverse process.

Here's how it works:

1. The model architecture remains the same for all reverse steps. This means that the same set of weights and biases are used throughout the reverse process.

2. The timestep is passed as an additional input to the model. This can be done by encoding the timestep as a vector representation and concatenating it with the noisy data input. Alternatively, the timestep can be used to modulate the activations or normalization parameters of the model.

3. During training, the model learns to interpret the timestep input and adapt its behavior accordingly. For example, at earlier timesteps (closer to the random noise), the model may learn to make coarser adjustments to the noisy data, while at later timesteps (closer to the original data), it may learn to make finer, more subtle refinements.

4. At inference time, the same model is used iteratively for each reverse step. The noisy data and the corresponding timestep are passed as inputs, and the model outputs the denoised data for that step. This process is repeated until the desired number of reverse steps is reached.

By using a common model with the timestep as a parameter, the diffusion model can efficiently learn the reverse process without requiring separate models for each step. The model learns to adapt its behavior based on the timestep, allowing it to perform different levels of denoising at different stages of the reverse process.

This approach has several advantages:

1. Parameter efficiency: Using a single model for all reverse steps significantly reduces the number of parameters compared to learning separate models for each step. This makes the model more memory-efficient and faster to train.

2. Shared knowledge: By sharing the same model across all steps, the knowledge learned at one step can be effectively transferred to other steps. This allows the model to learn more robust and coherent denoising strategies.

3. Flexibility: The model can learn to adapt its behavior based on the timestep input, allowing it to handle different levels of noise and make appropriate adjustments at each step.

4. Scalability: The approach of using a common model with the timestep as a parameter can be easily scaled to a larger number of reverse steps without significantly increasing the model complexity.

It's worth noting that the specific way in which the timestep is incorporated into the model can vary depending on the implementation. Some common approaches include concatenation with the input data, modulation of activations or normalization parameters, or using the timestep to control the scale and shift of the model's outputs.

Overall, the idea of using a common model with the timestep as a parameter is a key concept in diffusion models that enables efficient and effective learning of the reverse process.
