import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Simulasi Pangan", page_icon="🍽️", layout="centered")

# Tambahkan background
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1504674900247-0877df9cc836");
        background-size: cover;
        background-attachment: fixed;
        color: white;
        text-shadow: 1px 1px 3px black;
    }
    .main {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2rem;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar menu
halaman = st.sidebar.selectbox("📚 Pilih Halaman:", ["Beranda", "Simulasi", "Tentang Kelompok"])

# ========================== DATA ==========================
data_makanan = {
    "🥚 Telur": {
        "reaksi": [
            (30, {
                "chef": "Telur mulai terasa hangat, belum ada perubahan nyata.",
                "analis": "Molekul protein mulai bergerak lebih cepat namun belum terjadi denaturasi.",
                "tingkat_kematangan": "-"
            }),
            (62, {
                "chef": "Putih telur mulai mengeras – tekstur setengah matang.",
                "analis": "Albumin mulai menggumpal karena denaturasi protein dimulai.",
                "tingkat_kematangan": "Setengah Matang"
            }),
            (70, {
                "chef": "Kuning telur mulai mengeras – telur matang sempurna.",
                "analis": "Lipovitellenin mengalami denaturasi, menyebabkan kuning mengeras.",
                "tingkat_kematangan": "Matang"
            })
        ],
        "penjelasan_analis": "Protein dalam telur mengalami denaturasi akibat panas.",
        "penjelasan_chef": "Untuk telur rebus sedang, rebus sekitar 6-8 menit pada suhu 70–80°C.",
        "fun_fact": "Memasak telur perlahan menghasilkan tekstur creamy sempurna!",
        "penyimpanan": {
            "suhu": "0-4°C",
            "masa_simpan": "3-5 minggu",
            "tips": "Simpan di karton asli, jangan di pintu kulkas."
        }
    },
        "🍬 Gula": {
        "reaksi": [
            (100, {
                "chef": "Gula mulai meleleh dan membentuk sirup.",
                "analis": "Pelelehan fisik gula sukrosa dimulai di atas 100°C.",
                "tingkat_kematangan": "-"
            }),
            (160, {
                "chef": "Gula berubah warna coklat – karamelisasi awal.",
                "analis": "Sukrosa mulai terurai dan membentuk senyawa aroma & warna baru.",
                "tingkat_kematangan": "Karamel"
            }),
            (180, {
                "chef": "Gula gosong – rasa pahit muncul.",
                "analis": "Pembakaran gula menghasilkan senyawa pahit dan asap.",
                "tingkat_kematangan": "Gosong"
            })
        ],
        "penjelasan_analis": "Karamelisasi terjadi saat sukrosa terurai karena panas.",
        "penjelasan_chef": "Untuk saus karamel, panaskan hingga 165–170°C tanpa diaduk terlalu banyak.",
        "fun_fact": "Karamelisasi menghasilkan rasa toffee khas kue dan permen!",
        "penyimpanan": {
            "suhu": "20-25°C",
            "masa_simpan": "18-24 bulan",
            "tips": "Simpan di wadah kedap udara agar tidak menggumpal."
        }
    },
    "🍗 Daging Ayam": {
        "reaksi": [
            (30, {
                "chef": "Daging ayam mulai terasa hangat, namun belum ada perubahan nyata.",
                "analis": "Protein dalam daging ayam mulai terurai secara perlahan.",
                "tingkat_kematangan": "-"
            }),
            (75, {
                "chef": "Daging ayam mulai matang, tekstur lebih padat.",
                "analis": "Proses denaturasi protein semakin jelas pada suhu ini.",
                "tingkat_kematangan": "Setengah Matang"
            }),
            (85, {
                "chef": "Daging ayam matang sempurna, kulit berwarna keemasan.",
                "analis": "Protein ayam terdenaturasi sepenuhnya, mengunci kelembapan.",
                "tingkat_kematangan": "Matang"
            })
        ],
        "penjelasan_analis": "Pemanasan menyebabkan protein pada daging ayam terurai dan menyatu.",
        "penjelasan_chef": "Panggang ayam pada suhu 180°C untuk kulit yang renyah dan daging yang juicy.",
        "fun_fact": "Daging ayam kaya akan protein tinggi dan rendah lemak.",
        "penyimpanan": {
            "suhu": "0-4°C",
            "masa_simpan": "1-2 hari",
            "tips": "Simpan ayam di dalam kantong kedap udara agar tetap segar."
        }
    },
    "🍍 Nanas": {
        "reaksi": [
            (30, {
                "chef": "Nanas mulai terasa sedikit lebih lembut.",
                "analis": "Enzim dalam nanas mulai terurai akibat panas.",
                "tingkat_kematangan": "-"
            }),
            (60, {
                "chef": "Nanas lebih lunak, rasa manis mulai muncul.",
                "analis": "Asam dan gula dalam nanas mulai terkaramelisasi.",
                "tingkat_kematangan": "Setengah Matang"
            }),
            (90, {
                "chef": "Nanas matang sempurna, tekstur menjadi lembut dan manis.",
                "analis": "Karbohidrat dalam nanas semakin terurai, memberikan rasa manis alami.",
                "tingkat_kematangan": "Matang"
            })
        ],
        "penjelasan_analis": "Proses pemanasan menyebabkan gula alami pada nanas terkaramelisasi.",
        "penjelasan_chef": "Panggang nanas dengan api kecil agar rasa manisnya keluar.",
        "fun_fact": "Nanas mengandung bromelain, yang membantu pencernaan.",
        "penyimpanan": {
            "suhu": "10-15°C",
            "masa_simpan": "1-2 minggu",
            "tips": "Simpan nanas di suhu kamar sampai matang, kemudian di kulkas."
        }
    },
    "🍓 Stroberi": {
        "reaksi": [
            (30, {
                "chef": "Stroberi mulai agak lebih lembut.",
                "analis": "Sel-sel stroberi mulai melepaskan cairan.",
                "tingkat_kematangan": "-"
            }),
            (60, {
                "chef": "Stroberi lebih lembut, warnanya semakin cerah.",
                "analis": "Proses pemanasan mulai merusak struktur sel dan melepaskan jus.",
                "tingkat_kematangan": "Setengah Matang"
            }),
            (80, {
                "chef": "Stroberi matang sempurna, tekstur lembut dan juicy.",
                "analis": "Panas mengeluarkan jus alami dari stroberi, membuatnya lebih manis.",
                "tingkat_kematangan": "Matang"
            })
        ],
        "penjelasan_analis": "Pemanasan menyebabkan sel stroberi pecah dan mengeluarkan cairannya.",
        "penjelasan_chef": "Stroberi cocok untuk dipanggang atau dipanaskan dalam saus.",
        "fun_fact": "Stroberi adalah sumber vitamin C yang sangat baik.",
        "penyimpanan": {
            "suhu": "0-4°C",
            "masa_simpan": "2-4 hari",
            "tips": "Simpan stroberi dalam wadah terbuka agar tetap segar."
        }
    },
    "🍉 Semangka": {
        "reaksi": [
            (30, {
                "chef": "Semangka mulai terasa sedikit lebih lembut.",
                "analis": "Sel-sel semangka mulai terpengaruh oleh panas.",
                "tingkat_kematangan": "-"
            }),
            (60, {
                "chef": "Semangka semakin lembut dan cairan mulai keluar.",
                "analis": "Proses pemanasan menyebabkan pelepasan cairan lebih banyak.",
                "tingkat_kematangan": "Setengah Matang"
            }),
            (90, {
                "chef": "Semangka matang sempurna, tekstur menjadi lembut dan juicy.",
                "analis": "Pemanasan mengaktifkan karbohidrat dalam semangka, meningkatkan rasa manis.",
                "tingkat_kematangan": "Matang"
            })
        ],
        "penjelasan_analis": "Pemanasan menyebabkan sel semangka pecah dan melepaskan cairan manis.",
        "penjelasan_chef": "Semangka cocok dipanaskan untuk membuat sup buah atau hidangan manis.",
        "fun_fact": "Semangka mengandung banyak air dan sangat menyegarkan.",
        "penyimpanan": {
            "suhu": "10-15°C",
            "masa_simpan": "1 minggu",
            "tips": "Simpan di suhu kamar hingga matang, kemudian di kulkas."
        }
    },
    "🥒 Mentimun": {
        "reaksi": [
            (30, {
                "chef": "Mentimun mulai sedikit lebih lembut.",
                "analis": "Sel-sel dalam mentimun mulai melepaskan cairan.",
                "tingkat_kematangan": "-"
            }),
            (60, {
                "chef": "Mentimun semakin lembut dan lebih juicy.",
                "analis": "Sel-sel mentimun mengalami perubahan tekstur.",
                "tingkat_kematangan": "Setengah Matang"
            }),
            (80, {
                "chef": "Mentimun matang, tekstur lebih lembut.",
                "analis": "Panas menyebabkan perubahan selulosa dalam mentimun.",
                "tingkat_kematangan": "Matang"
            })
        ],
        "penjelasan_analis": "Pemanasan memecah selulosa dalam mentimun, menghasilkan tekstur yang lebih lembut.",
        "penjelasan_chef": "Mentimun bisa dipanaskan untuk saus atau salad segar.",
        "fun_fact": "Mentimun memiliki kandungan air yang sangat tinggi, menjadikannya penyegar alami.",
        "penyimpanan": {
            "suhu": "5-10°C",
            "masa_simpan": "5-7 hari",
            "tips": "Simpan mentimun dalam kantong plastik agar tetap segar lebih lama."
        }
    },
    "🥑 Alpukat": {
        "reaksi": [
            (30, {
                "chef": "Alpukat mulai sedikit lebih lembut.",
                "analis": "Panas mulai mempengaruhi tekstur alpukat.",
                "tingkat_kematangan": "-"
            }),
            (60, {
                "chef": "Alpukat semakin lembut dan creamy.",
                "analis": "Lemak dalam alpukat mulai terurai dan lebih mudah dicerna.",
                "tingkat_kematangan": "Setengah Matang"
            }),
            (90, {
                "chef": "Alpukat matang sempurna, tekstur sangat creamy.",
                "analis": "Lemak dalam alpukat mencapai konsistensi sempurna.",
                "tingkat_kematangan": "Matang"
            })
        ],
        "penjelasan_analis": "Panas menyebabkan perubahan pada lemak sehat dalam alpukat.",
        "penjelasan_chef": "Alpukat terbaik digunakan pada suhu kamar untuk tekstur lembut.",
        "fun_fact": "Alpukat kaya akan lemak sehat dan vitamin E.",
        "penyimpanan": {
            "suhu": "5-10°C",
            "masa_simpan": "2-4 hari",
            "tips": "Simpan alpukat pada suhu kamar hingga matang, lalu pindahkan ke kulkas."
        }
    },
    "🥥 Kelapa": {
        "reaksi": [
            (30, {
                "chef": "Kelapa mulai sedikit lebih lembut.",
                "analis": "Panas mulai mengubah tekstur daging kelapa.",
                "tingkat_kematangan": "-"
            }),
            (60, {
                "chef": "Daging kelapa semakin lembut, lebih mudah diparut.",
                "analis": "Kandungan air dalam kelapa mulai berkurang.",
                "tingkat_kematangan": "Setengah Matang"
            }),
            (90, {
                "chef": "Kelapa matang sempurna, daging menjadi kering dan mudah dikeluarkan.",
                "analis": "Proses pemanasan mengurangi kandungan air dalam kelapa.",
                "tingkat_kematangan": "Matang"
            })
        ],
        "penjelasan_analis": "Panas mengurangi kadar air dalam kelapa dan mengubah teksturnya.",
        "penjelasan_chef": "Kelapa bisa diparut atau dipanggang untuk mendapatkan aroma khas.",
        "fun_fact": "Kelapa kaya akan serat dan minyak sehat.",
        "penyimpanan": {
            "suhu": "20-25°C",
            "masa_simpan": "1-2 minggu",
            "tips": "Simpan kelapa di tempat kering dan sejuk."
        }
    },
     "🥩 Daging Sapi": {
        "reaksi": [
            (30, {
                "chef": "Daging sapi mulai hangat, belum ada perubahan signifikan.",
                "analis": "Protein pada daging sapi mulai bergerak.",
                "tingkat_kematangan": "-"
            }),
            (60, {
                "chef": "Daging sapi mulai matang, tekstur lebih padat.",
                "analis": "Denaturasi protein daging sapi mulai terlihat.",
                "tingkat_kematangan": "Setengah Matang"
            }),
            (80, {
                "chef": "Daging sapi matang, permukaan berwarna coklat keemasan.",
                "analis": "Pemanasan terus mengubah struktur protein, menghasilkan tekstur kenyal.",
                "tingkat_kematangan": "Matang"
            })
        ],
        "penjelasan_analis": "Proses pemanasan mengubah struktur protein dan lemak pada daging sapi.",
        "penjelasan_chef": "Panggang daging sapi pada suhu 180°C agar hasilnya empuk dan lezat.",
        "fun_fact": "Daging sapi adalah sumber zat besi yang baik untuk tubuh.",
        "penyimpanan": {
            "suhu": "0-4°C",
            "masa_simpan": "1-3 hari",
            "tips": "Simpan daging sapi dalam wadah kedap udara di kulkas."
        }
    },
    "🍠 Ubi Jalar": {
        "reaksi": [
            (30, {
                "chef": "Ubi jalar mulai terasa hangat, belum ada perubahan signifikan.",
                "analis": "Karbohidrat dalam ubi jalar mulai terurai.",
                "tingkat_kematangan": "-"
            }),
            (60, {
                "chef": "Ubi jalar mulai lunak, tekstur lebih kenyal.",
                "analis": "Starch dalam ubi jalar mulai terhidrolisis.",
                "tingkat_kematangan": "Setengah Matang"
            }),
            (90, {
                "chef": "Ubi jalar matang sempurna, rasa manis muncul.",
                "analis": "Starch terkonversi menjadi gula alami, memberi rasa manis.",
                "tingkat_kematangan": "Matang"
            })
        ],
        "penjelasan_analis": "Pemanasan mengubah karbohidrat dalam ubi jalar menjadi gula alami.",
        "penjelasan_chef": "Panggang atau rebus ubi jalar hingga empuk dan manis.",
        "fun_fact": "Ubi jalar kaya akan vitamin A yang baik untuk penglihatan.",
        "penyimpanan": {
            "suhu": "15-18°C",
            "masa_simpan": "2-3 minggu",
            "tips": "Simpan ubi jalar di tempat yang sejuk dan kering."
        }
    },
    "🍅 Tomat": {
        "reaksi": [
            (30, {
                "chef": "Tomat mulai lembut, namun belum ada perubahan signifikan.",
                "analis": "Asam dalam tomat mulai terpengaruh oleh panas.",
                "tingkat_kematangan": "-"
            }),
            (60, {
                "chef": "Tomat semakin lembut, warnanya lebih cerah.",
                "analis": "Asam dalam tomat mulai terurai, meningkatkan rasa manis.",
                "tingkat_kematangan": "Setengah Matang"
            }),
            (80, {
                "chef": "Tomat matang sempurna, tekstur lembut dan penuh rasa.",
                "analis": "Asam dalam tomat sudah terurai sepenuhnya, memberikan rasa manis.",
                "tingkat_kematangan": "Matang"
            })
        ],
        "penjelasan_analis": "Panas mengubah asam dalam tomat menjadi senyawa yang lebih manis.",
        "penjelasan_chef": "Tomat bisa dipanggang atau dijadikan saus untuk menambah cita rasa.",
        "fun_fact": "Tomat kaya akan likopen, antioksidan yang baik untuk kesehatan.",
        "penyimpanan": {
            "suhu": "5-10°C",
            "masa_simpan": "3-5 hari",
            "tips": "Simpan tomat di suhu kamar untuk mempertahankan kesegarannya."
        }
    },
    "🥝 Kiwi": {
        "reaksi": [
            (30, {
                "chef": "Kiwi mulai sedikit lebih lembut.",
                "analis": "Struktur sel kiwi mulai terganggu oleh panas.",
                "tingkat_kematangan": "-"
            }),
            (60, {
                "chef": "Kiwi semakin lembut, rasa asam mulai berkurang.",
                "analis": "Proses pemanasan menyebabkan senyawa asam dalam kiwi terurai.",
                "tingkat_kematangan": "Setengah Matang"
            }),
            (90, {
                "chef": "Kiwi matang sempurna, rasa manis semakin dominan.",
                "analis": "Proses pemanasan mengubah senyawa asam menjadi lebih manis.",
                "tingkat_kematangan": "Matang"
            })
        ],
        "penjelasan_analis": "Pemanasan menyebabkan perubahan senyawa asam dalam kiwi.",
        "penjelasan_chef": "Kiwi bisa dimakan segar atau digunakan untuk saus dan smoothie.",
        "fun_fact": "Kiwi adalah sumber vitamin C yang sangat tinggi.",
        "penyimpanan": {
            "suhu": "2-5°C",
            "masa_simpan": "1-2 minggu",
            "tips": "Simpan kiwi di kulkas agar tetap segar lebih lama."
        }
    },
    "🍇 Anggur": {
        "reaksi": [
            (30, {
                "chef": "Anggur mulai lebih lembut.",
                "analis": "Struktur sel anggur mulai melepaskan cairan.",
                "tingkat_kematangan": "-"
            }),
            (60, {
                "chef": "Anggur semakin lembut, jus mulai keluar.",
                "analis": "Karbohidrat dalam anggur mulai mengkaramel.",
                "tingkat_kematangan": "Setengah Matang"
            }),
            (80, {
                "chef": "Anggur matang sempurna, rasa manis alami semakin dominan.",
                "analis": "Pemanasan menyebabkan senyawa gula dalam anggur terkaramelisasi.",
                "tingkat_kematangan": "Matang"
            })
        ],
        "penjelasan_analis": "Pemanasan mengubah karbohidrat dalam anggur menjadi gula alami.",
        "penjelasan_chef": "Anggur bisa dipanggang atau dijadikan saus untuk hidangan manis.",
        "fun_fact": "Anggur kaya akan antioksidan, baik untuk kesehatan jantung.",
        "penyimpanan": {
            "suhu": "0-4°C",
            "masa_simpan": "3-5 hari",
            "tips": "Simpan anggur dalam wadah terbuka di kulkas."
        }
    },
    "🍞 Roti": {
        "reaksi": [
            (30, {
                "chef": "Roti mulai hangat, belum ada perubahan signifikan.",
                "analis": "Proses pemanasan mulai mempengaruhi pati dalam roti.",
                "tingkat_kematangan": "-"
            }),
            (60, {
                "chef": "Roti mulai keemasan, teksturnya lebih padat.",
                "analis": "Proses pemanasan mengubah pati menjadi gula.",
                "tingkat_kematangan": "Setengah Matang"
            }),
            (80, {
                "chef": "Roti matang sempurna, berwarna coklat keemasan.",
                "analis": "Pati dalam roti sudah terurai sepenuhnya, memberikan rasa manis.",
                "tingkat_kematangan": "Matang"
            })
        ],
        "penjelasan_analis": "Panas mengubah pati dalam roti menjadi gula, memberikan rasa manis.",
        "penjelasan_chef": "Panggang roti hingga berwarna keemasan untuk hasil terbaik.",
        "fun_fact": "Roti panggang meningkatkan rasa dan tekstur, cocok untuk sarapan.",
        "penyimpanan": {
            "suhu": "15-20°C",
            "masa_simpan": "3-5 hari",
            "tips": "Simpan roti dalam kantong kedap udara untuk menjaga kelembapannya."
        }
    },
    "🍌 Pisang": {
        "reaksi": [
            (30, {
                "chef": "Pisang mulai sedikit lebih lembut.",
                "analis": "Sel dalam pisang mulai mengalami perubahan tekstur.",
                "tingkat_kematangan": "-"
            }),
            (60, {
                "chef": "Pisang lebih lembut dan lebih manis.",
                "analis": "Panas menyebabkan konversi karbohidrat menjadi gula.",
                "tingkat_kematangan": "Setengah Matang"
            }),
            (80, {
                "chef": "Pisang matang sempurna, tekstur lebih lembut dan manis.",
                "analis": "Proses pemanasan meningkatkan rasa manis alami pisang.",
                "tingkat_kematangan": "Matang"
            })
        ],
        "penjelasan_analis": "Pemanasan mengubah karbohidrat dalam pisang menjadi gula alami.",
        "penjelasan_chef": "Pisang cocok untuk dijadikan smoothies atau dipanggang.",
        "fun_fact": "Pisang kaya akan kalium yang baik untuk otot dan jantung.",
        "penyimpanan": {
            "suhu": "15-20°C",
            "masa_simpan": "1-2 minggu",
            "tips": "Simpan pisang di suhu kamar untuk mempercepat pematangan."
        }
    },
    "🍄 Jamur": {
        "reaksi": [
            (30, {
                "chef": "Jamur mulai lembut, tetapi belum ada perubahan signifikan.",
                "analis": "Jamur mulai mengeluarkan cairan alami.",
                "tingkat_kematangan": "-"
            }),
            (60, {
                "chef": "Jamur semakin lembut, rasa dan aroma lebih intens.",
                "analis": "Cairan dalam jamur semakin banyak keluar.",
                "tingkat_kematangan": "Setengah Matang"
            }),
            (80, {
                "chef": "Jamur matang sempurna, tekstur kenyal dan rasa semakin kuat.",
                "analis": "Proses pemanasan meningkatkan rasa alami jamur.",
                "tingkat_kematangan": "Matang"
            })
        ],
        "penjelasan_analis": "Pemanasan menyebabkan jamur mengeluarkan cairan alami dan rasa umami.",
        "penjelasan_chef": "Jamur bisa dimasak untuk hidangan sup atau tumisan.",
        "fun_fact": "Jamur mengandung banyak vitamin D yang bermanfaat untuk tubuh.",
        "penyimpanan": {
            "suhu": "2-5°C",
            "masa_simpan": "3-5 hari",
            "tips": "Simpan jamur dalam wadah kertas agar tidak lembab."
        }
    },
    "🥥 Kelapa": {
        "reaksi": [
            (30, {
                "chef": "Kelapa mulai sedikit lebih lembut.",
                "analis": "Panas mulai mengubah tekstur daging kelapa.",
                "tingkat_kematangan": "-"
            }),
            (60, {
                "chef": "Daging kelapa semakin lembut, lebih mudah diparut.",
                "analis": "Kandungan air dalam kelapa mulai berkurang.",
                "tingkat_kematangan": "Setengah Matang"
            }),
            (90, {
                "chef": "Kelapa matang sempurna, daging menjadi kering dan mudah dikeluarkan.",
                "analis": "Proses pemanasan mengurangi kandungan air dalam kelapa.",
                "tingkat_kematangan": "Matang"
            })
        ],
        "penjelasan_analis": "Panas mengurangi kadar air dalam kelapa dan mengubah teksturnya.",
        "penjelasan_chef": "Kelapa bisa diparut atau dipanggang untuk mendapatkan aroma khas.",
        "fun_fact": "Kelapa kaya akan serat dan minyak sehat.",
        "penyimpanan": {
            "suhu": "20-25°C",
            "masa_simpan": "1-2 minggu",
            "tips": "Simpan kelapa di tempat kering dan sejuk."
        }
    },
    "🐟 Ikan": {
    "reaksi": [
        (30, {
            "chef": "Ikan mulai terasa hangat, namun teksturnya masih tetap kenyal.",
            "analis": "Proses pemanasan mulai memengaruhi protein dalam ikan, namun belum ada perubahan besar.",
            "tingkat_kematangan": "-"
        }),
        (50, {
            "chef": "Daging ikan mulai mengeras sedikit, tetapi masih terlihat transparan di tengah.",
            "analis": "Protein dalam ikan mulai denaturasi, mengeras di bagian luar, namun bagian tengah masih mentah.",
            "tingkat_kematangan": "Setengah Matang"
        }),
        (70, {
            "chef": "Ikan matang sempurna, teksturnya padat dan flakey.",
            "analis": "Protein dalam ikan terdenaturasi sepenuhnya, menghasilkan tekstur yang lebih padat dan mudah terpisah.",
            "tingkat_kematangan": "Matang"
        }),
        (90, {
            "chef": "Ikan mulai kering dan kehilangan kelembapannya.",
            "analis": "Kehilangan kelembapan yang tinggi menyebabkan ikan menjadi kering.",
            "tingkat_kematangan": "Kering"
        })
    ],
    "penjelasan_analis": "Pemanasan menyebabkan protein dalam ikan terdenaturasi, mengubah tekstur dan rasa ikan.",
    "penjelasan_chef": "Untuk ikan panggang, pastikan suhu berada pada 70–75°C agar tidak terlalu kering.",
    "fun_fact": "Ikan adalah sumber protein dan omega-3 yang sangat baik untuk kesehatan jantung.",
    "penyimpanan": {
        "suhu": "-18°C",
        "masa_simpan": "3-6 bulan",
        "tips": "Simpan ikan dalam wadah kedap udara untuk menjaga kesegarannya."
    }
},
    "🍏 Apel": {
    "reaksi": [
        (30, {
            "chef": "Apel mulai terasa hangat, tekstur masih segar.",
            "analis": "Pemanasan mulai mempengaruhi selulosa di dalam apel, namun belum ada perubahan signifikan.",
            "tingkat_kematangan": "-"
        }),
        (60, {
            "chef": "Apel menjadi lebih lunak, sedikit lebih manis.",
            "analis": "Selulosa mulai terurai, membuat apel menjadi lebih lunak.",
            "tingkat_kematangan": "Setengah Matang"
        }),
        (80, {
            "chef": "Apel mulai karamelisasi, teksturnya lebih empuk.",
            "analis": "Pelelehan pektin mulai terjadi, memberikan rasa manis dan tekstur yang lebih lembut.",
            "tingkat_kematangan": "Matang"
        })
    ],
    "penjelasan_analis": "Pemanasan menyebabkan pelembutan struktur selulosa dalam apel.",
    "penjelasan_chef": "Apel panggang dapat dibuat lebih manis dan empuk pada suhu sekitar 80°C.",
    "fun_fact": "Apel memiliki lebih dari 7.500 jenis di seluruh dunia!",
    "penyimpanan": {
        "suhu": "2-4°C",
        "masa_simpan": "2-4 minggu",
        "tips": "Simpan di tempat yang dingin agar tetap segar lebih lama."
    }
},
    "🍤 Udang": {
    "reaksi": [
        (30, {
            "chef": "Udang mulai terasa hangat, tetapi teksturnya masih kenyal.",
            "analis": "Pemanasan awal menyebabkan perubahan warna dari transparan menjadi agak keruh.",
            "tingkat_kematangan": "-"
        }),
        (60, {
            "chef": "Udang berubah warna menjadi merah muda, mulai matang.",
            "analis": "Protein dalam udang mengalami denaturasi, menyebabkan tekstur lebih kencang.",
            "tingkat_kematangan": "Matang"
        }),
        (80, {
            "chef": "Udang matang sempurna, dengan tekstur kenyal dan mudah terpisah.",
            "analis": "Proses pemanasan lebih lanjut membuat udang menjadi lebih keras dan kering jika terlalu lama.",
            "tingkat_kematangan": "Matang"
        })
    ],
    "penjelasan_analis": "Udang mengandung protein yang cepat terdenaturasi pada suhu tinggi.",
    "penjelasan_chef": "Untuk udang panggang, pastikan suhu mencapai 70-80°C agar tidak terlalu kering.",
    "fun_fact": "Udang adalah sumber protein yang tinggi dan mengandung selenium yang baik untuk kesehatan jantung.",
    "penyimpanan": {
        "suhu": "-18°C",
        "masa_simpan": "3-6 bulan",
        "tips": "Simpan udang dalam wadah kedap udara untuk menjaga kesegarannya."
    }
},
    "🦑 Cumi": {
    "reaksi": [
        (30, {
            "chef": "Cumi mulai terasa hangat, tetapi teksturnya masih kenyal.",
            "analis": "Pemanasan mulai mempengaruhi jaringan otot cumi.",
            "tingkat_kematangan": "-"
        }),
        (60, {
            "chef": "Cumi mulai mengeras dan berwarna putih pucat.",
            "analis": "Jaringan protein dalam cumi mulai terdenaturasi, tekstur menjadi lebih padat.",
            "tingkat_kematangan": "Matang"
        }),
        (90, {
            "chef": "Cumi menjadi kering dan lebih keras.",
            "analis": "Pemanasan berlebih menyebabkan kehilangan kelembapan, menjadikannya kering.",
            "tingkat_kematangan": "Kering"
        })
    ],
    "penjelasan_analis": "Cumi mengandung protein yang akan mengeras seiring dengan pemanasan.",
    "penjelasan_chef": "Untuk cumi yang empuk, pastikan tidak memasaknya terlalu lama pada suhu 60-70°C.",
    "fun_fact": "Cumi memiliki tinta yang digunakan sebagai mekanisme pertahanan diri dari predator.",
    "penyimpanan": {
        "suhu": "-18°C",
        "masa_simpan": "3-6 bulan",
        "tips": "Simpan cumi dalam kantong plastik kedap udara untuk mencegah bau."
    }
},
    "🧀 Keju": {
    "reaksi": [
        (30, {
            "chef": "Keju mulai melunak, namun belum meleleh sepenuhnya.",
            "analis": "Panas mulai mempengaruhi lemak dan protein dalam keju.",
            "tingkat_kematangan": "-"
        }),
        (60, {
            "chef": "Keju mulai meleleh, lebih mudah dipadukan dengan makanan.",
            "analis": "Lemak dalam keju meleleh, memberikan tekstur yang lebih creamy.",
            "tingkat_kematangan": "Matang"
        }),
        (80, {
            "chef": "Keju mulai mengeras kembali jika terlalu panas, mengurangi kelembapannya.",
            "analis": "Panas yang berlebihan membuat keju mengeras dan kehilangan kelembapannya.",
            "tingkat_kematangan": "Kering"
        })
    ],
    "penjelasan_analis": "Lemak dalam keju meleleh pada suhu tinggi, memberikan tekstur lembut.",
    "penjelasan_chef": "Keju leleh sempurna pada suhu sekitar 60–70°C, cocok untuk saus.",
    "fun_fact": "Keju memiliki lebih dari 1.800 jenis di seluruh dunia!",
    "penyimpanan": {
        "suhu": "4-10°C",
        "masa_simpan": "2-4 minggu",
        "tips": "Simpan keju dalam wadah kedap udara untuk menjaga kesegarannya."
    }
},
    "🥦 Brokoli": {
    "reaksi": [
        (30, {
            "chef": "Brokoli mulai terasa hangat, namun teksturnya masih renyah.",
            "analis": "Pemanasan mulai merusak dinding sel brokoli, tetapi belum ada perubahan besar.",
            "tingkat_kematangan": "-"
        }),
        (60, {
            "chef": "Brokoli mulai lebih empuk, dengan warna hijau cerah.",
            "analis": "Selulosa dalam brokoli mulai terurai, memberikan tekstur yang lebih lembut.",
            "tingkat_kematangan": "Setengah Matang"
        }),
        (80, {
            "chef": "Brokoli matang sempurna, dengan tekstur lembut dan rasa manis.",
            "analis": "Pemanasan lebih lanjut menyebabkan brokoli lebih lembut, dengan hilangnya beberapa nutrisi.",
            "tingkat_kematangan": "Matang"
        })
    ],
    "penjelasan_analis": "Pemanasan menyebabkan perubahan pada selulosa dan klorofil dalam brokoli.",
    "penjelasan_chef": "Brokoli panggang atau kukus di suhu 75°C untuk mempertahankan rasa manis dan nutrisinya.",
    "fun_fact": "Brokoli mengandung lebih banyak vitamin C dibandingkan jeruk.",
    "penyimpanan": {
        "suhu": "0-4°C",
        "masa_simpan": "1 minggu",
        "tips": "Jangan simpan brokoli terlalu lama, agar tetap segar dan renyah."
    }
},
    "🥬 Kangkung": {
    "reaksi": [
        (30, {
            "chef": "Kangkung mulai terasa hangat, namun masih renyah.",
            "analis": "Sel kangkung mulai terurai sedikit, namun belum ada perubahan besar.",
            "tingkat_kematangan": "-"
        }),
        (60, {
            "chef": "Kangkung mulai layu dan empuk, warna hijau tetap cerah.",
            "analis": "Selulosa dalam kangkung mulai terurai, memberikan tekstur yang lebih lembut.",
            "tingkat_kematangan": "Setengah Matang"
        }),
        (80, {
            "chef": "Kangkung matang sempurna, teksturnya lembut dan rasa manis.",
            "analis": "Pemanasan lebih lanjut menyebabkan hilangnya beberapa nutrisi.",
            "tingkat_kematangan": "Matang"
        })
    ],
    "penjelasan_analis": "Kangkung mengandung klorofil dan selulosa yang terurai saat dipanaskan.",
    "penjelasan_chef": "Untuk kangkung tumis, pastikan tidak terlalu lama memasak agar tetap hijau cerah.",
    "fun_fact": "Kangkung dikenal sebagai sayuran dengan pertumbuhan yang cepat.",
    "penyimpanan": {
        "suhu": "0-4°C",
        "masa_simpan": "2-3 hari",
        "tips": "Segera konsumsi kangkung setelah dibeli untuk menjaga kesegarannya."
    }
},"🌶️ Cabe": {
    "reaksi": [
        (30, {
            "chef": "Cabe mulai terasa hangat, namun belum ada perubahan signifikan.",
            "analis": "Pemanasan mulai merangsang kapsaisin, memberi rasa pedas.",
            "tingkat_kematangan": "-"
        }),
        (60, {
            "chef": "Cabe mulai kehilangan teksturnya dan lebih mudah dihaluskan.",
            "analis": "Kapsaisin pada cabe mulai aktif, memberikan rasa pedas yang lebih kuat.",
            "tingkat_kematangan": "Matang"
        }),
        (80, {
            "chef": "Cabe mulai mengering dan mengeluarkan aroma yang lebih tajam.",
            "analis": "Panas yang tinggi menyebabkan hilangnya kelembapan cabe.",
            "tingkat_kematangan": "Kering"
        })
    ],
    "penjelasan_analis": "Kapsaisin dalam cabe memberikan rasa pedas, dan akan lebih kuat dengan pemanasan.",
    "penjelasan_chef": "Cabe yang dipanaskan akan lebih pedas, jadi hati-hati saat mengolahnya.",
    "fun_fact": "Cabe bisa meningkatkan metabolisme tubuh dan mengandung banyak vitamin C.",
    "penyimpanan": {
        "suhu": "20-25°C",
        "masa_simpan": "1-2 minggu",
        "tips": "Simpan cabe di tempat sejuk dan kering."
    }
},
    "🌽 Jagung": {
    "reaksi": [
        (50, {
            "chef": "Jagung mulai terasa lebih empuk.",
            "analis": "Air dalam biji jagung mulai memanas dan mengakibatkan pelembutan jaringan.",
            "tingkat_kematangan": "-"
        }),
        (80, {
            "chef": "Jagung menjadi manis dan juicy saat dimakan.",
            "analis": "Pati mulai gelatinisasi dan meningkatkan rasa manis alami.",
            "tingkat_kematangan": "Matang"
        }),
        (150, {
            "chef": "Jagung bisa mulai menghitam jika dipanggang langsung.",
            "analis": "Reaksi Maillard terjadi pada permukaan jagung saat suhu tinggi.",
            "tingkat_kematangan": "Panggang"
        })
    ],
    "penjelasan_analis": "Pati pada jagung mengalami gelatinisasi dan Maillard pada suhu tinggi menghasilkan aroma khas.",
    "penjelasan_chef": "Untuk rasa terbaik, rebus jagung selama 10 menit atau panggang langsung di suhu 150–180°C.",
    "fun_fact": "Jagung adalah satu dari sedikit tanaman yang bisa berubah warna saat matang, tergantung jenisnya.",
    "penyimpanan": {
        "suhu": "0-4°C",
        "masa_simpan": "1 minggu",
        "tips": "Simpan dalam kulitnya untuk menjaga kelembaban lebih lama."
    }
},
    "🐟 Salmon": {
    "reaksi": [
        (40, {
            "chef": "Daging mulai menghangat tapi masih mentah.",
            "analis": "Protein belum mengalami denaturasi signifikan.",
            "tingkat_kematangan": "-"
        }),
        (55, {
            "chef": "Tekstur mulai lembut dan berwarna pucat – medium rare.",
            "analis": "Protein mulai menggumpal, menghasilkan tekstur lebih empuk.",
            "tingkat_kematangan": "Setengah Matang"
        }),
        (65, {
            "chef": "Salmon matang sempurna, juicy dan lezat.",
            "analis": "Sebagian besar protein telah terdenaturasi, warna menjadi lebih cerah.",
            "tingkat_kematangan": "Matang"
        }),
        (75, {
            "chef": "Salmon mulai terlalu kering dan serat terpisah.",
            "analis": "Overcooking menyebabkan kehilangan kelembaban dan struktur menjadi keras.",
            "tingkat_kematangan": "Overcook"
        })
    ],
    "penjelasan_analis": "Protein pada salmon terdenaturasi bertahap dan kehilangan air bila terlalu panas.",
    "penjelasan_chef": "Masak salmon di suhu sekitar 60–65°C untuk hasil juicy dan lembut.",
    "fun_fact": "Salmon mengandung omega-3 tinggi yang baik untuk jantung dan otak.",
    "penyimpanan": {
        "suhu": "0-2°C",
        "masa_simpan": "1-2 hari (segar), hingga 2 bulan (beku)",
        "tips": "Simpan di es batu atau vacuum-sealed untuk kualitas terbaik."
    }
},
    "🍫 Coklat": {
    "reaksi": [
        (30, {
            "chef": "Coklat mulai lunak dan mengkilap.",
            "analis": "Lemak kakao mulai mencair di suhu rendah.",
            "tingkat_kematangan": "-"
        }),
        (45, {
            "chef": "Coklat meleleh sempurna – ideal untuk dipping atau coating.",
            "analis": "Coklat mengalami pelelehan sempurna, komponen gula, lemak, dan kakao homogen.",
            "tingkat_kematangan": "Leleh Sempurna"
        }),
        (55, {
            "chef": "Coklat mulai berbau gosong dan menggumpal.",
            "analis": "Lemak kakao mulai terurai dan gula mulai terbakar.",
            "tingkat_kematangan": "Gosong"
        })
    ],
    "penjelasan_analis": "Coklat mencair pada suhu rendah karena kandungan lemak kakao. Pemanasan berlebih dapat merusak rasa dan tekstur.",
    "penjelasan_chef": "Gunakan teknik tempering di suhu sekitar 45°C lalu turunkan ke 31°C untuk hasil mengkilap.",
    "fun_fact": "Coklat hitam mengandung antioksidan flavonoid yang baik untuk kesehatan jantung!",
    "penyimpanan": {
        "suhu": "15-18°C",
        "masa_simpan": "12-24 bulan",
        "tips": "Hindari suhu tinggi dan kelembapan untuk mencegah 'bloom' (lapisan putih di permukaan)."
    }
},
   "🥥 Kelapa": {
    "reaksi": [
        (40, {
            "chef": "Kelapa parut mulai hangat dan aromanya keluar.",
            "analis": "Minyak dalam kelapa mulai menguap perlahan, melepaskan senyawa volatil.",
            "tingkat_kematangan": "-"
        }),
        (70, {
            "chef": "Kelapa mulai kecoklatan – cocok untuk taburan kue.",
            "analis": "Reaksi Maillard ringan dimulai, terutama pada protein-residu kelapa.",
            "tingkat_kematangan": "Kecoklatan"
        }),
        (100, {
            "chef": "Kelapa menjadi renyah dan coklat tua.",
            "analis": "Pengeringan intens dan karamelisasi sebagian terjadi pada sisa gula.",
            "tingkat_kematangan": "Renyan Karamel"
        })
    ],
    "penjelasan_analis": "Kelapa mengandung lemak dan gula alami yang sensitif terhadap panas. Pemanasan moderat meningkatkan aroma dan rasa.",
    "penjelasan_chef": "Sangrai kelapa tanpa minyak di suhu sedang selama 5–10 menit untuk hasil wangi dan gurih.",
    "fun_fact": "Kelapa bisa diproses menjadi santan, minyak, dan tepung yang bergizi tinggi.",
    "penyimpanan": {
        "suhu": "0–4°C (segar) / 20–25°C (kering)",
        "masa_simpan": "5–7 hari (segar) / 3–6 bulan (kering)",
        "tips": "Simpan kelapa kering dalam wadah kedap udara agar tidak tengik."
    }
   },
    "🥛 Susu": {
        "reaksi": [
            (30, {
                "chef": "Susu mulai sedikit hangat.",
                "analis": "Protein dalam susu mulai mengalami sedikit perubahan.",
                "tingkat_kematangan": "-"
            }),
            (60, {
                "chef": "Susu mulai terasa lebih hangat, protein mulai menggumpal sedikit.",
                "analis": "Denaturasi protein dalam susu mulai berlangsung.",
                "tingkat_kematangan": "Setengah Matang"
            }),
            (80, {
                "chef": "Susu mulai mendidih dan menggumpal.",
                "analis": "Panas menyebabkan kasein dalam susu menggumpal.",
                "tingkat_kematangan": "Matang"
            })
        ],
        "penjelasan_analis": "Pemanasan menyebabkan kasein dalam susu menggumpal dan membentuk lapisan.",
        "penjelasan_chef": "Panaskan susu perlahan untuk menghindari pecahnya susu.",
        "fun_fact": "Susu mengandung banyak kalsium dan protein yang baik untuk tulang.",
        "penyimpanan": {
            "suhu": "0-4°C",
            "masa_simpan": "5-7 hari",
            "tips": "Simpan susu dalam kemasan tertutup di kulkas."
        }
    }
}

# ======================== FUNGSI ==========================

def generate_table(makanan, mode):
    rows = []
    for suhu, detail in data_makanan[makanan]["reaksi"]:
        row = {
            "Suhu (°C)": suhu,
            "Penjelasan": detail[mode.lower()]
        }
        if mode == "Chef" and "tingkat_kematangan" in detail:
            row["Tingkat Kematangan"] = detail["tingkat_kematangan"]
        rows.append(row)
    return rows

# ========================= HALAMAN ========================

if halaman == "Beranda":
    st.title("🍽️Simulasi Interaktif Reaksi Pangan terhadap Suhu")
    st.markdown("Selamat datang di **aplikasi interaktif** untuk memahami bagaimana bahan pangan bereaksi terhadap panas.")
    st.markdown("👨‍🍳 Mode *Chef*: Fokus pada tingkat kematangan dan waktu memasak.")
    st.markdown("🔬 Mode *Analis*: Fokus pada penjelasan ilmiah dan reaksi molekuler.")
    st.image("https://cdn0-production-images-kly.akamaized.net/7ja7izhlU54w5VbkjPRxctPzwnw=/680x383/smart/filters:quality(75):strip_icc():format(webp)/kly-media-production/medias/3543870/original/067438200_1629277779-alex-lam-WOrdQ6Wgomw-unsplash.jpg",
             caption="Bolu Pandan Topping Keju & Choco Chip", use_container_width=True)
    st.markdown("➡️ Pilih menu **Simulasi** di sidebar untuk memulai.")

elif halaman == "Simulasi":
    st.title("Apa sih yang bakal terjadi? Cari tau yuk!")

    mode = st.radio("🎭 Simulasi Sebagai:", ("Chef", "Analis"))
    makanan = st.selectbox("🔍 Pilih Bahan Pangan:", list(data_makanan.keys()))

    if st.button("🚀 Jalankan Simulasi"):
        st.success(f"✅ Simulasi selesai untuk {makanan} dalam mode {mode}.")

        st.subheader("🔥 Reaksi Bertahap Sesuai Suhu:")
        for suhu, detail in data_makanan[makanan]["reaksi"]:
            st.info(f"**{suhu}°C**: {detail[mode.lower()]}")

        st.divider()
        st.subheader("📘 Penjelasan:")
        st.write(data_makanan[makanan][f"penjelasan_{mode.lower()}"])

        st.subheader("✨ Fun Fact:")
        st.success(data_makanan[makanan]["fun_fact"])

        st.subheader("🧊 Penyimpanan:")
        ps = data_makanan[makanan]["penyimpanan"]
        st.write(f"- **Suhu:** {ps['suhu']}\n- **Masa Simpan:** {ps['masa_simpan']}\n- **Tips:** {ps['tips']}")

        st.divider()
        st.subheader("📊 Tabel Reaksi Lengkap:")
        tabel = generate_table(makanan, mode)
        st.table(tabel)

elif halaman == "Tentang Kelompok":
    st.title("👥 Kelompok 3 PMIP 1E-2")

    st.markdown("""
    Berikut adalah anggota kelompok kami dalam pengembangan aplikasi simulasi pemanasan pangan:

    ### 👩‍💻 Anggota Kelompok:
    - **Arkadio Ariatama** 
    - **Cantika Mayora Mulyana** 
    - **Khanza Syakirah**
    - **Noorleysa Maulidzi Firmansyah**
    - **Shalina Putri Maharani**

    ### 🛠️ Tools yang Digunakan:
    - Python (Streamlit)
    - Canva (untuk UI Design)

    ### 📸 Foto Tim:
    """)

    st.image("https://i.imgur.com/zVlbSv9.jpeg", width=400, caption="Ilustrasi Tim")
    st.success("Teimakasih Sudah Mengunjungi Aplikasi Kami :)")
