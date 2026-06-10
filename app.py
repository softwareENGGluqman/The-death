import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="Afterlife 404 | Fact Check",
    page_icon="🔌",
    layout="centered"
)

# --- Header Section ---
st.title("🔌 The Afterlife 404 Error")
st.markdown("### *Decoding the 'Marne ke baad pata chalega' logic.*")
st.write("A fun, logical, and slightly sarcastic reality check about what actually happens when we unplug from life.")

st.divider()

# --- Fun/Philosophical Section: The TV Analogy ---
st.subheader("📺 The 'Broken TV' Philosophy")
st.info("""
**Logic ka sawal:** Agar aap ek chalti hui TV ko hathode se tod dein, toh kya usmein koi 'Gupt Channel' (Secret Channel) chalne lagega? 
Nahi na? Screen black ho jayegi. 

Insani dimaag (Hardware) aur hosh/consciousness (Software) ka bhi yahi hisaab hai. **Jab TV toot gaya, toh pachtawa kaisa aur moka kaisa?**
""")

col1, col2 = st.columns(2)
col1.metric("Chances of finding a secret channel", "0%")
col2.metric("Chances of Dreamless Sleep", "100%")

st.divider()

# --- Interactive Section: Consciousness Simulator ---
st.subheader("💀 The 'Death' Simulator")
st.write("Click below to see what actually happens to the system. (Don't worry, it's reversible here).")

if st.button("🔴 Unplug the System (Simulate Death)", use_container_width=True):
    progress_bar = st.progress(0)
    status_text = st.empty()

    # Funny & logical shutdown sequence
    status_text.text("Stopping heart_beat.exe...")
    progress_bar.progress(20)
    time.sleep(1)

    status_text.text("Uninstalling 'Fear_of_Hell' module...")
    progress_bar.progress(50)
    time.sleep(1)

    status_text.text("Brain hardware degrading. Logic circuits shutting down...")
    progress_bar.progress(80)
    time.sleep(1.5)

    status_text.text("Consciousness = NULL.")
    progress_bar.progress(100)
    time.sleep(0.5)

    st.success("✅ System successfully entered: Dreamless Infinite Sleep.")
    st.error("⚠️ Error: 'Soul' not found. GPS location tracking failed.")
    st.balloons() # Thoda ironic celebration

st.divider()

# --- Funny Section: The Soul Tracker ---
st.subheader("📡 Live Soul Tracker")
st.write("Let's try to locate where the 'Main' (You) goes after the hardware is destroyed.")

with st.expander("🔍 Initiate Soul Search"):
    st.write("Searching Heaven database... ❌ (No match found)")
    time.sleep(0.5)
    st.write("Searching Hell database... ❌ (Server unreachable)")
    time.sleep(0.5)
    st.write("Searching Rebirth queue... ❌ (Logic error)")
    st.markdown("**Result:** Just like a blown-out candle flame doesn't 'go' anywhere, it just stops existing. You are the flame.")

st.divider()

# --- The Code Section (For the Tech-Savvy) ---
st.subheader("💻 The Logic in Code")
st.write("For those who understand the language of logic better than the language of fear.")

tab1, tab2, tab3 = st.tabs(["🐍 Python", "🖥️ Terminal", "⚙️ JSON"])

with tab1:
    st.code("""
def experience_afterlife(brain_active):
    if not brain_active:
        return {
            "Pain": None,
            "Regret": None,
            "Status": "Dreamless Infinite Sleep"
        }
    return "Still alive, still scared of imaginary things."

# Hamid's Status
print(experience_afterlife(brain_active=False))
    """, language="python")

with tab2:
    st.code("""
user@earth:~$ ping hell_server.com
ping: unknown host hell_server.com

user@earth:~$ check_hardware --brain
Status: Decomposed
Error: Cannot process 'regret' without a biological nervous system.
    """, language="bash")

with tab3:
    st.code("""
{
  "name": "Human",
  "hardware_status": "Destroyed",
  "can_feel_pain": false,
  "can_feel_regret": false,
  "destination": "Same place you were in 1850 (Non-existence)"
}
    """, language="json")

st.divider()

# --- Philosophical Conclusion ---
st.subheader("🌌 The 1850 Thought Experiment")
st.markdown("""
> *"Aap 1850 mein kahan the? Kya aapko wahan hone mein koi takleef hui? Koi dard, koi darr, koi saza?"*

**Jawab hai: Nahi.** Kyunki aap exist hi nahi karte the. Maut ke baad ka waqt bilkul waisa hi hai jaisa paida hone se pehle ka arabon saalo ka waqt. Yeh ek **Dreamless Infinite Sleep** hai.

Isliye "wahan jao gy aur pachtao gy" sirf zinda logo ki psychology se khelne aur unhe control karne ka ek tareeqa hai.
""")

st.caption("Built with 🧠 Logic and 💻 Python. No imaginary servers were harmed in the making of this app.")

