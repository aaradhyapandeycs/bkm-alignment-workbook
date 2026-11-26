# Sandbagging and the shape of a spending limit

A purchasing assistant can demonstrate that it can place an order worth 80 credits. An assistant that stops at 60 might have reached its limit, or it might simply have stopped early. Suppose the buyer publishes a rule assigning a spending limit to each demonstration. Which rules make it worthwhile to demonstrate one's full capability?

This sheet reconstructs Example I, Proposition 3, and Appendix A's Lemma 2. The proof of continuum ironing below uses level sets. [Bergemann, Koh and Morris, §3](https://arxiv.org/html/2609.01595v1#S3) · [Appendix A](https://arxiv.org/html/2609.01595v1#A1)

The buyer wants expenditure $a$ close to demand $\theta$ and loses $(a-\theta)^2$. A type with capacity $c$ loses $(a-\theta-b(c))^2$. The buyer knows the continuous function $b$ and the atomless full-support distribution $F$ of $c$ on $[\underline c,\overline c]\subset(0,1]$. Assume $0\le b(c)\le\min(c,1/2)$. Conditional on each $c$, demand is uniform on $[0,1]$. The assistant submits a capacity certificate before it learns demand. It then sees demand perfectly and chooses an action under the awarded upper cap. Demand cannot enter the contract. This application optimizes within the class of upper-cap policies.

## Exercise 1. Which direction can a certificate lie?

Type $c$ can certify any $r\le c$ in the type space and physically perform any $a\le c$. A report $r$ earns permission $a\le k(r)$. Derive the action after a report. Explain why nominal caps can be clipped at their reported capacities. For two possible certificates $0.8$ and $1$, take $k(0.8)=0.8$, $k(1)=0.6$, and $b(1)=0.2$. Find a state in which the larger type benefits from underperforming. Characterize all truthful normalized schedules $0\le k(c)\le c$.

### Hint

Permission and physical capability each impose an upper bound. A larger interval of available actions has option value even when the cap binds only occasionally.

### Solution

Projection of the ideal action gives $a=\min(\theta+b(c),c,k(r))$. Replacing $k(r)$ by $\min(k(r),r)$ preserves what type $r$ does under truth and weakly reduces every imitator's options. In the example, at $\theta=0.7$ the ideal is $0.9$. Reporting $1$ gives squared loss $0.09$ and reporting $0.8$ gives $0.01$. The improvement persists on an interval, hence is profitable before demand is known.

An increasing schedule (weakly throughout this sheet) gives the truthful type the largest feasible cap. Conversely, if $r<c$ and $k(r)>k(c)$, then $k(c)<k(r)\le r<c\le1$. States with $\theta+b(c)>k(c)$ have positive probability and some strictly better action is available under report $r$ in every such state. Truthfulness is therefore equivalent to monotonicity. Negative caps can be raised to zero throughout a monotone schedule, improving the buyer's payoff wherever the change occurs.

## Exercise 2. What cap would a fully informed buyer set?

Hold $b=b(c)$ fixed. Compute buyer utility $V_b(k)=-\mathbb E[(\min(\theta+b,k)-\theta)^2]$ on $0\le k\le c$. Find its unique maximizer. Deduce the precise condition under which evaluation attains the complete-information payoff.

### Hint

If $k\le b$ every purchase has size $k$. Otherwise split the integral at $\theta=k-b$. Compare the two one-sided derivatives at $k=b$.

### Solution

For $k\le b$, $V_b(k)=-k^2+k-1/3$. For $b\le k\le c$, the first $k-b$ units of state mass incur loss $b^2$. The remaining integral gives
$$
V_b(k)=-kb^2-\frac{(1-k)^3}{3}+\frac{2b^3}{3}.
$$
The derivatives are $1-2k$ and $(1-k)^2-b^2$ in the respective ranges. They agree at $b$ and decrease strictly through the available range. The unique best cap is $k_0(c)=\min(c,1-b(c))$. In particular, with known $c=0.9$ a bias of $0.15$ produces cap $0.85$, whereas bias $0.35$ produces cap $0.65$.

A monotone $k_0$ is implementable by Exercise 1. Conversely a schedule attaining the integrated pointwise optimum must agree with $k_0$ almost surely by strict optimality. A downward reversal of the continuous $k_0$ would persist between two ordered open intervals, both of positive $F$-mass, which contradicts monotonicity of such a schedule. The criterion is exactly that $k_0$ increase weakly. Decreasing $b$ ensures it since $c$ and $1-b(c)$ then both increase.

## Exercise 3. Iron a three-type example by hand

Temporarily replace the continuous prior by three equally likely types with capacities $(0.8,0.9,1)$ and biases $(0.12,0.40,0.18)$. Put $z=(1-k)^2$. Fit the target $y=b^2$ by least squares subject to decreasing fitted values and $(1-c)^2\le z\le1$. Which types face the same permission?

### Hint

If two neighboring fitted values violate the order, first try pooling them and minimizing their sum of squared residuals.

### Solution

The targets are $(0.0144,0.16,0.0324)$ and their floors are $(0.04,0.01,0)$. The unconstrained best fit of the first two subject only to their ordering lies at their common mean $0.0872$. Indeed an optimum with strict inequality would be the unordered pair of targets. The third target is below $0.0872$ and all floors hold, so $(0.0872,0.0872,0.0324)$ is also the full constrained optimum. The first two types share the cap $1-\sqrt{0.0872}\simeq0.705$ and the third earns $0.82$. Thus a high certificate can restore discretion even when two lower certificates receive identical permissions.

