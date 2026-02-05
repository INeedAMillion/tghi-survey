import streamlit as st
import pandas as pd
import os

st.title("TGHI Hair Health Questionnaire")

st.markdown("""
You’ll be amazed what little thought people give to the treatment of hair trauma.  
That is why we think it’s amazing that you’re making a move to get the medical opinion necessary to help you confront the hair trauma you have encountered.  

We’re here to help you make the best of your journey towards what good hair is to you. Hair that serves you and does not work against you.  
This quick 2-minute check-in helps our medical team understand your journey so we can match you with the right therapy.  

**Note:** This is not a medical diagnosis, but it is the first step toward your expert consultation and a personalised plan.
""")

# Mapping for scores
score_map = {"a": 1, "b": 2, "c": 3, "d": 4}

# Section scores
section1_score = 0
section2_score = 0
section3_score = 0
section4_score = 0

# --- Section 1 ---
st.header("1. Relationship with Your Hair")

q1 = st.radio("How is your hair’s volume looking compared to 2-3 years ago?",
              ["a) Still thick and thriving.",
               "b) A little thinner.",
               "c) Noticeably thinner.",
               "d) Significant changes or patches."])
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

# --- Section 2 ---
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

# --- Section 3 ---
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

# --- Section 4 ---
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

# --- Results ---
if st.button("Submit Survey"):
    total_score = section1_score + section2_score + section3_score + section4_score

    st.subheader("Section Scores")
    st.write(f"Section 1 (Relationship with Hair): {section1_score}")
    st.write(f"Section 2 (Feelings): {section2_score}")
    st.write(f"Section 3 (Methods Used): {section3_score}")
    st.write(f"Section 4 (Deeper Concerns): {section4_score}")

    st.subheader("Total Hair Health Score")
    st.write(f"**{total_score} points**")

    # Stream allocation
    if 10 <= total_score <= 16:
        stream = "Replenish Stream"
        message = "Preventive Maintenance Programme"
    elif 17 <= total_score <= 24:
        stream = "Restoration Stream"
        message = "Damage Repair & Strengthening Programme"
    elif 25 <= total_score <= 32:
        stream = "Revitalise Stream"
        message = "Thinning Intervention & Follicle Reactivation Programme"
    elif 33 <= total_score <= 40:
        stream = "Regrow Stream"
        message = "Advanced Hair Loss & Regrowth Programme"
    else:
        stream = "Invalid"
        message = "Please check responses."

    st.success(f"Recommended Pathway: {stream} — {message}")

    # --- Save to CSV ---
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
    df = pd.DataFrame([new_data])

    if os.path.exists("survey_results.csv"):
        df.to_csv("Desktop/survey_results.csv", mode="a", header=False, index=False)
    else:
        df.to_csv("survey_results.csv", index=False)

    st.info("Your response has been recorded.")


