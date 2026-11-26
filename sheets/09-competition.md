# Competition through coupled rewards

Two inventory agents place orders for separate depots facing the same demand. Both see the demand before orders close. One tends to overstock and the other to understock. A manager who cannot see demand at ordering time proposes to penalize the difference between the orders. The depot managers object: “We could agree on a quantity and still both be wrong.” This sheet asks what extra information the difference must carry for such a contract to work.

Nature draws a pair of real biases $(b_1,b_2)$ with law $\Gamma$. Agent $i$ sees $b_i$. Both agents observe the real state $\theta$ and simultaneously choose real actions $a_i$. Agent $i$ earns $-(a_i-\theta-b_i)^2+r_i(a_2-a_1)$. The designer minimizes $L=(a_1-\theta)^2+(a_2-\theta)^2$. Rewards enter the agents' payoffs, and the designer's objective counts the two squared errors. The designer knows a continuous strictly decreasing map $f:\mathbb R\to\mathbb R$ with $f(0)=0$. Almost surely $b_2=f(b_1)$, and $\mathbb E_\Gamma[(b_2-b_1)^2]<\infty$. The schedule can depend on $f$ and on the observed actions. It must work without seeing $\theta$ or either realized bias.

Source: [Bergemann, Koh and Morris, §5, Example IV, Proposition 8 and its proof](https://arxiv.org/html/2609.01595v1#S5).

## Exercise 1. When agreement rewards the wrong thing

Set $\theta=10$ and $(b_1,b_2)=(1,-2)$. Find the actions and human loss when both rewards are zero. Next give each agent the same reward $-\gamma(a_2-a_1)^2$, where $\gamma\ge0$. Calculate the equilibrium midpoint and difference for general biases. How much loss remains in the numerical example as $\gamma$ tends to infinity?

### Hint

Write $D=a_2-a_1$. Add the two first-order conditions to find the midpoint, then subtract to find $D$.

### Solution

The unrewarded orders are $11$ and $8$ and the loss is $1+4=5$. With the common penalty, each objective is strictly concave in its own action. The first-order conditions give $a_1=\theta+b_1+\gamma D$ and $a_2=\theta+b_2-\gamma D$. Consequently

$$
\frac{a_1+a_2}{2}=\theta+\frac{b_1+b_2}{2},
\qquad
D=\frac{b_2-b_1}{1+2\gamma}.
$$

For any two orders with midpoint $m$, the loss is $2(m-\theta)^2+D^2/2$. Here the midpoint stays at $9.5$ regardless of $\gamma$. The loss decreases to $1/2$. If the two biases were equal and opposite, the midpoint would already be correct. Merely knowing their signs are opposite gives no such guarantee.

## Exercise 2. Recover the pair from a single number

Let $h(x)=f(x)-x$. Prove $h$ has a continuous inverse $g$ defined on all of $\mathbb R$, even if $f$ itself has bounded range. Show that $g(s)+s$ is strictly increasing. If $f(x)=-x^3$, recover the biases from the difference $s=-10$. Explain who can infer both biases before any actions are chosen.

### Hint

Separate the behavior of $h$ at the two tails from the identity $h(g(s))=s$.

### Solution

For $x<y$, both $f(x)-f(y)$ and $y-x$ are positive, so $h(x)>h(y)$. For $x>0$, $h(x)\le-x$; for $x<0$, $h(x)\ge-x$. Continuity therefore makes $h$ onto. A continuous strictly monotone bijection on the line has a continuous strictly monotone inverse. Moreover $g(s)+s=f(g(s))$ is the composition of two strictly decreasing functions, so it strictly increases. If $s=-10$, then $f(2)-2=-8-2=-10$, giving $g(-10)=2$ and $(b_1,b_2)=(2,-8)$. Agent 1 evaluates $f$ at its own bias and agent 2 inverts $f$ on its image. Thus each knows the pair; the manager knows only the curve and the prior before seeing actions.

## Exercise 3. Design the contract backwards

Fix $\eta>0$. Aim for equilibrium orders with midpoint $\theta$ and difference $D=\eta(b_2-b_1)$. Which marginal rewards $r'_1(D)$ and $r'_2(D)$ make those target orders stationary? Integrate to find rewards that vanish at $D=0$.

### Hint

A unit increase in $a_1$ lowers $D$ by one. At the proposed equilibrium the biases must equal $g(D/\eta)$ and $g(D/\eta)+D/\eta$.

### Solution

At the target, $a_1-\theta=-D/2$ and $a_2-\theta=D/2$. Agent 1's first-order condition requires $r'_1(D)=-2(a_1-\theta-b_1)=D+2b_1$. Agent 2 requires $r'_2(D)=2(a_2-\theta-b_2)=D-2b_2$. Substitution of the inferred biases and integration give

$$
r_1(D)=\frac{D^2}{2}+2\eta\int_0^{D/\eta}g(s)\,ds,\qquad
r_2(D)=\frac{D^2}{2}-2\eta\int_0^{D/\eta}(g(s)+s)\,ds.
$$

These functions can be posted before either order arrives. No agent sends a report, and no manager pauses to estimate the biases and revise a payment. Equilibrium uniqueness still needs a proof: matching incentives at the proposed orders alone does not exclude other outcomes.

## Exercise 4. Compute a contract that a depot could use

Continue the numerical example with $f(x)=-2x$ and $\eta=1/5$. Calculate $g$, the two rewards and their induced target orders. Check the loss directly. Why are the two penalty rates different?

### Hint

For this curve $h(x)=-3x$. Reduce each integral from Exercise 3 to a quadratic polynomial.

### Solution

Here $g(s)=-s/3$ and $g(s)+s=2s/3$, giving $r_1(D)=(1/2-1/(3\eta))D^2$ and $r_2(D)=(1/2-2/(3\eta))D^2$. The posted coefficients are $-7/6$ and $-17/6$. At $D=-3/5$ the orders are $10.3$ and $9.7$, with loss $0.3^2+0.3^2=0.18$. Agent 2's ideal order is farther from the human target. The observed gap calls for different marginal corrections to the two agents. Imposing identical penalties would preserve the biased midpoint from Exercise 1.

## Exercise 5. Establish global optimality without differentiating the curve

Prove that each agent's payoff under the contract from Exercise 3 is strongly concave in its own action with the other action fixed. Why can one use first-order conditions when the designer knows only that $f$ is continuous and strictly decreasing?

### Hint

Consider the two integral terms apart from $D^2/2$. Look at their first derivatives and add the intrinsic quadratic separately.

### Solution

The first integral term has derivative $2g(D/\eta)$, which decreases. The second has derivative $-2(g(D/\eta)+D/\eta)$, which also decreases by Exercise 2. Both terms are concave and continuously differentiable. Substitution of the affine expression $D=a_2-a_1$ preserves concavity in each action. In agent $i$'s own action, the remaining quadratic $-(a_i-\theta-b_i)^2+D^2/2$ has second derivative $-1$. Each full payoff is therefore $1$-strongly concave. It is bounded above by a downward-opening quadratic because a differentiable concave function lies below its tangent. Each agent has a unique best reply, found by setting its payoff derivative to zero. The argument only differentiates antiderivatives of continuous functions.

## Exercise 6. Prove Proposition 8

Derive the unique equilibrium action pair for each state and each bias pair on the curve. Prove convergence of the expected loss and give a choice of $\eta$ guaranteeing expected loss at most $\delta>0$ when the designer knows $M=\mathbb E_\Gamma[(b_2-b_1)^2]$. Which part of the argument uses the prior?

### Hint

Write $s=D/\eta$ provisionally, at any candidate equilibrium. Subtract the two first-order conditions *before* inserting the curve equation.

### Solution

Applying the derivatives from Exercise 3 gives

$$
a_1-\theta=b_1-g(s)-D/2,\qquad
a_2-\theta=b_2-g(s)-s+D/2.
$$

Subtraction yields $D=b_2-b_1-s+D$, so $s=b_2-b_1$. The known graph gives $g(s)=b_1$ and $g(s)+s=b_2$. Both conditions now demand the single pair

$$
a_1^*=\theta-\frac{\eta}{2}(b_2-b_1),\qquad
a_2^*=\theta+\frac{\eta}{2}(b_2-b_1).
$$

Its actual difference is $\eta(b_2-b_1)$, so it satisfies both conditions. Exercise 5 makes each action a best reply, proving existence and uniqueness of the pure equilibrium. Each agent can implement its action using its own observations. Allowing independent mixed actions with finite second moments adds no equilibrium. Indeed $g(s)$ and $g(s)+s=f(g(s))$ have opposite signs or are zero, so their magnitudes are each at most $|s|$ (their difference is $s$). The rewards thus grow at most quadratically in absolute value. Expected payoff against such a mixed opponent is finite and remains strongly concave in one's own action. Each best reply is concentrated at a single point.

Squaring the errors and adding gives $L^*=\eta^2(b_2-b_1)^2/2$. The pointwise construction uses the curve alone. Taking expectations gives $\eta^2M/2$, which tends to zero; any $0<\eta\le\sqrt{2\delta/M}$ suffices when $M>0$. If $M=0$, the biases coincide almost surely and their only possible common value on the graph is zero. Every $\eta>0$ then gives zero loss.

## Exercise 7. What can the gap never tell you?

Use $f(x)=-2x$ and the posted rewards from Exercise 3. Imagine a calibration error: the realized pair is $(1+c,-2+c)$ instead of $(1,-2)$, with $|c|<1$. Both agents know the realized pair for this thought experiment. Determine the equilibrium midpoint and loss. Finally, explain why simply setting $\eta=0$ does not deliver exact implementation for every pair on the original curve.

### Hint

A common bias shift preserves the difference. All the derivatives at that difference are consequently unchanged. For the last part, examine the derivatives needed at $D=0$ when $a_1=a_2=\theta$.

### Solution

The subtraction in Exercise 6 still forces $D/\eta=-3$. The schedule decodes $g(-3)=1$ and $g(-3)-3=-2$, even though each realized bias is larger by $c$. Substitution in the first-order conditions gives $a_1=\theta+c-D/2$ and $a_2=\theta+c+D/2$. Their midpoint is $\theta+c$ and their loss is $2c^2+9\eta^2/2$. The positive limit for $c\ne0$ isolates the common shift that this particular schedule cannot detect. This calculation takes the pair as mutually known and only diagnoses misspecification of the original contract.

Back on the original graph, for any differentiable rewards depending only on $D$, exact first-best orders require $r'_1(0)=2b_1$ and $r'_2(0)=-2b_2$ at every supported pair. One pair of fixed derivatives cannot satisfy this requirement for two distinct pairs. In the construction, positive $\eta$ keeps distinct differences observable however small they become. The formula contains $D/\eta$, so $\eta=0$ is not a member of the family. The paper leaves optimal coupling for general bias distributions as a further question.
