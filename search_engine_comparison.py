"""
(very) simple job website lister (in one page)
v0.1 - basic version
"""

from string import Template

import streamlit as st
import streamlit.components.v1 as components

DEF_SEARCH_TERMS = "data"
IFRAME_X, IFRAME_Y = 1200, 500


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


def get_engines() -> dict:
    """
    get the ingfo on engines to use
    use `$input_text` where to inject the search term

    Returns:
        dict: id and template are mandatory
    """
    # pylint: disable=C0301

    return {
        "justjoin": {
            "id": "justjoin",
            "template": Template(
                "https://justjoin.it/job-offers/all-locations?keyword=$input_text&from=0"
            ),
        },
        "inhire": {
            "id": "inhire *",
            "template": Template("https://inhire.io/?roles=big_data"),
        },
        "solid jobs": {
            "id": "solid jobs",
            "template": Template("https://solid.jobs/offers/it;searchTerm=$input_text"),
        },
        "indeed": {
            "id": "indeed",
            "template": Template("https://pl.indeed.com/jobs?q=$input_text"),
        },
        "theprotocol": {
            "id": "theprotocol",
            "template": Template(
                "https://theprotocol.it/filtry/gdansk;wp?kw=$input_text"
            ),
        },
        "rocketjobs": {
            "id": "rocketjobs",
            "template": Template(
                "https://rocketjobs.pl/oferty-pracy/wszystkie-lokalizacje?keyword=$input_text&from=0"
            ),
        },
        "pracuj": {
            "id": "pracuj",
            "template": Template(
                "https://www.pracuj.pl/praca/$input_text"
            ),
        },
        "nofluffjobs": {
            "id": "nofluffjobs",
            "template": Template(
                "https://nofluffjobs.com/pl//$input_text"
            ),
        },
        # // add more here
        # https://snaphunt.com/resources/sourcing-and-assessing-talent/top-job-posting-sites-in-poland
    }


def get_container(input_text: str, jl_id: str, template: Template):
    """get container rendered html

    Args:
        input_text (str): the search term
        jl_id (str): some job lister id
        template (Template): a template to hold the metadata
    """
    src = template.safe_substitute(input_text=input_text)

    with st.container():
        col1, col2 = st.columns([0.3, 0.7],gap="small", vertical_alignment="top", border=False)
        with col1:
            st.write(jl_id)
            st.link_button(label=src, url=src)
        with col2:
            components.iframe(src, width=IFRAME_X, height=IFRAME_Y, scrolling=True)
        st.divider()


if __name__ == "__main__":
    main()
