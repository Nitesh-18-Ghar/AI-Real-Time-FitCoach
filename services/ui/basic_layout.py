import streamlit as st

def style_login_page():
    st.markdown(""" 
    <style>
        .stApp {
            background-color: #293132 !important;
        }
                
        .stApp div[data-testid="stColumn"]{
            background-color: #4a4b4b !important;
            padding: 2rem !important;
            border-radius: 2rem !important;
        }
    </style>
    """, unsafe_allow_html=True)         

def style_base_dashboard():
    st.markdown(""" 
    <style>
        .stApp {
            background: #00ABE4 !important;
        }
    </style>
    """, unsafe_allow_html=True) 

def style_background_dashboard():
    st.markdown(""" 
    <style>
        .stApp {
            background: #d0e6ff !important;
            color: black !important;
        }
                
        label {
            color: #3d348b !important;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True) 

def style_base_layout():
    st.markdown(""" 
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@100..900&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Anton&family=Roboto+Slab:wght@100..900&display=swap');
                
       /* Hide Top Bar Of Streamit */
                
            #MainMenu, footer, header{
                visibility: visible;
            }

            .block-container {
                padding-top: 1.5rem !important;
            }
                
            /* Streamlit ke by defualt cheezon ko overwrite kr rhe hain */
            h1 {
                font-family: "Anton", sans-serif !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
            }
                
            h2 {
                font-family: "Anton", sans-serif !important;
                font-size: 2rem !important;
                line-height: 0.9 !important;
                margin-bottom: 0rem !important;
            }
            
            h3, h4, p{
                font-family: "Roboto Slab", serif !important;
            }
                
            /* Input box background */
            .stTextInput > div > div > input {
                background-color: white;
                color: black;
                border: 2px solid #6C63FF;
                border-radius: 10px;
            }
                
            /* Placeholder color */
            .stTextInput input::placeholder {
                color: gray;
            }
                
            button[kind="primary"] {
                border-radius: 2.5rem !important;
                background-color: #5DD39E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                cursor: pointer !important;
                transition: transform 0.25s ease-in-out !important;
            }
                
            button[kind="secondary"] {
                border-radius: 1.5rem !important;
                background-color: #4a4b4b !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }
                
            button[kind="tertiary"] {
                border-radius: 1.5rem !important;
                background-color: #4cb1ff !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }
                
            button:hover{
                button-shadow: 0 0 20px #F1D302 !important
                transform:scale(1.05);
            }
    </style>
    """, unsafe_allow_html=True) 

def webrtc_styles():
    st.markdown(""" 
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@100..900&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Anton&family=Roboto+Slab:wght@100..900&display=swap');
        
        video {
            width: 100% !important;
            max-width: 1000px !important;
            min-height: 600px !important;
            border-radius: 50px !important;
            border: 4px solid #60b5ff !important;
        }
                
        button {
            border-radius: 20px !important;
            font-size: 16px !important;
            font-weight: 700 !important;
            transition: all 0.3s ease !important;
        }
                
        button:hover {
            transform: translateY(-2px);
        }
                
        /* START BUTTON */
        button[kind="primary"] {
            background-color: #4ade80 !important;
            color: white !important;
            border: none !important;
            font-size: 16px !important;
            border-radius: 10px !important;
        }
                
        /* DEVICE SELECT DROPDOWN */
        select {
            background: #1f2937 !important;
            color: white !important;
            border-radius: 15px !important;
            padding: 8px !important;
            font-size: 15px !important;
        }

    </style>
    """, unsafe_allow_html=True) 