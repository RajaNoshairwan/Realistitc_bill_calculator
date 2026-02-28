import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Electricity Bill Predictor", page_icon="⚡", layout="wide")

# -------------------------------
# Custom Styling (Premium UI)
# -------------------------------
st.markdown("""
<style>
.big-card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Title Section
# -------------------------------
st.title("⚡ Smart Electricity Bill Predictor")
st.markdown("### 🇵🇰 Advanced Energy Usage & Cost Estimator")

# -------------------------------
# Appliance Data
# -------------------------------
appliance_power = {
    "Fan": 120,
    "Light": 20,
    "AC": 1800,
    "Refrigerator": 200,
    "Water Pump": 1500,
    "TV": 100,
    "Iron": 1000,
    "Washing Machine": 500
}

# -------------------------------
# Sidebar Inputs
# -------------------------------
st.sidebar.header("🔌 Enter Your Usage")

fan = st.sidebar.slider("Fans", 0, 10, 2)
fan_h = st.sidebar.slider("Fan hours/day", 0, 24, 8)

light = st.sidebar.slider("Lights", 0, 20, 5)
light_h = st.sidebar.slider("Light hours/day", 0, 24, 6)

ac = st.sidebar.slider("AC", 0, 3, 1)
ac_h = st.sidebar.slider("AC hours/day", 0, 24, 5)

tv = st.sidebar.slider("TV", 0, 5, 1)
tv_h = st.sidebar.slider("TV hours/day", 0, 24, 4)

iron_h = st.sidebar.slider("Iron (hours/day)", 0, 5, 1)
wm_h = st.sidebar.slider("Washing Machine (hours/day)", 0, 5, 1)

fridge = st.sidebar.checkbox("Refrigerator (24 hrs)", True)
pump_h = st.sidebar.slider("Water Pump (hours/day)", 0, 5, 1)

# -------------------------------
# Calculate Usage
# -------------------------------
data = {
    "Fan": fan * 120 * fan_h / 1000,
    "Light": light * 20 * light_h / 1000,
    "AC": ac * 1800 * ac_h / 1000,
    "TV": tv * 100 * tv_h / 1000,
    "Iron": 1000 * iron_h / 1000,
    "Washing Machine": 500 * wm_h / 1000,
    "Refrigerator": 200 * 24 / 1000 if fridge else 0,
    "Water Pump": 1500 * pump_h / 1000
}

df = pd.DataFrame(list(data.items()), columns=["Appliance", "Daily kWh"])

daily_kwh = df["Daily kWh"].sum()
monthly_units = daily_kwh * 30

# -------------------------------
# Slab Billing + Breakdown
# -------------------------------
def bill_breakdown(units):
    slabs = []
    remaining = units

    if remaining > 0:
        use = min(100, remaining)
        slabs.append(("0-100", use, 20))
        remaining -= use

    if remaining > 0:
        use = min(100, remaining)
        slabs.append(("101-200", use, 30))
        remaining -= use

    if remaining > 0:
        use = min(100, remaining)
        slabs.append(("201-300", use, 40))
        remaining -= use

    if remaining > 0:
        slabs.append(("300+", remaining, 50))

    total = sum(units * rate for _, units, rate in slabs)
    return slabs, total

slabs, bill = bill_breakdown(monthly_units)

# -------------------------------
# Layout
# -------------------------------
col1, col2, col3 = st.columns(3)

col1.markdown(f"<div class='big-card'><h4>⚡ Daily Usage</h4><h2>{daily_kwh:.2f} kWh</h2></div>", unsafe_allow_html=True)
col2.markdown(f"<div class='big-card'><h4>📅 Monthly Units</h4><h2>{monthly_units:.0f}</h2></div>", unsafe_allow_html=True)
col3.markdown(f"<div class='big-card'><h4>💰 Estimated Bill</h4><h2>Rs. {bill:,.0f}</h2></div>", unsafe_allow_html=True)

# -------------------------------
# Charts
# -------------------------------
st.markdown("### 📊 Appliance Consumption")
st.bar_chart(df.set_index("Appliance"))

# -------------------------------
# Slab Breakdown Table
# -------------------------------
st.markdown("### 🧾 Bill Breakdown (Slabs)")
slab_df = pd.DataFrame(slabs, columns=["Slab", "Units", "Rate"])
slab_df["Cost"] = slab_df["Units"] * slab_df["Rate"]
st.dataframe(slab_df)

# -------------------------------
# Smart Insights
# -------------------------------
st.markdown("### 🤖 Smart Insights")

if monthly_units > 300:
    st.error("⚠️ High electricity usage detected! Consider reducing AC usage.")
elif monthly_units > 150:
    st.warning("⚡ متوسط usage — You can still optimize usage.")
else:
    st.success("✅ Efficient usage — Great job!")

# -------------------------------
# Tips Section
# -------------------------------
st.markdown("### 💡 Energy Saving Tips")

tips = [
    "Switch to LED bulbs",
    "Set AC at 26°C",
    "Use inverter appliances",
    "Turn off idle devices",
    "Avoid peak hour usage"
]

for tip in tips:
    st.write("✔️", tip)

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("⚠️ This is an estimate based on Pakistani slab rates. Actual bills may vary.")













# import streamlit as st
# import pandas as pd

# st.set_page_config(page_title="Electricity Bill Calculator", page_icon="⚡", layout="wide")

# # Title
# st.title("⚡ Smart Electricity Bill Calculator (Pakistan)")
# st.markdown("Estimate your electricity usage using realistic appliances and slab rates.")

# # -------------------------------
# # Appliance Power Ratings (Watts)
# # -------------------------------
# appliance_power = {
#     "Fan": 120,
#     "Light": 20,
#     "AC": 1800,
#     "Refrigerator": 200,
#     "Water Pump": 1500,
#     "TV": 100,
#     "Iron": 1000,
#     "Washing Machine": 500
# }

# # -------------------------------
# # Sidebar Inputs
# # -------------------------------
# st.sidebar.header("🔌 Appliance Usage")

# fan = st.sidebar.slider("Fans", 0, 10, 2)
# fan_h = st.sidebar.slider("Fan hours/day", 0, 24, 8)

# light = st.sidebar.slider("Lights", 0, 20, 5)
# light_h = st.sidebar.slider("Light hours/day", 0, 24, 6)

# ac = st.sidebar.slider("AC", 0, 3, 1)
# ac_h = st.sidebar.slider("AC hours/day", 0, 24, 5)

# tv = st.sidebar.slider("TV", 0, 5, 1)
# tv_h = st.sidebar.slider("TV hours/day", 0, 24, 4)

# iron_h = st.sidebar.slider("Iron usage (hours/day)", 0, 5, 1)

# wm_h = st.sidebar.slider("Washing Machine (hours/day)", 0, 5, 1)

# fridge_on = st.sidebar.checkbox("Refrigerator (24 hrs)", True)
# pump_h = st.sidebar.slider("Water Pump (hours/day)", 0, 5, 1)

# # -------------------------------
# # Consumption Calculation
# # -------------------------------
# data = {
#     "Fan": fan * appliance_power["Fan"] * fan_h / 1000,
#     "Light": light * appliance_power["Light"] * light_h / 1000,
#     "AC": ac * appliance_power["AC"] * ac_h / 1000,
#     "TV": tv * appliance_power["TV"] * tv_h / 1000,
#     "Iron": appliance_power["Iron"] * iron_h / 1000,
#     "Washing Machine": appliance_power["Washing Machine"] * wm_h / 1000,
#     "Refrigerator": appliance_power["Refrigerator"] * 24 / 1000 if fridge_on else 0,
#     "Water Pump": appliance_power["Water Pump"] * pump_h / 1000
# }

# df = pd.DataFrame(list(data.items()), columns=["Appliance", "Daily kWh"])

# total_kwh = df["Daily kWh"].sum()
# monthly_units = total_kwh * 30

# # -------------------------------
# # Slab-Based Billing Function
# # -------------------------------
# def calculate_bill(units):
#     bill = 0

#     if units <= 100:
#         bill = units * 20
#     elif units <= 200:
#         bill = (100 * 20) + (units - 100) * 30
#     elif units <= 300:
#         bill = (100 * 20) + (100 * 30) + (units - 200) * 40
#     else:
#         bill = (100 * 20) + (100 * 30) + (100 * 40) + (units - 300) * 50

#     return bill

# monthly_bill = calculate_bill(monthly_units)

# # -------------------------------
# # Layout
# # -------------------------------
# col1, col2 = st.columns(2)

# with col1:
#     st.subheader("📊 Energy Usage Breakdown")
#     st.bar_chart(df.set_index("Appliance"))

# with col2:
#     st.subheader("💰 Bill Summary")
#     st.metric("Daily Consumption", f"{total_kwh:.2f} kWh")
#     st.metric("Monthly Units", f"{monthly_units:.0f} Units")
#     st.metric("Estimated Bill", f"Rs. {monthly_bill:,.0f}")

# # -------------------------------
# # Tips Section
# # -------------------------------
# st.markdown("---")
# st.subheader("💡 Tips to Reduce Electricity Bill")

# tips = [
#     "Use energy saver (LED) bulbs",
#     "Limit AC usage to 6–8 hours",
#     "Unplug devices when not in use",
#     "Use inverter appliances",
#     "Avoid using iron during peak hours"
# ]

# for tip in tips:
#     st.write("✔️", tip)

# # -------------------------------
# # Footer
# # -------------------------------
# st.markdown("---")
# st.caption("Based on estimated slab rates in Pakistan. Actual bills may vary.")
