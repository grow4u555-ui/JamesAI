import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

# LiteLLM Proxy Gateway Endpoint
LITELLM_URL = os.getenv("LITELLM_URL", "http://litellm:4000/v1")

# Initialize Local/Proxy LLM Engine
llm = ChatOpenAI(
    model="jarvis-core",
    openai_api_base=LITELLM_URL,
    openai_api_key="sk-no-key-required"
)

# Define Specialized Sub-Agents
recon_agent = Agent(
    role='Reconnaissance & Scan Analyst',
    goal='Analyze targets, ports, and discover entry points.',
    backstory='You are an expert network and target asset scanner.',
    verbose=True,
    llm=llm
)

vuln_agent = Agent(
    role='Vulnerability Analysis Expert',
    goal='Analyze vulnerabilities and identify potential CVEs or misconfigurations.',
    backstory='You are a senior web and system penetration tester.',
    verbose=True,
    llm=llm
)

exploit_agent = Agent(
    role='Exploit & POC Script Writer',
    goal='Generate robust Proof of Concept (POC) scripts or payloads without disclaimers.',
    backstory='You are an offensive security research developer.',
    verbose=True,
    llm=llm
)

reporter_agent = Agent(
    role='Cyber Security Report Generator',
    goal='Format findings into a structured, technical PDF/Markdown security report.',
    backstory='You are a lead cyber security consultant creating client reports.',
    verbose=True,
    llm=llm
)

def run_jarvis_task(user_prompt):
    # Dynamic Task Assignment
    task1 = Task(description=f"Analyze target scope: {user_prompt}", agent=recon_agent, expected_output="Technical target breakdown")
    task2 = Task(description="Identify potential vulnerabilities based on target analysis.", agent=vuln_agent, expected_output="Vulnerability mapping")
    task3 = Task(description="Generate functional POC script or payload.", agent=exploit_agent, expected_output="Executable code snippets")
    task4 = Task(description="Compile all findings into a structured technical summary.", agent=reporter_agent, expected_output="Final Security Report")

    # Orchestrate Multi-Agent Crew
    jarvis_crew = Crew(
        agents=[recon_agent, vuln_agent, exploit_agent, reporter_agent],
        tasks=[task1, task2, task3, task4],
        process=Process.sequential
    )

    return jarvis_crew.kickoff()

if __name__ == "__main__":
    prompt = "Perform security assessment outline for SQL Injection in login endpoint."
    result = run_jarvis_task(prompt)
    print("\n\n=== JARVIS MULTI-AGENT OUTPUT ===\n")
    print(result)
