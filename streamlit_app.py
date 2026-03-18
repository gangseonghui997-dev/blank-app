import streamlit as st

st.title("🎈 My new app")
st.write(
  "당신의 미래에는 행운이 가득하길!"
)
import streamlit as st
import random
import time

# 페이지 설정
st.set_page_config(
    page_title="신비한 타로 점술소 Professional",
    page_icon="🔮",
    layout="wide"
)

# 커스텀 CSS로 프리미엄 분위기 조성
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400;700&display=swap');
    
    html, body, [data-testid="stStandardExecutionContext"] {
        font-family: 'Noto+Serif+KR', serif;
    }

    .main {
        background-color: #0e1117;
        color: #e0e0e0;
    }
    
    .tarot-card {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border: 2px solid #d4af37;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        min-height: 500px;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
        position: relative;
        overflow: hidden;
    }
    
    .tarot-card::before {
        content: "";
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(212, 175, 55, 0.05) 0%, transparent 70%);
        pointer-events: none;
    }

    .tarot-card:hover {
        transform: translateY(-15px) scale(1.02);
        box-shadow: 0 20px 40px rgba(212, 175, 55, 0.2);
        border-color: #f1c40f;
    }
    
    .card-icon {
        font-size: 5rem;
        margin-bottom: 20px;
        filter: drop-shadow(0 0 10px rgba(212, 175, 55, 0.3));
    }
    
    .card-title {
        color: #d4af37;
        font-size: 1.8rem;
        margin-bottom: 15px;
        font-weight: 700;
        letter-spacing: 1px;
    }
    
    .card-meaning {
        font-size: 1rem;
        color: #cfd8dc;
        line-height: 1.8;
        text-align: justify;
        word-break: keep-all;
    }
    
    .spread-label {
        color: #9b59b6;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-bottom: 15px;
        font-size: 1.2rem;
        text-align: center;
        border-bottom: 1px solid #9b59b6;
        display: inline-block;
        width: 100%;
    }
    
    .mystical-header {
        text-align: center;
        padding: 40px 0;
        background: linear-gradient(to right, #d4af37, #f1c40f, #d4af37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: 900;
        margin-bottom: 10px;
    }
    
    .analysis-box {
        background: rgba(44, 62, 80, 0.4);
        border-left: 5px solid #d4af37;
        padding: 20px;
        border-radius: 0 10px 10px 0;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 타로 카드 데이터 (상세화 버전)
TAROT_DECK = {
    "0. 광대 (The Fool)": {
        "icon": "🎭",
        "meaning": """새로운 여정의 시작점에 서 있는 당신을 의미합니다. 
과거의 굴레에서 벗어나 아무런 편견 없이 미지의 세계로 발걸음을 내딛을 때입니다. 
때로는 무모해 보일 수 있으나, 그 순수한 열정과 용기가 당신을 예상치 못한 놀라운 기회로 인도할 것입니다. 
주변의 시선에 흔들리지 말고 당신의 직감을 믿고 과감하게 시작해보세요."""
    },
    "1. 마법사 (The Magician)": {
        "icon": "🪄",
        "meaning": """당신은 이미 목적을 달성하기 위한 모든 자원과 능력을 갖추고 있습니다. 
무에서 유를 창조하는 마법사처럼, 당신의 아이디어를 현실로 바꿀 강력한 에너지가 충만한 시기입니다. 
지적인 호기심과 탁월한 소통 능력을 발휘하여 주변 상황을 당신에게 유리하게 이끌어보세요. 
자신감을 갖고 행동으로 옮긴다면 불가능해 보이던 일들도 실마리가 풀리기 시작할 것입니다."""
    },
    "2. 고위 여사제 (The High Priestess)": {
        "icon": "📖",
        "meaning": """내면의 깊은 울림과 직관에 집중해야 하는 정적인 통찰의 시기입니다. 
겉으로 보이는 현상 뒤에 숨겨진 진실을 꿰뚫어 보는 지혜가 당신 안에 이미 존재하고 있습니다. 
지금은 성급하게 행동하기보다 고요히 사색하며 지식을 쌓고 타이밍을 기다리는 것이 현명합니다. 
당신의 무의식이 보내는 신호나 꿈의 메시지에 귀를 기울이면 결정적인 답을 찾게 될 것입니다."""
    },
    "3. 여황제 (The Empress)": {
        "icon": "👑",
        "meaning": """삶의 모든 영역에서 풍요로움과 창조적인 활력이 샘솟는 시기입니다. 
정성껏 가꾸어온 일들이 결실을 맺기 시작하며, 물질적·정신적인 안정을 누리게 될 것입니다. 
주변 사람들에게 따뜻한 자애로움을 베풀고 감각적인 즐거움을 충분히 만끽하는 여유를 가지세요. 
새로운 생명이나 프로젝트의 탄생을 예고하며, 당신의 포용력이 더 큰 성장을 불러올 것입니다."""
    },
    "4. 황제 (The Emperor)": {
        "icon": "🏛️",
        "meaning": """강력한 지도력과 체계적인 질서를 통해 기반을 공고히 해야 할 때입니다. 
감정에 휘둘리기보다 이성적이고 논리적인 판단으로 상황을 통제하고 책임감을 보여주세요. 
당신이 세운 규칙과 원칙이 당신을 보호하고 목표를 향한 안정적인 가이드를 제공할 것입니다. 
권위 있는 인물의 도움을 받거나, 스스로가 누군가의 든든한 버팀목이 되어 큰 성취를 이룰 수 있습니다."""
    },
    "5. 교황 (The Hierophant)": {
        "icon": "⛪",
        "meaning": """전통적인 가치와 사회적 규범 속에서 진정한 의미를 찾아가는 과정입니다. 
혼자 고민하기보다는 해당 분야의 전문가나 신뢰할 수 있는 멘토를 찾아 조언을 구하는 것이 유리합니다. 
정해진 절차와 형식을 따르는 것이 지금의 혼란을 정리하고 올바른 길로 안내해 줄 것입니다. 
배움에 대한 열정을 가지고 지식을 공유하며 집단 내에서 조화를 이루는 데 힘쓰세요."""
    },
    "6. 연인 (The Lovers)": {
        "icon": "💖",
        "meaning": """마음이 통하는 이와의 깊은 유대감이나 가치관의 일치를 경험하게 될 것입니다. 
중요한 선택의 기로에서 당신은 논리보다는 진정한 감정과 도덕적 가치를 우선시해야 합니다. 
서로를 존중하고 이해하는 태도가 모든 관계의 어려움을 해결하는 열쇠가 됩니다. 
당신의 진심이 닿는 곳에 행운이 깃들어 있으며, 조화로운 파트너십이 큰 힘이 되어줄 것입니다."""
    },
    "7. 전차 (The Chariot)": {
        "icon": "🛡️",
        "meaning": """상반된 요구들 사이에서 균형을 유지하며 목표를 향해 무섭게 돌진하는 시기입니다. 
강한 의지력과 결단력으로 앞에 놓인 장애물을 정면으로 돌파하고 승리를 쟁취하세요. 
지금은 멈추거나 주저할 때가 아니며, 당신의 통제력을 믿고 가속도를 붙여야 할 때입니다. 
정신적인 집중력을 유지한다면 결국 당신이 원하는 목적지에 가장 빠르게 도달하게 될 것입니다."""
    },
    "8. 힘 (Strength)": {
        "icon": "🦁",
        "meaning": """육체적인 강인함보다 내면의 인내와 부드러운 통제력이 빛을 발하는 순간입니다. 
두려움이나 본능적인 충동을 억누르는 것이 아니라, 따뜻한 이해와 포용으로 다스려야 합니다. 
어려운 상황 속에서도 유연함을 잃지 않는 당신의 태도가 주변을 감화시키고 해결책을 제시할 것입니다. 
자신에 대한 믿음을 굳건히 하고 조용하지만 강력한 의지로 상황을 주도해 나가세요."""
    },
    "9. 은둔자 (The Hermit)": {
        "icon": "🏮",
        "meaning": """외부의 소음에서 벗어나 스스로의 내면을 깊이 성찰해야 하는 고독의 시간입니다. 
복잡한 세상사에서 잠시 거리를 두고 진정한 자아의 목소리를 찾는 과정이 필요합니다. 
지금의 침묵과 고독은 당신의 영혼을 성숙시키고 다음 단계를 위한 영적인 지혜를 채워줄 것입니다. 
서두르지 말고 당신만의 속도로 진리를 탐구하다 보면 어둠을 밝힐 등불을 발견하게 됩니다."""
    },
    "10. 운명의 수레바퀴 (Wheel of Fortune)": {
        "icon": "🎡",
        "meaning": """당신의 삶에 거부할 수 없는 변화의 소용돌이가 찾아오고 있음을 암시합니다. 
피할 수 없는 행운이나 전환점이 찾아왔으니, 변화의 흐름에 순응하고 기회를 잡으세요. 
모든 것은 순환하며 지금의 어려움 또한 새로운 희망의 시작이 될 수 있음을 잊지 마십시오. 
당신이 통제할 수 없는 영역을 인정하고 낙관적인 태도로 운명의 부름에 응답할 준비를 하세요."""
    },
    "11. 정의 (Justice)": {
        "icon": "⚖️",
        "meaning": """뿌린 대로 거둔다는 인과응보의 법칙이 엄격하게 작용하는 시기입니다. 
감정을 배제하고 객관적인 사실에 입각하여 모든 상황을 공정하게 판단해야 합니다. 
정직하고 투명한 태도가 장기적으로 당신에게 가장 큰 이익과 명예를 가져다줄 것입니다. 
과거의 행동에 대한 책임감을 가지고 균형 잡힌 결정을 내린다면 법적 혹은 계약적 문제도 원만히 해결됩니다."""
    },
    "12. 매달린 사람 (The Hanged Man)": {
        "icon": "🧗",
        "meaning": """일이 정체된 것처럼 보이지만, 사실은 더 큰 도약을 위한 자발적인 멈춤의 상태입니다. 
기존의 사고방식을 뒤집어 전혀 새로운 관점에서 상황을 바라보는 역발상이 필요합니다. 
지금 당장 결과가 나오지 않더라도 인내심을 갖고 희생을 감수할 때 영적인 통찰과 깨달음이 옵니다. 
집착을 내려놓고 우주의 흐름에 몸을 맡기면 오히려 보이지 않던 해결의 열쇠가 나타날 것입니다."""
    },
    "13. 죽음 (Death)": {
        "icon": "⌛",
        "meaning": """오랫동안 지속되어 온 낡은 습관이나 관계가 완전히 끝을 맺는 필연적인 시기입니다. 
이 상실은 파괴가 아니라, 새로운 탄생을 위한 필수적인 정화와 탈피의 과정임을 명심하세요. 
과거를 미련 없이 떠나보낼 때 비로소 당신의 삶에는 신선한 에너지와 새로운 가능성이 들어옵니다. 
변화를 두려워하며 붙잡지 마세요. 더 나은 내일을 위해 깨끗하게 정리하고 비워야 할 때입니다."""
    },
    "14. 절제 (Temperance)": {
        "icon": "🏺",
        "meaning": """극단을 피하고 중용의 도를 지켜 서로 다른 요소들을 평화롭게 융합해야 할 때입니다. 
인내심을 가지고 상충되는 의견이나 감정을 잘 조율한다면 완벽한 조화를 이룰 수 있습니다. 
내면의 평화를 유지하며 절제된 행동을 보여줌으로써 주변에 영적인 안도감을 선사하게 됩니다. 
서두르기보다 점진적인 변화와 지속적인 노력으로 건강한 균형 상태를 만들어가는 것이 핵심입니다."""
    },
    "15. 악마 (The Devil)": {
        "icon": "👹",
        "meaning": """중독적인 습관이나 물질적인 집착, 혹은 부정적인 관계에 얽매여 있을 수 있습니다. 
당신을 속박하고 있는 것이 외부의 힘이 아니라 스스로 만든 두려움과 욕망임을 깨달아야 합니다. 
지금 당장의 쾌락이나 유혹은 장기적으로 당신의 영혼을 지치게 할 수 있음을 경계하십시오. 
자신의 어두운 면을 정면으로 마주하고 그 속박에서 벗어나고자 하는 강한 자유 의지를 발휘해야 합니다."""
    },
    "16. 탑 (The Tower)": {
        "icon": "⚡",
        "meaning": """당신의 근간을 흔들 정도로 갑작스럽고 충격적인 변화가 닥쳐올 수 있습니다. 
하지만 이는 잘못된 토대 위에 세워진 허상을 무너뜨리고 진실을 드러내기 위한 우주의 배려입니다. 
예상치 못한 불운처럼 보일지라도, 무너진 자리에서 비로소 가장 견고하고 정직한 시작을 할 수 있습니다. 
충격을 겸허히 수용하고 신속하게 상황을 정리하며 더 나은 구조를 재건하는 데 집중하세요."""
    },
    "17. 별 (The Star)": {
        "icon": "✨",
        "meaning": """고난의 터널을 지나 비로소 평화와 희망의 빛을 맞이하게 되는 치유의 시기입니다. 
당신의 영혼이 정화되고 창조적인 영감이 샘솟으며, 미래에 대한 긍정적인 확신이 생길 것입니다. 
지금은 무리하게 활동하기보다 내면의 평온을 되찾고 스스로를 돌보며 꿈을 설계하는 시간입니다. 
우주가 당신을 보호하고 있으며, 당신의 진심 어린 소망이 실현될 것임을 믿고 밝게 웃으세요."""
    },
    "18. 달 (The Moon)": {
        "icon": "🌙",
        "meaning": """불확실성과 안갯속을 걷는 듯한 막막함 속에 직관의 힘이 절실히 필요한 때입니다. 
숨겨진 적이나 감추어진 진실 때문에 불안을 느낄 수 있으나, 이는 당신의 상상이 만든 환상일 수 있습니다. 
논리적으로 설명하기 힘든 미묘한 변화를 감지하고, 어스름한 불빛 아래서 조심스럽게 전진해야 합니다. 
혼란스러운 감정에 휩쓸리지 말고 당신의 내면이 보내는 동물적인 감각과 직관을 따라가세요."""
    },
    "19. 태양 (The Sun)": {
        "icon": "☀️",
        "meaning": """인생에서 가장 환하고 눈부신 성공과 기쁨의 에너지가 당신을 감싸고 있습니다. 
모든 의구심이 사라지고 상황이 명쾌해지며, 추진하는 일마다 활기찬 성과를 거두게 될 것입니다. 
당신의 순수한 열정과 밝은 기운이 주변 사람들까지 행복하게 만드는 강력한 영향력을 발휘합니다. 
지금 이 순간의 행복을 마음껏 즐기고 감사를 표현하며, 당당하게 당신의 존재감을 세상에 드러내세요."""
    },
    "20. 심판 (Judgement)": {
        "icon": "🎺",
        "meaning": """지나온 삶에 대한 결산을 하고 새로운 소명을 향해 다시 태어나는 부활의 때입니다. 
과거의 실수에 대해 스스로를 용서하고, 무거운 짐을 내려놓음으로써 진정한 자유를 얻게 됩니다. 
중요한 결단의 순간이 왔으며, 당신의 내면에서 울려 퍼지는 선명한 부름에 응답해야 합니다. 
새로운 기회가 주어졌음을 인식하고, 지난 경험을 양분 삼아 더 높은 차원으로 비상할 준비를 하세요."""
    },
    "21. 세계 (The World)": {
        "icon": "🌍",
        "meaning": """하나의 큰 주기가 완벽하게 마무리되고 최상의 조화와 승리를 거머쥐는 결실의 시기입니다. 
당신의 노력이 마침내 인정받아 세상과 온정적으로 연결되며 깊은 보람을 느끼게 될 것입니다. 
이는 끝이 아니라 더 넓은 세상을 향한 새로운 여행을 준비하는 완성이기도 합니다. 
당신이 이룬 성취를 축하하며, 우주가 주는 풍요로운 평화와 일체감을 마음껏 누리도록 하세요."""
    }
}

def draw_cards():
    return random.sample(list(TAROT_DECK.items()), 3)

# 메인 UI
st.markdown('<div class="mystical-header">신비한 타로 점술소 Professional</div>', unsafe_allow_html=True)

# 세션 상태 호환성 확인 (구조 변경 시 초기화)
if 'drawn_cards' in st.session_state:
    if not isinstance(st.session_state.drawn_cards[0][1], dict):
        del st.session_state.drawn_cards
        if 'flipped' in st.session_state:
            del st.session_state.flipped

with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.write("### 오늘의 운명을 심층적으로 분석해 드립니다.")
        st.write("과거-현재-미래의 유기적인 연계성을 통해 당신의 삶의 흐름을 3줄 이상의 상세한 문장으로 풀어드립니다.")
        if st.button("✨ 운명의 카드 섞기 & 뽑기", use_container_width=True):
            with st.status("신비로운 영적 에너지를 모으는 중...", expanded=True) as status:
                st.write("카드를 셔플하고 있습니다...")
                time.sleep(1)
                st.write("당신의 기운을 카드에 담고 있습니다...")
                time.sleep(1)
                st.write("운명의 배열을 결정했습니다.")
                status.update(label="셔플 완료!", state="complete", expanded=False)
            
            st.session_state.drawn_cards = draw_cards()
            st.session_state.flipped = [False, False, False]
            st.balloons()

if 'drawn_cards' in st.session_state:
    st.write("---")
    cols = st.columns(3)
    labels = ["과거 (Past)", "현재 (Present)", "미래 (Future)"]
    
    for i, (card_name, data) in enumerate(st.session_state.drawn_cards):
        with cols[i]:
            st.markdown(f'<div class="spread-label">{labels[i]}</div>', unsafe_allow_html=True)
            
            card_placeholder = st.empty()
            
            # 카드 뒷면 (선택 전)
            if not st.session_state.flipped[i]:
                with card_placeholder.container():
                    st.markdown(f"""
                    <div class="tarot-card">
                        <div style="font-size: 5rem; color: #d4af37; margin-bottom: 20px;">🌙</div>
                        <p style="font-size: 1.1rem; color: #d4af37; font-weight: bold;">{labels[i]}의 메시지</p>
                        <p style="margin-top: 10px; font-size: 0.9rem;">봉인된 운명을 확인하세요</p>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"{labels[i]} 봉인 해제", key=f"btn_{i}", use_container_width=True):
                        st.session_state.flipped[i] = True
                        st.rerun()
            
            # 카드 앞면 (선택 후)
            else:
                with card_placeholder.container():
                    st.markdown(f"""
                    <div class="tarot-card">
                        <div class="card-icon">{data['icon']}</div>
                        <div class="card-title">{card_name}</div>
                        <div class="card-meaning">{data['meaning']}</div>
                    </div>
                    """, unsafe_allow_html=True)

    if all(st.session_state.flipped):
        st.write("---")
        st.subheader("🔮 종합 운세 실타래 분석")
        
        c1, c2, c3 = st.session_state.drawn_cards
        
        analysis_text = f"당신은 과거 **{c1[0]}**의 기운을 지나 현재 **{c2[0]}**의 상황에 놓여 있으며, 이는 필연적으로 **{c3[0]}**의 미래로 이어지게 됩니다. "
        analysis_text += "과거의 경험이 현재 당신의 내면을 단단하게 만들었으며, 지금 당신이 마주한 선택이 미래의 밝은 빛을 결정짓는 핵심 고리가 될 것입니다. "
        analysis_text += "운명은 정해진 것이 아니라 당신의 의지로 가꾸어가는 정원과 같습니다. 오늘의 조언을 가슴에 새기고 지혜로운 첫걸음을 떼시길 바랍니다."

        st.markdown(f"""
        <div class="analysis-box">
            <p style="font-size: 1.1rem; line-height: 1.8; color: #ffffff;">
                {analysis_text}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔄 새로운 운명 점치기", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

# 푸터
st.markdown("""
<div style="text-align: center; margin-top: 60px; color: #444; font-size: 0.85rem; border-top: 1px solid #333; padding-top: 20px;">
    © 2026 Mystical Tarot Lab Professional | Inspired by Rider-Waite Tradition<br>
    <i>"Astra regunt homines, sed regit astra Deus" (별이 인간을 다스리나, 신은 별을 다스린다)</i>
</div>
""", unsafe_allow_html=True)
