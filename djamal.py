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
    ## **Djamal Moussadek | Modern Central Defender with Tactical Intelligence**
    
    **🌟 Overview**
    - A promising and versatile center-back capable of playing on both left and right sides.
    - Natural left-footed player with good adaptability, making him valuable in different tactical setups.
    - Combines defensive solidity with ball-playing ability, ideal for possession-based or transitional systems.

    ### **🧠 Personality & Mentality**
    - **Resilient & Hardworking:** Maintains high intensity throughout the game, showing great endurance.
    - **Team-Oriented:** Works well within the defensive unit, prioritizing collective success.

    ### **🎯 Football Profile**
    - **Defensive Strengths:**
      - **Excellent in duels** 🤺 (both aerial and ground battles).
      - **Strong shot-blocking ability** 🛑, especially in dangerous areas.
      - **Good anticipation & positioning** 📍 to intercept and cover spaces.
    
    - **Ball-Playing Ability:**
      - **Comfortable under pressure** 💡, key in possession-based football.

    ### **🚀 Future Potential**
    - Ready for a step up to a **higher level (Ligue 2 or equivalent)**.
    - Ideal for a **progressive team needing a mobile, ball-playing defender**.
    - With the right development, could become a key defensive asset at a **higher professional level**.

    **🎯 Conclusion: Djamal is a modern, intelligent central defender with strong physical attributes and quality passing. A high-potential player who could thrive in a competitive environment.**
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
    if image:
        st.image(image, use_container_width=True)

    # Player profile analysis
    st.write("""
    ### Profile Overview:
    - **Versatile Defender:** Djamal is an all-around center-back, without an elite standout skill but a balanced profile.
    - **Key Strengths:**
      - Strong in defensive duels, showing good anticipation.
      - Solid in clearances and blocking shots, essential in defensive transitions.
      - Capable of playing forward, breaking lines with passes, and delivering accurate long balls.
    - **Areas for Improvement:**
      - Can work on increasing his defensive actions to match the league's top performers.
    
    ### Tactical Fit:
    - Ideal for a **possession-based team** needing a ball-playing defender.
    - Can thrive in a **low-block defensive system**, where his clearance and blocking ability shine.
    - With improved physical dominance, could transition into a higher level of competition.

    🚀 **Djamal is a reliable central defender with strong defensive fundamentals and good passing range. With targeted improvements, he could become a top-tier defender.**
    """)

with st.expander("📈 Performance Progression | Individual Development"):
    if image:
        st.image(image, use_container_width=True)

    # Performance Improvements Analysis
    st.write("""
    ### Key Improvements in 24/25 (Blue):
    - **Defensive Stability:** 
      - Dribbled past less often, showing better positioning and 1v1 defending.
      - Improved in blocks and clearances, making him more reliable defensively.
    - **Aerial Dominance:**
      - Increased aerial win percentage, becoming a stronger presence in duels.
    - **Passing & Progression:** 
      - Improved in passing metrics (OBV & carries), showing confidence in build-up play.
      - More effective under pressure, leading to better ball retention.
    
    ### Areas to Keep Developing:
    - Further reduce turnovers and improve passing security.
    - Continue refining long-ball accuracy for better distribution.
    - Maintain defensive consistency over the season.

    🚀 **Djamal has shown strong progression, becoming a more complete and resilient defender. His growth in defensive duels and aerial ability makes him a key asset for his team!**
    """)

# with st.expander("👥 Player Comparison | Ernest Nuamah (Ligue 1)"):
#     image = load_image_from_github("radar.png")
#     if image:
#         st.image(image, use_container_width=True)
#     st.write("Advanced radar stats highlighting Freddy's capabilities to reach top level.")


with st.expander("🏋️ Physical Performance | High Intensity & Explosiveness"):
    if image:
        st.image(image, use_container_width=True)

    # Physical Profile Analysis
    st.write("""
    ### 🚀 **Djamal Moussadek's Physical Profile**
    
    #### **Top Physical Attributes:**
    - **Max Speed:** Around 30-32 km/h, which is exceptional for a central defender.
    - **Acceleration & Deceleration:** Consistently above 20+ high-intensity accelerations (>4m/s²) per game, showing strong explosiveness.
    - **High-Speed Running (16-24 km/h):** Covers a notable distance at high intensity, proving endurance and mobility.
    - **Sprinting Capacity:** While not a primary sprinter, he maintains good short-burst sprint ability.

    #### **Strengths in His Role:**
    - **Explosive Acceleration:** Quick bursts allow him to react swiftly to defensive transitions.
    - **Endurance for Defensive Work:** Can maintain high activity levels over 90 minutes.
    - **Speed Recovery:** Above-average top speed helps cover defensive spaces.

    #### **Areas for Development:**
    - **Increase Sprint Frequency:** While he reaches high speed, increasing short bursts could improve his pressing and recovery runs.
    - **Maintain High-Speed Consistency:** Keeping high-intensity running over multiple games will be key for long-term performance.

    ✅ **Overall, Djamal is a physically dominant center-back with a rare combination of speed, endurance, and explosiveness.** His ability to cover ground and handle high-intensity actions makes him a modern, dynamic defender.
    """)
with st.expander("🤕 Injury History | Robust Player"):
    image = load_image_from_github("injuries.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("He had no injuries this year. Djamal is very robust and take care of his body")

with st.expander("⚖️ Weight Evolution"):
    image = load_image_from_github("poids.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Monitoring body composition is key to performance optimization.Djamal show a good body composition")

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

