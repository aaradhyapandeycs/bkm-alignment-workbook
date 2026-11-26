# Why implementability takes two cycle tests

An archivist chooses a contract before opening a document. Once the document is open, the archivist sees a signal about its contents and chooses whether to release it. The archive can observe the release decision but cannot condition the reward on the underlying state. Can it implement a prescribed map from each type and signal to an action? For a deterministic, physically feasible policy on finite spaces, the paper answers this question exactly.

## Lemma 1. Signal-policy cyclical monotonicity

Fix the true type and suppress its index. At each positive-probability signal $s$, let $U(a,s)$ be the agent's posterior expected intrinsic payoff and $a_s$ the prescribed action. At a state-independent reward $r$, obedience requires $U(a_s,s)+r(a_s)\ge U(a,s)+r(a)$ for every available $a$. The designer can prohibit actions outside the range of prescribed actions. Within that range, let $w(s,s')=U(a_{s'},s)-U(a_s,s)$, the gain from swapping to the action prescribed at $s'$. Obedience now requires $r(a_s)-r(a_{s'})\ge w(s,s')$.

Adding these inequalities around a closed loop cancels the rewards. Lemma 1 says that requiring $\sum w(s,s')\le0$ on every directed signal cycle suffices as well. To see it, let $V(s)$ be the maximum weight of a path starting at $s$, with the empty path allowed. Deleting a nonpositive cycle can only improve a path, so a finite graph has a finite maximum. Prepending an edge gives $V(s)-V(s')\ge w(s,s')$. Signals prescribing the same action have zero-weight edges in both directions and therefore have the same $V$. Taking $r(a_s)=V(s)-\max_q V(q)$ gives an actual reward on actions. [Build the reward from a graph](03-obedience.html#exercise-4).

There is a transport interpretation. Give signal $s$ its probability $p_s$ and action $a$ its prescribed frequency $m_a=\sum_{s:a_s=a}p_s$. The prescribed assignment must maximize the expected surplus $U(a,s)$ among couplings of these marginals. Indeed, adding $r(a)$ changes every coupling's value by the same $\sum_a m_ar(a)$, and obedience maximizes the augmented surplus at each signal. Conversely a positive-gain cycle would improve the coupling by rerouting a small equal mass through each edge, keeping both marginals fixed. This is a way to read the lemma; the paper states it as a signal-cycle condition. [Work out the coupling argument](03-obedience.html#exercise-5).

## A false report buys the whole contract

Choose a normalized supporting schedule $r_j$ for each type's prescribed policy, paying $-\infty$ off its prescribed range. If $t$ reports $j$ and can execute a permitted action, its best continuation value is
$$
 G_t(j)=\sum_{s:p_t(s)>0}p_t(s)\max_{a\in A[t]}\{U_t(a,s)+r_j(a)\}.
$$

The maximum is inside the signal average because the action comes after the reading. The choice of $j$ comes before it. The same $r_j$ can look quite different in another agent's hands. In the archive example, a schedule that induces the intended release rule in type A also pays type B to release *every* file. Lowering the release premium can preserve A's behavior while making a false report less attractive to B. [Compute both continuation matrices](04-nested-cycles.html#exercise-1).

## Proposition 2. Cycle characterization

A constant $c_j$ attached to report $j$ leaves its internal action incentives intact. To induce honesty we need
$$
 c_t-c_j\ge G_t(j)-G_t(t)
$$
on each permitted report edge $t\to j$ with finite continuation value. A report under which no permitted action is executable offers $-\infty$ and cannot give a finite improvement. Summing the displayed inequalities around any remaining directed type cycle gives $\sum_{t\to j}[G_t(j)-G_t(t)]\le0$. As in the signal graph, longest-path potentials supply the constants if this test holds. The final reward is $c_j+r_j(a)$.

Proposition 2 includes an existence quantifier: the signal conditions must hold, and **some** choice of supporting schedules must pass the type-cycle test. A failed outer test for one arbitrarily chosen collection cannot establish impossibility. Together the two conditions characterize state-independent implementation in the finite model. They also yield a feasibility problem for a specified target policy. [Reconstruct Proposition 2](04-nested-cycles.html#exercise-4) and [derive a linear program](04-nested-cycles.html#exercise-5).

## What the designer can measure

If the state can be verified, a contract can pay for a pair $(a,\theta)$ and change incentives state by state. If only coarse labels of the state and action are observable, two actions with the same label earn identical rewards in every state for a fixed report. A designer who can distinguish “release” from “withhold” but cannot observe an internal quality check has fewer instruments than one who records all three decisions. These distinctions organize §2.5 and determine when the state-independent cycle theorem applies. [Trace the nine measurement cases](04-nested-cycles.html#exercise-6). [Original paper, §§2.4–2.5](https://arxiv.org/html/2609.01595v1#S2.SS4)
