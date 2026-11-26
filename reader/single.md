# What can a spending limit reveal?

Imagine testing a purchasing assistant that will eventually see the day's demand and place an order on its own. The buyer can verify the size of a demonstration order and can set a spending limit, but cannot write a contract contingent on the unobserved demand. Two features of the assistant matter: how much it *can* order, and how much extra it *wants* to order. The two applications in §3 change which of these features a certificate reveals. [Bergemann, Koh and Morris, §3](https://arxiv.org/html/2609.01595v1#S3)

## Capability certificates and sandbagging

Let demand $\theta$ be uniform on $[0,1]$ conditional on the assistant's type. The human loses $(a-\theta)^2$, whereas the assistant loses $(a-\theta-b(c))^2$. Its physical capacity $c$ has an atomless distribution $F$ with full support on an interval in $(0,1]$. The known, continuous bias function satisfies $0\le b(c)\le\min(c,1/2)$. The assistant can certify any capacity at most $c$. If the certificate earns cap $k$, the eventual purchase is $\min(\theta+b(c),c,k)$.

A truthful effective cap schedule must rise weakly with $c$. If an easier certificate earned a larger cap, the capable assistant could take it and spend more whenever the truthful cap curtailed its ideal purchase. Conversely, when the schedule rises, the highest attainable certificate gives the largest permission set. For a known type the buyer prefers cap $\min(c,1-b(c))$. Thus evaluation recovers the complete-information payoff exactly when those preferred caps already rise with capability. Falling bias guarantees this property. [Derive the incentive test](05-sandbagging.html#exercise-1) · [Optimize a known type's cap](05-sandbagging.html#exercise-2)

### Proposition 3. Optimal caps

What if the preferred caps reverse order? Proposition 3 asks the designer to fit squared bias $b(c)^2$ by a decreasing function $z(c)$ in least squares under $F$, with $(1-c)^2\le z(c)\le1$. The optimal effective cap is $1-\sqrt{z(c)}$. When bias rises, one nominal cap $k$ suffices. If $\overline c\le1-b(\overline c)$, take $k=\overline c$. Otherwise the unique binding choice satisfies $(1-k)^2=\mathbb E[b(c)^2\mid c>k]$. Only assistants that can reach the cap enter this average. Proposition 3 optimizes over upper-cap policies. [Pool three types by hand](05-sandbagging.html#exercise-3) · [Prove continuum ironing](05-sandbagging.html#exercise-4) · [Derive the tail average](05-sandbagging.html#exercise-5)

### Lemma 2. Continuum ironing

Why fit squared bias by least squares when the buyer actually minimizes a different loss? The actual loss and regression loss have marginal costs at a common height $z=t$ differing by the same positive factor for every type. Fitting a pooled block therefore serves both objectives. [Reconstruct the continuum argument](05-sandbagging.html#exercise-4)

## Proposition 4. One cap is optimal

Now every assistant can choose any real action and claim any supported bias. A report earns an arbitrary nonempty closed permission set. Write $m=\mathbb E b$, $v=\operatorname{Var}(b)$ and $M=m^2+v$. Under full discretion, expenditure exceeds demand by $b$ and expected human loss is $M$. Suppose $0\le b\le1-\sqrt M$ almost surely. Proposition 4 gives a common cap $q=1-\sqrt M$ that is optimal among all truthful delegation menus. Its loss is
$$
L^*=M-\frac23M^{3/2}-\frac23\mathbb E[b^3].
$$

Why does the much richer menu allow so little screening? Match each reported set to a half-line giving its designated type the same expected loss. A distance inequality shows that this replacement weakly helps the human for that type. Incentive compatibility implies that the matched caps rise with bias, while the human's favorite cap falls. A single endpoint can consequently lie between these two caps for every type, moving them all toward their respective human optima. [Prove the distance bound](06-interpretability.html#exercise-3) · [Pool the matched caps](06-interpretability.html#exercise-4) · [Compute optimal loss](06-interpretability.html#exercise-5)

## Proposition 5. Substitutes in control, complements in value

Proposition 5 varies $b=m+\sqrt v\,\xi$ for a fixed symmetric finite-support shock of mean zero and variance one. Within the admissible region, smaller $m$ means greater alignment and smaller $v$ means greater interpretability. Squared mean bias and variance trade one-for-one in the cap. Welfare also depends on the third moment. At interior points $\partial_vL^*=q-2m$, so reducing variance can even increase loss. Yet $\partial_m\partial_vL^*=-2-m/\sqrt M<0$: on admissible rectangles, reducing mean bias increases the payoff gain from reducing variance. This is the paper's distinction between substitution in the instrument and complementarity in its value. [Check the derivatives](06-interpretability.html#exercise-6) · [Choose a point on the training frontier](06-interpretability.html#exercise-7)
