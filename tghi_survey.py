import streamlit as st

st.title("TGHI Hair Health Questionnaire")

# Mapping for scores
score_map = {"a": 1, "b": 2, "c": 3, "d": 4}

total_score = 0

# --- Section 1 ---
st.header("1. Relationship with Your Hair")

q1 = st.radio("How is your hair’s volume looking compared to 2-3 years ago?",
              ["a) Still thick and thriving.",
               "b) A little thinner. I can see more of my scalp than I used to.",
               "c) Noticeably thinner. My puff is smaller or my part is looking noticeably wider.",
               "d) I see significant changes or visible patches of hair loss."])
total_score += score_map[q1[0]]

q2 = st.radio("Are wigs, weaves, or braids your 'crutch' right now to hide damage or thinning?",
              ["a) Not at all—I mostly rock my natural hair.",
               "b) Sometimes, but just for a switch-up. Not to hide anything.",
               "c) Often. I use them to cover up thinning areas or breakage.",
               "d) Every day. I don’t feel comfortable showing my natural hair due to loss."])
total_score += score_map[q2[0]]

q3 = st.radio("How often are you using heat, colour, or chemicals (relaxers, bleach, etc.)?",
              ["a) Rarely or never. I’m Team Natural all the way.",
               "b) Only when I need to, for a special look.",
               "c) Every few weeks. I love a fresh look.",
               "d) I used to go hard with the chemicals, but I’ve stopped because of the damage."])
total_score += score_map[q3[0]]

# --- Section 2 ---
st.header("2. How You’re Feeling")

q4 = st.radio("Does your hair affect your mood or confidence during the day?",
              ["a) Not really—I’m feeling good about my hair.",
               "b) Some days are harder than others to make it look 'right.'",
               "c) I feel self-conscious and avoid certain styles or social events.",
               "d) It’s really stressing me out and affecting my social life in a negative way."])
total_score += score_map[q4[0]]

q5 = st.radio("What is your main 'Hair Goal' right now?",
              ["a) Maintenance: Just keeping my healthy hair at its best.",
               "b) Repair: Fixing the damage and getting my strength back.",
               "c) Reversal: Stopping the thinning and getting my density back.",
               "d) Regrowth: Bringing back my edges or filling in bald spots."])
total_score += score_map[q5[0]]

# --- Section 3 ---
st.header("3. Methods You’ve Used Before")

q6 = st.radio("Have you ever seen a doctor or derm about your hair before?",
              ["a) No, never needed to.",
               "b) No, I’ve just been trying DIY hacks or products I have bought by myself.",
               "c) Yes, I’ve tried medical treatments and the results have not been so great.",
               "d) Yes, for a specific condition (such as Alopecia, PCOS, or post-medical treatment)."])
total_score += score_map[q6[0]]

q7 = st.radio("What does your 'Wash Day' look like lately?",
              ["a) Nothing fancy—just the basics.",
               "b) I use specific products to help with moisture and breakage.",
               "c) I have a strict routine with specialised products, but I’m still worried.",
               "d) Very gentle. I barely touch it because my scalp is sensitive or hair is falling out."])
total_score += score_map[q7[0]]

# --- Section 4 ---
st.header("4. Let’s Go a Little Deeper")

q8 = st.radio("How long has your hair been a concern for you?",
              ["a) My Hair isn’t much of a concern for me right now—I'm just looking for ways to take better care of it.",
               "b) I’ve been sideways worrying about my hair for more than 6 months now",
               "c) It’s been more than 2 years that my concern about my hair has been nagging me.",
               "d) It’s been over 5 years, or since a specific medical event (ie Surgery, diagnosis, treatment etc)"])
total_score += score_map[q8[0]]

q9 = st.radio("Have you been going through the most lately? (Stress, new baby, health changes in the last 2 years?)",
              ["a) No major changes.",
               "b) Maybe a little extra stress or a change in diet.",
               "c) Yes—I’ve dealt with a lot of stress, grief, or a long illness.",
               "d) Yes—a major event like surgery, childbirth, or menopause."])
total_score += score_map[q9[0]]

# --- Results ---
if st.button("Submit Survey"):
    st.subheader("Your Total Hair Health Score")
    st.write(f"**{total_score} points**")

    # Stream allocation based on score
    if 10 <= total_score <= 16:
        st.success("Replenish Stream: Preventive Maintenance Programme")
    elif 17 <= total_score <= 24:
        st.info("Restoration Stream: Damage Repair & Strengthening Programme")
    elif 25 <= total_score <= 32:
        st.warning("Revitalise Stream: Thinning Intervention & Follicle Reactivation Programme")
    elif 33 <= total_score <= 40:
        st.error("Regrow Stream: Advanced Hair Loss & Regrowth Programme")
