### Mathematical Summary:

- **Unit Allocation:** Each faction has \( U = 10 \) units to allocate among tasks:
  \[
  u_w + u_f + u_e + u_d + u_a \leq U
  \]
  where \( u_w, u_f, u_e, u_d, u_a \) are units for gathering water, food, energy, defending, and attacking, respectively.

- **Hazard Impact:** A hazard \( H_r \) (level 1-3) reduces the effectiveness of units gathering resource \( r \) (water, food, energy):
  \[
  \text{Effective Units} = \max(0, u_r - H_r)
  \]

- **Resource Collection:** Resources collected \( C_r \) each round:
  \[
  C_r = \text{Effective Units}
  \]

- **Total Score:** The faction's score is the sum of all resources collected across 8 rounds:
  \[
  \text{Total Score} = T_w + T_f + T_e
  \]
  where \( T_w, T_f, T_e \) are the total water, food, and energy collected.

--- 
