so now we understand 
$$dX_t = a(X_t, t)dt + \sigma(X_t, t)dW_t $$ and 
$$dW_t \approx W_{t+dt} - W_t \sim \mathcal{N}(0, dt)$$
the paper now looks as discretising  this to:

$$X_{t+dt} - X_t \approx a(X_t, t)dt + \sigma(X_t, t)U \text{ where } U \sim \mathcal{N}(0, dt)$$

$$X_{t+dt} \approx X_t + a(X_t, t)dt + U' \text{ where } U' \sim\mathcal{N}(0, \sigma^2(X_t, t)dt)$$

But what the fuck does this even mean and how is it done and what the actual fuck, mate. 

OK, so, the original is $$dX_t = a(X_t, t)dt + \sigma(X_t, t)dW_t $$ and then we want to disretise it, which means that we want to consider it not over continuous timestems of which dt is an infinitesimally small one, but rather over small, discrete ones. 

In order to do this we:
a) definte the discrete time steps. For the interval $[0, T]$ to be divided into N small, discrete steps of equal length $\Delta t$ then we just sat $\Delta t = \frac{T}{N}$

then timestep 3 (i.e $t_3$) = $3*\Delta t$ or
$$t_i = i \Delta t \text{for } i = 0,1,2,...N $$
and
$$t_{i+1} = t_i + \Delta t$$

b) discretize Wiener
$$dW_t \approx W_{t_{i+1}} - W_{t_i} \sim \mathcal{N}(0, \Delta t)$$

So $dW_t$ is normally distributed with mean of 0 and variance $\Delta t$

c) discrete SDE
we do this move which is where
$$dX_t = a(X_t, t)dt + \sigma(X_t, t)dW_t $$ becomes
$$X_{t+dt} - X_t \approx a(X_t, t)dt + \sigma(X_t, t)dW_t $$ and then 

$$X_{t+dt} \approx X_t + a(X_t, t)dt + \sigma(X_t, t)dW_t $$ and then 
$$X_{t+dt} \approx X_t + a(X_t, t)dt + \sigma(X_t, t)U \text{   where     } U \sim \mathcal{N}(0, dt)$$

Now, $\sigma(X_t, t)U$ where $U$ is a prob distribution is the same as a constant time a probability distribution as $\sigma(X_t, t)$ is just a constant.

The rule for this is as follows.

If $X \sim \mathcal{N}(2, 4)$ then X has mean of 2 and variance (sd^2) of 4.

if $c$ is some constant of value 10 and $Y$ is new distribution of the value $$Y= cX$$ then the rules are as follows:

**mean of 10X** 
$\mathbb{E}[Y]=\mathbb{E}[cX]$
 $\mathbb{E}[Y]= c*\mathbb{E}[X]$ 
 $\mathbb{E}[Y]= c*2$ 
 $\mathbb{E}[Y]= 20$ 
 
 **Var of 10X**
 $\text{Var}[Y]=\text{Var}[cX]$
 $\text{Var}[Y]= c^2 * \text{Var}[Y]$ 
 $\text{Var}[Y]= c^2 * 4$ 
 $\text{Var}[Y]= 100 * 4$
 $\text{Var}[Y]= 400$ 
  
 
Given these rules, in this case $$\sigma(X_t, t)U = cU$$
 And we know:  $$U \sim \mathcal{N}(0, dt)$$ and 
 
 so $$cU \sim \mathcal{N}(c*0,  c^2*dt)$$
give $c=\sigma(X_t, t)$ then we can say

$$\sigma(X_t, t)U \sim \mathcal{N}(\sigma(X_t, t)*0,  \sigma^2(X_t, t)*dt)$$ which multiplies out to:
$$\sigma(X_t, t)U \sim \mathcal{N}(0,  (\sigma(X_t, t))^2dt)$$
We can then call this $U'$ and rewwrite the initial equation as 

$$X_{t+dt} \approx X_t + a(X_t, t)dt + U' \text{   where     } U' \sim \mathcal(0,  (\sigma(X_t, t))^2dt)$$


