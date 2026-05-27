try:
    import streamlit as st
    import streamlit.components.v1 as components
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "Streamlit belum terinstall. Jalankan: pip install streamlit"
    )

import time

# ====================================
# KONFIGURASI HALAMAN
# ====================================

st.set_page_config(
    page_title="Simulasi Gas Ideal Interaktif",
    layout="centered"
)

# ====================================
# JUDUL
# ====================================

st.title("Simulasi Gas Ideal Interaktif")

st.write("""
Aplikasi ini menghitung massa jenis gas menggunakan persamaan gas ideal.

Pengguna dapat mengubah:
- tekanan (atm)
- suhu (K)
- Bobot Molekul gas (g/mol)
""")

# ====================================
# INPUT PENGGUNA
# ====================================

st.subheader("⚙️ Input Variabel")

P = st.slider(
    "Tekanan Gas (atm)",
    0.1,
    10.0,
    2.0,
    0.1
)

T = st.slider(
    "Suhu Gas (K)",
    100,
    1000,
    298
)

M = st.number_input(
    "Bobot Molekul Gas (g/mol)",
    value=32.0
)

R = 0.082

# ====================================
# KECEPATAN ANIMASI
# ====================================

kecepatan = max(1, 12 - (T / 100))

# ====================================
# PENJELASAN
# ====================================

st.info(
    f"""
Tekanan = {P} atm

Suhu = {T} K

Bobot Molekul = {M} g/mol

Semakin tinggi suhu, partikel bergerak semakin cepat.
"""
)

# ====================================
# HTML + CSS ANIMASI
# ====================================

html_code = f"""
<!DOCTYPE html>
<html>

<head>

<style>

body {{
    margin:0;
    overflow:hidden;
    background-color:transparent;
}}

.kotak {{
    width:100%;
    height:420px;

    position:relative;
    overflow:hidden;

    border-radius:20px;

    background:
    radial-gradient(circle,
    #1e3a8a,
    #020617);

    border:2px solid cyan;

    box-shadow:
    0px 0px 25px rgba(0,255,255,0.4);
}}

.bola {{

    width:18px;
    height:18px;

    position:absolute;

    border-radius:50%;

    background:cyan;

    box-shadow:
    0 0 15px cyan,
    0 0 30px cyan;
}}

.b1 {{
    animation: gerak1 {kecepatan}s linear infinite alternate;
}}

.b2 {{
    animation: gerak2 {kecepatan*0.8}s linear infinite alternate;
}}

.b3 {{
    animation: gerak3 {kecepatan*1.2}s linear infinite alternate;
}}

.b4 {{
    animation: gerak4 {kecepatan*0.6}s linear infinite alternate;
}}

@keyframes gerak1 {{

    from {{
        transform: translate(0px,0px);
    }}

    to {{
        transform: translate(320px,240px);
    }}
}}

@keyframes gerak2 {{

    from {{
        transform: translate(0px,200px);
    }}

    to {{
        transform: translate(280px,-60px);
    }}
}}

@keyframes gerak3 {{

    from {{
        transform: translate(150px,0px);
    }}

    to {{
        transform: translate(-120px,250px);
    }}
}}

@keyframes gerak4 {{

    0% {{
        transform: translate(0px,0px);
    }}

    25% {{
        transform: translate(220px,50px);
    }}

    50% {{
        transform: translate(100px,220px);
    }}

    75% {{
        transform: translate(260px,130px);
    }}

    100% {{
        transform: translate(50px,260px);
    }}
}}

</style>

</head>

<body>

<div class="kotak">

    <div class="bola b1"
    style="left:20px; top:20px;">
    </div>

    <div class="bola b2"
    style="left:80px; top:100px;">
    </div>

    <div class="bola b3"
    style="left:180px; top:150px;">
    </div>

    <div class="bola b4"
    style="left:300px; top:80px;">
    </div>

    <div class="bola b1"
    style="left:400px; top:200px;">
    </div>

    <div class="bola b2"
    style="left:520px; top:140px;">
    </div>

    <div class="bola b3"
    style="left:620px; top:240px;">
    </div>

    <div class="bola b4"
    style="left:700px; top:100px;">
    </div>

</div>

</body>
</html>
"""

# ====================================
# TAMPILKAN ANIMASI
# ====================================

st.subheader("🌌 Simulasi Pergerakan Partikel")

components.html(
    html_code,
    height=430
)

# ====================================
# PERSAMAAN GAS IDEAL
# ====================================

st.subheader("Persamaan Gas Ideal")

st.latex(r"PV = nRT")

st.write(
    "Untuk mencari massa jenis gas:"
)

st.latex(r"\rho = \frac{PM}{RT}")

# ====================================
# PERHITUNGAN OTOMATIS
# ====================================

hasil = (P * M) / (R * T)

# ====================================
# LANGKAH PERHITUNGAN
# ====================================

st.subheader("Langkah Perhitungan")

st.latex(
    rf"\rho = \frac{{({P})({M})}}{{({R})({T})}}"
)

st.latex(
    rf"\rho = {hasil:.2f}\ g/L"
)

# ====================================
# TOMBOL HASIL + kesimpulan
# ====================================

if st.button("✨ Tampilkan Hasil"):
    st.markdown(
    f"""
    <div style="
    background:linear-gradient(to right,#22c55e,#16a34a);
    padding:30px;
    border-radius:20px;
    color:white;
    box-shadow:0px 0px 25px rgba(0,255,0,0.5);
    animation: fadein 1s;
    ">

    <h1 style="
    text-align:center;
    font-size:40px;
    ">
    Massa Jenis Gas
    </h1>

    <hr>

    <h2 style="
    text-align:center;
    font-size:35px;
    ">
    {hasil:.2f} g/L
    </h2>

    <br>

    <h3> Kesimpulan</h3>

    <p style="font-size:20px; line-height:1.8;">

    Dengan:
    <br>
    • tekanan = {P} atm
    <br>
    • suhu = {T} K
    <br>
    • Bobot Molekul = {M} g/mol
    <br><br>

    maka massa jenis gas adalah:

    <b>{hasil:.2f} g/L</b>

    </p>

    </div>
    """,
    unsafe_allow_html=True
)

# ====================================
# TEST
# ====================================

assert hasil > 0, "Hasil tidak boleh negatif"
