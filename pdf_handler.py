# from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.docstore.document import Document
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.chains import SimpleSequentialChain
from dotenv import load_dotenv
import arxiv_loader

load_dotenv()


def split_text_by_length(text, length):
    return [text[i:i + length] for i in range(0, len(text), length)]


def summary_latex(arxiv_id: str) -> list[str]:
    # Load PDF using PyPDFLoader
    documents = arxiv_loader.get_arxiv_paper(arxiv_id)

    # Define a LaTeX slide template
    summary_prompt = ("Summary the text (less than 500 words) "
                      "and transform into latex code of text(after:) "
                      ":{text} ")
    summary_prompt = PromptTemplate(template=summary_prompt,
                                    input_variables=["text"])
    latex_prompt = ("Generate LaTeX slide code with at most three slides "
                    "each slide must include the suitable frametitle "
                    "The each slide must start from begin{{frame}} "
                    "and must end with end{{frame}} "
                    "The title should only use the format "
                    "frametitle{{title}} "
                    "if the content include the import definition or theorem "
                    "the slide should include the suitable "
                    "definition or theorem "
                    "or list the key concept of text "
                    "the return should not include the begin{{document}} "
                    "and end{{document}} "
                    "for the text "
                    "(after:):{text}")

    latex_prompt = PromptTemplate(template=latex_prompt,
                                  input_variables=["text"])
    # Initialize language model with the new prompt
    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')

    # Prepare the summarization chain with the new language model
    summary_chain = LLMChain(llm=llm, prompt=summary_prompt)
    latex_chain = LLMChain(llm=llm, prompt=latex_prompt)
    overall_chain = SimpleSequentialChain(chains=[summary_chain, latex_chain],
                                          verbose=True)

    # Initialize a list to hold the summaries
    first_latex_code = r"""
    \documentclass{beamer}
    \usetheme{Madrid}
    \begin{document}
    """
    end_latex_code = r"""
    \end{document}
    """
    latex_slides = [first_latex_code]

    for page, doc in enumerate(documents[:2]):
        print("Current in the page {}".format(page + 1))
        # Create a Document for each text
        docs = [
            Document(page_content=t)
            for t in split_text_by_length(doc.page_content, 1024)
        ]
        # Run the chain with the documents
        latex_result = [overall_chain.run(a_text) for a_text in docs]
        # Extract the latex_slide from the result
        latex_slides += latex_result
    latex_slides.append(end_latex_code)
    final_code_ori = "\n".join(latex_slides)
    return final_code_ori
