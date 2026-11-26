# Paying an agent for predicting its peer

Two reviewers choose whether to release a catalog. Each would enjoy pressing the release button. The editor wants release only when both private checks were favorable. The editor can record both reports and both buttons, but learning the true quality of the catalog could take weeks. Can one reviewer’s report help discipline the other? The distinction between forecasting an honest peer and simply agreeing with a peer drives this sheet.

We begin with the binary instance of Example III, use it to build Proposition 7 for a finite supported type model, and then test its assumptions. [Bergemann, Koh and Morris, Section 5, Example III](https://arxiv.org/html/2609.01595v1#S5)

## Exercise 1. A low report predicts a high peer

Let $\theta\in\{0,1\}$ be fair. If $\theta=1$ the types are $(H,H)$. If $\theta=0$ the ordered pair is equally likely to be $(H,L)$ or $(L,H)$. Each agent sees its own type and learns nothing further before acting. The common prior is as given. Compute each type's conditional law of the other type, with coordinates ordered $(H,L)$. Compute also its conditional probability of $\theta=1$. Each reviewer chooses a bit and likes its own bit to equal one. Which rule earns the editor a unit payoff for both actions being correct?

### Hint

The unconditional probability that your own type is $H$ is $3/4$. Seeing $L$ leaves only one possible peer type.

### Solution

For either agent, the peer forecast given $H$ is $p_H=(2/3,1/3)$ and that given $L$ is $p_L=(1,0)$. The state probabilities of one are respectively $2/3$ and zero. Although a single $H$ leaves doubt, the joint type determines the state. With truthful reports, recommend action $b=1$ to both agents at $(H,H)$ and $b=0$ otherwise. This yields human payoff one with certainty if both agents obey. A bonus for matching the peer's report would give an $L$ type a reason to say $H$.

## Exercise 2. Derive the scoring rule and fill the ledger

For a reported forecast vector $q$ on a finite set $Y$ and a realized peer report $y$, define $S(q,y)=2q(y)-\sum_{z\in Y}q(z)^2$. If the genuine forecast is $p$, find the expected loss from submitting $q$ instead. In Exercise 1 compute the score for each of the four ordered pairs (own report, peer report), and each type's expected scores for truth and a lie.

### Hint

Complete the square in $2\langle p,q\rangle-\|q\|_2^2$. For a peer forecast $(2/3,1/3)$ the sum of squares is $5/9$.

### Solution

The expected score equals $\|p\|_2^2-\|p-q\|_2^2$. Truth maximizes it strictly whenever a different report represents a different forecast. An $H$ report scores $7/9$ against $H$ and $1/9$ against $L$. An $L$ report scores $1$ against $H$ and $-1$ against $L$.

With an honest peer, an $H$ type's expected scores are $5/9$ for truth and $1/3$ for a lie. An $L$ type's corresponding scores are $1$ and $7/9$. Both lose $2/9$, the squared Euclidean distance of the two forecast vectors. An individual draw can reward a lie more highly. The incentive calculation uses the expected score at the time of reporting.

## Exercise 3. Forecasts alone do not move the buttons

Suppose agent $i$'s private utility is $a_i$ and its feasible actions are $0,1$. Let the target $b(h)$ at reports $h$ be as in Exercise 1. First suppose an agent is paid only a positive multiple $\Lambda$ of its score, independently of the buttons. What will it do when $b(h)=0$? Now construct a reward schedule that enforces the recommendation and induces honesty. Does the schedule for this particular example require the editor to observe the state?

### Hint

Make the total payoff on the recommended action profile equal to the peer score. Use the paper's allowance of an extended-real penalty elsewhere.

### Solution

If the reward is independent of the action, switching one's own bit from zero to one gains one unit. Instead, when both buttons equal $b(h)$ pay each $i$ the amount $\Lambda S(p_{h_i},h_j)-a_i$, and pay $-\infty$ otherwise. If the peer follows its recommendation, choosing the prescribed bit gives the finite score and choosing the opposite bit incurs the penalty. This holds after either feasible report. Reporting honestly then gains $2\Lambda/9$ over the alternative, so any $\Lambda>0$ works. The editor's state-contingent objective is attained using the observed reports and buttons. No payment here depends on $\theta$.

## Exercise 4. Which beliefs can a peer report distinguish?

For each $i$, let $T_i^0$ be the finite marginal support of its type under the designer's distribution $\Gamma$. Write $p_i(t_i)$ for its subjective probability vector on $Y_i=\prod_{j\ne i}T_j^0$. Assume the type assigns all its peer-type probability to this product. Suppose two own types give distinct predictions about $\theta$ but the same vector $p_i$. Can a function of these two candidate reports and a single truthful peer profile make honesty strictly optimal for both through the scoring term alone? Now assume $p_i$ is injective on $T_i^0$ for every $i$. Why is there a single positive separation for all distinct supported pairs?

### Hint

For the first question, compare the expected score difference for the two possible genuine types. For the second, consider squared Euclidean distances on each finite peer alphabet.

### Solution

For two reports $t,h$ with the same peer prediction $p$, the expected score advantage of reporting $t$ instead of $h$ is the same number for both genuine types, namely $\sum_y p(y)[S(t,y)-S(h,y)]$ for any proposed peer-only score $S$. It cannot be strictly positive for one type and strictly negative for the other. This applies even when the joint beliefs on $(\theta,t_{-i})$ are different. The marginal on the observable peer reports drives the test.

If there is at least one distinct pair, the finite minimum
$$
\delta=\min_{i,\ t,h\in T_i^0,\ t\ne h}\|p_i(t)-p_i(h)\|_2^2
$$
is positive by injectivity. If every marginal support is a singleton, there is no supported misreport to deter. An infinite collection of different forecasts can have arbitrarily small distances. For example, the Bernoulli probabilities $1/2+1/(4k)$ are all different for integer $k\ge1$, while neighboring vectors approach each other.

## Exercise 5. Derive the reward for an arbitrary feasible target

Use at least two agents. The primitive action and state sets are finite, the supported own types are finite, and private utilities $u_i[t_i](a,\theta)$ are real-valued. Assume belief closure and peer separation as in Exercise 4. Any own type can claim any report. Let $\gamma(h)$ draw private plans conditional on report profile $h$, each feasible for its reported type. Define $K_\theta(h)$ as the support of the resulting played action profile when the plan draw is evaluated at signals from $\pi(\cdot\mid\theta,h)$. Even at a report profile with zero designer probability, these kernels are specified.

Find a transfer using only the reported types, the actual action profile, and the state that implements $\gamma$ on the supported types. Give a bound on the scale sufficient against a joint report-and-action deviation. Distinguish the uses of belief closure, separation, and action feasibility in your proof.

### Hint

On $K_\theta(h)$ cancel the reported private utility. Ask what part of the true utility survives when the reported type differs from the true type. A uniform bound can ignore whether every conceivable action is attainable by the deviation.

### Solution

On a profile of individually supported reports and for $a\in K_\theta(h)$, set
$$
r_i(h,a,\theta)=\Lambda S(p_i(h_i),h_{-i})-u_i[h_i](a,\theta).
$$
Give $-\infty$ otherwise. At truth all peer reports are in the supported alphabet almost surely by belief closure. The prescribed plan is feasible, and under the true signal kernel obedience lands in $K_\theta(t)$ almost surely. Private utility cancels there. Any action under a truthful report that stays on target earns the same score. An action putting positive probability on the forbidden set gives expected payoff $-\infty$. Thus obedience is optimal.

Let $M$ be the largest absolute discrepancy $|u_i[t_i](a,\theta)-u_i[h_i](a,\theta)|$ across all players, supported own-type pairs, action profiles and states. Finiteness guarantees $M<\infty$. A report outside $T_i^0$ is always penalized. For a supported lie followed by any action rule that gives finite expected payoff, the score loses at least $\Lambda\delta$ in expectation because peers report their true types. The discrepancy in intrinsic utility and its cancellation can recover at most $M$, even if the deviator uses everything learned from its private plan and true signal. The gain over truth is at most $M-\Lambda\delta$. Choosing $\Lambda\ge M/\delta$ gives weak incentives and choosing a strict inequality makes every supported false report strictly worse. If there are no distinct pairs, omit this bound. This proves Proposition 7 under its support-wise criterion.

The proof uses the agents' own peer forecasts. They need not coincide with the designer's conditional beliefs. The general cancellation and support test can require verifiable state-dependent payments even though Exercise 3 avoided them. An unbounded scoring scale and exclusion penalties are part of this benchmark.

## Exercise 6. What does the implementation guarantee?

Keep Exercise 1's type law and utilities, but let a new rule $\gamma$ draw the two recommended action bits independently and fairly at every report profile, with the same rule in both states. Both actions are feasible for both types, and there are no further signals. Apply Exercise 5's mechanism. Do truthful reports followed by obedience form an equilibrium? Can the same mechanism have a different equilibrium outcome even when supported reports strictly prefer honesty against truthful peers?

### Hint

Determine $K_\theta(h)$. Once private utility is canceled, examine the payoff from any played action profile.

### Solution

The target support is $\{0,1\}^2$ for every $h,\theta$. Thus every action profile leads to exact cancellation and the only remaining payoff is the report score. Against a truthful peer both types strictly prefer honesty for any $\Lambda>0$. Playing the recommended bits is a best response, so the independent fair actions are attained in equilibrium.

There is also an equilibrium in which both agents tell the truth and always play zero. The reports remain optimal and every action is a best response at every recommendation. Its action distribution is a point mass. The theorem constructs one truthful and obedient equilibrium for the target, and the proof enforces membership of the permitted support. A claim about the distribution in every equilibrium would require another argument.
