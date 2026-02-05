import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import json

# ---------------- Google Sheets Setup ----------------
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

# Replace with the filename of your downloaded JSON key

creds_dict = json.loads(st.secrets["gcp_service_account"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)

client = gspread.authorize(creds)

# Replace with the name of your Google Sheet
sheet = client.open("TGHI Survey Results").sheet1

# ---------------- Survey Intro ----------------
st.title("TGHI Hair Health Questionnaire")

st.markdown("""
You’ll be amazed what little thought people give to the treatment of hair trauma.  
That is why we think it’s amazing that you’re making a move to get the medical opinion necessary to help you confront the hair trauma you have encountered.  

We’re here to help you make the best of your journey towards what good hair is to you. Hair that serves you and does not work against you.  
This quick 2-minute check-in helps our medical team understand your journey so we can match you with the right therapy.  

**Note:** This is not a medical diagnosis, but it is the first step toward your expert consultation and a personalised plan.
""")

# ---------------- Scoring Setup ----------------
score_map = {"a": 1, "b": 2, "c": 3, "d": 4}

section1_score = 0
section2_score = 0
section3_score = 0
section4_score = 0

# ---------------- Section 1 ----------------
st.header("1. Relationship with Your Hair")

q1 = st.radio("How is your hair’s volume looking compared to 2-3 years ago?",
              ["a) Still thick and thriving.",
               "b) A little thinner. I can see more of my scalp than I used to.",
               "c) Noticeably thinner. My puff is smaller or my part is looking noticeably wider.",
               "d) I see significant changes or visible patches of hair loss."])
section1_score += score_map[q1[0]]

q2 = st.radio("Are wigs, weaves, or braids your 'crutch' right now?",
              ["a) Not at all—I mostly rock my natural hair.",
               "b) Sometimes, just for a switch-up.",
               "c) Often, to cover thinning/breakage.",
               "d) Every day—I don’t feel comfortable showing natural hair."])
section1_score += score_map[q2[0]]

q3 = st.radio("How often are you using heat, colour, or chemicals?",
              ["a) Rarely or never.",
               "b) Only for special looks.",
               "c) Every few weeks.",
               "d) I used to, but stopped due to damage."])
section1_score += score_map[q3[0]]

# ---------------- Section 2 ----------------
st.header("2. How You’re Feeling")

q4 = st.radio("Does your hair affect your mood or confidence?",
              ["a) Not really—I’m feeling good.",
               "b) Some days are harder.",
               "c) I feel self-conscious.",
               "d) It’s stressing me out."])
section2_score += score_map[q4[0]]

q5 = st.radio("What is your main 'Hair Goal' right now?",
              ["a) Maintenance.",
               "b) Repair.",
               "c) Reversal.",
               "d) Regrowth."])
section2_score += score_map[q5[0]]

# ---------------- Section 3 ----------------
st.header("3. Methods You’ve Used Before")

q6 = st.radio("Have you ever seen a doctor or derm about your hair?",
              ["a) No, never.",
               "b) No, just DIY hacks/products.",
               "c) Yes, tried medical treatments (poor results).",
               "d) Yes, for a specific condition."])
section3_score += score_map[q6[0]]

q7 = st.radio("What does your 'Wash Day' look like?",
              ["a) Just the basics.",
               "b) Specific products for moisture/breakage.",
               "c) Strict routine, still worried.",
               "d) Very gentle, scalp sensitive/hair falling."])
section3_score += score_map[q7[0]]

# ---------------- Section 4 ----------------
st.header("4. Let’s Go a Little Deeper")

q8 = st.radio("How long has your hair been a concern?",
              ["a) Not much concern, just care.",
               "b) More than 6 months.",
               "c) More than 2 years.",
               "d) Over 5 years or since medical event."])
section4_score += score_map[q8[0]]

q9 = st.radio("Have you been going through major changes (stress, baby, health)?",
              ["a) No major changes.",
               "b) Some stress/diet change.",
               "c) Yes—stress, grief, illness.",
               "d) Yes—major event (surgery, childbirth, menopause)."])
section4_score += score_map[q9[0]]

# ---------------- Results ----------------
if st.button("Submit Survey"):
    total_score = section1_score + section2_score + section3_score + section4_score

    st.subheader("You are the ideal candidate for our")


    

    # Stream allocation
    if 10 <= total_score <= 16:
        stream = "Replenish Stream"
        st.write("REPLENISH STREAM")
        st.write("Your responses indicate a strong baseline of hair and scalp health with minimal signs of damage or loss. The focus at this stage is preservation, protection, and long-term optimisation")
        st.success("Replenish Stream: Preventive Maintenance Programme \n \nIt’s wonderful to see that your crown is standing strong with a healthy foundation. Because you aren’t currently facing hair trauma, our Replenish Stream is all about protecting your peace. It’s a medically backed, preventative journey designed to keep your hair serving you beautifully for years to come.")
    elif 17 <= total_score <= 24:
        stream = "Restoration Stream"
        st.write("RESTORATION STREAM")
        st.write("Your assessment suggests mild to moderate hair damage, commonly linked to chemical processing, heat styling, or inconsistent care routines.")
        st.info("Restoration Stream: Damage Repair & Strengthening Programme \n \nIt sounds like your hair has been through a lot, and we recognize that accumulated damage is a trauma of its own. Our Restoration Stream is here to help you confront that damage and hit the reset button. We’ll work with you to repair and strengthen your strands, turning your hair journey back into a story of health")
    elif 25 <= total_score <= 32:
        stream = "Revitalise Stream"
        st.write("REVITALISE STREAM")
        st.write("Your responses point to active thinning or early-stage hair loss, often accompanied by lifestyle stressors, hormonal changes, or nutritional imbalances.")
        st.warning("Revitalise Stream: Thinning Intervention & Follicle Reactivation Programme \n \nNoticing that your hair is thinning can be a heavy experience, but you are making an amazing move by seeking a medical opinion now. Our Revitalise Stream is designed to address this hair trauma at the root. We use a multi-phase approach to stop active thinning in its tracks and help your hair work for you again, not against you.")
    elif 33 <= total_score <= 40:
        stream = "Regrow Stream"
        st.write("REGROW STREAM")
        st.write("Your responses reflect advanced thinning, patchy loss, or extensive hair loss, often associated with medical conditions, long-term stress, or clinical treatments.")
        st.error("Regrow Stream: Advanced Hair Loss & Regrowth Programme \n \nSignificant hair loss is a deeply personal trauma, and we want you to know you don’t have to face it alone. Our Regrow Stream is our most intensive, doctor-led programme, created specifically for this stage of your journey. We are here to help you recover and reclaim your crown through a specialized medical plan focused on true regrowth.")


    else:
        st.write("Invalid")
        message = "Please check responses."
        

    st.success(f"Recommended Pathway:")

    # ---------------- Save to Google Sheets ----------------
    new_data = {
        "Q1": q1, "Q2": q2, "Q3": q3,
        "Q4": q4, "Q5": q5,
        "Q6": q6, "Q7": q7,
        "Q8": q8, "Q9": q9,
        "Section1": section1_score,
        "Section2": section2_score,
        "Section3": section3_score,
        "Section4": section4_score,
        "TotalScore": total_score,
        "Stream": stream
    }

    # Append row to Google Sheet
    sheet.append_row(list(new_data.values()))

    st.info("✅ Your response has been recorded in Google Sheets.")



