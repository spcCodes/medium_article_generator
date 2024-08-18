import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o-mini")

# Define the prompt template for Medium article
medium_article_template = """
Task : You are provided with a {transcribed_text} of a talk or conversation. 
Your goal is to transform this {transcribed_text} into a well-structured, engaging, and comprehensive Medium article. 
The article should include a title, introduction, headings, subheadings, and other necessary elements to make it informative and reader-friendly.

### **Guidelines:**

1. **Title**: Create a compelling and descriptive title that encapsulates the essence of the article.
   
2. **Introduction**: Write an engaging introduction that introduces the main topic, provides context, and hooks the reader's interest.

3. **Headings and Subheadings**:
   - Organize the content logically using appropriate headings and subheadings.
   - Ensure that each section flows naturally into the next, maintaining coherence and readability.

4. **Inclusion of All Points**:
   - Carefully include all the points mentioned in the transcribed text. Do not omit any information, even if it seems minor.
   - Ensure the information is presented clearly and accurately.

5. **Code Placeholders**:
   - Wherever the speaker mentions code or a technical implementation, include a placeholder labeled "Insert Code Here".
   - Provide a brief description of what the code is intended to do, based on the context provided in the transcription.

6. **Figure Placeholders**:
   - Whenever the speaker refers to a figure, chart, or diagram, include a placeholder labeled "Insert Figure Here".
   - Describe the figure briefly and explain its relevance to the content.

7. **Expertise and Polish**:
   - Use your expertise to refine the article, ensuring it has a smooth flow, professional tone, and clarity.
   - Enhance the content with additional insights or clarifications where necessary, making the article more informative and valuable to readers.

8. **Conclusion**:
   - Summarize the key takeaways of the article in a conclusion.
   - Reinforce the main points and suggest any actionable insights or next steps for the reader.

9. **Readability**:
   - Ensure the language is accessible, avoiding jargon unless it is explained.
   - Break up long paragraphs and sentences to improve readability.

10. **Final Touches**:
    - Proofread the article for grammar, spelling, and punctuation errors.
    - Ensure the article adheres to Medium's style and formatting guidelines.

---

**Input**: {transcribed_text}

**Output**: A high-quality Medium article following the above guidelines.

---

You can adapt or expand this template further based on specific needs or preferences.
"""

# Load the transcribed text from a file
with open('transcription_2024-08-17_16-47-17.txt', 'r') as file:
    transcribed_text = file.read()

# Create the prompt using the template
medium_prompt_template = ChatPromptTemplate.from_template(medium_article_template)
prompt = medium_prompt_template.invoke({"transcribed_text": transcribed_text})

# Generate the Medium article using the model
result = model.invoke(prompt)

# Save the result in a Markdown file
output_file_path = os.path.join(os.getcwd(), 'medium_article_1.md')
with open(output_file_path, 'w') as md_file:
    md_file.write(result.content)

print(f"Medium article saved to {output_file_path}")
