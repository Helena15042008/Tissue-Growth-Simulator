
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def nutrient_growth(T, t, r, K0, Km, N):
    K = K0 * (N / (N + Km))
    dTdt = r * T * (1 - T / K)
    return dTdt

st.title("🧬 Tissue Growth Simulator (Advanced Model)")

r = st.slider("Growth rate (r)", 0.1, 1.0, 0.3, 0.01)
time_max = st.slider("Simulation time (days)", 10, 200, 50, 5)
T0 = st.slider("Initial cell density", 1, 100, 10, 1)
N0 = st.slider("Initial nutrient concentration", 1, 100, 50, 1)
K0 = st.slider("Max carrying capacity K₀", 100, 1000, 500, 50)
Km = st.slider("Half-max nutrient constant Kₘ", 1, 100, 10, 1)

t = np.linspace(0, time_max, 200)
sol = odeint(nutrient_growth, T0, t, args=(r, K0, Km, N0))
T = sol.flatten()

fig, ax = plt.subplots()
ax.plot(t, T, color="teal", lw=2)
ax.set_xlabel("Time (days)")
ax.set_ylabel("Tissue mass / cell density")
ax.set_title("Tissue Growth Over Time")
ax.grid(True)
st.pyplot(fig)

st.markdown(f'''
### 🧾 Model details
- Growth rate (r): **{r}**
- Initial cell density (T₀): **{T0}**
- Nutrient concentration (N₀): **{N0}**
- Scaffold factor: K₀={K0}, Kₘ={Km}
''')

if st.button("Show raw data"):
    st.write({ "time": t.tolist(), "tissue": T.tolist() })
