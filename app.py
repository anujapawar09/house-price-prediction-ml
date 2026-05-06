import streamlit as st
import pickle
import pandas as pd

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="HomeValue AI",
    page_icon="🏠",
    layout="centered"
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500&display=swap');

/* ── Root & Reset ── */
:root {
    --cream:   #F5F0E8;
    --sand:    #E8DFD0;
    --brown:   #8B6F47;
    --dark:    #1C1712;
    --charcoal:#2D2520;
    --gold:    #C8973A;
    --gold-lt: #E8B85A;
    --rust:    #A0522D;
    --white:   #FDFAF6;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--dark) !important;
    color: var(--cream) !important;
}

.stApp {
    background: linear-gradient(160deg, #1C1712 0%, #2D2520 50%, #1A1510 100%) !important;
    min-height: 100vh;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding-top: 2rem !important;
    padding-bottom: 3rem !important;
    max-width: 620px !important;
}

/* ── Hero section ── */
.hero {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
    position: relative;
}
.hero-icon {
    font-size: 3rem;
    display: block;
    margin-bottom: 0.5rem;
    filter: drop-shadow(0 0 20px rgba(200, 151, 58, 0.4));
}
.hero h1 {
    font-family: 'DM Serif Display', serif;
    font-size: 2.8rem;
    font-weight: 400;
    color: var(--cream) !important;
    margin: 0 0 0.25rem;
    line-height: 1.1;
    letter-spacing: -0.02em;
}
.hero h1 em {
    font-style: italic;
    color: var(--gold) !important;
}
.hero-sub {
    font-size: 0.95rem;
    color: var(--brown) !important;
    font-weight: 300;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-top: 0.5rem;
}
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
    margin: 1.5rem auto;
    opacity: 0.4;
    max-width: 300px;
}

/* ── Card ── */
.card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(200, 151, 58, 0.15);
    border-radius: 16px;
    padding: 2rem;
    backdrop-filter: blur(4px);
    margin-bottom: 1.2rem;
}
.card-label {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    color: var(--gold) !important;
    font-weight: 500;
    margin-bottom: 0.4rem;
    display: block;
}

/* ── Number input override ── */
.stNumberInput > div > div > input {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(200,151,58,0.25) !important;
    border-radius: 10px !important;
    color: var(--cream) !important;
    font-family: 'DM Serif Display', serif !important;
    font-size: 1.6rem !important;
    padding: 0.6rem 1rem !important;
    text-align: center !important;
    transition: border-color 0.2s;
}
.stNumberInput > div > div > input:focus {
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 2px rgba(200,151,58,0.15) !important;
}
.stNumberInput label {
    display: none !important;
}

/* ── Selectbox (bedrooms) ── */
.stSelectbox > div > div {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(200,151,58,0.25) !important;
    border-radius: 10px !important;
    color: var(--cream) !important;
}
.stSelectbox > div > div:hover {
    border-color: var(--gold) !important;
}
.stSelectbox label { display: none !important; }

/* ── Slider ── */
.stSlider [data-baseweb="slider"] div[role="slider"] {
    background: var(--gold) !important;
    border-color: var(--gold) !important;
}
.stSlider [data-baseweb="slider"] div[data-testid="stThumbValue"] {
    color: var(--gold) !important;
}
.stSlider label { display: none !important; }

/* ── Predict button ── */
.stButton > button {
    width: 100% !important;
    background: linear-gradient(135deg, var(--gold) 0%, var(--gold-lt) 100%) !important;
    color: var(--dark) !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.85rem 2rem !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.06em !important;
    text-transform: uppercase !important;
    cursor: pointer !important;
    transition: all 0.2s !important;
    margin-top: 0.5rem !important;
    box-shadow: 0 4px 20px rgba(200,151,58,0.25) !important;
}
.stButton > button:hover {
    box-shadow: 0 6px 28px rgba(200,151,58,0.45) !important;
    transform: translateY(-1px) !important;
}
.stButton > button:active {
    transform: translateY(0) !important;
}

