import google.generativeai as genai

def summarize_with_gemini(sources, query, api_key, gemini_model="gemini-2.5-pro"):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(gemini_model)
    context = "\n\n".join([f"- {src['title']}: {src['text']}" for src in sources if src['text']])
    prompt = (
        "As a friendly medical assistant, write a concise and accurate answer to the user's question using ONLY the following web search results. Use a conversational tone, and cite sources.\n\n"
        f"{context}\n\n"
        f"User's question or problem: {query}\n\nSummary answer (with sources):"
    )
    response = model.generate_content(prompt)
    return response.text.strip() if hasattr(response, "text") else str(response)
