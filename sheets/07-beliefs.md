# What can a private recommendation tell a team?

Two agents assign rooms for a conference. A coordinator privately tells each agent which room it may use. A sensor later tells each one whether its assigned equipment arrived. The coordinator can correlate the room assignments before either sensor fires. The agents can also disagree about whether the equipment will arrive. What would it take to replace the coordinator's whole protocol with a single round of type reports?

This sheet builds the multi-agent model and proves the two inclusions in Proposition 6. Throughout, $-i$ denotes everyone except $i$, and $\Delta(E)$ denotes probability laws on $E$. [Bergemann, Koh and Morris, Section 4](https://arxiv.org/html/2609.01595v1#S4)

## Exercise 1. Two people can agree about the equipment

Let the state be a bit $\theta$. Under one common prior it is fair, a second bit $Z$ is fair independently, and the second agent sees $(Z,W)$, where $W=\theta$ if $Z=1$ and $W=*$ otherwise. Agent 1 sees only $Z$. Both agents' payoffs and available actions are common knowledge and independent of $Z$.

Compute agent 1's probability of $\theta=1$ after each value of $Z$. If $\mu_2$ denotes agent 2's probability of $\theta=1$, calculate the conditional distribution of $\mu_2$ from agent 1's perspective. Suppose agent 1 receives a unit payoff if it correctly predicts whether agent 2 knows $\theta$. What information would be lost by replacing agent 1's type by its probability of $\theta=1$?

### Hint

First compute the posterior of the person who sees $W$. Then take its distribution given $Z$.

### Solution

In both cases agent 1 assigns probability $1/2$ to $\theta=1$. At $Z=0$, agent 2 also assigns $1/2$, so agent 1 assigns probability one to $\mu_2=1/2$. At $Z=1$, agent 2 observes the state, so agent 1 assigns probability $1/2$ each to $\mu_2=0$ and $\mu_2=1$. The event that agent 2 knows the state is precisely $Z=1$. The full type earns one by predicting $Z$. A decision using only agent 1's state probability has success probability $1/2$ under the common prior.

## Exercise 2. Build a belief hierarchy

Write $D_j=(A_j,u_j)$ for the pair made up of agent $j$'s available actions and its payoff function on joint actions and the state. Begin with a singleton $H_j^0$. Define what agent $i$ believes at orders one and two and write the recursion at a general order. Explain how to test a proposed second-order law for consistency with a specified first-order law. Describe the additional object obtained when this construction is carried through every order.

### Hint

The random object at order two includes each peer's first-order law. Projecting away a layer must recover the law already specified at the preceding order.

### Solution

Write $\mathcal D_j$ for the space of possible $D_j$. At order one the uncertainty concerns $(\theta,(D_j)_{j\ne i})$. At order two it also concerns each peer's first-order belief. In general,
$$
H_i^{k+1}=\Delta\!\left(\Theta\times
                  \prod_{j\ne i}(\mathcal D_j\times H_j^k)\right).
$$
Push a second-order law forward by forgetting the peers' beliefs. The result must equal $i$'s first-order law, including any correlations between the state and peer characteristics. At higher levels use the analogous truncations of peers' hierarchies. For example, a first-order state marginal of $1/2$ is inconsistent with a second-order law assigning total mass $3/4$ to $\theta=1$.

A type records $D_i$ and a coherent hierarchy. The universal-space construction used in the paper represents such beliefs by a law $\beta_i[t_i]$ of $(\theta,t_{-i})$. Its finite-order projections recover the beliefs just described. This representation theorem is an input from the theory of hierarchies. In a finite Bayesian model like Exercise 1, repeated conditioning and truncation already produce the example without constructing the entire universal space.

## Exercise 3. Whose probability enters the incentive constraint?

For a given type of agent 1, let the designer's conditional probability of $\theta=1$ be $1/4$ and the agent's subjective probability be $3/4$. Hold all other types fixed. Both agree on a private indicator $s$ with $\Pr(s=1\mid\theta=1)=4/5$ and $\Pr(s=1\mid\theta=0)=1/5$. Find their respective probabilities of $\theta=1$ given $s=1$. What does the model's condition $\Gamma(\cdot\mid t_i)\ll\beta_i[t_i]$ guarantee, and which of these posteriors determines a best response?

### Hint

A likelihood is common to both calculations. Each calculation uses its own prior odds.

### Solution

The likelihood ratio for $s=1$ is four. The designer's posterior odds are $4/3$ and its posterior is $4/7$. The agent's posterior odds are $12$ and its posterior is $12/13$. Both assign positive mass to both states. More generally, if an event in $(\theta,t_{-i})$ has subjective probability zero for an agent, it also has conditional probability zero for the designer, for almost every own type under the designer's law. Equality of probabilities would impose a stronger restriction. The agent's $12/13$ is the relevant posterior at this decision. The designer averages achieved outcomes using $\Gamma$ and the common signal kernel $\pi(ds\mid\theta,t)$, which may correlate the agents' signals.

## Exercise 4. A lottery over plans is a joint lottery

Each room agent will have a private bit $s_i$ and may choose private room label $0$, room label $1$, or the action “wait.” The coordinator draws $B$ uniformly in $\{0,1\}$. It gives agent 1 the plan “use room $B$ when your bit is one, otherwise wait” and gives agent 2 the same instruction with room $1-B$. Both agents can carry out all three actions. Assume the bits are independent of $B$ and that both bits being one has positive probability.

Conditional on both bits being one, compare the chance of a collision under this lottery with that under independent sampling from the two marginal plan lotteries. Specify the order of events in a direct mechanism.

### Hint

The two room labels have identical uniform marginals in both experiments.

### Solution

Under the shared draw the two active agents always get different rooms. Independent uniform draws collide with probability $1/2$. Marginalizing and then independently sampling the recommendations changes the designer's outcome even if both agents obey.

An agent first observes its own type $t_i$. The agents simultaneously make claims $h_i$ from their admissible sets $C_i(t_i)$. The mechanism privately sends each agent its component $p_i$ of a jointly drawn plan profile with law $\gamma(h)$. Then each agent receives its signal $s_i$ under the physical kernel for the true profile $t$, and finally the agents choose actions simultaneously. The recommendation is the function $p_i:S_i\to A$. Under obedience the actual action is $p_i(s_i)$. Feasibility requires plans assigned to reported type $h_i$ to take values in $A_i[h_i]$.

## Exercise 5. Write down one complete deviation

Fix $t_i$. Agent $i$ can send $h_i\in C_i(t_i)$, receive $p_i$, see $s_i$, and choose $d_i(p_i,s_i)\in A_i[t_i]$. Write its expected payoff $J_i(h_i,d_i\mid t_i)$ when all peers are truthful and obedient. State the full incentive inequality. Why can a false claim change both the peer actions and what the agent learns from its recommendation?

### Hint

Keep track of which arguments are true types in $\pi$ and which are reports in $\gamma$. Write $o_i(p_i,s_i)=p_i(s_i)$ for obedience.

### Solution

Draw $(\theta,t_{-i})$ under $\beta_i[t_i]$. Given these objects, draw $s$ under $\pi(\cdot\mid\theta,t)$ and draw $p$ independently under $\gamma(h_i,t_{-i})$. Set $a^d_i=d_i(p_i,s_i)$ and $a^d_j=p_j(s_j)$ for $j\ne i$. Then
$$
J_i(h_i,d_i\mid t_i)=
\mathbb E\!\left[
 u_i[t_i](a^d,\theta)+r_i((h_i,t_{-i}),a^d,\theta)
\right].
$$
For all such $h_i,d_i$, the requirement is $J_i(t_i,o_i\mid t_i)\ge J_i(h_i,d_i\mid t_i)$, together with feasibility of the recommendation rule. A claim can change the joint distribution of all plans. The realized private plan may itself reveal information about peer types through that distribution. Optimizing only over a fixed action chosen before the plan arrives can miss a profitable deviation.

## Exercise 6. Reconstruct the revelation principle

An indirect protocol has feasible input menus $X_i(t_i)$ and draws a private output vector $y$ from $\rho(\cdot\mid x)$ after inputs $x$. Its reward is $R_i(x,a,\theta)$. In a pure equilibrium, let $x_i(t_i)$ be the input and $\alpha_i(t_i,x_i,y_i,s_i)$ be the action. Assume $X_i(h_i)\subseteq X_i(t_i)$ whenever $h_i\in C_i(t_i)$. Construct a direct protocol that reproduces the equilibrium outcome. Prove it satisfies Exercise 5. Prove the reverse inclusion of outcome sets.

### Hint

Use the indirect protocol as a simulator. One sample of the entire output vector should supply all the plans. For the reverse direction use direct reports themselves as input symbols.

### Solution

At reported profile $h$ form $x(h)=(x_j(h_j))_j$ and draw one vector $y$ from the original output kernel at $x(h)$. Privately send each agent the function
$$
p_j^{h_j,y_j}(s_j)=\alpha_j(h_j,x_j(h_j),y_j,s_j).
$$
These functions have the required reported-type action ranges since the original strategies are feasible. Their joint law defines $\gamma(h)$. Pay $r_i(h,a,\theta)=R_i(x(h),a,\theta)$. At truthful reports, the action profile conditional on $(\theta,t)$ has exactly its original law: the same joint draw is used and the same signal kernel generates the private observations.

If agent $i$ could improve with $(h_i,d_i)$ in this direct protocol, it could send $x_i(h_i)$ in the indirect protocol. Menu inclusion makes that input available. From its private output $y_i$ it can compute $p_i^{h_i,y_i}$ and, on receiving its true signal, take $d_i(p_i^{h_i,y_i},s_i)$. With the other agents fixed at equilibrium this gives exactly the same subjective payoff as the direct deviation. Original optimality precludes the improvement.

Conversely take any direct incentive-compatible protocol. Give the indirect protocol input menus $C_i(t_i)$, output alphabets equal to the plan spaces, joint output kernel $\gamma$, and rewards $r_i$. Transitivity of the imitation relation gives menu inclusion. Honest inputs and obedient actions form an equilibrium by Exercise 5. Both directions concern outcome laws attainable in an equilibrium, allowing other equilibria in the same mechanism.
