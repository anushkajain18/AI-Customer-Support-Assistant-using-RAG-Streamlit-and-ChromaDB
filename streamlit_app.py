import streamlit as st
import asyncio
from src.llm.agent import CustomerSupportAgent

st.set_page_config(
    page_title="AI Customer Support Assistant",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 AI Customer Support Assistant")

query = st.text_input("Ask a Customer Support Question")

if st.button("Get Response"):

    if query:

        try:
            with st.spinner("Searching Knowledge Base..."):

                agent = CustomerSupportAgent()

                asyncio.run(agent.initialize())

                response = asyncio.run(
                    agent.process_query(query)
                )

            st.success("Response Generated")

            st.code(response)

        except Exception as e:

            st.error(str(e))