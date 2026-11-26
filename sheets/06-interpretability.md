# When a common cap beats a menu

A buyer is comparing two purchasing assistants. One consistently orders a little too much. The other is sometimes exactly right and sometimes orders substantially too much. If either assistant can buy anything, the buyer can compare their mean squared excess orders. If the buyer can also set a spending limit, will that comparison still rank the two systems correctly?

This sheet develops Example II, Propositions 4 and 5, and the cap comparison in Appendix A. [Bergemann, Koh and Morris, §3](https://arxiv.org/html/2609.01595v1#S3) · [Appendix A](https://arxiv.org/html/2609.01595v1#A1)

Conditional on each bias $b\ge0$, demand $\theta$ is uniform on $[0,1]$. The human wants action $\theta$ and the agent wants $\theta+b$; each loses squared distance from its ideal. All types have the full action set $\mathbb R$ and learn $\theta$ perfectly after reporting their privately known bias. Each report is available to each type. The human chooses a menu of nonempty closed permission sets $D_r$, with measurable induced losses. Under a truthful menu a type minimizes its expected loss by choosing the set assigned to its own report. The bias distribution $\tau$ represents the human's uncertainty prior to a report. Write $m=\mathbb E b$, $v=\operatorname{Var}(b)$, and $M=\mathbb E b^2=m^2+v$.

## Exercise 1. Two technologies, one choice of instrument

Technology A has constant bias $1/4$. Technology B draws either $0$ or $\sqrt{2}/4$ with equal probability. Compare their full-discretion losses. Now impose a common cap $q=3/4$. Which technology does the buyer prefer?

### Hint

For $b\le q\le1$, the cap binds when $\theta>q-b$. Split the buyer's loss integral at that threshold.

### Solution

Full discretion gives action $\theta+b$ and expected loss $M=1/16$ under either technology. At cap $q$ and bias $b$, expected loss equals
$$
(q-b)b^2+\int_{q-b}^1(q-\theta)^2d\theta
=qb^2+\frac{(1-q)^3}{3}-\frac{2b^3}{3}.
$$
The respective third moments are $1/64$ and $\sqrt2/64$. Thus B has lower capped loss by $(\sqrt2-1)/96$. Equal second moments can produce equal control instruments and unequal welfare. Exercise 5 will show that $3/4$ is in fact optimal among all truthful delegation menus for both.

## Exercise 2. What does a permission set tell us through its distances?

For a nonempty closed set $D$, put $d_D(x)=\inf_{a\in D}|x-a|$. Let $A_D(t)$ and $H_D(t)$ be the agent's and human's expected losses when the actual bias is $t$ and the agent chooses a nearest point $a_D(\theta,t)$ to $\theta+t$. Express $A_D(t)$ and its derivative using endpoints of a length-one interval. Prove
$$
H_D(t)=A_D(t)-tA_D'(t)+t^2.
$$
Where does the uniform prior enter?

### Hint

The function $d_D^2$ is locally Lipschitz. At every point with a unique nearest point, its derivative is twice the displacement from that point.

### Solution

As $\theta$ ranges uniformly from zero to one, the agent's ideal traverses $[t,t+1]$ with unit density. Hence
$$
A_D(t)=\int_t^{t+1}d_D(x)^2\,dx,\qquad
A_D'(t)=d_D(t+1)^2-d_D(t)^2.
$$
A tie can occur only at the midpoint of an open gap in the closed set. The gaps are countable since each contains a rational. Except on this null set, the derivative of $d_D^2$ is $2(x-a_D)$, as follows by comparing nearest-point distances at nearby targets. Integrating the derivative gives $A_D'(t)=2\mathbb E[\theta+t-a_D(\theta,t)]$. Now expand $(a_D-\theta)^2=((a_D-\theta-t)+t)^2$. The cross term yields the asserted identity. A nonuniform prior would insert a weight into the sliding integral and alter the endpoint formula.

## Exercise 3. Why is a half-line a useful comparison for an arbitrary closed set?

For any nonnegative 1-Lipschitz function $d$ on $[0,1]$ let $y=\int d^2$. Prove the sharp bound
$$
d(1)^2-d(0)^2\le \Phi(y),\qquad
\Phi(y)=
\begin{cases}
(3y)^{2/3},&0\le y\le1/3,\\
2\sqrt{y-1/12},&y\ge1/3 .
\end{cases}
$$
For a type $b$, choose a half-line $K_c=(-\infty,c]$ giving the same agent loss as $D$. Show that it weakly lowers the human's loss at $b$ and gives at least as much agent loss as $D$ at every higher type $t\ge b$.

### Hint

Fix $p=d(1)$ and draw the smallest permissible graph to its left. On a translated unit interval the distance to a half-line is precisely such a graph when its right endpoint is at or beyond the cap.

### Solution

The lower envelope is $(p-1+x)_+$. If $p\le1$, its squared integral is $p^3/3$. The endpoint difference is at most $p^2$, hence at most $(3y)^{2/3}$ when $y\le1/3$, and at most $1\le2\sqrt{y-1/12}$ otherwise. If $p\ge1$, the lower envelope has squared integral $(p-1/2)^2+1/12\ge1/3$ and $d(0)\ge p-1$. The endpoint difference is at most $2p-1\le2\sqrt{y-1/12}$. The envelope itself attains equality in the branch corresponding to its integral.

The quantity $A_{K_c}(b)=\int_b^{b+1}(x-c)_+^2\,dx$ runs continuously and strictly from zero to infinity as $c$ decreases from $b+1$. Choose the unique $c\le b+1$ giving $A_{K_c}(b)=A_D(b)$. Applying the bound to $d_D$ on $[t,t+1]$ gives $A_D'(t)\le\Phi(A_D(t))$; for $K_c$ there is equality for all $t\ge b$. Thus $A_D'(b)\le A_{K_c}'(b)$, and Exercise 2 gives $H_{K_c}(b)\le H_D(b)$ since $b\ge0$.

To compare higher types without assuming Lipschitz continuity of $\Phi$ at zero, use $S(y)=\int_0^y1/\Phi(u)\,du$, finite since $u^{-2/3}$ is integrable there. On a positive-loss interval $(S\circ A_D)'\le1$. If the loss vanishes between $b$ and $t$, restart this integration at its last zero before $t$. This gives $S(A_D(t))\le S(A_D(b))+t-b$ in either case. The cap achieves equality, including when its initial loss is zero, because its loss is positive immediately to the right of $b$ then. Strict increase of $S$ completes the comparison.

## Exercise 4. How can all types end up with one cap?

Assume $b\le1$ on the support for this exercise. Given any truthful menu, let $c(b)$ be the matched cap in Exercise 3 for its assigned set $D_b$. Prove $c(b)$ is increasing. Find the human's optimal cap if it knows the bias. Use the two orderings to exhibit one common cap that does at least as well for every type as its original permission set.

### Hint

Use the incentive constraint of a *higher* type reporting a lower one. Then draw the closed interval between the matched cap and the human's favorite cap for each type.

### Solution

If $b<t$, complete report access, truthfulness, and Exercise 3 give
$$
A_{K_{c(t)}}(t)=A_{D_t}(t)\le A_{D_b}(t)\le A_{K_{c(b)}}(t).
$$
Cap loss is strictly decreasing with its endpoint up to $t+1$, and $c(b)\le b+1<t+1$, $c(t)\le t+1$. Consequently $c(b)\le c(t)$. These matched caps are comparison devices. The proof uses the original menu's incentives.

For a fixed bias, direct differentiation of the integrated human loss $L_b(q)=H_{K_q}(b)$ gives
$$
L_b'(q)=
\begin{cases}
2q-1,&q\le b,\\
b^2-(1-q)^2,&b<q<b+1,\\
0,&q\ge b+1 .
\end{cases}
$$
A favorite cap is $q_0(b)=\max(1/2,1-b)$. Moving any endpoint toward $q_0(b)$ weakly lowers loss, including in the flat region beyond $1+b$.

Let $I_b$ be the closed interval with endpoints $c(b)$ and $q_0(b)$. For $b<t$, its lower endpoint is at most $c(b)\le c(t)\le\sup I_t$; the lower endpoint of $I_t$ is at most $q_0(t)\le q_0(b)\le\sup I_b$. Thus the supremum of all lower endpoints is at most the infimum of all upper endpoints. These quantities are finite since $1/2\le q_0(b)\le1$ and there is at least one type. A common $q$ between them improves on every matched cap for its own type. The constant menu is truthful because every report earns the identical set. Composing the two pointwise human-loss comparisons proves the reduction from arbitrary closed menus.

## Exercise 5. Optimize the cap and find its range of validity

Assume BKM's condition (II), $0\le b\le1-\sqrt M$ almost surely. Derive the optimal common cap and its loss. Check the signs of the derivatives for caps below some of the biases as well as above one. What happens to the proposed formula for a deterministic bias $b=0.8$ outside (II)?

### Hint

At the candidate cap all biases lie below the cap. To check a lower cap with $0\le q\le b$, compare $2q-1$ with $b^2-(1-q)^2$.

### Solution

Let $q^*=1-\sqrt M$. Condition (II) gives $b\le q^*\le1$. For $q<0$ the derivative is negative for every type. On $0\le q<q^*$, the bound $2q-1\le b^2-(1-q)^2$ holds when $q\le b$ since their difference, right side minus left, is $b^2-q^2$. Otherwise the right side is the exact derivative. The average derivative is therefore at most $M-(1-q)^2<0$. For $q^*<q\le1$ the derivative averaged across types is exactly $M-(1-q)^2>0$. Above one, any binding threshold has derivative $b^2-(q-1)^2\ge0$; slack thresholds have zero derivative. The uniform bound on $b$ justifies the averaging. With $M=0$, larger slack caps also attain the same minimum.

Substitution into Exercise 1 gives Proposition 4:
$$
q^*=1-\sqrt{m^2+v},\qquad
L^*=M-\frac23M^{3/2}-\frac23\mathbb E[b^3].
$$
For deterministic $b=0.8$ the numerical prescription $1-\sqrt M=0.2$ would give the constant action $0.2$. The human prefers $q=1/2$ by Exercise 4. This shows why the support condition matters for the displayed formula.

## Exercise 6. Does making the technology more interpretable always help?

Fix a symmetric, finitely supported $\xi$ of mean zero and variance one. Vary $b=m+\sqrt v\,\xi$ within the nonnegative region satisfying (II). Here lower $m$ means better mean alignment, and lower $v$ means greater interpretability. Derive the first derivatives of optimized loss and its mixed derivative at admissible interior points. Give one admissible example in which reducing variance locally *raises* optimized loss. Explain the complementarity statement in Proposition 5.

### Hint

Symmetry removes the third centered moment. Keep the shock distribution fixed when changing either parameter.

### Solution

Here $\mathbb E b^3=m^3+3mv$. Differentiating the formula from Exercise 5 gives
$$
\partial_v L^*=q^*-2m,\qquad
\partial_m L^*=2mq^*-2M,\qquad
\partial_m\partial_v L^*=-2-\frac{m}{\sqrt M}.
$$
For a symmetric two-point shock $\xi=\pm1$ with equal probabilities, take $m=0.4$ and $\sqrt v=0.1$. The support is $\{0.3,0.5\}$ and $q^*=1-\sqrt{0.17}>0.5$, leaving room for a small change in $v$. Here $\partial_vL^*<0$, so reducing $v$ raises loss. More generally the zero of $\partial_vL^*$ occurs at $v=(1-m)(1-3m)$ when the threshold is admissible and $1-2m\ge0$.

The cap depends on $m^2$ and $v$ only through their sum. For welfare $-L^*$ as a function of the two improvements $(-m,-v)$, the mixed derivative is $2+m/\sqrt M>0$. Integrating over an admissible rectangle gives increasing differences: the payoff gain from reducing variance is larger when mean bias is smaller. A marginal gain can be negative and still satisfy increasing differences. Under full discretion the mixed derivative of $-M$ with respect to these improvement variables is zero.

## Exercise 7. Pick a training technology before designing the mechanism

For equal-probability shocks $\xi=\pm1$, consider the paper's illustrative frontier
$$
m(k)=0.36-0.10k,\qquad \sqrt{v(k)}=0.26k^{1.4},\qquad 0\le k\le1.
$$
Describe a reproducible numerical comparison between the choice under full discretion and the choice under the optimal delegation menu. Which design accepts the higher variance?

### Hint

Evaluate the two loss functions on the same grid. Check the allowed bias range and condition (II) before using the optimal loss formula.

### Solution

Throughout the frontier $m-\sqrt v\ge0$ since it decreases to zero. Also $m+\sqrt v\le0.52$ by convexity in $k$ and the endpoint values. Since $\sqrt M\le\sqrt{0.36^2+0.26^2}<0.445$, condition (II) holds. For each $k=j/10000$, $0\le j\le10000$, compute $M=m(k)^2+v(k)$ and compare this to $M-\tfrac23(M^{3/2}+m(k)^3+3m(k)v(k))$ as two separate objective functions. The respective grid minimizers are $0.5346$ and $0.8169$, with losses approximately $0.10567$ and $0.05382$ under their respective protocols. This is a numerical comparison on the specified frontier. The permission cap makes the high-bias realization less costly, changing the buyer's preferred training point.
