import time
import streamlit as st

class VoicePipeline:
    def __init__(self, llm, tts):
        self.llm = llm
        self.tts = tts
        self.last_spoken_at = 0 

    def _find_form_issue(self, exercise, metrics):
        if "issue" in metrics:
            return metrics["issue"]
        
        if exercise == "Squats":
            depth = metrics.get("depth_status", "")
            back_angle = metrics.get("back_angle", 100)

            if depth == "TOO HIGH":
                return "The User's Squat Is Not Deep Enough - Knees Are Not Bending Sufficiently."
            
            if isinstance(back_angle, (int, float)) and back_angle < 130:
                return "The User Is Leaning Too Far Forward During The Squat."
            
        elif exercise == "Push-Ups":
            alignment = metrics.get("body_alignment", "")
            hip_status = metrics.get("hip_status", "")

            if alignment == "Poor Form":
                return "The User's Body Is Not Straight During The Push-Up."
            
            if hip_status == "SAGGING":
                return "The User's Hip's Are Sagging Down During The Push-Up."
            
            if hip_status == "PIKED UP":
                return "The User's Hip's Are Too High - Lower Them To Form A Straight Line."
            
        elif exercise == "Biceps Curls (Dumbell)":
            swing = metrics.get("swing_status", "")
            shoulder = metrics.get("shoulder_status", "")

            if swing == "SWINGING":
                return "The User Is Swinging Their Torse During The Curl - Keep The Body Still."
            
            if shoulder == "ELBOW DRIFTING":
                return "The User's Elbow Is Drifting Away From Their Side During The Curl."
            
        elif exercise == "Shoulder Press":
            back_arch = metrics.get("back_arch_status", "")
            extension = metrics.get("extension_status", "")

            if back_arch == "Excessive Arch":
                return "The User Is Arching Their Lower Back Excessively During The Press."
            
            if back_arch == "Slight Arch":
                return "Slight Back Arch Detected - Encourage The User To Brace Their Core."
            
        elif exercise == "Lunges":
            balance = metrics.get("balance_status", "")

            if balance == "OFF BALANCE":
                return "The User Is Losing Balance During The Lunge - Feet Should Be Hip-Width."
            
            return None

    def process_event(self, event, exercise, metrics):
        issue = self._find_form_issue(exercise, metrics)

        now = time.time()

        is_major_issue = event in ["workout_started", "set_completed", "workout completed"]

        if not is_major_issue:
            if not issue:
                return None
            
            if now - self.last_spoken_at < 5:
                return None
            
        text = self.llm.give_feedback(event, issue)
        voice = self.tts.speak(text)

        self.last_spoken_at = now
        return voice, text
    
def autoplay_audio(audio_bytes):
    if not audio_bytes:
        return
    
    st.markdown("<style>[data-testid='stAudio'] {display: none;}</style>", unsafe_allow_html=True)

    st.audio(audio_bytes, format="audio/mp3", autoplay=True)