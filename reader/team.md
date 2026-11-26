# What one agent can tell us about another

## Types that describe a team

Imagine two reviewers deciding whether a catalog is ready. A reviewer might know that its colleague has seen the source database. That fact can change its decision even when its own estimate of the catalog's accuracy stays fixed. BKM give such information a place in the type. Each agent knows its own feasible actions and payoff, and has a belief about the state and the other agents' capabilities, preferences and beliefs. Higher orders must agree with lower orders when one projects away the extra information. The resulting type $t_i$ determines a law $\beta_i[t_i]$ on $(\theta,t_{-i})$. The designer assesses outcomes under its own law $\Gamma$. Agents can disagree with that law, although a supported agent must allow the events the designer considers possible conditional on its type. [Original paper, Section 4](https://arxiv.org/html/2609.01595v1#S4)

## Proposition 6. Multi-agent revelation principle

Each agent first learns its type and sends an admissible report. The designer draws a joint collection of plans $p_i:S_i\to A$ and gives each agent only its own plan. Physical signals then arrive, potentially correlated across agents. If all comply, agent $i$ plays $p_i(s_i)$. Correlation in plans matters. A pair of fair private instructions can allocate two different rooms with certainty. Drawing independently from the same two marginals would double-book a room half the time.

Proposition 6 shows why direct reports suffice. Fix an equilibrium of an indirect protocol. At a reported type profile, simulate the inputs those types would send and sample the original vector of private outputs once. Each output and reported type determine how that agent would act after each possible signal. Send this function as its plan, and use the original reward at the simulated inputs and actual actions. A genuine type could reproduce a profitable direct deviation in the indirect game: the imitation order makes the mimicked input available, the private output determines its plan, and it still receives its true signal. Conversely, letting agents submit type reports as the inputs to an indirect game realizes any direct mechanism. [Work through Proposition 6](07-beliefs.html)

## Paying for a forecast of an honest peer

In Example III the designer knows each supported type's forecast $p$ of the other agents' type reports. If those agents tell the truth, scoring a claimed forecast $q$ against their realized report vector $y$ with $S(q,y)=2q(y)-\|q\|_2^2$ has a simple consequence:
$$
\mathbb E_p[S(p,Y)-S(q,Y)]=\|p-q\|_2^2.
$$
For instance, in the catalog example let the probabilities of $(H,H),(H,L),(L,H)$ be $1/2,1/4,1/4$. An $H$ reviewer predicts a high peer with probability $2/3$. An $L$ reviewer is certain of a high peer. Claiming the other type sacrifices $2/9$ in expected score. Rewarding agreement would instead tempt the low reviewer to announce $H$.

### Proposition 7. Support-wise implementability of every feasible rule

Proposition 7 extends this calculation to any feasible action rule. Supported types must assign probability one to the supported peer alphabet, and two distinct types of the same agent must predict different peer distributions. Finite support then gives a positive minimum squared gap $\delta$ whenever there are competing reports. On the target action support the designer pays the scaled peer score minus the reported private utility. Truth cancels intrinsic preferences. A supported lie can recover at most a finite utility discrepancy $M$, and loses at least $\Lambda\delta$ in expected score. Choose $\Lambda\delta>M$ and exclude off-target actions and unsupported reports with the permitted penalty. Truth and obedience implement the rule in an equilibrium. Utility cancellation in the general formula can require state-contingent rewards. The binary catalog example needs only the reports and played actions. [Work through Proposition 7](08-peer-discipline.html) · [Original paper, Example III](https://arxiv.org/html/2609.01595v1#S5)
