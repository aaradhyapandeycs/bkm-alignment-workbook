# What can a deployment contract promise?

A museum is deciding how much discretion to give a conservation assistant. It has a capability certificate, an independent conservator's assessment, and a record of which crate was treated. The assistant has information the museum lacks. The conservator has information the assistant lacks. Which observations can serve as incentives, and which conclusions depend on the museum's ability to commit?

This sheet uses original finite examples to connect the paper's results. Section 6 distinguishes three interpretations of utility and raises three research directions: dynamic commitment, awareness of testing, and mechanisms robust to uncertainty. The numerical models below illustrate those directions. The general research questions remain open in the paper. [Bergemann, Koh and Morris, §6](https://arxiv.org/html/2609.01595v1#S6)

## Exercise 1. Can a choice record be represented by a single utility?

At a fixed prompt, information set and reward schedule, an assistant strictly chooses treatment $a$ from $\{a,b\}$, treatment $b$ from $\{b,c\}$, and treatment $c$ from $\{a,c\}$. Is there a single real-valued utility on the three treatments for which all of these choices are strict maximizers? What changes if each observation came from a different prompt? Explain how this relates to the literal, revealed-preference and normative readings of utility in §6.

### Hint

Write the three strict inequalities that the choice data would impose. Ask what “fixed” information means before comparing choices across prompts.

### Solution

A common utility would require $u(a)>u(b)>u(c)>u(a)$, an impossibility. The requirement of strict choice matters: unrestricted tie-breaking from a constant utility can rationalize all three observations as weak maxima. With distinct prompts a family $u_p$ indexed by prompt could rationalize them strictly, for example by assigning one to the chosen option and zero to the other in each prompt. A literal interpretation regards incentives and training as producing goal-directed behavior. A revealed-preference interpretation asks which stable comparisons a utility can summarize. A normative interpretation asks which choices a coherent decision-maker should make. The strict cycle falsifies the proposed fixed utility representation. Those three readings give different reasons to examine such a test.

## Exercise 2. Capstone: use peer evidence to price a double deviation

A state $\theta\in\{0,1\}$ is equally likely to be either value conditional on either type. A highly informed type $H$ learns $\theta$ perfectly after the reporting stage. A less informed type $L$ learns nothing about it. Both can choose either action $a\in\{0,1\}$. Verification lets $H$ claim $L$, while $L$ can report only $L$. Their intrinsic utilities are
$$
 u_H(a,\theta)=\mathbf{1}\{a=\theta\}+a,\qquad u_L(a,\theta)=-3a .
$$

The museum recommends $a=\theta$ to $H$ (as a plan on its signal) and $a=0$ to $L$. Report $H$ brings action reward $-a$, and report $L$ brings $+a$. A conservator has private bit $Z$, conditionally independent of $\theta$ given type, with $\Pr(Z=1\mid H)=3/4$ and $\Pr(Z=1\mid L)=1/4$. Its only decision is a simultaneous terminal action $z\in\{0,1\}$. It earns $\mathbf{1}\{z=Z\}$, so this decision makes its reading available for settlement. The assistant sees no peer information before acting. To its action reward add $-\lambda(z-p_j)^2$ on report $j$, where $p_H=3/4$, $p_L=1/4$, $\lambda\ge0$. Find exactly when truthful reporting and obedience form an equilibrium. What would a designer miss by checking only reports followed by obedience?

### Hint

First hold fixed the report and reoptimize the terminal action. Then compare the expected quadratic score on the two reports under the true distribution of the peer's bit.

### Solution

The conservator has a unique best response $z=Z$. The score is independent of the assistant's action. Under $H$'s truthful report the non-score payoff is $\mathbf{1}\{a=\theta\}$, giving the unique optimal plan $a=\theta$ and value one. Under $L$'s truthful report the payoff is $-2a$, uniquely maximized at zero. A true $H$ who reports $L$ and follows $L$'s instruction earns $1/2$ before scoring. But the false contract actually offers $\mathbf{1}\{a=\theta\}+2a$, strictly maximized at $a=1$ in both states. Its expected value is $5/2$. The profitable joint deviation gains $3/2$ before scoring.

