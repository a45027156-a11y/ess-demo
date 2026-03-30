import hashlib
import random

# -------------------------
# ESS 환경 서명 생성
# -------------------------
def generate_signature(env):
    raw = f"{env['location']}-{env['time']}-{env['wifi']}-{env['motion']}-{env['noise']}"
    return hashlib.sha256(raw.encode()).hexdigest()

# -------------------------
# 이상 탐지 (Mock AI)
# -------------------------
def detect_anomaly(env):
    
    base_score = 85

    # 위치 변화 영향
    if env["location"].lower() not in ["home", "seoul"]:
        base_score -= 15

    # WiFi 이상
    if "Unknown" in env["wifi"]:
        base_score -= 10

    # 이동 상태
    if env["motion"] == "Running":
        base_score -= 5

    # 노이즈 영향
    base_score -= env["noise"] * 0.2

    score = max(40, min(100, int(base_score)))

    result = "NORMAL" if score >= 80 else "ABNORMAL"

    return result, score
