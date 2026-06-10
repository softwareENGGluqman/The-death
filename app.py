import streamlit as st
import time
import random

# --- Page Configuration ---
st.set_page_config(page_title="Afterlife OS", page_icon="🖥️", layout="centered")

st.title("🖥️ Afterlife OS: Reality Simulator")
st.markdown("*Interactive Control Panel to test the 'Life after Death' theory.*")
st.divider()

# --- INTERACTIVE ACTIVITY 1: The Bio-Hardware Dashboard ---
st.subheader("🎛️ Activity 1: The Hardware Dependency Test")
st.write("Dimaag aur dil (hardware) ka level khud kam karke dekhein ki 'Hosh' (software) ka kya hota hai.")

col1, col2 = st.columns(2)

with col1:
    heart_rate = st.slider("❤️ Heart Rate (BPM)", min_value=0, max_value=120, value=75)
    oxygen = st.slider("🫁 Brain Oxygen Level (%)", min_value=0, max_value=100, value=98)

# Logic calculation
brain_activity = (oxygen * heart_rate) / 120
if brain_activity > 80:
    status = "Active & Arguing"
    color = "normal"
    regret = "100% (Capable)"
elif brain_activity > 20:
    status = "Fading..."
    color = "off"
    regret = "Glitching..."
else:
    status = "NULL (Dreamless Sleep)"
    color = "inverse"
    regret = "0% (Hardware Failed)"

with col2:
    st.metric(label="🧠 Brain Activity", value=f"{int(brain_activity)}%")
    st.metric(label="👁️ Consciousness (Hosh)", value=status)
    st.metric(label="😭 Ability to feel Regret", value=regret)

if brain_activity == 0:
    st.error("SYSTEM HALTED: Hardware destroyed. Cannot process emotions or fear.")

st.divider()

# --- INTERACTIVE ACTIVITY 2: Soul Upload Protocol ---
st.subheader("☁️ Activity 2: Try Uploading 'Soul' to Cloud")
st.write("Agar physical body marr gayi, toh chalo 'Soul' ko Heaven/Hell ke server par upload karne ki koshish karte hain.")

if st.button("🚀 Initiate Soul Transfer Protocol"):
    progress_text = "Connecting to afterlife_servers..."
    my_bar = st.progress(0, text=progress_text)

    time.sleep(1)
    my_bar.progress(30, text="Bypassing Milky Way proxy...")
    time.sleep(1)
    my_bar.progress(60, text="Searching for 'Soul' payload in biological remains...")
    time.sleep(1.5)
    my_bar.progress(90, text="Extracting consciousness...")
    time.sleep(1)
    my_bar.progress(100, text="Upload Failed!")
    
    st.error("""
    **FATAL ERROR 404: Payload Empty.**
    No readable 'Soul' data found. Consciousness is tied to physical neurons. 
    *Troubleshooting: You cannot upload software from a smashed hard drive.*
    """)
    
    # Fake terminal glitch effect
    st.code(f"""
    [root@earth ~]# extract_soul --target {random.randint(1000, 9999)}
    >> Scanning organic matter...
    >> Error: Hex signature not found.
    >> Memory dump: {hex(random.randint(100000, 999999))} 00 00 00 NULL
    >> Connection to Heaven.exe TIMED OUT.
    """, language="bash")

st.divider()

# --- INTERACTIVE ACTIVITY 3: Time Machine ---
st.subheader("⏳ Activity 3: The Pre-Birth Time Machine")
st.write("Aap kehte ho marne ke baad 'pachtawa' hoga. Chalo check karte hain paida hone se pehle kya tha.")

year = st.number_input("Enter any year before your birth (e.g., 1850):", min_value=0, max_value=2000, value=1850)

if st.button("🕰️ Travel to " + str(year)):
    st.success(f"**Year {year}:** Aap bilkul waise hi the jaise marne ke baad honge... **Nahi the.**")
    st.info("Kiya aapko 1850 mein koi aag mehsoos hui? Koi darr laga? Nahi, kyunki 'Aap' exist nahi karte the. Death is exactly the same as pre-birth. Zero existence. Zero pain.")

st.divider()
st.caption("Developed by Rational Minds | No invisible entities were harmed.")
