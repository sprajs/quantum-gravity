# Counting states with two copies of a clock-filtered preparation

Can a positive two-copy return distinguish a finite clock window from an infinite window with arbitrarily many states at the same area? Chandrasekaran's Eq. (D.47) gives a sufficient trace bound. The finite-cut return also obeys a sharp two-sided **rank** bound. It can be calculated from open cap overlaps, and an area filter gives an exact rank calibration. The gravitational proof gap is to control these overlaps on a family that exhausts the physical clock window. [Chandrasekaran, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1) · [Eqs. (D.47)–(D.49)](https://arxiv.org/pdf/2611.34924v1#page=75) · [Earlier sufficient bound](dimension-crosscheck.md)

## A finite preparation using open amplitudes

Fix a nonzero physical clock window $H$ and the same cap $C=C_b$ throughout. Assume $mI\le W=C^\dagger C\le MI$ on $H$, with $0<m\le M<\infty$ independent of the cutoff. Eq. (5.30) supplies such bounds if the proposed cap and compact area range hold, since $W=e^{-s}f_b(s)$ is positive and continuous there. Choose a rank-$r$ projection $P$ on $H$ with orthonormal basis $e_i$ for its range. Its range may mix areas. [Eqs. (5.21)–(5.25)](https://arxiv.org/pdf/2611.34924v1#page=39) · [Eq. (5.30)](https://arxiv.org/pdf/2611.34924v1#page=41)

Choose an input $e_i$ uniformly, apply $C/\sqrt M$ and condition on success. The output density operator is $CPC^\dagger/Z_P$, where $Z_P=\sum_i\|Ce_i\|^2$. This prescription gives greater weight to outputs with greater success probability. On two independently accepted copies, exchange their **whole** output states. The swap expectation is the purity. Equivalently, compute only the finite open Gram matrix $G_{ij}=\langle Ce_i,Ce_j\rangle$ and form

$$
 R_P=\frac{\sum_{i,j}|G_{ij}|^2}{(\sum_iG_{ii})^2}
     =\frac{\operatorname{Tr}(G^2)}{(\operatorname{Tr}G)^2}.
$$

Indeed, exchanging two output vectors gives $|\langle Ce_i,Ce_j\rangle|^2$ in the product expectation. Every term has specified external states and both sums are finite. Equating this ratio to the independently computed gravitational replica amplitude would require a further matching argument. In particular, a calculation confined to the regular saddles in (D.48)–(D.49) has to account for all microscopic sectors accessed by the open preparations.

## What the return implies

Let $\mu$ be the mean of the $r$ eigenvalues of $G=PWP|_{PH}$, each in $[m,M]$. Cauchy–Schwarz gives $rR_P\ge1$. The inequality $(\lambda-m)(M-\lambda)\ge0$ gives

$$
 rR_P\le\frac{(m+M)\mu-mM}{\mu^2}
       \le K,\qquad K=\frac{(m+M)^2}{4mM}.
$$

The maximum occurs at $\mu=2mM/(m+M)$. For $m<M$ the constant is attained when the fraction of eigenvalues at $M$ is $m/(m+M)$ and all others equal $m$, whenever the multiplicities are integral. Equal eigenvalues attain the lower bound. Thus $1/R_P\le r\le K/R_P$. If an estimate $\widehat R$ has certified absolute error $e<\widehat R$, the integer interval is

$$
 \left\lceil\frac{1}{\widehat R+e}\right\rceil
 \le r\le
 \left\lfloor\frac{K}{\widehat R-e}\right\rfloor .
$$

These are bounds on the prepared rank. To infer the dimension of $H$, let finite-rank projections increase strongly to $I_H$ (a sequence for separable $H$, a directed net in general). In finite dimension the ranges eventually fill $H$, giving a fixed positive $R_I$. In infinite dimension the ranks eventually exceed every integer, hence $R_P\to0$ along **every** such exhaustion. A positive limsup on even one exhaustion is therefore necessary and sufficient for finite dimension under the stated cap bounds. A certified physical lower limit $R_*>0$ gives $\dim H\le\lfloor K/R_*\rfloor$. Conversely, one certified rank $r>K/R_*$ already excludes that proposed lower limit for any exhaustion of the same window. Larger finite dimensions remain possible. Holding the clock and the lower weight bound fixed matters. On an infinite basis with weights $2^{-j}$, $j\ge1$, the first $r$ states give $R_r=(1+2^{-r})/[3(1-2^{-r})]\to1/3$.

## Keeping the disk factor in a continuous-area control

One can match **both** integrals of Eq. (D.48) exactly and still lose a factor of the cell width in the two-copy return. Set the model multiplicity $d(s)=1$ and choose $k(s)=e^s w(s)$ with the same positive weight $w(s)=e^{-s}f_b(s)$ used by the cap. With $x=e^s$ the two regular integrals, including the disk factor $e^{-s}$ in the cyclic one, are exactly $A=\int w\,dx$ and $B=\int w^2\,dx$. Their return is $R^{\rm reg}=B/A^2>0$. Here and below $w$ as a function of $x$ means $w(\log x)$. [Eq. (D.48)](https://arxiv.org/pdf/2611.34924v1#page=75)

Realize dimensionless area by multiplication by $\log x$ on $H=L^2([x_-,x_+],dx)$ and $W$ by multiplication by $w$. Take dyadic partitions into $N$ equal cells of width $h=(x_+-x_-)/N$. The unit vector on each cell is its indicator divided by $\sqrt h$. Their spans increase densely, and compression of $W$ gives one diagonal entry equal to the **cell mean** of $w$ per state. If $w_N$ is the cell-mean function, then $\operatorname{Tr}G=A/h$, $\operatorname{Tr}G^2=\int w_N^2\,dx/h$, and hence

$$
 R_N=h R^{\rm reg}-\frac{h}{A^2}\int|w-w_N|^2\,dx .
$$

If $w$ is Lipschitz in $x$ with constant $L$, then $0\le hR^{\rm reg}-R_N\le (x_+-x_-)L^2 h^3/(12 A^2)$. Indeed, the variance on a cell is half the mean of $|w(X)-w(Y)|^2$ for independent uniform $X,Y$ in it, and $\mathbb E|X-Y|^2=h^2/6$. Thus the finite Hilbert return vanishes linearly even though the two regular integrals have exactly the proposed measure and disk factor. The discrepancy already occurs at multiplicity one. With $1\le x\le3$, $s_b=1/4$ and $\sigma_s=1$, the Gaussian packet gives $R^{\rm reg}=0.586222$ throughout, above the bound $1/2$ in (D.49). Yet the endpoint weights give $K=1.601978$, so **every cut of rank four or greater** has $R_P\le K/4<1/2$. The finite Gram returns at $N=8,32,128$ are $0.14612776,0.03663220,0.00915962$. This continuum model tests the identification of the two returns. The area representation and measure in the microscopic gravitational theory remain to be determined.

## An area filter to calibrate the rank

If the open area filter $F=\sqrt m\,W^{-1/2}$ can be implemented on the clock window, apply it **before** the cap. It is a contraction depending only on area for the stated $W$. The successful map $CF/\sqrt M$ has Gram operator $(m/M)I$ on $H$. Every input succeeds with probability $m/M$, and the conditioned two-copy return on any finite cut is exactly $1/r$. This changes the preparation. It offers a calibration of state coverage, while comparison to the original (D.49) requires the original cap.

The calibration tolerates error. Suppose the implemented real filter differs by a relative amplitude at most $\delta<1$ at every area. An overall rescaling can make it a contraction and cancels from the normalized return. After factoring out the common scale the resulting Gram eigenvalues lie in $[(1-\delta)^2,(1+\delta)^2]$, also after compression to a cut mixing different areas. The bound above becomes

$$
 1\le rR_P^{\mathrm{cal}}
 \le 1+\frac{4\delta^2}{(1-\delta^2)^2}.
$$

A 5% uniform amplitude error permits just over 1% excess in the scaled return. The exact single-copy success probability $m/M$ can be very small. The criterion assumes the specified open preparations and their completeness can be established in gravity. A long plateau from a single prepared subspace supplies no bound on hidden states.

## Full swap and area-only swap

Use the two-area model with equal weights. At cutoff $N$, the lower area has $kN$ orthogonal states and the upper area has $N$. For each fixed positive integer $k$ these cuts exhaust the same infinite space. The full conditioned density is uniform on $(k+1)N$ states. If only the two-valued area label is kept, tracing out the multiplicity gives probabilities $k/(k+1)$ and $1/(k+1)$. The full swap retains the multiplicity label. [Finite boost model](05-2.md)

| $k$ | Full swap, $N=8$ | Full swap, $N=32$ | Area-only swap, every $N$ |
|---:|---:|---:|---:|
| 1 | $1/16$ | $1/64$ | $1/2$ |
| 4 | $1/40$ | $1/160$ | $17/25$ |

The full return tends to zero with the exact value $1/[(k+1)N]$. The positive area-only returns survive because the partial trace discards the multiplicity being tested. A measured positive purity for an arbitrary wave packet also tests only that preparation. A floor for the full clock-filtered return requires coverage of the full state labels along an exhaustion.

Run `python3 checks/purity_test.py` from the repository root. It prints these four full returns and their area-only controls, the continuous-area returns for $N=8,32,128$, the sharp bound at $m=1/4,M=1$, and the calibrated return for a two-dimensional subspace mixing three distinct weights. The same command checks the 5% error bound and the decaying-weight example. [Executable calculation](../checks/purity_test.py)