/* ── Result box ── */
.result-box {
    background: linear-gradient(135deg, rgba(200,151,58,0.08) 0%, rgba(200,151,58,0.02) 100%);
    border: 1px solid rgba(200,151,58,0.35);
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    margin-top: 1.2rem;
    animation: fadeUp 0.5s ease;
}
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0); }
}
.result-label {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    color: var(--brown);
    margin-bottom: 0.6rem;
}
.result-price {
    font-family: 'DM Serif Display', serif;
    font-size: 3.2rem;
    color: var(--gold);
    line-height: 1;
    margin: 0;
}
.result-unit {
    font-size: 0.85rem;
    color: var(--brown);
    margin-top: 0.4rem;
    font-weight: 300;
}
.result-bar {
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
    margin: 1rem auto 0;
    opacity: 0.5;
    width: 60%;
}

/* ── Area display ── */
.area-display {
    font-family: 'DM Serif Display', serif;
    font-size: 2.5rem;
    color: var(--cream);
    text-align: center;
    padding: 0.5rem 0;
    letter-spacing: -0.01em;
}
.area-unit {
    font-size: 0.85rem;
    color: var(--brown);
    font-family: 'DM Sans', sans-serif;
    text-align: center;
    margin-top: -0.5rem;
    margin-bottom: 0.5rem;
}

/* ── Footer ── */
.footer {
    text-align: center;
    padding: 2rem 0 0.5rem;
    font-size: 0.75rem;
    color: rgba(139, 111, 71, 0.6);
    letter-spacing: 0.06em;
}
.footer strong {
    color: var(--gold);
    font-weight: 400;
}

/* ── Info note ── */
.note {
    font-size: 0.78rem;
    color: rgba(139,111,71,0.7);
    text-align: center;
    padding: 0.8rem 0 0;
    font-style: italic;
}
</style>
""", unsafe_allow_html=True)


# ── Load model ────────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    try:
        with open("models/model.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None

model = load_model()


# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <span class="hero-icon">🏠</span>
    <h1>Home<em>Value</em> AI</h1>
    <p class="hero-sub">Intelligent price estimation · Linear Regression</p>
</div>
<div class="divider"></div>
""", unsafe_allow_html=True)


# ── Area input ────────────────────────────────────────────────────────────────
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<span class="card-label">📐 Property Area</span>', unsafe_allow_html=True)

area = st.slider("area_slider", min_value=500, max_value=5000, step=50,
                 value=1500, label_visibility="collapsed")

st.markdown(f'<div class="area-display">{area:,}</div>', unsafe_allow_html=True)
st.markdown('<div class="area-unit">square feet</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# ── Bedrooms input ────────────────────────────────────────────────────────────
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<span class="card-label">🛏️ Number of Bedrooms</span>', unsafe_allow_html=True)

bedrooms = st.selectbox(
    "bedrooms_select",
    options=[1, 2, 3, 4, 5, 6],
    format_func=lambda x: f"{x} BHK",
    index=2,
    label_visibility="collapsed"
)

st.markdown(f'<div class="area-display" style="font-size:2rem;">{bedrooms} BHK</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# ── Predict button ────────────────────────────────────────────────────────────
predict = st.button("✦  Estimate Price")


# ── Result ────────────────────────────────────────────────────────────────────
if predict:
    if model is None:
        # Demo mode — show a plausible price
        demo_price = round((area * 0.045) + (bedrooms * 3.5) + 10, 2)
        st.markdown(f"""
        <div class="result-box">
            <div class="result-label">Estimated Market Value</div>
            <div class="result-price">₹ {demo_price:.2f}</div>
            <div class="result-unit">Lakhs &nbsp;·&nbsp; {area:,} sq ft &nbsp;·&nbsp; {bedrooms} BHK</div>
            <div class="result-bar"></div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<p class="note">⚠ Model file not found — showing demo estimate. Add models/model.pkl to activate.</p>',
                    unsafe_allow_html=True)
    else:
        input_df  = pd.DataFrame([[area, bedrooms]], columns=["area", "bedrooms"])
        predicted = model.predict(input_df)[0]
        st.markdown(f"""
        <div class="result-box">
            <div class="result-label">Estimated Market Value</div>
            <div class="result-price">₹ {predicted:.2f}</div>
            <div class="result-unit">Lakhs &nbsp;·&nbsp; {area:,} sq ft &nbsp;·&nbsp; {bedrooms} BHK</div>
            <div class="result-bar"></div>
        </div>
        """, unsafe_allow_html=True)


# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    Built by <strong>Anuja Pawar</strong> &nbsp;·&nbsp;
    <a href="https://github.com/anujapawar09" style="color:#C8973A; text-decoration:none;">github.com/anujapawar09</a>
</div>
""", unsafe_allow_html=True)