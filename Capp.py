# GAME SPESIAL BUAT VERA/PEYA 💙
# by: Erza Malviano - STREAMLIT VERSION FINAL
# Background: MAROON ELEGAN

import streamlit as st
import time

# ============== KONFIGURASI HALAMAN ==============
st.set_page_config(
    page_title="Game kecil-kecilan Buat Kamu 🩶",
    page_icon="🎮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============== CSS BACKGROUND MAROON ==============
st.markdown("""
<style>
    /* Background utama MAROON */
    .stApp {
        background-color: #800000 !important;
        background-image: linear-gradient(145deg, #800000 0%, #660000 100%) !important;
    }
    
    /* Semua teks jadi putih biar kontras */
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, h5, h6, 
    .stTextInput label, .stNumberInput label, .stSelectbox label {
        color: white !important;
    }
    
    /* Styling input box */
    .stTextInput input {
        background-color: rgba(255, 255, 255, 0.15) !important;
        color: white !important;
        border: 2px solid #b22222 !important;
        border-radius: 10px !important;
        padding: 10px !important;
        font-size: 16px !important;
    }
    
    .stTextInput input:focus {
        border-color: #ff6b6b !important;
        box-shadow: 0 0 10px rgba(255, 107, 107, 0.5) !important;
    }
    
    /* Styling button */
    .stButton button {
        background-color: #b22222 !important;
        color: white !important;
        border: 2px solid #ff6b6b !important;
        border-radius: 20px !important;
        padding: 10px 25px !important;
        font-weight: bold !important;
        transition: all 0.3s !important;
    }
    
    .stButton button:hover {
        background-color: #ff6b6b !important;
        border-color: white !important;
        transform: scale(1.05) !important;
    }
    
    /* Kotak pesan spesial */
    .pesan-box {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 30px;
        border: 2px solid #b22222;
        backdrop-filter: blur(5px);
        margin: 20px 0;
    }
    
    /* Garis pembatas */
    hr {
        border-color: #b22222 !important;
        border-width: 2px !important;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: rgba(255, 255, 255, 0.05);
        padding: 10px;
        border-radius: 20px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: transparent !important;
        color: white !important;
        border-radius: 15px !important;
        padding: 8px 20px !important;
        font-weight: bold !important;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #b22222 !important;
    }
    
    /* Success/warning boxes */
    .stAlert {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border-left-color: #b22222 !important;
    }
    
    /* Footer */
    footer {
        color: rgba(255, 255, 255, 0.5) !important;
    }
</style>
""", unsafe_allow_html=True)

# ============== FUNGSI EFEK ==============
def tulis_perlahan(teks, delay=0.02):
    placeholder = st.empty()
    hasil = ""
    for karakter in teks:
        hasil += karakter
        placeholder.markdown(f"<p style='font-size:18px; color:white;'>{hasil}</p>", unsafe_allow_html=True)
        time.sleep(delay)
    return hasil

def garis():
    st.markdown("---")

# ============== GAME 1: MATEMATIKA (FIXED) ==============
def game_matematika():
    st.markdown("## 🧮 GAME 1: MATEMATIKA")
    garis()
    time.sleep(0.5)
    
    tulis_perlahan("Hai sayang... siap main matematika?")
    time.sleep(0.5)
    tulis_perlahan("Pasti kamu siap banget😂")
    tulis_perlahan("Jawab sebisa kamu aja sayang, yang penting diisi")
    
    # Inisialisasi session state
    if 'math_skor' not in st.session_state:
        st.session_state.math_skor = 0
        st.session_state.math_soal_terjawab = [False, False, False, False]
    
    # SOAL 1
    st.markdown("---")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("**Soal 1: 1 + 2 = ?**")
    with col2:
        if st.session_state.math_soal_terjawab[0]:
            st.success("✅ Sudah Dijawab")
    
    if not st.session_state.math_soal_terjawab[0]:
        jawab1 = st.text_input("Jawaban soal 1:", key="math1")
        if jawab1:
            if jawab1 == "3":
                st.success("✅ Kacaw keren! pinter juga nih mermaid")
                st.session_state.math_skor += 1
                st.session_state.math_soal_terjawab[0] = True
            else:
                st.warning("❌ Coba lagi sayang, pasti bisa. 1+2 = 3 ya")
    
    # SOAL 2
    if st.session_state.math_soal_terjawab[0]:
        st.markdown("---")
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("**Soal 2: 5 - 2 = ?**")
        with col2:
            if st.session_state.math_soal_terjawab[1]:
                st.success("✅ Sudah Dijawab")
        
        if not st.session_state.math_soal_terjawab[1]:
            jawab2 = st.text_input("Jawaban soal 2:", key="math2")
            if jawab2:
                if jawab2 == "3":
                    st.success("✅ Widih jago amat! udah kayak profesor 🎓")
                    st.session_state.math_skor += 1
                    st.session_state.math_soal_terjawab[1] = True
                else:
                    st.warning("❌ Yok cobain lagi. 5-2 = 3, inget ya sayang")
    
    # SOAL 3
    if st.session_state.math_soal_terjawab[1]:
        st.markdown("---")
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("**Soal 3: 5 × 5 = ?**")
        with col2:
            if st.session_state.math_soal_terjawab[2]:
                st.success("✅ Udah dijawab")
        
        if not st.session_state.math_soal_terjawab[2]:
            jawab3 = st.text_input("Jawaban soal 3:", key="math3")
            if jawab3:
                if jawab3 == "25":
                    st.success("✅ Anjayy! pinter amat")
                    st.session_state.math_skor += 1
                    st.session_state.math_soal_terjawab[2] = True
                else:
                    st.warning("❌ Gapapa sayang, 5×5 = 25. Aku tetep bangga sama kamu")
    
    # SOAL 4
    if st.session_state.math_soal_terjawab[2]:
        st.markdown("---")
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("**Soal 4: 6 ÷ 3 = ?**")
        with col2:
            if st.session_state.math_soal_terjawab[3]:
                st.success("✅ Udah dijawab")
        
        if not st.session_state.math_soal_terjawab[3]:
            jawab4 = st.text_input("Jawaban soal 4:", key="math4")
            if jawab4:
                if jawab4 == "2":
                    st.success("✅ Pinter banget! 100 buat kamu")
                    st.session_state.math_skor += 1
                    st.session_state.math_soal_terjawab[3] = True
                else:
                    st.warning("❌ 6÷3 = 2 ya sayangg")
    
    # SOAL TERAKHIR (setelah semua soal terjawab)
    if all(st.session_state.math_soal_terjawab):
        st.markdown("---")
        st.markdown("### 🔥 SOAL TERAKHIR (jawab aja sebisa kamu sayang):")
        st.markdown("### 123 × 456 × 789 = ?")
        
        if 'math_akhir_terjawab' not in st.session_state:
            st.session_state.math_akhir_terjawab = False
        
        if not st.session_state.math_akhir_terjawab:
            jawab_akhir = st.text_input("Jawaban kamu:", key="math_akhir")
            if jawab_akhir:
                st.session_state.math_akhir_terjawab = True
                
                st.markdown("""
                <div class='pesan-box'>
                    <h3 style='text-align:center; color:white;'>JAWABAN KAMU SALAH, TAPI GAPAPA ❌</h3>
                </div>
                """, unsafe_allow_html=True)
                
                tulis_perlahan("Karena di dunia ini,")
                tulis_perlahan("Ada hal-hal yang ga perlu dihitung tepat.")
                tulis_perlahan("kayak seberapa besar rasa sayang aku ke kamu.")
                tulis_perlahan("Ga akan cukup angka 123 × 456 × 789...")
                tulis_perlahan("Bahkan infinity sekalipun")
                
                st.markdown("""
                <div style='text-align:center; margin:30px 0;'>
                    <h2 style='color:white;'>🩶 Rasa sayang aku ke kamu = ∞</h2>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"### Skor kamu: {st.session_state.math_skor}/4")
                if st.session_state.math_skor == 4:
                    st.balloons()
                    st.success("🎉 Kerenn! Kamu pinter banget")
                elif st.session_state.math_skor >= 2:
                    st.info("👍 Mantap! pinter banget cewe nya si erza.")
                else:
                    st.info("Gapapa sayang, yang penting udah berusaha")

# ============== GAME 2: TEBAK KATA (FIXED) ==============
def game_tebak_kata():
    st.markdown("## 🧩 GAME 2: SATUIN KATA")
    garis()
    time.sleep(0.5)
    
    st.markdown("Nah sekarang tebak kata yang saling berkaitan")
    st.markdown("Contoh: **Amplop** sama... **perangko**")
    st.markdown("Sekarang giliran kamu")
    
    # Inisialisasi session state
    if 'tebak_progress' not in st.session_state:
        st.session_state.tebak_progress = 0
        st.session_state.tebak_jawaban = ["", "", "", "", ""]
    
    soal_kata = [
        {"soal": "Handphone sama...", "jawab": "charger", 
         "benar": "Nah bener! Pinter banget sayang",
         "salah": "Coba tebak lagi sayang... hp kalo abis baterai butuh apa?"},
        
        {"soal": "Dompet sama...", "jawab": ["uang" "duit"], 
         "benar": "Buset, lancar banget kalo soal uang 💰",
         "salah": "Dompet isi nya apa sayang? biar bisa beli naspad"},
        
        {"soal": "Buku sama...", "jawab": "pulpen", 
         "benar": "Keren! kamu pinter banget",
         "salah": "Buku tulis sama... yang ada tinta nya"},
        
        {"soal": "Matahari sama...", "jawab": "bulan", 
         "benar": "Nah bener sayangg ☀️🌙",
         "salah": "Sinar di siang hari, terang di malam hari..."},
        
        {"soal": "Pantai sama...", "jawab": "laut", 
         "benar": "ga usah remed sayang, kamu keturunan mermaid dari lahir",
         "salah": "Pantai itu deket sama... tempat mermaid tinggal"}
    ]
    
    # Tampilkan soal sesuai progress
    for i in range(len(soal_kata)):
        if i <= st.session_state.tebak_progress:
            st.markdown("---")
            st.markdown(f"**Soal {i+1}: {soal_kata[i]['soal']}**")
            
            if i < st.session_state.tebak_progress:
                # Soal sudah dijawab
                st.success(f"✅ {soal_kata[i]['benar']}")
            
            elif i == st.session_state.tebak_progress:
                # Soal sedang aktif
                jawaban = st.text_input("Jawaban kamu:", key=f"tebak_{i}")
                if jawaban:
                    if jawaban.lower() in [soal_kata[i]['jawab'], soal_kata[i]['jawab'] + "an"]:
                        st.success(f"✅ {soal_kata[i]['benar']}")
                        st.session_state.tebak_progress += 1
                        st.session_state.tebak_jawaban[i] = jawaban
                        st.rerun()
                    else:
                        st.warning(f"❌ {soal_kata[i]['salah']}")
    
    # Setelah semua soal terjawab
    if st.session_state.tebak_progress >= len(soal_kata):
        st.markdown("---")
        st.markdown("### 🌟 SOAL TERAKHIR: Aku sama... ?")
        
        if 'tebak_akhir_terjawab' not in st.session_state:
            st.session_state.tebak_akhir_terjawab = False
        
        if not st.session_state.tebak_akhir_terjawab:
            jawaban_akhir = st.text_input("Jawaban kamu:", key="tebak_akhir")
            if jawaban_akhir:
                st.session_state.tebak_akhir_terjawab = True
                st.session_state.tebak_akhir_jawab = jawaban_akhir.lower()
                st.rerun()
        
        else:
            jawaban_akhir = st.session_state.tebak_akhir_jawab
            
            if jawaban_akhir in ["kamu", "you", "sayang", "cinta", "erza"]:
                st.balloons()
                st.markdown("""
                <div class='pesan-box'>
                    <h3 style='text-align:center;'>🎉 JAWABAN KAMU BENAR! 🎉</h3>
                </div>
                """, unsafe_allow_html=True)
                
                tulis_perlahan("Dari sekian banyak pasangan kata di dunia,")
                tulis_perlahan("Yang paling pas cuman 'Aku' dan 'Kamu'.")
                tulis_perlahan("Kayak amplop sama perangko,")
                tulis_perlahan("Handphone sama charger,")
                tulis_perlahan("Dompet sama ["uang","duit"]...")
                tulis_perlahan("Kita berdua saling melengkapi.")
            else:
                st.info(f"Apapun jawaban kamu ('{jawaban_akhir}'), yang jelas aku sama KAMU itu yang paling cocok")
        
        # Soal BONUS
        st.markdown("---")
        st.markdown("###SOAL BONUS: Erza sama... ?")
        
        if 'tebak_bonus_terjawab' not in st.session_state:
            st.session_state.tebak_bonus_terjawab = False
        
        if not st.session_state.tebak_bonus_terjawab:
            jawaban_bonus = st.text_input("Jawaban bonus:", key="tebak_bonus")
            if jawaban_bonus:
                st.session_state.tebak_bonus_terjawab = True
                st.session_state.tebak_bonus_jawab = jawaban_bonus.lower()
                st.rerun()
        
        else:
            if st.session_state.tebak_bonus_jawab in ["peya", "vera", "mermaid", "sayang","aku"]:
                st.success("Anjay bener! salah ga mungkin, bener udah pasti")
                st.balloons()
            else:
                st.info("Apapun jawaban kamu, kamu tetap spesial🩶")

# ============== PESAN SPESIAL ==============
def pesan_spesial():
    st.markdown("## 💌 PESAN SPESIAL BUAT KAMU")
    garis()
    
    st.markdown("""
    <div class='pesan-box'>
        <h3 style='text-align:center;'>Hai sayang...</h3>
    </div>
    """, unsafe_allow_html=True)
    
    time.sleep(1)
    
    pesan = [
        "Hidup itu kayak game tadi.",
        "Ada soal yang gampang, ada yang susah.",
        "Ada jawaban yang bener, ada yang salah.",
        "Tapi yang penting, kamu udah berusaha dan terus maju",
        "",
        "Jangan pernah ngerasa sendirian.",
        "Jangan pernah berkecil hati",
        "Kalo kamu gagal dalam suatu hal,",
        "Inget, aku selalu ngedukung kamu.",
        "walaupun kamu gagal dalam suatu hal,",
        "Aku bakal tetep bangga sama kamu,",
        "karna kamu udah berusaha buat dapet hasil yang terbaik.",
        "",
        "Kalo kamu cape, istirahat dulu.",
        "Kalo kamu nangis, gapapa.",
        "Kalo kamu salah, perbaiki.",
        "Kalo kamu mau nyerah...",
        "Inget ada aku yang percaya kamu bisa.",
        "",
        "Kamu itu kuat.",
        "Kamu itu bijak.",
        "Kamu itu pinter.",
        "Jadi kamu ga boleh nyerah ya sayang.",
        "Semangat sayang.",
    ]
    
    for baris in pesan:
        if baris:
            tulis_perlahan(baris)
            time.sleep(0.2)
        else:
            st.markdown("")
            time.sleep(0.5)
    
    st.markdown("""
    <div class='pesan-box' style='text-align:center; margin-top:30px;'>
        <h2>Semangat sayangg, aku bakal selalu support kamu.</h2>
        <p style='margin-top:20px;'>~ Dari fans sejati pak Jokowi si pria Solo</p>
        <h3> Erza</h3>
    </div>
    """, unsafe_allow_html=True)

# ============== FUNGSI UTAMA ==============
def main():
    # Header
    st.markdown("""
    <h1 style='text-align:center; color:white; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);'>
        GAME SPESIAL BUAT MERMAID 🎮
    </h1>
    """, unsafe_allow_html=True)
    
    # Input nama
    nama = st.text_input("Halo, namanya siapa?")
    
    if nama:
        if nama.lower() in ["vera", "peya"]:
            st.success(f"Halo sayangg..")
            st.markdown("Aku punya 3 game kecil-kecilan buat kamu!")
            
            # Tabs untuk 3 game
            tab1, tab2, tab3 = st.tabs(["🧮 Matematika", "🧩 Tebak Kata", "💌 Pesan Spesial"])
            
            with tab1:
                game_matematika()
            
            with tab2:
                game_tebak_kata()
            
            with tab3:
                pesan_spesial()
            
            # Footer
            st.markdown("---")
            st.markdown("""
            <div style='text-align:center; margin:50px 0;'>
                <h3>Makasih udah mau main</h3>
                <h4>Love you, sayang 🩶</h4>
            </div>
            """, unsafe_allow_html=True)
            
        else:
            st.error("""
            ## ❌ AKSES DITOLAK ❌
            
            Sorry mas bro, game ini hanya untuk Vera atau Peya. Selain Vera atau Peya ga boleh akses
            """)

# ============== JALANKAN PROGRAM ==============
if __name__ == "__main__":
    main()