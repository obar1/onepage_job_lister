"""
(very) simple job website lister (in one page)
v0.1 - basic version
"""

from string import Template
import yaml

import streamlit as st
import streamlit.components.v1 as components
import requests
from bs4 import BeautifulSoup
import streamlit as st
import html

DEF_SEARCH_TERMS = "data engineer"
IFRAME_X, IFRAME_Y = 1200, 500


def get_engines() -> dict:
    """
    get the ingfo on engines to use
    use `$input_text` where to inject the search term

    Returns:
        dict: id and template are mandatory
    """
    with open("engines.yaml", "r", encoding="utf-8") as file:
        engines = yaml.safe_load(file)

    for engine in engines.values():
        engine["template"] = Template(engine["template"])

    return engines


def get_container(input_text: str, jl_id: str, template: Template):
    """get container rendered html

    Args:
        input_text (str): the search term
        jl_id (str): some job lister id
        template (Template): a template to hold the metadata
    """
    src = template.safe_substitute(input_text=input_text)

    with st.container():
        col1, col2 = st.columns(
            [0.3, 0.7], gap="small", vertical_alignment="top", border=False
        )
        with col1:
            st.write(jl_id)
            st.link_button(label=src, url=src)
        with col2:
            components.iframe(
                src,
                width=IFRAME_X,
                height=IFRAME_Y,
                scrolling=True,
            )
        st.divider()

def  get_combined_html(st, input_txt, search_engines):

    urls = []
    for k in search_engines.keys():
        template = search_engines[k]["template"]
        src = template.safe_substitute(input_text=input_txt)
        urls.append(src)

    print(urls)

    def fetch_html(url):
        """
        Fetch the HTML content from the given URL.
        
        Args:
            url (str): The URL to fetch HTML from.
        
        Returns:
            str: The HTML content if successful, None otherwise.
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            st.error(f"Error fetching {url}: {e}")
            return None

    def extract_body(html):
        """
        Extract the inner HTML content of the <body> tag.
        
        Args:
            html (str): The HTML content to parse.
        
        Returns:
            str: The inner HTML of the <body> tag if found, otherwise an empty string.
        """
        if html is None:
            return ""
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.find('body')
        if body:
            return body.decode_contents()
        else:
            return ""

    # Initialize an empty string to hold the combined HTML content
    combined_html = ""
    for url in urls:
        html_content = fetch_html(url)
        if html_content is None:
            combined_html += f"<h2>Content from {url}</h2><p>Failed to load content.</p><hr>"
        else:
            body_content = extract_body(html_content)
            combined_html += f"<h2>Content from {url}</h2>{body_content}<hr>"

    # Create the full HTML document
    full_html = f"<html><body>{combined_html}</body></html>"

    # Escape the HTML to make it safe for srcdoc
    escaped_html = html.escape(full_html)

    # Streamlit app
    st.write("Below are the job listings from various websites consolidated into one view.")
    st.components.v1.html(f'<iframe srcdoc="{escaped_html}" width="100%" height="600" frameborder="0"></iframe>', height=600)

def main():
    """main"""
    # pylint: disable=C0201,C0206
    st.set_page_config(layout="wide", page_title="obar1 1P Job lister")
    st.title("Search Engine Comparison")
    st.header("Enter your search query:")
    input_txt = st.text_input("search term:", DEF_SEARCH_TERMS)

    search_engines: dict = get_engines()
    if st.button("Submit"):
        st.subheader(f"Search Results for '{input_txt}'")
        for k in search_engines.keys():
            get_container(
                input_txt, search_engines[k]["id"], search_engines[k]["template"]
            )
    get_combined_html(st, input_txt, search_engines)

if __name__ == "__main__":
    main()
