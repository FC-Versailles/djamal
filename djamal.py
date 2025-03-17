#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 15:23:43 2025

@author: fcvmathieu
"""

import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import urllib.parse


# GitHub repository where images are stored (raw URL format)
GITHUB_BASE_URL = "https://raw.githubusercontent.com/FC-Versailles/djamal/main/"

# Function to fetch images from GitHub
def load_image_from_github(filename):
    url = GITHUB_BASE_URL + filename
    response = requests.get(url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        st.error(f"⚠️ Could not load image: {filename}")
        return None

image = load_image_from_github("pic.png")
if image:
    st.image(image, width=100)
# Title & Player Overview
st.title("Djamal Moussadek - 22 (FR)")
# Button linking to Transfermarkt profile
st.link_button("Transfermarkt Profile", "https://www.transfermarkt.fr/djamal-moussadek/profil/spieler/855021")

st.markdown("<hr style='border:1px solid #ddd' />", unsafe_allow_html=True)

# Key Insights
st.header("🔍 Key Insights")
st.markdown(
    """
    **Djamal is an talented central defender with a good potential. He has the huge advantage to have left & right foot. His main position is left defender.**
    
    **Personality & mentality** 🏃‍♂️💨
    - A team player
    - 

    
    **Football Profile**  🎯
    - Strong in duals
    - Block shot in the golden zone
    - Passing quality to initiate the possession

    """
)

# Define the WhatsApp number (include country code, no '+' sign)
whatsapp_number = "33771730001"  # Example: +33 for France

# Message to send
message = "Hello, I am interested in Djamal Moussadek. Can we discuss further?"

# Encode message for URL
encoded_message = urllib.parse.quote(message)

# WhatsApp URL
whatsapp_url = f"https://api.whatsapp.com/send?phone={whatsapp_number}&text={encoded_message}"

# Button to open WhatsApp chat
if st.button("📲 Contact Sport Director"):
    st.markdown(f'<a href="{whatsapp_url}" target="_blank">Send a whatsapp</a>', unsafe_allow_html=True)


st.markdown("<hr style='border:1px solid #ddd' />", unsafe_allow_html=True)

# Vertical Display with Expanders
with st.expander("👤 Player Career | Special profil of central defender"):
    if image:
        st.image(image, use_container_width=True)

    # Career analysis
    st.write("""
    ### Career Path Analysis:
    - **Early Career:** Developed at Le Mans FC, progressing through youth and B team.
    - **Professional Debut:** Joined Le Havre AC but had limited opportunities.
    - **Loan Moves:** Loaned to Villefranche to gain experience.
    - **Recent Move:** Signed with FC Versailles in July 2024 to gain more playing time.

    ### Next Step:
    - **Key Strengths:** Experience in multiple clubs.
    - **Potential Progression:** If he performs well at Versailles, he could attract interest from higher level.
    """)

with st.expander("📍 Position Played | Left Central Defender"):
    if image:
        st.image(image, use_container_width=True)

    # Positional analysis
    st.write("""
    ### Positional Profile:
    - **Main Position:** Left Center-Back (LCB) – Played 12.8 matches in this role.
    - **Other Positions:** Right Center-Back (6.0), occasional roles as Right-Back (0.4) and Right Wing-Back (0.2).
    - **Strengths:** Versatility in the backline, ability to play on both sides, making him a valuable defensive asset.
    - **Key Advantage:** Comfortable with both feet, allowing flexibility in build-up play and defensive adaptability.

    ### Tactical Insights:
    - **Best Fit:** A left-footed or two-footed center-back role in a three or four-man defensive setup.
    - **Next Step:** Strengthening leadership at the back and refining tactical positioning for a potential move to Ligue 2.
    """)
    
    
with st.expander("⏳ Minutes Played | A Key Player"):
    if image:
        st.image(image, use_container_width=True)

    # Performance Analysis
    st.write("""
    ### Match Involvement:
    - **Appearances:** 18 out of 23 matches, demonstrating high reliability.
    - **Playing Time:** Regular starter, playing full 90 minutes in most matches.
    - **Substitutions:** Only a few instances of being benched or subbed off.

    """)

with st.expander("🛡 Player Profile | Complete Central Defender"):
    image = load_image_from_github("leaugue_Comparison.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Djamal is a complete central defender without a strong skills. For this reason he is not in the top regarding the data. But Djamal is quite strong in duals, his a good lecture of the game, he showed some skills in the golden area like clearance and block/shot. He has also a good passing skills, able to play forward, breaking lines & long balls. 🚀")


# with st.expander("📈 Performance Progression | Individual Development"):
#     image = load_image_from_github("progression.png")
#     if image:
#         st.image(image, use_container_width=True)
#     st.write("Freddy Mbemba has transitioned into a more effective goal-scorer and playmaker (xG assisted), as seen by his higher xG assisted and goal contribution stats. However, there is a slight trade-off in his dribbling and ball progression, suggesting either a tactical shift (e.g., playing higher up the pitch) or defensive adaptation from opponents.")

# with st.expander("👥 Player Comparison | Ernest Nuamah (Ligue 1)"):
#     image = load_image_from_github("radar.png")
#     if image:
#         st.image(image, use_container_width=True)
#     st.write("Advanced radar stats highlighting Freddy's capabilities to reach top level.")


with st.expander("🏋️ Physical Performance | High Intensity & Explosiveness"):
    image = load_image_from_github("physique.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("For a central defender Djamal a really good vmax (around 30Km/h. He can also repeat effort & have a good ability to sprint")
with st.expander("🤕 Injury History | Robust Player"):
    image = load_image_from_github("injuries.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("He had no injuries this year. Djamal is very robust and take care of his body")

# with st.expander("⚖️ Weight Evolution"):
#     image = load_image_from_github("poids.png")
#     if image:
#         st.image(image, use_container_width=True)
#     st.write("Monitoring body composition is key to performance optimization.")

# with st.expander("🔥 Personnality & Motivation | high self determination"):
#     image = load_image_from_github("Happiness.png")
#     if image:
#         st.image(image, use_container_width=True)
#     st.write("Freddy is highly motivated and dedicated to his football journey. His motivation runs deep, rooted in his childhood passion, with a constant desire to progress and reach the highest levels of football.")

# with st.expander("📊 Game Report"):
#     image = load_image_from_github("game_report.png")
#     if image:
#         st.image(image, use_container_width=True)
#     st.write("Example of Game report, please contact Mathieu Feigean for more explanation or request.")






st.markdown("<hr style='border:1px solid #ddd' />", unsafe_allow_html=True)

st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #f8f9fa;
            padding: 10px;
            text-align: center;
            font-size: 14px;
            color: #333;
        }
    </style>
    <div class="footer">
        <p><strong>M.Feigean</strong> - Football Development</p>
    </div>
    """, unsafe_allow_html=True)

