# Paying for a truthful report before the signal arrives

An archive offers two operating agreements. Under one agreement, an archivist may release a scan or send it to inspection. Under the other, every scan goes to inspection. An archivist chooses its agreement before opening the file. A false report buys access to an agreement; after reading the file the archivist still decides what to do. This freedom is the reason a second cycle test is needed.

Fix finite type, state, signal and action sets. The prescribed policy $a_{ts}$ is physically feasible for type $t$, whose feasible actions form $A_t$. Its own signal probabilities are $p_t(s)$ and its posterior expected intrinsic payoff from action $a$ is $U_t(a,s)$. The relation $t\succeq j$ means $t$ can substantiate report $j$. A state-independent schedule pays for the measured action and can prohibit actions. The goal is an equilibrium with truthful reports followed by obedience. Sources: [§2.4, Proposition 2 and Tables 1–2](https://arxiv.org/html/2609.01595v1#S2.SS4), [§2.5, measurement](https://arxiv.org/html/2609.01595v1#S2.SS5).

## Exercise 1. A false report followed by a different policy

Both types can file either report and perform either action $X$ (inspect) or $Y$ (release). Both observe one of two equally likely signals, low or high. For both types, $X$ has payoff zero at either signal. The release payoff of type $A$ is $-2$ at low and $2$ at high. For type $B$ it is $1$ at either signal. Agreement $A$ recommends $X$ at low and $Y$ at high and pays a release premium $z$ relative to $X$, which pays zero. Agreement $B$ permits only $X$ and pays zero.

Find the values of $z$ that support the policy within agreement $A$. At $z=1$, compare what type $B$ earns by following $A$'s recommendation after reporting $A$ with what it can actually earn after the same report. Can fixed report bonuses induce truth here? Repeat for $z=-1$.

### Hint

Compute four numbers: each true type's expected utility under each agreement, allowing that type to choose its best action at each signal. A report bonus shifts one whole column of this matrix.

### Solution

Type $A$'s target is obedient for $-2\le z\le2$. At $z=1$ type $B$ earns $1$ on average from following $A$'s script, but earns $2$ by always releasing. Writing rows for true types $A,B$ and columns for reports $A,B$, the actual continuation-value matrix is

$$
G=\begin{pmatrix}3/2&0\\2&0\end{pmatrix}.
$$

For bonuses $c_A,c_B$, truth requires $c_B-c_A\le3/2$ for type $A$ and $c_B-c_A\ge2$ for type $B$. No bonuses work. At $z=-1$ the matrix is instead $\bigl(\begin{smallmatrix}1/2&0\\0&0\end{smallmatrix}\bigr)$. Equal bonuses implement the target in the weak equilibrium sense. Thus two schedules can both induce the right action after an honest report yet differ in their ability to elicit that report. If desired, subtract the largest permitted payment from each agreement and absorb the subtraction into its bonus.

## Exercise 2. Derive the report-cycle obstruction

Fix one schedule $r_j$ supporting each type's prescribed policy on its own report, normalized to have largest on-path payment zero. Prohibit actions outside $B_j=\{a_{js}:p_j(s)>0\}$. Derive the value $G_t(j)$ of filing report $j$ before the signal arrives. Derive a necessary inequality for any feasible closed report sequence $t_1,\ldots,t_K,t_{K+1}=t_1$. Which report edges can be omitted from the test?

### Hint

The signal law and feasible actions belong to the genuine type. Add the one-report truthfulness inequalities around the cycle.

### Solution

On a feasible report $j$, type $t$ reoptimizes after each of its signals. Its value before report constants is

$$
G_t(j)=\sum_{s:p_t(s)>0}p_t(s)\max_{a\in A_t}\{U_t(a,s)+r_j(a)\}.
$$

A report the type cannot substantiate creates no incentive constraint. If $A_t\cap B_j$ is empty, its continuation value is $-\infty$, and no finite report bonus can make that deviation profitable. Retain edges $t\to j$ with $t\succeq j$ and finite $G_t(j)$. On each edge, truth with report constants $c_t$ requires $G_t(t)+c_t\ge G_t(j)+c_j$. Cancellation of constants around the closed sequence gives condition (T):

$$
\sum_{i=1}^K\bigl[G_{t_i}(t_i)-G_{t_i}(t_{i+1})\bigr]\geq0.
$$

A one-way edge can still impose a large difference between bonuses even if it occurs on no nontrivial cycle.

## Exercise 3. Compute the prices of two reports

A type has a single signal. Report 1 permits only $X$, report 2 only $Y$, and both types can make both reports. Their intrinsic values for these actions give the continuation matrix

$$
G=\begin{pmatrix}2&4\\0&3\end{pmatrix}.
$$

Check the outer cycle. For each edge $t\to j$, compute $q(t,j)=G_t(j)-G_j(j)$. Find the maximum weight $W_t$ of any path starting at $t$, including the empty path. Compute bonuses $c_t=W_t-G_t(t)$ and verify truth directly.

### Hint

Each two-step return adds the sum of the two edge weights. Check whether repeating the trip can improve on a single edge.

### Solution

The outer cycle has truthful-minus-deviation sum $(2-4)+(3-0)=1$. The two cross-report edge weights are $q(1,2)=1$ and $q(2,1)=-2$. Self-edges have weight zero. A complete return has weight $-1$, giving $W_1=1$ and $W_2=0$. The resulting bonuses are $c_1=-1$ and $c_2=-3$. Type 1 earns $1$ after either report. Type 2 earns $0$ after report 2 and $-1$ after report 1. Truth is an equilibrium, including the tie for type 1.

## Exercise 4. Assemble Proposition 2

Prove that a feasible policy admits state-independent implementation if and only if every type passes the within-report signal-cycle test (O) and one can choose supporting schedules for which (T) holds. Explain the order of the two tests. Where does finiteness enter?

### Hint

For necessity, start with one implementing mechanism and separate each report's price schedule into a normalized schedule and a constant. For sufficiency, use $q(t,j)$ and the path construction from Exercise 3 for the whole report graph.

### Solution

Suppose a mechanism implements the policy with finite payments on prescribed actions. After report $j$, prohibit every action outside $B_j$. This preserves the truthful payoff at every signal and can only reduce the value of a deviation. Subtract the largest remaining reward $c_j$ to obtain $r_j$. Its differences support obedience, which implies (O) by [Sheet 3](03-obedience.md). The original bonuses restore report truthfulness, so Exercise 2 gives (T).

Conversely, choose normalized supporting schedules satisfying (T). For the finite-weight edges from Exercise 2, the sum of $q(t,j)$ around each cycle equals the negative of the expression in (T): the diagonal terms $G_j(j)$ simply rotate. Hence every directed cycle has nonpositive weight. Let $W_t$ be the maximum path weight starting at $t$. Deleting a cycle never decreases a path's weight, so a maximum is attained on one of finitely many simple paths (or the empty path). Prepending $t\to j$ shows $W_t\ge q(t,j)+W_j$. Pay

$$
R(j,a)=r_j(a)+W_j-G_j(j).
$$

The additive constant preserves obedience after a truthful report. Truth gives type $t$ the value $W_t$. Its best possible continuation after any admissible finite-valued report $j$ gives $G_t(j)+W_j-G_j(j)=q(t,j)+W_j\le W_t$. This proves joint truthfulness and obedience. Finite signals support the inner path argument, and finite types support its outer counterpart. Exercise 1 shows why the outer condition quantifies over a *choice* of supporting schedules.

## Exercise 5. Decide feasibility without listing all cycles

Give a linear feasibility program for a *fixed* target policy, including false reports followed by disobedience. Use reward variables only on the prescribed action set $B_j$ for report $j$. Show both directions of equivalence. How does this differ from choosing the designer's optimal policy?

### Hint

Introduce an upper bound on the largest rewarded action payoff for each pair of true type and false report and each true signal. At any feasible menu the actual maximum is the tightest such upper bound.

### Solution

For $a\in B_j$ use finite reward variables $R_{ja}$, with all other actions prohibited. At truth impose, for every $s$ in the true signal support and every $a\in A_t\cap B_t$,

$$
U_t(a_{ts},s)+R_{t,a_{ts}}\ge U_t(a,s)+R_{ta}.
$$

Set $W_t=\sum_s p_t(s)[U_t(a_{ts},s)+R_{t,a_{ts}}]$ on that support. For each admissible false report $j$ with $A_t\cap B_j\ne\varnothing$, impose

$$
D_{tjs}\ge U_t(a,s)+R_{ja}\quad(a\in A_t\cap B_j),
\qquad
W_t\ge\sum_s p_t(s)D_{tjs}.
$$

Once the target is fixed all constraints are linear. An implementing menu yields feasible variables by taking $D$ equal to the corresponding maxima. In the other direction, the first inequalities guarantee obedience and every possible continuation after a false report is bounded by the last inequalities. The number of variables and constraints is polynomial in the explicitly listed finite inputs, giving polynomial-time feasibility for rational data in the usual bit model. Optimizing over policies changes the entries $a_{ts}$ themselves. Enumerating them can require exponentially many runs even when one run is short.

## Exercise 6. Recover static screening and identify the role of measurement

First suppose every type can file every report and perform every action, and there is no new information after reporting. There is then one assigned action $a_t$ per type and an expected payoff $\bar U_t(a)$ under that type's own state belief. Reduce (T) to static cyclical monotonicity. If $\bar U_t(a)=t\cdot a$, identify a convex function that supports the assigned actions. Describe the other three combinations of observed/private type and presence/absence of an interim signal.

Next imagine that the archive can measure an action only as $M(a)$ and the state only as $N(\theta)$. Give an example in which this coarsening prevents a desired action. How do the nine possibilities in the paper's measurement taxonomy follow by varying the two maps from constant, to coarse, to exact?

### Hint

With no new signal, a singleton action menu reduces a misreport to swapping one assignment for another. With a coarse instrument, compare two actions with the same measured label.

### Solution

With singleton menus and zero normalized rewards, $G_t(j)=\bar U_t(a_j)$. For every cycle the test is $\sum_i[\bar U_{t_i}(a_{t_i})-\bar U_{t_i}(a_{t_{i+1}})]\ge0$. Under linear payoffs and truthful bonuses $c_j$, define $F(x)=\max_j(x\cdot a_j+c_j)$. It is convex; the $t$-indexed affine function attains the maximum at $x=t$. Thus $a_t\in\partial F(t)$. If type is observed, the report test disappears: with one signal any feasible assigned action can be the sole permitted action; with several signals the inner obedience test remains. A private type with an informative signal requires both tests.

For a fixed report the measured reward has the form $R(M(a),N(\theta))$. If immediate release and release after a quality check are both logged simply as “release,” their rewards are identical in each state. An agent that strictly prefers skipping the check under every state belief cannot be induced by this reward to perform it. Reading the measurement taxonomy one row at a time gives the following instruments.

- With no action measurement the reward is constant in the action. As state observation improves from absent to coarse to exact, rewards go from report-dependent constants to scores on a state label to scores on the state itself. A proper score for a state label can distinguish beliefs only through their induced law on that label.
- With a coarse action label, the designer can price that label alone, price a pair of coarse labels, or price each action label separately in every state.
- With exact actions, the designer can price actions alone (the setting of Proposition 2), price actions conditional on a state label, or price each action–state pair separately. In the fully informed finite example with a common feasible target $a^*(\theta)$, prohibiting all pairs with $a\ne a^*(\theta)$ implements the statewise first best. Implementing a state-dependent action also requires the agent to have the information and physical capability to execute it.
