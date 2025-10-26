import streamlit as st
from search import google_custom_search
from summarize import summarize_with_gemini, summarize_all_snippets_parallel
from user_dialog import friendly_problem_understanding
from config import get_google_api_key, get_google_cx, get_gemini_api_key

st.set_page_config(page_title="Medical Perplexity", layout="wide")
st.title("Medical Perplexity — Fast, Trusted, Friendly Medical Search Assistant")
st.markdown("Enter your medical question to search trusted health sites and get AI-powered summaries.")


# Config/keys (get from env variables or .streamlit/secrets.toml for deployment)
google_api_key = get_google_api_key()
cx = get_google_cx()
gemini_api_key = get_gemini_api_key()
num_results = st.slider("Number of top web results:", 3, 10, 5)
# gemini_model = st.text_input("Gemini model (default: gemini-2.5-pro):", value="gemini-2.5-pro")

user_input = st.text_area("Describe your question or medical problem:")
if st.button("Ask Medical Assistant"):
    if not (google_api_key and cx and gemini_api_key):
        st.error("API keys or CX missing! Please provide them above.")
    else:
        st.info("Great! I'll research your problem and summarize the medical sources.")
        with st.spinner("Searching trusted medical sites..."):
            results = google_custom_search(user_input, google_api_key, cx, num_results)
        if not results:
            st.error("No results found.")
        else:
            # Combined multi-site summary
            with st.spinner("Summarizing across all sources..."):
                overall_summary = summarize_with_gemini(results, user_input, gemini_api_key, gemini_model)
            st.header("Synthesized Medical Summary (All Sources)")
            st.success(overall_summary)

            st.markdown("### Individual Source Summaries")
            # Parallel summary for all sources!
            with st.spinner("Summarizing all sources in parallel..."):
                all_summaries = summarize_all_snippets_parallel(
                    results,
                    user_input,
                    gemini_api_key,
                    gemini_model,
                    max_workers=min(8, len(results))  # up to 8 parallel jobs
                )
            for i, (res, single_sum) in enumerate(zip(results, all_summaries), 1):
                st.markdown(f"**{i}. {res['title']}**")
                st.info(single_sum)
                st.markdown(f"[Source website]({res['url']})")
                st.markdown("---")


st.markdown("""
_Results powered by Google Custom Search API (trusted medical domains).  
Summaries provided by Gemini (Google Generative AI)._
""")