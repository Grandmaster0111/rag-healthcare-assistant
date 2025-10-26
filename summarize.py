import google.generativeai as genai
from concurrent.futures import ThreadPoolExecutor

# Combined summary for all results
def summarize_with_gemini(sources, query, api_key, gemini_model="gemini-2.5-pro"):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(gemini_model)
    context = "\n\n".join([
        f"- {src['title']}: {src['text']}"
        for src in sources if src['text']
    ])
    prompt = (
        "As a friendly medical assistant, write a concise and accurate answer to the user's question using only the following web search results. "
        "Cite website titles as sources in your response, use clear language, and avoid generic openers. "
        f"User's question: {query}\n\n{context}\n\nSummary answer (with citations):"
    )
    response = model.generate_content(prompt)
    return response.text.strip() if hasattr(response, "text") else str(response)

# Parallel worker: concise, direct, non-generic opener
def summarize_single_snippet_worker(args):
    snippet, site_title, site_url, query, api_key, gemini_model = args
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(gemini_model)
    prompt = (
        "As a professional medical assistant, answer the user's question only with directly relevant information from the snippet below."
        "Start your summary with the answer—do NOT use phrases like 'Of course', 'According to', 'Sure', 'Certainly', or similar. "
        "Do not include apologies or explanations. Begin immediately with useful medical facts, and use bullet points for lists. "
        "Mention the website title for attribution at the end, separated in parentheses. Example: (Source: Mayo Clinic)\n\n"
        f"Snippet: {snippet}\n\n"
        f"User question: {query}\n\n"
        "Summary:"
    )
    response = model.generate_content(prompt)
    text = response.text.strip() if hasattr(response, "text") else str(response)
    # Still post-process if needed:
    unwanted_openers = ['Of course', 'According to', 'Sure', 'Certainly', 'Surely', 'It appears', 'Apparently']
    for opener in unwanted_openers:
        if text.lower().startswith(opener.lower()):
            text = text[len(opener):].lstrip(" ,.!:")
    return text


# Parallel executor for all snippets
def summarize_all_snippets_parallel(results, query, api_key, gemini_model="gemini-2.5-pro", max_workers=5):
    args_list = [
        (res['text'], res['title'], res['url'], query, api_key, gemini_model)
        for res in results
    ]
    summaries = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for single_summary in executor.map(summarize_single_snippet_worker, args_list):
            summaries.append(single_summary)
    return summaries
