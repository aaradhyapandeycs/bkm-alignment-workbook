# How much authority should the monitor have?

A human asks a forecasting system to choose tomorrow's inventory level. The system sees tomorrow's demand unusually well, but tends to overorder. A reviewer can diagnose that tendency today. The reviewer cannot forecast demand, and has an inventory preference of its own. Should it be able to veto the system, cap its order, or write its performance score?

The exercises reconstruct Example V through Proposition 9, including the single-type comparison of permission sets used in its proof. [Bergemann, Koh and Morris, §5 and Appendix A](https://arxiv.org/html/2609.01595v1)

Let $\theta$ be uniform on $[0,1]$. The actor's bias $b$ is independent of $\theta$, has law $\tau$ and finite second moment. The human wants $a=\theta$, the monitor wants $a=\theta+w$, and the actor wants $a=\theta+b$. Each measures loss by squared distance to its ideal. The human knows $w$ here, chooses the oversight regime before $b$ is drawn, and does not observe $b$. The monitor observes $b$ and chooses an instrument. The actor then sees the instrument and $\theta$ and takes a real action. It knows $b$. Rewards add to the actor's utility and carry no direct cost for the monitor or human.

## Exercise 1. Whose information determines the fallback?

The monitor may approve unrestricted action or require the fixed action $1/2$. Derive the monitor's approval rule and the human's loss following either choice. Why would replacing $1/2$ by $1/2+w$ change the game? Work out the choices when $w=1/10$ and $b$ is either $0$ or $1/2$.

### Hint

Compute the variance of $\theta$. The monitor commits before observing tomorrow's demand. Use approval at a tie.

### Solution

The best fixed action for the human is the state mean, $1/2$. Approval lets the actor choose $\theta+b$. The monitor's loss is $(b-w)^2$ and the human's is $b^2$. After rejection the monitor's expected loss is $\operatorname{Var}(\theta)+w^2=1/12+w^2$, and the human loses $1/12$. Thus the monitor approves exactly when $(b-w)^2\le 1/12+w^2$. A fallback of $1/2+w$ would give the monitor its preferred constant and change the rejection payoffs. With the given biases the rejection threshold in squared-loss units is $7/75$. The monitor approves $b=0$ because $1/100<7/75$ and rejects $b=1/2$ because $4/25>7/75$.

## Exercise 2. Can a permission set with holes beat a cap?

Now the monitor can specify any nonempty closed subset of the action line. Translate the action by $-w$ and write $t=b-w>0$. If $D$ is the translated permission set, let $d_D$ be its distance function and $q(x)$ a nearest allowed point to $x$. Put

$$
A_D(t)=\int_t^{t+1}d_D(x)^2\,dx,\qquad
H_D(t)=\int_0^1(q(\theta+t)-\theta)^2\,d\theta .
$$

Match $D$ to a cap $C=(-\infty,c]$ having the same $A(t)$. Prove $H_C(t)\le H_D(t)$. Here $H_D$ measures the loss of the monitor in translated coordinates.

### Hint

Expand the square to obtain $H_D(t)=A_D(t)-t A_D'(t)+t^2$. A cap maximizes the possible increase in squared distance from one end of a unit interval to its other end, given the integral of squared distance.

### Solution

The actor projects its ideal $\theta+t$ onto $D$. A nearest point exists by closedness, and ties are confined to the countably many midpoints of complementary bounded intervals. The locally Lipschitz function $d_D^2$ has derivative $2(x-q(x))$ almost everywhere. Integrating this derivative gives $A_D'(t)=d_D(t+1)^2-d_D(t)^2$. Expanding $q(\theta+t)-\theta=q(\theta+t)-(\theta+t)+t$ yields the identity in the hint.

Write $y=A_D(t)$ and $p=d_D(t+1)$. On this interval the distance is bounded below by the ramp $x\mapsto(p-1+x-t)_+$ because distance is one-Lipschitz. If $p\le1$, then $y\ge p^3/3$ and $A_D'(t)\le p^2$. If $p\ge1$, then $y\ge p^2-p+1/3$ and $A_D'(t)\le p^2-(p-1)^2=2p-1$. Consequently

$$
A_D'(t)\le
\begin{cases}
(3y)^{2/3},&y\le1/3,\\
2\sqrt{y-1/12},&y\ge1/3 .
\end{cases}
$$

In the overlap check $p\le1$, $y\ge1/3$ by bounding $p^2\le1$. The cap distance is exactly such a ramp. Moving $c$ down from $t+1$ to $-\infty$ makes its squared integral increase continuously from zero to infinity. The matching cap attains equality in the displayed bound, so $A_C'(t)\ge A_D'(t)$. Multiplication by $-t$ proves the claim. This comparison justifies optimizing over caps even though the monitor can choose disconnected sets.

## Exercise 3. Where does a cap become a constant?

For $t=b-w>0$, minimize the monitor's loss over caps in translated coordinates. Give an optimal permission set in original coordinates for every sign and size of $b-w$, including equality at the transition.

### Hint

The translated action is $\min(\theta+t,c)$. Split the integral at $\theta=c-t$ when this point is in $(0,1)$.

### Solution

For $c\le t$ the action is constant, so the loss is $(c-1/2)^2+1/12$. For $t<c<t+1$ it is

$$
(c-t)t^2+\int_{c-t}^1(c-\theta)^2\,d\theta .
$$

Differentiation gives $t^2-(1-c)^2$ in this middle range; the moving-endpoint terms cancel. Above $t+1$ the loss is constant at $t^2$. For $0<t<1/2$, the derivative changes sign from negative to positive at $c=1-t$ and stays nonnegative thereafter. For $t\ge1/2$ the constant-action region contains its minimum $c=1/2$, and the middle region cannot improve it. Reflection $(\theta,y)\mapsto(1-\theta,1-y)$ gives the lower bound on the action for negative $t$. Thus one optimal original permission set is

$$
D^*(b)=
\begin{cases}
(-\infty,w+1-t],&0<t<1/2,\\
\mathbb R,&t=0,\\
[w-t,\infty),&-1/2<t<0,\\
\{w+1/2\},&|t|\ge1/2 .
\end{cases}
$$

At $t=1/2$ the cap also implements the constant almost surely. For example, $w=0.1$ and $b=0.3$ give an upper limit of $0.9$. When $\theta=0.75$ the actor's ideal is $1.05$, so the order is $0.9$.

## Exercise 4. Why do two kinds of error enter human welfare?

Under optimal permission delegation, compute the mean and mean square of the monitor error $e=a-\theta-w$. Recover the human's conditional loss and check the limit at $|b-w|=1/2$.

### Hint

For $0<t<1/2$, the cap binds on an interval of length $2t$. Across that interval $e$ runs linearly from $t$ down to $-t$.

### Solution

On the remaining interval of length $1-2t$ the error equals $t$. The mean contribution from the binding interval is zero, and its second-moment contribution is $\int_{-t}^t z^2\,dz=2t^3/3$. Reflection reverses the mean for a negative bias and leaves its square unchanged. Writing $s=|t|$ gives

$$
\mathbb E[e]=t(1-2s)_+,\qquad
\mathbb E[e^2]=h(s)=
\begin{cases}s^2-4s^3/3,&s<1/2,\\ 1/12,&s\ge1/2.\end{cases}
$$

For a constant translated action $1/2$, the error $1/2-\theta$ has mean zero and variance $1/12$, which also gives the limit from the interior. The human's loss is $h(s)+2wt(1-2s)_++w^2$ because its error is $e+w$. Minimizing the monitor's mean square leaves the human sensitive to the mean error as well.

## Exercise 5. Give the monitor a reward-writing pen

With any state-independent reward schedule that gives the actor a maximizer at every state and bias, exhibit an instrument attaining the monitor's first best. Compare the three regimes for both players when $b=0$ and $w=1/10$.

### Hint

A linear reward changes the maximizer of a quadratic payoff by half its slope.

### Solution

Take $r(a)=-2(b-w)a$. Completing the square in $-(a-\theta-b)^2+r(a)$ gives a strictly concave quadratic centered at $\theta+w$. Thus the monitor loses zero and the human loses $w^2$ for every $b$. Every permission set is available as the schedule paying zero on the set and $-\infty$ outside. Approval and rejection are particular permission sets. This nesting guarantees that more authority weakly reduces the monitor's loss for each $b$.

In the numerical example, the monitor's losses in order of increasing authority are $1/100$, $13/1500$ and $0$. The human's are $0$, $1/375$ and $1/100$. Here the actor starts perfectly aligned with the human. Giving the reviewer better tools to impose its preference strictly increases the human's loss.

## Exercise 6. Recover the switches in Figure 11

The actor has bias $3/10$ with probability $p$ and $0$ otherwise. Hold $w=1/10$. Identify all values of $p$ at which the human's optimal regime changes. Explain why the human takes the expectation over $b$ *after* solving the monitor's optimization.

### Hint

Compute two conditional losses for each regime. Every ex ante loss is an affine function of $p$.

### Solution

Both biases are approved in the binary regime. The two human losses there are $0$ and $9/100$. For permission delegation they are $1/375$ and $19/300$. Full reward authority costs $1/100$ at either bias. Hence

$$
L_H^{I}=\frac9{100}p,\qquad
L_H^{II}=\frac1{375}+\frac{91}{1500}p,\qquad
L_H^{III}=\frac1{100}.
$$

The lower envelope passes from I to II at $p=1/11$, and from II to III at $p=11/91$. At each switch the adjacent regimes tie. The I–III intersection $p=1/9$ lies above regime II. The human selects a single regime today, whereas the monitor will choose an instrument after diagnosing the actor. Optimizing a single instrument for the average actor would change that information structure.

## Exercise 7. Vary the reviewer's bias instead

Take the same two actor types, fix $p=1/20$, and increase $w$ from zero. Recover the order of the human's choices in the other panel of Figure 11. Distinguish a change in the reviewer's approval decision from a change in the human's preferred regime.

### Hint

The reviewer always approves the unbiased type. Compute when it approves the biased type. For $0\le w\le3/10$, write the permission losses for the two types as polynomials in $w$.

### Solution

Approval of the biased type switches on at $w=1/90$ because $(3/10-w)^2\le 1/12+w^2$ exactly above this threshold, including equality. Binary approval costs the human $1/240$ below the threshold and $9/2000$ from the threshold onward. Full reward authority costs $w^2$.

For $0\le w\le3/10$, the conditional human loss under permissions for the unbiased type is $8w^3/3$. For the biased type, putting $t=3/10-w$ in Exercise 4 gives $9/100-(4/3)t^2(3/10+2w)$. Weighting the two types gives

$$
L_H^{II}=\frac{27}{10000}+\frac{3}{50}w^2+\frac{12}{5}w^3 .
$$

It first meets $w^2$ at $w\approx0.058072$ and then meets $9/2000$ at $w\approx0.083241$. These roots belong to $(0.05,0.06)$ and $(0.08,0.09)$ respectively. The permission loss is increasing. Its difference from $w^2$ decreases up to $w=47/180$ and increases afterward; it is still negative at $3/10$. These signs and the binary approval rule show that the lower envelope passes from III to II to I at the two roots. At $w=1/90$ the monitor changes an approval decision inside regime I, while the human still selects III.

For $w\ge3/10$ both actor biases satisfy $b\le w$. If $s=w-b\in[0,1/2]$, Exercise 4 gives $L_H^{II}(b)=b^2+4s^2(w-s/3)\ge b^2$; if $s\ge1/2$, its value $w^2+1/12$ also exceeds $b^2$. Thus I continues to be optimal on this range, with expected cost $9/2000$. Switching thresholds depend on the prior, and reversing which parameter is varied can reverse the ordering of optimal authority.
