import requests

def google_custom_search(query, api_key, cx, num_results=5):
    api_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": cx,
        "q": query,
        "num": num_results
    }
    resp = requests.get(api_url, params=params)
    items = []
    if resp.status_code == 200 and "items" in resp.json():
        for item in resp.json()["items"]:
            snippet = item.get("snippet", "")
            title = item.get("title", "")
            url = item.get("link", "")
            items.append({"title": title, "url": url, "text": snippet})
    return items
