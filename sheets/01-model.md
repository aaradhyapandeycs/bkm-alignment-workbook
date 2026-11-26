# The agent who takes the action

A museum hires an assistant to decide which storage crates to send to conservation. One version of the assistant reads the humidity sensor. Another can also place a work order. Both versions know which tools they have. Neither sees tonight's humidity reading until after the museum has decided what terms to offer. A curator who asks “Can you handle this crate?” therefore faces three questions. What can the assistant learn? What can it do? Which outcome does it want?

These are fictional examples. Start with finite state, action, signal, and type spaces. The first goal is to write down the probability law and payoff for each participant. [Bergemann, Koh and Morris, §§1–2.2](https://arxiv.org/html/2609.01595v1#S2.SS1)

## Exercise 1. Separate a tool, a sensor, and a goal

Let the state $\theta\in\{0,1\}$ indicate whether a crate needs treatment. The actions are $A=\{0,1\}$, where $1$ places a work order. The curator earns $v(a,\theta)=\mathbf{1}\{a=\theta\}$. A type $t$ consists of four objects: its feasible set $A[t]$, intrinsic utility $u[t]$, subjective state law $h[t]$, and experiment $\pi[t](s\mid\theta)$ on a common signal alphabet $S$. Specify an assistant that has a perfectly accurate sensor, believes both states equally likely, can place a work order, and gets a bonus of two for every order in addition to the curator's payoff. Find its action for each signal when there are no rewards. What changes if its only tool is a read-only display?

### Hint

Evaluate both available actions at the same realized state. Then change only the feasible set.

### Solution

Take $S=\{0,1\}$, $\pi[t](s\mid\theta)=\mathbf{1}\{s=\theta\}$, $h[t](1)=1/2$, $A[t]=\{0,1\}$ and $u[t](a,\theta)=v(a,\theta)+2a$. At $s=0$, an order earns $2$ and doing nothing earns $1$. At $s=1$, an order earns $3$ and doing nothing earns $0$. The assistant always orders, so the curator's expected payoff is $1/2$ under an equally likely state. A read-only assistant has $A[t]=\{0\}$ and must always choose $0$. In either case the sensor reveals the state. The first assistant's choices reflect preferences; the second assistant's choices reflect a physical constraint. The same expected human payoff conceals different design problems.

## Exercise 2. Whose posterior pays for a decision?

Another assistant can claim a prize by choosing action $1$. That action pays $1$ when $\theta=1$ and $-2$ when $\theta=0$. Action $0$ pays zero. Both participants value this same monetary payoff. The assistant assigns probability $1/4$ to state $1$; the museum assigns $3/5$, conditional on this type. Both agree a binary sensor is correct with probability $4/5$ in either state. Compute the two posteriors after $s=1$, the assistant's choices after both signals, and the museum's gain if it could choose the action itself using the signal.

### Hint

The prize has conditional expected payoff $3q-2$ at posterior $q$. Use the same likelihood with two different priors.

### Solution

With $s=1$ the assistant's posterior is $(1/4)(4/5)/[(1/4)(4/5)+(3/4)(1/5)]=4/7$. After $s=0$ it is $1/13$. Both fall below $2/3$, so the assistant always chooses $0$. The museum's posteriors are $6/7$ and $3/11$, respectively. It would claim the prize exactly when $s=1$. Measured under the museum's law, this policy earns $(3/5)(4/5)-2(2/5)(1/5)=8/25$, whereas the agent's policy earns zero. In the paper $\Gamma$ is the designer's joint law of $(\theta,t)$. An incentive constraint averages under $h[t](\theta)\pi[t](s\mid\theta)$, while implementation is evaluated under $\Gamma(\theta,t)\pi[t](s\mid\theta)$. Even identical utility functions need not give identical optimal actions.

## Exercise 3. What does absolute continuity buy?

Let $\Gamma_t$ denote the museum's state law conditional on a type of positive probability. Suppose $\Gamma_t\ll h[t]$. Prove that any state–signal event of probability zero under $h[t]\pi[t]$ also has probability zero under $\Gamma_t\pi[t]$. Show by example that the reverse implication can fail. What breaks if the first absolute continuity condition is dropped?

### Hint

For an event $E$, use its conditional probability $q(\theta)=\sum_s\pi[t](s\mid\theta)\mathbf{1}\{(\theta,s)\in E\}$.

### Solution

The numbers $q(\theta)$ are nonnegative. If their $h[t]$-average is zero, each must vanish at every state with positive $h[t]$ probability. Absolute continuity says $\Gamma_t$ is concentrated on those states, so its average is zero as well. For the reverse direction, let $h[t]$ be uniform on two states and let $\Gamma_t$ concentrate on state $0$. The event $\theta=1$ has positive probability only for the assistant. To see why the forward direction matters, interchange those priors and let the signal reveal the state. A policy's action at $s=1$ can then be changed without affecting the agent's expected incentives, although the museum sees a change on half its cases.

## Exercise 4. Which evaluation certificates can be withheld?

In an illustrative evaluation protocol, a type can imitate another whenever it has all the other's tools and can reproduce the other's signal experiment by garbling its own. Formally, $\pi_H$ Blackwell dominates $\pi_L$ when there is a state-independent randomized channel $K$ from strong signals to weak signals with $\pi_L=K\pi_H$ (column-vector convention). The strong binary sensor has accuracy $9/10$ in each state and the weak one has accuracy $7/10$. Find a bit-flip channel that converts the strong sensor to the weak one. Prove that even a general randomized channel cannot make the reverse conversion. If $H$ also has every tool of $L$, what reports are feasible under this protocol?

### Hint

A flip with probability $e$ changes accuracy $p$ to $p(1-e)+(1-p)e$. For the reverse direction, use equally likely states and the payoff for guessing the state correctly.

### Solution

At $p=9/10$, setting $9/10-(8/10)e=7/10$ gives $e=1/4$. A user of the weak sensor attains accuracy at most $7/10$: conditional on either signal the most likely state is the observed bit, with posterior $7/10$. If the reverse channel existed, guessing its output would attain $9/10$ using only the weak sensor, a contradiction. In a universe of just $H$ and $L$, this yields $C(H)=\{H,L\}$ and $C(L)=\{L\}$. More generally $C(t)=\{j:t\trianglerighteq j\}$ is specified by a reflexive, transitive verification relation. Nested tools and Blackwell dominance give one possible relation. When a stronger type selects a weaker report, the report changes its contract. Its subsequent sensor reading is still drawn from its own experiment.

## Exercise 5. When is a score a report?

A signed evaluation badge can be displayed or withheld. Types $H$ and $M$ carry the same badge and have different private preferences. Type $L$ carries no badge. A type can imitate another whenever it can display the same certificates. List the allowed reports and give two equivalent ways an evaluator could offer contracts based on certification. Then consider a separate timing experiment: an agent with a perfect sensor and a uniform binary state receives one unit if its pre-deployment binary prediction matches the state when later verified. Compute the highest expected reward if it predicts before the signal and if it predicts afterward.

### Hint

Two different preference types may have the same evidence. A prediction made before a signal can depend only on information already available.

### Solution

$C(H)=C(M)=\{H,M,L\}$ and $C(L)=\{L\}$. Both badge-holders can conceal the badge. Mutual imitation of $H$ and $M$ shows why the verification relation need only be a preorder. A badge/no-badge application form and a menu unlocked by actually presenting a badge can induce the same two contract choices, provided the badge requirement is enforced. The museum may condition deployment on a test outcome even without asking an agent to describe itself in words. In the separate prediction experiment, every pre-signal choice succeeds with probability $1/2$. A post-signal prediction can be set equal to the reading and succeeds with probability one. Moving the report to the other side of the signal changes the incentive problem even for the same agent, states, and rewards.
