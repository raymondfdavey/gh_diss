$$dX_t = a(X_t, t)dt + \sigma(X_t, t)dW_t $$

Ok so this is a special type of differential equation as STOCASTIC differential equation (SDE) where with $dX_t$ we are actually specifying the infintesimal change in $X_t$ over time.

Where before we might write $y = f(x)$ and then $\frac{dy}{dx} = f'(x)$ we can also write it $dy = f'(x)dx$ which is saying for an infintesimal change in dx, what is the change in y?

For a stochastic process, unlike deterministic functions, we musy include random fluctuations in the change to $X_t$ and so we get 

$$dX_t = a(X_t, t)dt + \sigma(X_t, t)dW_t $$

where the $a$ term is the deterministic bit (that is multiplied only by the change in time $dt$ and so is affected only by $t$ and $X_t$ (and the drift function)). But the $\sigma$ term is the random bit.  

$a(Xt, t)dt$ is the drift term and represents the determininstic part of the process where $a(X_t, t)$ considers the current state, the timestep we are on, all scaled by the size of the time step $dt$
eg  $a(X_t, t) = \alpha X_t + \beta t$
The diffusion term $\sigma(X_t, t)dW_t$ is actually a bit more complex because $dW_t$ is it's own crazy thing...

$\sigma(X_t, t)$ is also deterministic in that is procvides a specific value for each X_t and t. It scales the magnitude of the component dWt - it defines, deterministically, the extent of the randomness. 

eg  $\sigma(X_t, t) = \alpha X_t + \beta t$

$dW_t$ has a 2 things going on $W_t$ which is the 'wiener process' and $dW_t$ which is the incrementing of the weiner process. $dW_t$ specifically denotes the random increment in the Weiner process and is not a product of dt and Wt. 

so, $W_t$ is the weinder process and is a 'continuous time stochastic process' that models random motion and was inspired by and often explained with refrence to particles suspended in fluid. 

It has the following properties: 

1. $W_0$ = 0
This means that at t=0 the displacement is 0. In the particle instance the particle start from an initial position, say the origin.

2. The incriments $W_{t+s} - W_t$ are NORMALLY DISTRIBUTED with mean 0 and variance $s$ where s is the size (length) of the time interval. That is if the interval is longer, the displacement can be larger. 

3. **Independent Increments**: For any $0 ≤ t_1 < t_2 < . . . <t_n​$, the increments $W_{t_2}−W_{t_1}, W_{t_3} - W_{t_2}​​, ..., W_{t_n} - W_{t_{n-1}}​​$ are independent
This means that if we were to observe the particle as fifferent times t 1, t2 etx, then the increment W_t2= Wt_1 is independent of any other intervals. Meaning knowing about how the particle moved in the first interval woudnt tell us how it moved in another (for the weiner process part. )
This insudres that each segment of the particles trajectory is influences bu new independent random forces, reflecting the erratic and unpredicatable nature of brownian motion

4.  The paths of $W_t$ are almost surely continuous

For the increment $dW_t$ then, $dW_t represents the small displacement of the particle over an infitensimal time interval dT
$dW_t$ is Normally distributed with a mean of 0, and a variability of dt - the size of the time interval.
This is scaled by $\sigma$ which scales the intensity of these random kicks. 

In the paper $dW_t \approx W_{t+dt} - W_t \sim \mathcal{N}(0, dt)$ is saying that the $dW_t$ value in $$dX_t = a(X_t, t)dt + \sigma(X_t, t)dW_t $$ which is an infintesimal incriment of the Winer process over dt can be approximated by the finite difference $W_{t+dt} - W_t$.
This means that $dW_t$ is approximately the change in teh weiner process from time t to t+dt

 $\sim \mathcal{N}(0, dt)$ means that  $\sim \mathcal{N}(0, dt)$ and hence $dW_t$ follows a normal distrinbution with a mean of ) and variance dt

Intuition Using the Particle Example:
- **Random Motion**: Imagine a particle undergoing Brownian motion. Over a very small time interval dtdtdt, the particle's position changes randomly.
- **Normal Distribution**: The change in the particle's position (modeled by the Wiener process) over this interval is normally distributed with a mean of 0 (no bias in any direction) and a variance proportional to the length of the interval dtdtdt.
- **Approximation**: For practical purposes, especially in numerical simulations, we approximate the infinitesimal change dWtdW_tdWt​ by the finite difference Wt+dt−WtW_{t+dt} - W_tWt+dt​−Wt​.

[[weinder process summary]]

so now we understand 
$$dX_t = a(X_t, t)dt + \sigma(X_t, t)dW_t $$ and 
$$dW_t \approx W_{t+dt} - W_t \sim \mathcal{N}(0, dt)$$
the paper now looks as discretising  this to:

$$X_{t+dt} - X_t \approx a(X_t, t)dt + \sigma(X_t, t)U \text{ where } U \sim \mathcal{N}(0, dt)$$

$$X_{t+dt} \approx X_t + a(X_t, t)dt + U' \text{ where } U' \sim\mathcal{N}(0, \sigma^2(X_t, t)dt$$

explain in [[discretising]]


