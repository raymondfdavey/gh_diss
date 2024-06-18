[[md notes]]
Looking at [[DPMs_medium.pdf]], trying to understand the bones of diffusion. 

#### 1. What is a diffusion process 

**MARKOV**
So when the markov prcoess is written $P(X_{t_n} | X_{t_{n-1}})$ this is actually the same as $P(X_{t_{n+1}} | X_{t_n})$

And in terms of it being a random variable, we can think of $X_t$ as representing the position of a particle at time $t$, whose value is uncertain because of random influences, and so it is best represented by a pronability distribution. 

It being markov just means it has no memory - it depends only on the immediately preceeding step. 

**DIFFERENTIAL EQUATIONS**

OK so in the first section, the fist bit I am stuck on are the [[diffusion differential equations]] relating to the general case diffusion process:

$$dX_t = a(X_t, t)dt + \sigma(X_t, t)dW_t $$

So, i need to understand what $dX_t$ actually is as well as $dW_t$ see [[diffusion differential equations]] 

Like, what do these mean? change in X between timesteps? 
And what is the $dt$ after $a(X_t, t)dt$?

I am thinking we are describing how $X_t$ changes over time which is a function of $X_t$, $t$, $dW_t$ and the drift and diffusion functions. 

But then I also don't understand 
$$ dW_t \approx W_{t+dt} - W_t \sim \mathcal{N}(0, dt) $$

like the change in Wt is the previous W_t - some random noise with mean of 0 and variance of dt? what is dt?

And why call a and $\sigma$ coefficients when in fact they are functions??

This seems to be very important as it underlys the transformation of the information into noise (and the process also allows for the reverse)

SO, the first bit is explained in [[diffusion differential equations]] and [[discretising]] to get from 
$$dX_t = a(X_t, t)dt + \sigma(X_t, t)dW_t $$ 
to
$$X_{t+dt} \approx X_t + a(X_t, t)dt + U'$$

where $U' \sim \mathcal(0,\sigma^2(X_t, t) * dt)$

at this point i can quote the paper when I say:

"We can then see that the value of $X_{t+dt}$ is the value of $X_t$ to which we add a **deterministic drift term** and a **stochastic diffusion term** defined by a normal random variable with variance **proportional to the diffusion coefficient squared**. 

So, the diffusion coefficient indicates the strength of the randomness to be applied."

And remember, the diffusion cooeficient is the function $\sigma(X_t, t)$ which scales the intensity of the random part, and the drift term is the deterministic part $a(X_t, t)$ which describes the expected of average rate of change of direction the process tends to take.

if we think of the drif and diffusion coefficients as constants a and b then the graph below shows the impact of them taking on different values over time:

![[drfty.png]]

### Interpretation in the Graph

- **Top three paths**:
    
    - Since the drift terms do not depend on xxx, the paths either follow a pure Brownian motion (dWtdW_tdWt​), a constant drift (2⋅dt2 \cdot dt2⋅dt), or a trivial constant process.
    - These processes do not pull the trajectory back towards a mean value, resulting in the typical diffusive behavior of Brownian motion or linear drift.
- **Bottom three paths**:
    
    - The inclusion of −x-x−x in the drift term causes the process to exhibit mean-reverting behavior.
    - These processes tend to drift back towards the origin due to the −x⋅dt-x \cdot dt−x⋅dt term.
    - The variance and spread of these paths can be influenced by the diffusion coefficient (e.g., dWtdW_tdWt​ vs. 4⋅dWt4 \cdot dW_t4⋅dWt​).

### Summary

The key in the graph distinguishes between processes with:

- **No dependence on xxx** in the drift term (top three equations).
- **Dependence on xxx** in the drift term (bottom three equations).

This difference is crucial for understanding the behavior of the stochastic processes, particularly how they evolve over time and whether they exhibit mean-reverting properties or not.

And finally the define the [[REVERSED-TIME DIFFUSION PROCESS]]
