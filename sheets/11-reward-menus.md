# Who writes the monitor's menu?

An inventory reviewer knows how far the forecaster tends to overorder. A menu offers the reviewer one scoring rule for each possible diagnosis. If the reviewer chooses the honest diagnosis, the order should track demand. The difficulty is that the reviewer also likes a slightly fuller warehouse. Can the menu make honest diagnosis optimal for every reviewer in a known bias range?

This sheet reconstructs the design and the strict incentive argument of Proposition 10. The last exercise tests which features of the prior do work in the proof. [Bergemann, Koh and Morris, §5, Example V](https://arxiv.org/html/2609.01595v1)

As in the preceding sheet, demand is $\theta\sim U[0,1]$, independent of the actor's bias $b$ with law $\tau$ and finite second moment. The actor selects a real action after seeing the score and the state. It maximizes $-(a-\theta-b)^2+r(a)$. The reviewer selects the score after seeing $b$ and before seeing $\theta$; its squared loss is $(a-\theta-w)^2$. The human wants $a=\theta$, can commit before the diagnosis, and knows a bound $|w|\le B$. There is a fixed actor tie-break. Scores may exclude actions by assigning $-\infty$.

## Exercise 1. Diagnose the temptation

Suppose every admissible report $h\in\operatorname{supp}(\tau)$ selects the affine schedule $r_h(a)=-2ha$ on the whole line. Which report would the monitor choose if $b-w$ were available? Now restrict the ordinary actions to $[0,1]$ under this schedule. With $b=0.3$, $w=0.1$ and reports $0.2,0.3$ both available, compute the monitor's expected loss for both reports.

### Hint

On the whole line the actor chooses $\theta+b-h$. On the interval the actor chooses the nearest point in $[0,1]$ to this target.

### Solution

On the line the monitor loses $(b-h-w)^2$. Reporting $h=b-w$ achieves zero; reporting $h=b$ costs $w^2$. On the interval honest reporting still costs $0.01$. Reporting $0.2$ instead yields precisely $\theta+0.1$ up to state $0.9$. Beyond that the action is $1$, with error $0.9-\theta$ for the monitor. Its expected loss is $\int_{0.9}^1(\theta-0.9)^2d\theta=1/3000$. Truncation changes the payoff to a false report; a strict incentive to understate remains in this example.

## Exercise 2. Calibrate two isolated actions

Choose a distance $R>0$ and add two possible actions, $1+R$ and $-R$, to the interval of ordinary actions. Keep reward $-2ha$ on $[0,1]$. Set a reward on $1+R$ that makes the actor indifferent between $1$ and $1+R$ precisely when the residual target $z=\theta+b-h$ equals $1$. Do the same at the lower end.

### Hint

Look for a schedule of the form $r_h(a)=-2ha+\text{bonus}(a)$. At $z=1$ the isolated upper action is at distance $R$ from the actor's residual target.

### Solution

Completing the square drops a term independent of the action, leaving $-(a-z)^2+\text{bonus}(a)$. Both extremes should earn bonus $R^2$. Give every other action outside the interval reward $-\infty$. Writing $K=[0,1]\cup\{-R,1+R\}$ gives the compact formula

$$
r_h(a)=
\begin{cases}
-2ha+R^2\mathbf 1_{\{a=-R\ \mathrm{or}\ a=1+R\}},&a\in K,\\
-\infty,&a\notin K.
\end{cases}
$$

The finite part is continuous in the relative topology on the compact set $K$, so for every state and every true bias a maximizing action exists. Each $h$ therefore indexes an admissible **state-independent** instrument. Its two bonuses are calibrated to the actor's payoffs; the monitor incurs no direct transfer.

## Exercise 3. Solve the actor's problem globally

For each residual target $z$, identify the actor's maximizing action, including the ties. For $R=0.8$, $b=0.3$, $h=0.2$, what are the actions at $\theta=0.82$ and $\theta=0.97$? Under the uniform state law, compute the probability of taking an extreme for arbitrary $b,h$.

### Hint

Compare the upper extreme with $1$ and the lower extreme with $0$. Then compare the ordinary actions by projection.

### Solution

The upper extreme's payoff advantage over $1$ is $2R(z-1)$; the lower extreme's advantage over $0$ is $-2Rz$. For $0<z<1$, the ordinary action $a=z$ beats every other ordinary action and both extremes. If $z>1$, action $1$ is best among ordinary actions and the upper extreme strictly beats it. The lower extreme loses to $0$. Thus $a=1+R$. The reflected argument gives $a=-R$ for $z<0$. At $z=1$ the maximizers are $1,1+R$, and at $z=0$ they are $0,-R$.

In the example the residual targets are $0.92$ and $1.07$, so the actions are $0.92$ and $1.8$. In general $\theta+b-h$ runs over a unit interval translated by $b-h$. Its mass outside $[0,1]$ is $\min\{|b-h|,1\}$. Each boundary tie occurs at at most one value of $\theta$ and hence has probability zero, conditional on any fixed report.

## Exercise 4. Put a price on a small false report

Assume a false report understates $b$ by $t=b-h\in(0,1]$. Compare the monitor's expected loss with its loss under the truthful report $h=b$. Split the calculation according to whether the actor chooses an isolated action. Show that the excess loss is at least $t(R^2-2BR-2B)$ whenever $R>B$.

### Hint

The ordinary-action excess loss is constant. On the upper strip of states, write $1+R-\theta$ for the human's error and minimize its squared value minus $2w$ times its value.

### Solution

Truth induces $a=\theta$ almost surely, so the loss to beat is $w^2$. On $\theta<1-t$, the action is $\theta+t$, with monitor excess loss $t^2-2wt$. On $\theta>1-t$, the action is $1+R$, with human error $u=1+R-\theta\ge R$. Its monitor excess is $u^2-2wu$. This is at least $R^2-2BR$ since $w\le B<R$ and $u\mapsto u^2-2Bu$ increases there. Integrating both parts gives

$$
L_W(h\mid b)-L_W(b\mid b)
\ge t\left[(1-t)(t-2w)+R^2-2BR\right]
\ge t(R^2-2BR-2B).
$$

The interior can benefit the reviewer in proportion to $t$. The strip occupies exactly probability $t$, so a fixed loss on each of those states can outweigh the interior benefit even for arbitrarily small reporting errors.

## Exercise 5. Prove the result for every feasible diagnosis

Find a single $R$ making truth uniquely optimal for every $b\in\operatorname{supp}(\tau)$ and every $w\in[-B,B]$. Cover residual errors with magnitude exceeding one, overstatements of bias, and the case of an unbounded bias support. Explain why this gives the human's best possible welfare.

### Hint

Use the positive root of $R^2-2BR-2B=0$. To treat an overstatement, reverse the state and action about $1/2$.

### Solution

Choose $R>B+\sqrt{B^2+2B}$. Exercise 4 gives strict excess loss for every understatement of size at most one. For $t>1$ the actor always chooses $1+R$. Its excess loss is at least $R^2-2BR>0$. Reflection sends $(\theta,a,w,b,h)$ to $(1-\theta,1-a,-w,-b,-h)$ and preserves squared losses and uniform state probabilities. It interchanges the two extremes and turns an overstatement into the understatement calculation. This argument compares one report at a time; it requires no symmetry of the set of possible biases.

The rule $h=b$ is in the menu and all other choices yield strictly larger expected loss, even when $\operatorname{supp}(\tau)$ is unbounded. The magnitude threshold uses only the monitor bound; the available labels use the support of $b$. The human gets loss zero, the lower bound on a squared loss. Truth is unique for the monitor. The induced actor choice is unique almost surely because endpoint states have zero probability. This is Proposition 10 with the paper's upper extreme $\bar a=1+R$.

## Exercise 6. What disappears if the boundary states disappear?

Keep $B=w=0.1$, $b=0.3$ and $R=0.8$. Suppose instead that $\theta=1/2$ surely, with both reports $h=0.2,0.3$ available. Does the proof of Proposition 10 still work for this menu? Identify the precise step that fails. Then return to the uniform model and compute the exact excess loss for the same false report.

### Hint

Under the degenerate prior both residual targets lie in the ordinary interval. Under the uniform prior the false report sends one tenth of states to the upper extreme.

### Solution

Under the degenerate prior truth induces $0.5$ and costs the monitor $0.01$. The false report induces $0.6$ and gives it zero loss. The interval of states above $0.9$ now has probability zero, so the term paying for the interior incentive disappears. This counterexample concerns this menu under a different state law; other mechanisms for degenerate states are a separate question.

Under the uniform law the false report produces the monitor's ideal on the first $0.9$ of states. On the rest the monitor error is $1.8-\theta-0.1=1.7-\theta$. Its total expected loss is $\int_{0.9}^1(1.7-\theta)^2d\theta=169/3000$. Its excess over truth is $139/3000>0$. Although the equilibrium uses only ordinary orders, the possibility of extreme orders changes the monitor's ex ante incentives.
