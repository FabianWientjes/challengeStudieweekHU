import os
import warnings

import streamlit as st

warnings.simplefilter(action="ignore", category=FutureWarning)


def main() -> None:
    st.title("Company graphs")

    out_folder = "visualisaties/exploraties"
    for i in os.listdir(out_folder):
        if i.endswith(("png")):
            st.image(out_folder + i, caption=i)


if __name__ == "__main__":
    main()