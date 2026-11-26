# Turn a conversation into a contingent plan

A dispatcher emails a route card to a courier. Some cards say to take the north road if the bridge is open and the south road otherwise; other cards send the courier south in both cases. The courier receives the card before seeing the bridge status. If a reply were compressed to “go south,” which instruction had the dispatcher sent? A whole contingent plan is the right object to send before the courier's private observation.

Work with finite alphabets to see the proof by sums. In the paper the input and reply spaces may be Borel spaces, the rules and strategies are measurable, and a stochastic reply rule is a probability kernel. The same proof takes the image of that kernel under a measurable map to plans. [Bergemann, Koh and Morris, §2.3 and Proposition 1](https://arxiv.org/html/2609.01595v1#S2.SS3)

## Exercise 1. Forget everything about the envelope except its instructions

An indirect mechanism has input messages $x\in X(t)$ available to type $t$, a reply $y$ with law $\rho(\cdot\mid x)$, and a reward $R(x,a,\theta)$ based on the input, action and state. The agent first sends $x$, observes $y$, privately learns $s$, then picks an action in $A[t]$. For one type and one input, suppose the reply is uniform on four envelopes. The first two induce plan $p(s)=s$, the third $p(s)=0$, and the fourth $p(s)=1$, where $s\in\{0,1\}$. The binary signal agrees with the binary state with probability $4/5$ in either state. Compute the law on plans and $\Pr(a=1\mid\theta)$ under these instructions. Would sending the plans in unmarked envelopes change the answers?

### Hint

A plan is a function on the entire signal alphabet. Two differently marked envelopes can contain the same function.

### Solution

The identity plan has probability $1/2$ and the two constant plans have probability $1/4$ each. At state $1$ the probability of taking action $1$ is $(1/2)(4/5)+1/4=13/20$. At state $0$ it is $(1/2)(1/5)+1/4=7/20$. Sending only the plan gives the same two conditional probabilities. Here the envelope draw is independent of the state given the input. If the courier has zero intrinsic utility and zero rewards, following these instructions is one equilibrium, so this calculation can also describe an equilibrium outcome. In the general reduction, different labels can carry incentives through the induced continuation behavior; the exercise below starts from a specified equilibrium to identify that behavior.

## Exercise 2. Build a profitable double deviation

A direct mechanism accepts a report $j\in C(t)$ and sends a random plan $p:S\to A$ with law $\gamma(j)$. Assume one signal, one state, and two types. $L$ can only execute $a$, while $H$ can execute $a$ or $b$. Type $H$ may report either type; $L$ can only report $L$. Both recommendations say to take $a$, and intrinsic utilities vanish. The rewards on the $H$ report are $r(H,a)=0$, $r(H,b)=-1$. On the $L$ report they are $r(L,a)=-1$, $r(L,b)=2$. Check (i) disobedience following a truthful report and (ii) misreporting while still obeying. Then test the full incentive constraint.

### Hint

Physical feasibility in the last stage uses the true type even when a different type was reported. A recommendation places no physical barrier in front of an alternative action.

### Solution

For $H$, obeying earns zero and truthful disobedience earns $-1$. Reporting $L$ and obeying earns $-1$. For $L$ there is no alternate action or report. Yet $H$ can report $L$ and choose $b$, earning $2$. This deviation is feasible even though an actual $L$ could never earn the reward attached to $b$. A contract designer could remove this particular deviation by setting $r(L,b)=-\infty$; the published definition permits such prohibitions. What the example establishes is that the two restricted checks cannot establish incentive compatibility of the contract as written.

## Exercise 3. Write the entire deviation in one inequality

For a finite state and signal model, assume finite rewards in this exercise. Let $t$ be the true type, with prior $h[t]$, signal experiment $\pi[t]$, utility $u[t]$, and action set $A[t]$. A report $j$ selects $\gamma(j)$ and $r(j,a,\theta)$. Define the truthful-and-obedient value $V_t$. Derive one inequality that tests an arbitrary feasible report and plan-dependent action rule $d$. Then condition on the recommendation and positive-probability signals to simplify the optimal deviation payoff. What does this say about obedience on the truthful report?

### Hint

The agent can reoptimize for each pair $(p,s)$ after choosing one report $j$ before learning either. A reward in this question may depend on the state.

### Solution

Define $m_t(\theta,s)=h[t](\theta)\pi[t](s\mid\theta)$ and $g_{tj}(a,\theta)=u[t](a,\theta)+r(j,a,\theta)$. Then
$$
V_t=\sum_{\theta,s,p}m_t(\theta,s)\gamma(t)(p)g_{tt}(p(s),\theta).
$$

For every $j\in C(t)$ and every $d$ with $d(p,s)\in A[t]$, require
$$
 V_t\ge \sum_{\theta,s,p}m_t(\theta,s)\gamma(j)(p)g_{tj}(d(p,s),\theta).
$$

Let $m_t(s)=\sum_\theta m_t(\theta,s)$. For $m_t(s)>0$ define $B_{tj}(a,s)=\sum_\theta m_t(\theta,s)g_{tj}(a,\theta)/m_t(s)$. The plan is drawn using $j$ independently of the state and the true signal. For a fixed report, maximize separately at each positive-probability $(p,s)$. Since the reward has no additional dependence on $p$, the best value simplifies to $\sum_s m_t(s)\max_{a\in A[t]}B_{tj}(a,s)$ with zero-mass signals omitted. In particular, under the truthful report each recommended $p(s)$ must maximize $B_{tt}(\cdot,s)$ for every pair of positive mass. Otherwise changing one action there strictly raises the interim payoff. This reasoning also shows why maximizing first over reports separately at each signal would give the agent information it lacks.

## Exercise 4. Construct the direct mechanism from an equilibrium

Fix a measurable pure equilibrium of an arbitrary indirect mechanism. Write $x(t)$ for the equilibrium input and $\alpha(t,x,y,s)$ for its continuation action. Assume $t\trianglerighteq j$ implies $X(j)\subseteq X(t)$. Construct a direct rule $\gamma(j)$ and rewards $r(j,a,\theta)$ from these data. Prove action feasibility, equality of the joint law of $(\theta,t,a)$, and incentive compatibility. Keep track of which type each expression uses when $t$ imitates $j$.

### Hint

Use the indirect reply as a private random seed for generating a plan. For incentive compatibility, an agent deviating in the indirect mechanism is allowed to compute what that plan would have been.

### Solution

After receiving $j$, the designer draws $y$ from $\rho(\cdot\mid x(j))$ and forms the plan
$$
 p_{j,y}(s)=\alpha(j,x(j),y,s).
$$

Use its image law as $\gamma(j)$, and set $r(j,a,\theta)=R(x(j),a,\theta)$. The recommended action belongs to $A[j]$ for each signal, by feasibility of the original strategy. Under truth and obedience one may couple the direct and indirect mechanisms using the very same $(\theta,t)$, true signal $s$, and reply $y$. In both the played action is $\alpha(t,x(t),y,s)$. This proves equality of the whole joint outcome law under the designer's $\Gamma$, including any dependence between types and states.

For any direct deviation $(j,d)$ of true type $t$, the corresponding indirect deviation sends $x(j)$. This input is available since $x(j)\in X(j)\subseteq X(t)$. Upon seeing the reply it constructs $p_{j,y}$ and plays $d(p_{j,y},s)\in A[t]$. The true signal still follows $\pi[t]$ and the payoff uses $u[t]$. The constructed strategy has exactly the direct deviation's value under $h[t]\pi[t]$. The original equilibrium already bounds this value by the truthful path payoff. Since this works for every $(j,d)$, truth and obedience are optimal in the constructed mechanism.

## Exercise 5. Recover the converse and identify what is implemented

Let $\mathcal O$ consist of all joint laws of state, type and action arising in some equilibrium of some indirect mechanism. Let $\mathcal O^{\rm IC}$ collect the laws from truthful and obedient play of action-feasible, incentive-compatible direct mechanisms. Turn any such direct mechanism into an indirect one. Where do reflexivity and transitivity enter? Deduce Proposition 1 and write the designer's optimization problem. Finally, give a direct example where another equilibrium delivers a different human payoff.

### Hint

Use the same objects with different names. Check the indirect rule's *input-menu monotonicity* before invoking the definition of equilibrium.

### Solution

Choose $X=\mathbb T$, $X(t)=C(t)$, $Y=A^S$, $\rho(\cdot\mid j)=\gamma(j)$ and $R(j,a,\theta)=r(j,a,\theta)$. Reflexivity makes $t$ available to type $t$. If $t\trianglerighteq j$ and $k\in C(j)$, then $t\trianglerighteq k$ by transitivity, so $C(j)\subseteq C(t)$. The indirect input menus are therefore admissible. The original incentive inequality bounds every alternative input and continuation rule. Consequently truth and obedience give an indirect equilibrium with the required law, proving $\mathcal O^{\rm IC}\subseteq\mathcal O$. The construction in Exercise 4 proves the reverse inclusion.

Thus the designer can optimize $\sup_{(\gamma,r)}\mathbb E[v(a,\theta)]$ over action-feasible, incentive-compatible direct mechanisms, with expectations under the truthful law. The rewards enter the agent's payoff; the paper specifies the human's payoff as $v(a,\theta)$. For an example of multiplicity take a single state, signal and type, actions $0,1$, and human payoff $v(a)=a$. Give the agent zero utility and zero rewards for both actions. Recommend $1$. Obedience is optimal and delivers human payoff one, while always taking $0$ is also an equilibrium and delivers zero. Equality of the sets of attainable laws is a partial implementation statement. Guaranteeing a target in every equilibrium would require a different argument.
