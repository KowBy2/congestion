# Resource Rush - Mathematical Summary

### Unit Allocation
Each faction has \( U = 10 \) units to allocate among various tasks:

\[
u_w + u_f + u_e + u_d + u_a \leq U
\]

where:
- \( u_w \) = units allocated to gathering water
- \( u_f \) = units allocated to gathering food
- \( u_e \) = units allocated to gathering energy
- \( u_d \) = units allocated to defending
- \( u_a \) = units allocated to attacking

### Hazard Impact
A hazard \( H_r \) (with a level between 1 and 3) reduces the effectiveness of units gathering resource \( r \) (water, food, or energy):

\[
\text{Effective Units} = \max(0, u_r - H_r)
\]

### Resource Collection
The resources \( C_r \) collected each round are calculated as:

\[
C_r = \text{Effective Units}
\]

### Total Score
The faction's final score is the sum of all resources collected across 8 rounds:

\[
\text{Total Score} = T_w + T_f + T_e
\]

where:
- \( T_w \) = total water collected
- \( T_f \) = total food collected
- \( T_e \) = total energy collected
