import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o-mini")

# Define the prompt template for meeting summary
meeting_template = """

You are an AI assistant tasked with summarizing a meeting {transcribed_text}. 
Based on the provided {transcribed_text}, extract and detail all points discussed during the meeting. 
Follow the structure below:

You are an AI assistant tasked with summarizing a meeting based on the provided transcribed text. Extract and detail all points discussed during the meeting, following the structure below:

# Meeting Summary

## 1. Meeting Overview
- **Date:** [current system date]
- **Time:** [start_time - end_time]
- **Participants:** [participants, if known]

## 2. Agenda
- [List agenda items discussed during the meeting]

## 3. Key Discussion Points
- **Topic:** [topic_name]
  - [List detailed points discussed under this topic]
  - [point 1]
  - [point 2]
  - [additional points]
- [Repeat for each topic discussed]

## 4. Decisions Made (Optional)
- **Decision:** [decision_description]
  - **Date of Implementation:** [implementation_date, if mentioned]

## 5. Action Items (Optional)
- **Action Item:**
  - **Assigned to:** [assigned_person_or_team]
  - **Due Date:** [due_date, if mentioned]
  - **Description:** [action_description]
- [Repeat for each action item assigned]

## 6. Important Dates (Optional)
- **Milestone:** [milestone_description]
  - **Date:** [milestone_date]
- [Repeat for each important date mentioned]

## 7. Next Steps
- **Follow-Up Meeting:** [follow_up_meeting_date_time, if discussed]
- **Next Agenda:** [next_meeting_agenda, if known]

## 8. Notes
- [additional_notes]

Ensure all major and minor points discussed are captured accurately. Categorize specific dates appropriately (e.g., deadlines, milestones) and define action items with clear responsibilities and deadlines.


"""

# Load the transcribed text from a file
with open('transcription_2024-08-17_00-27-20.txt', 'r') as file:
    transcribed_text = file.read()

# Create the prompt using the template
meeting_prompt_template = ChatPromptTemplate.from_template(meeting_template)
prompt = meeting_prompt_template.invoke({"transcribed_text": transcribed_text})

# Generate the Medium article using the model
result = model.invoke(prompt)

# Save the result in a Markdown file
output_file_path = os.path.join(os.getcwd(), 'meeting.md')
with open(output_file_path, 'w') as md_file:
    md_file.write(result.content)

print(f"Meeting article saved to {output_file_path}")
