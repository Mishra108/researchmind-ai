import streamlit as st
from agents import (
    build_search_agent,
    build_reader_agent,
    writer_chain,
    critic_chain,
)

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="ResearchMind AI",
    page_icon="🔬",
    layout="wide",
)

# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------

st.markdown("""
<style>

/* Background */
.stApp{
    background: linear-gradient(
        135deg,
        #020617 0%,
        #0f172a 50%,
        #1e293b 100%
    );
}

/* Container */
.block-container{
    max-width:1200px;
    padding-top:1.5rem;
}

/* Hero */
.hero{
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);
    border:1px solid rgba(255,255,255,0.08);
    border-radius:24px;
    padding:35px;
    text-align:center;
    margin-bottom:30px;
}

.main-title{
    font-size:4.8rem;
    font-weight:900;
    color:white;
}
.sub-title{
    color:#cbd5e1;
    font-size:1.1rem;
}

/* Input */
.stTextInput input{
    background:#1e293b !important;
    color:white !important;
    border:2px solid #334155 !important;
    border-radius:14px !important;
}

/* Button */
.stButton button{
    width:100%;
    height:55px;
    border:none;
    border-radius:14px;
    font-size:18px;
    font-weight:700;
    color:white;
    background:linear-gradient(
        90deg,
        #3b82f6,
        #6366f1
    );
}

/* Report Card */
.report-card{
    background:#111827;
    border:1px solid #374151;
    border-radius:16px;
    padding:20px;
}

/* Footer */
.footer{
    text-align:center;
    color:#94a3b8;
    margin-top:40px;
    padding:20px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

with st.sidebar:

    st.title("🔬 ResearchMind AI")

    st.markdown("### Multi-Agent Workflow")

    st.success("🔍 Search Agent")
    st.info("📄 Reader Agent")
    st.warning("✍️ Writer Agent")
    st.error("🧐 Critic Agent")

    st.divider()

    st.markdown("""
### Tech Stack

- Gemini
- Tavily
- LangChain
- Streamlit

### Workflow

Search → Read → Write → Critique
""")

# -------------------------------------------------
# HERO
# -------------------------------------------------

st.markdown("""
<div class="hero">

<div class="main-title">
🔬 ResearchMind AI
</div>

<div class="sub-title">
AI-Powered Multi-Agent Research Assistant
<br>
Search • Read • Analyze • Critique
</div>

</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# INPUT
# -------------------------------------------------

topic = st.text_input(
    "Research Topic",
    placeholder="e.g. Future of AI Agents in 2026"
)

run_btn = st.button("🚀 Generate Research")

# -------------------------------------------------
# PIPELINE
# -------------------------------------------------

if run_btn:

    if not topic.strip():
        st.warning("Please enter a research topic.")
        st.stop()

    status = st.status(
        "Starting Research...",
        expanded=True
    )

    try:

        # ---------------- SEARCH ---------------- #

        status.write("🔍 Search Agent running...")

        search_agent = build_search_agent()

        search_result = search_agent.invoke({
            "messages": [
                (
                    "user",
                    f"Find recent, reliable and detailed information about {topic}"
                )
            ]
        })

        search_content = (
            search_result["messages"][-1].content
        )

        # ---------------- READER ---------------- #

        status.write("📄 Reader Agent analyzing sources...")

        reader_agent = build_reader_agent()

        reader_result = reader_agent.invoke({
            "messages": [
                (
                    "user",
                    f"""
Based on these search results:

{search_content[:1000]}

Pick the best URL and scrape it.
"""
                )
            ]
        })

        scraped_content = (
            reader_result["messages"][-1].content
        )

        # ---------------- WRITER ---------------- #

        status.write("✍️ Writer Agent generating report...")

        combined_research = f"""
SEARCH RESULTS:
{search_content}

SCRAPED CONTENT:
{scraped_content}
"""

        report = writer_chain.invoke({
            "topic": topic,
            "research": combined_research
        })

        # ---------------- CRITIC ---------------- #

        status.write("🧐 Critic Agent reviewing report...")

        feedback = critic_chain.invoke({
            "report": report
        })

        status.update(
            label="✅ Research Complete",
            state="complete"
        )

        # -------------------------------------------------
        # METRICS
        # -------------------------------------------------

        st.divider()

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Agents",
            "4"
        )

        col2.metric(
            "Words",
            len(report.split())
        )

        col3.metric(
            "Topic",
            topic[:15] + "..."
            if len(topic) > 15
            else topic
        )

        col4.metric(
            "Status",
            "Complete"
        )

        st.divider()

        # -------------------------------------------------
        # TABS
        # -------------------------------------------------

        tab1, tab2, tab3 = st.tabs(
            [
                "📑 Report",
                "📝 Feedback",
                "🔍 Sources"
            ]
        )

        # ---------------- REPORT ---------------- #

        with tab1:

            st.markdown("## Research Report")

            st.markdown(report)

            st.download_button(
                "⬇ Download Report",
                data=report,
                file_name="research_report.md",
                mime="text/markdown"
            )

        # ---------------- FEEDBACK ---------------- #

        with tab2:

            st.markdown("## Critic Feedback")

            st.markdown(feedback)

        # ---------------- SOURCES ---------------- #

        with tab3:

            with st.expander(
                "🔍 Search Results",
                expanded=True
            ):
                st.write(search_content)

            with st.expander(
                "📄 Scraped Content"
            ):
                st.write(scraped_content)

    except Exception as e:

        st.error(f"Error: {e}")

# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.markdown("---")

st.markdown("""
<div class="footer">
ResearchMindAI  • Multi-Agent AI Research Assistant
<br>
Built with Streamlit  • Gemini • Tavily • LangChain
</div>
""", unsafe_allow_html=True)