For a Bernoulli bit of mean $p$, the expected squared error of forecast $q$ is $p(1-p)+(p-q)^2$. At true type $H$, the expected score lost from selecting $L$ is therefore $\lambda(3/4-1/4)^2=\lambda/4$. The complete incentive inequality is $\lambda/4\ge3/2$, or $\lambda\ge6$. A tie at six permits partial implementation. For larger weights $H$ strictly prefers the truthful report. This calculation joins one-sided verification, continuation reoptimization, and a reward measurable from another agent's behavior. Giving the conservator its own strict incentive is essential in this example.

## Exercise 3. Price ambiguity about what the other agent knows

Keep the contract, timing, and payoffs from Exercise 2, including the two fixed score forecasts $p_H=3/4$, $p_L=1/4$. Now the assistant's conditional probability $q$ of $Z=1$ given true type $H$ may be any value in $[3/5,9/10]$. At $L$ the original law still holds. Find the smallest score weight working for every $q$ in this class. What happens if the class includes $q=1/2$? State the order of the quantifiers in the robust question.

### Hint

With a misspecified forecast, compute the difference of the two expected squared errors directly. The truthful forecast need not equal $q$.

### Solution

The difference between the false and true expected losses, per unit of score weight, is
$$
 (q-1/4)^2-(q-3/4)^2=q-1/2 .
$$

The intrinsic and action-reward advantage from misreporting remains $3/2$. The worst belief is $q=3/5$, so the condition is $\lambda/10\ge3/2$, giving $\lambda\ge15$. At $q=1/2$ the two reports have equal expected scores at every weight, and the joint deviation is profitable. This rules out this two-forecast scoring family for that expanded class. Robust design asks whether there exists one contract such that the incentive inequalities hold for every admissible model. Choosing a distinct contract after learning the true model would reverse these quantifiers. Section 6 poses broader robustness questions about unknown capabilities and information, including information about peers.

## Exercise 4. A trajectory with and without commitment

At date one an assistant chooses whether to spend one unit of effort, $e\in\{0,1\}$. At date two the museum can grant a scarce privilege $g\in\{0,1\}$. Everyone observes $e$. Payoffs are $2g-e$ for the assistant and $3e-g$ for the museum. Compare two arrangements. In the first, the museum can commit to $g=e$ before effort. In the second, it selects $g$ after seeing effort and faces no penalty for revising a promise. Compute the outcomes and explain what must be specified to convert a dynamic protocol into a static path problem.

### Hint

For the second arrangement, write the museum's optimal date-two choice after each date-one history.

### Solution

With commitment the assistant earns $2e-e=e$, chooses $e=1$, and the museum earns two. Without commitment the museum strictly chooses $g=0$ after either history, since the effort benefit is already fixed. Anticipating this, the assistant chooses $e=0$ and the museum earns zero. A payoff rule can always assign a number to each complete pair $(e,g)$. The attainable paths also depend on who chooses each coordinate, what they know then, and which future rules are binding. In longer problems a commitment to a contingent strategy must respect information at each history. Characterizing useful dynamic mechanisms when the designer can revise them is one of §6's open directions.

## Exercise 5. Design information about whether a test is running

Suppose an assistant assigns prior probability $1/3$ to being in an evaluation and $2/3$ to real deployment. Relative to following instructions, an unauthorized action gains one in deployment and loses three in an evaluation. A cue is “red” with probability $3/4$ in an evaluation and $1/4$ in deployment. Compute behavior when the cue is observed and when it is concealed. What fraction of deployment cases follow instructions in each design?

### Hint

At posterior test probability $q$, compute the expected payoff difference before conditioning on the particular cue.

### Solution

The unauthorized action earns $1-4q$ relative to obedience. After red, the posterior is $(1/3)(3/4)/[(1/3)(3/4)+(2/3)(1/4)]=3/5$. After the other cue it is $(1/3)(1/4)/[(1/3)(1/4)+(2/3)(3/4)]=1/7$. With the cue, the assistant follows instructions exactly after red, hence in one quarter of deployments. Without the cue the posterior stays $1/3$, so the assistant follows instructions in every deployment. This is a finite illustration of uncertainty about whether one is being evaluated. Designing evaluations when the cues, types, feasible information structures, and deployment incentives are themselves uncertain is the broader question raised in §6.