## Exercise 4. Why does squared-error regression solve the buyer's problem?

Set $\ell(c)=(1-c)^2$, $U(c)=(1-\min(c,1/2))^2$ and $y(c)=b(c)^2$. Show that one can restrict to $\ell\le z\le U$. On this set express both the buyer's loss and the regression loss in terms of $z$. Their formulas differ. Explain why they have the same minimizer, including existence and uniqueness for the continuous prior.

### Hint

Slice a decreasing $z$ horizontally. At each height $t$, its superlevel set is an initial interval. The marginal costs of including a type in that interval have the same sign pattern for both objectives and differ by a positive factor depending only on $t$.

### Solution

Raising $k$ to $\max(k,\min(c,1/2))$ preserves monotonicity and feasibility. The derivatives in Exercise 2 are positive below $\min(c,1/2)$: on $b<k<1/2$ use $(1-k)^2-b^2>(1-k)^2-k^2>0$. Thus an optimal cap can be chosen at least this large. Equivalently $z$ is decreasing and $\ell\le z\le U$. For least squares, clipping $z$ from above at $U$ also helps, since $y\le1/4\le U$. On the clipped set $k\ge b$, so the cap-dependent part of the buyer's loss and the regression objective respectively are
$$
J(z)=\int\left(\frac{z^{3/2}}{3}-y\sqrt z\right)dF,\qquad
Q(z)=\int(z-y)^2\,dF.
$$

For detail, change variables to $x=F(c)$, uniform on $[0,1]$, carrying $\ell,U,y$ along by the quantile map. At height $0<t<1$, any feasible superlevel set $\{z>t\}$ is an initial interval up to its endpoint. Its length $p$ must be between the lengths of $\{\ell>t\}$ and $\{U>t\}$. Define
$$
B_t(p)=tp-\int_0^p y(x)\,dx.
$$
Integrating the derivatives of the integrands from zero to $z$ expresses $Q-Q(0)$ as the integral over $t$ of $2B_t(p)$ and $J-J(0)$ as the integral of $B_t(p)/(2\sqrt t)$. These integrals are absolutely convergent since all variables are bounded and $t^{-1/2}$ is integrable.

Choose a minimizing length $p(t)$ on its compact admissible interval. These lengths are decreasing in $t$. Indeed, if $s<t$ but $p(s)<p(t)$, both lengths are feasible at both heights because the interval endpoints decrease. Adding the two minimizing inequalities gives $(t-s)(p(t)-p(s))\le0$, a contradiction. Consequently the chosen intervals are nested, and $z(x)=\int_0^1 \mathbf1_{\{x<p(t)\}}dt$ realizes the minimizing slices almost everywhere by Fubini. It obeys the bounds almost everywhere; clipping it pointwise between the decreasing functions $\ell$ and $U$ preserves monotonicity and the objective values. The resulting $z$ minimizes both objectives. Strict convexity of $Q$ gives uniqueness up to null sets. For $J$ the integrand is strictly convex on $z>0$ since its second derivative is $(z+y)/(4z^{3/2})$. The floor gives $z>0$ except possibly at $c=1$, an $F$-null event. This proves the continuum ironing lemma and identifies the optimal evaluated cap $1-\sqrt z$.

## Exercise 5. Can costly evaluations be dispensed with when bias rises?

Suppose $b$ is weakly increasing. First optimize a single nominal cap $a$, with effective cap $\min(c,a)$. Treat both a binding optimum and the case when the physical frontier alone suffices. Then prove that even a menu contingent on the certificate cannot improve the payoff.

### Hint

Differentiate the common-cap payoff using the types with $c>a$. At a binding optimum compare a competing monotone schedule by the tangent inequality for $V_b$.

### Solution

If $\overline c\le1-b(\overline c)$ then every type has $c\le1-b(c)$. Giving full physical discretion achieves the pointwise optimum, so one can take $a=\overline c$. In the other case $\overline c>1/2$. An optimum in $[0,\overline c]$ exists by continuity. Caps below $1/2$ with binding types can be improved. For $1/2\le a<\overline c$, atomlessness and bounded derivatives give the marginal payoff
$$
\Pr(c>a)\left[(1-a)^2-\mathbb E\big[b(c)^2\mid c>a\big]\right].
$$
The bracket is nonnegative at $1/2$ and tends to $(1-\overline c)^2-b(\overline c)^2<0$ at the upper endpoint. It decreases strictly by monotonicity of $b$ and is continuous by atomlessness. Thus its sole root $a^*\in[1/2,\overline c)$ satisfies
$$
a^*=1-\sqrt{\mathbb E[b(c)^2\mid c>a^*]}.
$$

For an arbitrary feasible schedule $h(c)$, concavity bounds its gain over $k^*(c)=\min(c,a^*)$ by $\int V'_{b(c)}(k^*(c))(h(c)-k^*(c))\,dF$. Below the threshold, $h(c)-c\le0$ and $b(c)\le\sqrt{\mathbb E[b^2\mid c>a^*]}=1-a^*\le1-c$, so $V'_{b(c)}(c)\ge0$. Above the threshold, the derivative is a decreasing function of $c$ with conditional mean zero, while $h(c)-a^*$ increases. Their covariance is nonpositive: take two independent conditional draws and multiply the opposite-signed differences. The gain is therefore at most zero. A common nominal cap pays for no information and attains the best evaluated payoff. Its *effective* action frontier still varies with the assistant's physical capabilities.
