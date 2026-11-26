# Which null-cone brackets survive an unresolved boundary condition?

The bulk jump of the radiative bracket in (A.36) leaves a homogeneous term. One class of smeared brackets can nevertheless be computed on the fixed-area radiative block without choosing that term. The complement can be singular even when there is no normalizable zero mode. [Version 1, (A.34)–(A.36)](https://arxiv.org/pdf/2611.34924v1#page=58) · [Boundary variation](03-3.md)

## The common interior algebra

Work at a smooth background with positive, pointwise fixed area density, fixed generator labels and a monotone compact radial interval. Transport target-space tangent vectors back to an orthonormal frame at the initial cut and multiply each by the local area radius. In these variables, denoted by $X,Y$, the fixed-area shear block on the increasing interval $[0,L]$ takes the form
$$
 \Omega(X,Y)=c\int_0^L (X'\cdot Y-Y'\cdot X)\,dv,
 \qquad c=(16\pi G_N)^{-1}.
$$
Angular integration is implicit. A reversed branch orientation reverses the overall sign. A smooth interior source $dH(Y)=\int f\cdot Y$ with zero transported radial mean $\int_0^L f\,dv=0$ has the solution $X(v)=\int_0^v f(w)dw/(2c)$ to $\Omega(X,Y)=dH(Y)$. It vanishes at both endpoints. This calculation works even with unrestricted endpoint test variations. It also works with every endpoint identification below. These are brackets of linear perturbations at the chosen background. Extending them to nonlinear gravitational observables requires a definition of the source as the background varies.

## Boundary rotations and a quantitative test

As an explicit family of endpoint conditions impose $X(L)=U X(0)$ in transported variables, with $U$ orthogonal. This is a model of lossless endpoint matching on the fixed-area block with no extra boundary two-form. It cancels the endpoint pairing from integration by parts. For a source with arbitrary mean $F=\int_0^L f$, the endpoint condition becomes $(U-I)X(0)=F/(2c)$. When $U-I$ is invertible the Green function for the convention above is
$$
 G_U(v,w)=\frac{1}{2c}\left[\mathbf 1_{v>w}I+(U-I)^{-1}\right].
$$
Indeed $B=(U-I)^{-1}$ satisfies $B+B^T=-I$. For a plane rotation by $\theta$, $B+I/2=-\frac12\cot(\theta/2)J$ with $J$ the positive quarter turn. The inverse of the constraint operator in (A.34) carries the opposite sign. Undoing the transport and radius factors on its sign kernel gives precisely the bulk coefficient of (A.36). Differences between two invertible graph choices enter a smeared bracket only through the two radial means. Modes with zero mean on either side give the same answer. If $U$ has a fixed vector, compatibility requires $F$ orthogonal to all such vectors and a homogeneous solution remains free.

For an angular family of rotations, invertibility at almost every generator is insufficient. The radial derivative on each graph has frequencies $(2\pi n\pm\theta)/L$. The inverse from bulk $L^2$ sources to $L^2$ perturbations is bounded exactly when the essential angular infimum of $\operatorname{dist}(\theta,2\pi\mathbb Z)$ is positive (here $L$ is fixed). Its norm is $L/(2|c|\operatorname*{ess\,inf}\operatorname{dist}(\theta,2\pi\mathbb Z))$. This statement concerns bulk sources. Endpoint evaluation is a different functional.

## The geometric clock has an endpoint source

In this same fixed-area block the paper's own clock probes the limitation of the graph domain. In the original coordinate $v\in[\epsilon,1]$, write $\rho=\rho_S v$, $\Xi(v)=\tfrac14\int_\epsilon^v s|z'(s)|^2ds$, $u_*=\rho_S\int_\epsilon^1 e^{\Xi(v)}dv$. Let $T$ be $z'$ parallel transported to the initial frame and $K(v)=\int_v^1e^{\Xi(s)}ds$. Vary at fixed $\rho_S$ using the transported variable $Y$ above. Exchanging the two radial integrals gives
$$
 d u_*(Y)=\tfrac12\int_\epsilon^1 K\,T\cdot(Y'-Y/v)\,dv .
$$
Integration by parts exhibits the cap evaluation $-K(\epsilon)T(\epsilon)\cdot Y(\epsilon)/2$. The other endpoint has $K(1)=0$. For the graph domain, $\Omega(X,Y)$ for any $H^1$ vector $X$ is an ordinary $L^2$ density against $Y$. If the cap shear is nonzero, the trace functional above cannot equal such a density. For instance keep $Y(\epsilon)$ and its graph-matched final value fixed and shrink their smooth support to the endpoints; the $L^2$ norm goes to zero. The clock thus fails to have an $H^1$ Hamiltonian vector on this graph even when all bulk Green operators are uniformly bounded. This test uses the radiative form alone. Cap degrees of freedom can pair with endpoint traces, and the differential of the full coupled clock has other components. [Clock (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27)

For example, choose $\epsilon=1/2$, $\rho_S=1$, $z^1=2\log v$ and $z^2=0$. Then $e^\Xi=2v$, $u_*=3/4$ and the longitudinal differential is exactly $2\int Y_1dv-3Y_1(1/2)/2$. The graph $U=-I$ has a uniform bulk gap. Any antisymmetric pair of shrinking endpoint bumps with initial value one has zero mean, vanishing $L^2$ norm and the same nonzero clock variation $-3/2$. The script also differentiates the original nonlinear clock along $Y_1=3-4v$ and recovers this value.

## A smooth source with no square-integrable response

There is a geometrical mechanism for small rotations. The polarization metric of (4.21) admits the orthonormal coframe $dz^1,e^{z^1}dz^2$. In this frame parallel transport rotates a vector by $-\int e^{z^1}dz^2$. Traverse the boundary of the coordinate rectangle $[0,t]\times[0,t]$ in the positive parametrized order, returning to the same target point. Each straight leg can be traversed with all derivatives vanishing at its two ends. The resulting smooth path has integrated connection $\theta(t)=t(e^t-1)$. If one identifies the two weighted perturbation frames directly in physical endpoint coordinates, the identification in the transported frame is the inverse holonomy. Its small rotation is quadratic in $t$. [Polarization chart (4.21)](https://arxiv.org/html/2611.34924v1#S4.E21)

Take $t$ to be a signed angular coordinate across a short arc in a polarization chart. Use this family on the angular patch. Choose an interior smooth source with transported mean $F=t\chi e$, where $e$ is a fixed polarization and $\chi=1$ on a smaller arc with compact support in the chart. The source vanishes on the zero-rotation set and is compatible on each individual ray. For $t\ne0$, however, the required endpoint amplitude is proportional to $|t|/[2|\sin(\theta(t)/2)|]\sim1/|t|$. Its square has divergent angular integral. The primitive term is smooth and bounded and cannot remove this divergence anywhere in the radial interval. The zero-rotation curve itself has measure zero, so this graph family has no $L^2$ kernel on the patch. It still has smooth sources outside its range.

This is an obstruction for that endpoint identification. The manuscript would have to derive its own physical endpoint relation and the contributions of the cap Cauchy data. The zero-mean result and the exact bulk jump supply checks on any such derivation. Run `python3 checks/endpoint_inverse.py`. The check verifies the endpoint condition, skew Green kernel, source-independence for zero radial mean, and the predicted pole with $t$ decreasing from $1/10$ to $1/1000$. [Calculation](../checks/endpoint_inverse.py)
