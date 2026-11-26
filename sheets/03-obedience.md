# Paying for an action when the signal is private

A digital archivist must decide whether to release a scanned manuscript or hold it for inspection. Its private quality check can distinguish a readable scan from a corrupted one. The library can see the release decision. No accountant sees the quality check. Can a single price for releasing the file induce the archivist to use its information in the way the library wants?

Throughout this sheet the agent's type is fixed. The agent maximizes its own conditional expected intrinsic payoff plus an action reward. There are finitely many states, signals and actions. Partial implementation permits ties: the desired action must be an optimal choice at each signal of positive probability. Source: [Bergemann, Koh and Morris, §2.4, Lemma 1](https://arxiv.org/html/2609.01595v1#S2.SS4).

## Exercise 1. Price the release decision

The archivist assigns probability $2/3$ to a readable scan. A positive quality check occurs with probability $3/4$ if the scan is readable and $1/4$ otherwise. Holding pays zero. Releasing pays $3$ for a readable scan and $-3$ otherwise. Compute the archivist's posterior beliefs and expected release payoffs. Find every release premium $\delta=r(\mathrm{release})-r(\mathrm{hold})$ that induces release after a positive check and hold after a negative check. Could a premium ever induce the reverse assignment?

### Hint

A reward paid regardless of the state enters both conditional release values with the same coefficient.

### Solution

The positive check has probability $7/12$, of which $1/2$ comes from readable scans. Its posterior probability of readability is $6/7$. The negative check has probability $5/12$, of which $1/6$ comes from readable scans, so its posterior is $2/5$. With posterior $\pi$, release earns $6\pi-3$ before rewards. The two conditional values are $15/7$ and $-3/5$. The desired behavior requires

$$
-15/7\leq\delta\leq 3/5 .
$$

At either endpoint one signal leaves the agent indifferent. Reversing the assignment would require simultaneously $\delta\leq-15/7$ and $\delta\geq3/5$. The archivist's response to quality evidence rules out this particular policy at every state-independent price.

## Exercise 2. A profitable loop cancels every proposed price

Let $S$ be the support of the type's signal law, $A$ its feasible actions, $U(a,s)$ its expected intrinsic payoff conditional on signal $s$, and $a_s\in A$ the recommendation. Define the gain from switching at $s$ to the action for signal $t$ by $w(s,t)=U(a_t,s)-U(a_s,s)$. Show that a reward paid as a function of action can support the recommendation only if, for every closed sequence $s_1,\ldots,s_K,s_{K+1}=s_1$,

$$
\sum_{i=1}^K w(s_i,s_{i+1})\leq 0 . 
$$

In the archivist example, what is the two-edge cycle gain for the reverse assignment?

### Hint

Write down one obedience inequality at each node of the loop. Every price on the left of one inequality appears on the right of another.

### Solution

Obedience requires $r(a_s)-r(a_t)\geq w(s,t)$. The sum of the left sides around a closed sequence is zero, giving the claimed inequality. This is condition (O) of the paper, expressed in deviation gains. For the reverse assignment, the agent switches from holding to releasing after a positive check, gaining $15/7$, and from releasing to holding after a negative check, gaining $3/5$. Their sum is $96/35>0$. The two terms are evaluations at different signals. The argument adds hypothetical deviations to eliminate the unobservable prices; it does not require both signals to occur in one play.

## Exercise 3. Why checking every swap can miss a contradiction

Three signals $1,2,3$ are perfectly informative about three corresponding states. The desired actions are $A,B,C$, respectively. In rows ordered by signal and columns by action the agent's intrinsic payoffs are

$$
\begin{pmatrix}
0&2&-3\\
-3&0&2\\
2&-3&0
\end{pmatrix}.
$$

Check every two-signal cycle. Find one cycle that decides whether the target is implementable. Would knowing the probabilities of the three signals change this calculation if each has positive probability?

### Hint

From each diagonal entry, find the action that gives $2$ more. Follow those three arrows.

### Solution

Each unordered pair of signals has a two-cycle of total gain $2-3=-1$. All three swaps pass. But the loop $1\to2\to3\to1$ gives $2+2+2=6$. Adding its three obedience inequalities would give $0\geq6$. The test is conditional on each signal, so changing positive signal probabilities leaves this contradiction intact. Removing a signal from the support would remove its obedience inequality.

## Exercise 4. Recover an actual reward from the inequalities

Assume every signal cycle has nonpositive total gain. Construct a supporting price using paths, allowing the empty path. Resolve the following practical difficulty: two different signals can recommend the same action, and the library pays for an action only once. Specify the reward on actions never recommended.

### Hint

Let $V(s)$ be the largest path weight for a path *starting* at $s$. Prepend an edge to a path attaining $V(t)$. Examine both directed edges between signals with identical recommendations.

### Solution

Deleting a repeated-node subpath deletes a nonpositive cycle and weakly increases the weight. A maximum therefore exists among the finitely many simple paths, including the empty path of weight zero. Prepending $s\to t$ to an optimal path from $t$ gives $V(s)\geq w(s,t)+V(t)$. If $a_s=a_t$, the two directed edges between these signals each have weight zero. Their inequalities imply $V(s)=V(t)$.

Set $r(a_s)=V(s)-\max_{t\in S}V(t)$ on recommended actions and prohibit every other action by assigning reward $-\infty$. This is a single well-defined reward per action. For every $s,t$ the difference in rewarded payoffs favoring $a_s$ over $a_t$ equals $V(s)-V(t)-w(s,t)\geq0$. Prohibition eliminates all other deviations. Together with Exercise 2 this proves both directions of Lemma 1. The upper normalization of zero is a convention; adding one constant to all permitted rewards has no effect on obedience.

## Exercise 5. Interpret the signal cycle as a transport test

This exercise gives a finite optimal-transport interpretation of Lemma 1. Write $p_s>0$ for signal probabilities and $m_a=\sum_{s:a_s=a}p_s$ for the induced action frequencies. A *coupling* is a nonnegative matrix $\pi_{sa}$ with row sums $p_s$ and column sums $m_a$. Show that if the policy is supported by prices, its deterministic coupling $\pi^0_{sa}=p_s\mathbf1_{\{a=a_s\}}$ maximizes

$$
\sum_{s,a}\pi_{sa} U(a,s)
$$

over couplings with these marginals. Conversely, turn a positive-gain cycle into a competing coupling with higher payoff. Explain why this test does not require the agent to see anyone else's signal.

### Hint

An action price has the same expectation under every coupling with the same column sums. To construct a competitor, circulate a little mass between the recommended actions of the signals on a cycle.

### Solution

Restrict columns to $m_a>0$. At each $s$ the point mass on $a_s$ maximizes the rewarded payoff in its row. Multiplying by $p_s$ and summing, the deterministic coupling beats any competing coupling in rewarded payoff. The reward terms on both sides equal $\sum_a m_a r(a)$, which proves optimality for intrinsic payoff.

If a positive-gain cycle exists, deleting or splitting repeated-node segments yields a simple positive-gain cycle. Choose $\epsilon>0$ no larger than its smallest signal mass. In each cycle row $s_i$ redirect $\epsilon$ from $a_{s_i}$ to $a_{s_{i+1}}$. Every column receives exactly as much mass as it loses, including when several signals use the same action. The gain equals $\epsilon\sum_i w(s_i,s_{i+1})>0$. Thus transport optimality rules out positive cycles, and Exercise 4 recovers supporting prices. The coupling is an analyst's comparison of assignments with the same frequencies. The actual agent simply observes its own signal and chooses its own action.
