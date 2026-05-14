import wikipedia

def fetch_festival_data(festival_name):

    try:

        summary = wikipedia.summary(
            festival_name,
            sentences=5
        )

        page = wikipedia.page(
            festival_name
        )

        return {
            "title": page.title,
            "summary": summary,
            "url": page.url
        }

    except:

        return None
