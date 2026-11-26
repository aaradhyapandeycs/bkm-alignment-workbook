# How much can a disagreement reveal?

## When agreeing on the wrong order is easy

Two depot managers see the same demand $\theta$ before placing orders. Each would choose $\theta+b_i$ for its own depot in the absence of rewards. The central buyer wants both orders to equal $\theta$ and suffers total squared error. It knows that the biases satisfy $b_2=f(b_1)$ for a continuous, strictly decreasing function with $f(0)=0$. Each manager observes its own bias. Since the curve is known and one-to-one, each can infer the other's bias as well. The buyer sees the two actions for payment and still lacks the information each manager uses to act. [Original paper, Section 5, Example IV](https://arxiv.org/html/2609.01595v1#S5)

Consider a buyer who simply charges both depots $\gamma(a_2-a_1)^2$. Write $D=a_2-a_1$. The first-order conditions give $a_1=\theta+b_1+\gamma D$ and $a_2=\theta+b_2-\gamma D$. Consequently the equilibrium gap shrinks as the charge grows, but the midpoint stays at $\theta+(b_1+b_2)/2$. For biases $(1,-2)$ the two depots can come arbitrarily close to agreement while their common midpoint is half a unit below demand.

## Using the gap to price each manager's next unit

Suppose the buyer wants equilibrium midpoint $\theta$ and a small gap $\eta(b_2-b_1)$, for a chosen $\eta>0$. There is only one unknown coordinate on the bias curve. The function $h(x)=f(x)-x$ strictly decreases from $+\infty$ to $-\infty$, even if $f$ has bounded range. Its inverse $g$ recovers $b_1$ from the difference $b_2-b_1$; adding that difference recovers $b_2$.

Which payments would make the proposed orders optimal? At a gap $D$, put $s=D/\eta$. Give the first manager marginal reward $r_1'(D)=D+2g(s)$ and the second marginal reward $r_2'(D)=D-2(g(s)+s)$. A manager raising its own order changes $D$ in opposite directions at the two depots. Choosing antiderivatives with value zero at agreement gives
$$
r_1(D)=\frac{D^2}{2}+2\eta\int_0^{D/\eta}g(z)\,dz,\qquad
r_2(D)=\frac{D^2}{2}-2\eta\int_0^{D/\eta}(g(z)+z)\,dz .
$$
The buyer posts these schedules before observing any decisions. The prices themselves use only the realized orders. For example, when the curve is $f(x)=-2x$, a gap of $-3\eta$ encodes exactly the pair $(1,-2)$. The slope charged to the second depot must offset a bias twice as large in magnitude, which explains why a common disagreement penalty misses the target.

## Proposition 8. Coupled rewards make loss arbitrarily small

The two marginal terms $g(s)$ and $-(g(s)+s)$ decrease because $g$ decreases and $g(s)+s=f(g(s))$ increases. Their integrals are concave. Combining $D^2/2$ with each manager's original quadratic payoff leaves a strictly concave objective in that manager's action for every peer action. Thus each first-order condition singles out a best reply. Subtracting the two conditions at any equilibrium forces $D/\eta=b_2-b_1$. Once the rates have identified the biases, substitution yields the unique pair
$$
(a_1,a_2)=\left(\theta-\tfrac{\eta}{2}(b_2-b_1),
                 \theta+\tfrac{\eta}{2}(b_2-b_1)\right).
$$

This is Proposition 8. Conditional loss is exactly $\eta^2(b_2-b_1)^2/2$. A finite second moment of the bias difference therefore makes expected loss tend to zero with $\eta$. Keeping $\eta$ positive lets different bias pairs leave different observable gaps. If every pair instead produced exact agreement, a differentiable reward depending on the gap would have just one slope at zero for each depot, while offsetting each realized bias would require different slopes. The approximation uses a small, informative disagreement to make the midpoint exactly right. [Derive the contract and test a common calibration error](09-competition.html)
