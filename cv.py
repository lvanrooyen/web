import streamlit as st

# Main function to display the CV
def main():
    # Title and profile section
    st.title("Louis van Rooyen CV")
    st.subheader("(B Eng) Electric and Electronic Engineering")
    
    # Contact information
    st.write("**Email**: vanrooyenl@outlook.com")
    st.write("**Phone**: +27 83 399 7850")
    st.write("[**LinkedIn**](#) | [**Portfolio**](#)")  # Replace with actual links
    
    # Profile section
    st.write("## Profile")
    st.write("""
    Enthusiastic and dedicated engineer with a strong foundation in Electric and Electronic Engineering, specializing in robotics 
    and embedded systems. Proficient in embedded software development, PCB design, and IoT technologies, with experience in 
    designing and implementing test systems for production environments. I am eager to contribute to innovative projects, solving 
    complex technical challenges while continuously expanding my knowledge.
    """)

    # Work experience section
    st.write("## Work Experience")
    
    st.write("### Electronics Engineer – Stage Zero (Feb 2024 – Present)")
    st.write("""
    - Designed and implemented unit system tests on the production line to ensure compliance with technical specifications.
    - Spearheaded the redesign of test jigs for production, incorporating a custom PCB integrated with a Raspberry Pi, utilizing 
      a screen and input peripherals to eliminate the need for a PC, improving testing efficiency by 30%.
    - Collaborated with cross-functional teams to troubleshoot and resolve production issues, maintaining high product quality standards.
    """)
    
    st.write("### Engineering Intern – SmartGrid Technologies (Pty) Ltd (Feb 2020 – Feb 2021)")
    st.write("""
    - Supported the R&D department in lab setups, prototype assembly, field trials, and documentation, demonstrating flexibility and ownership.
    - Developed a test jig for a magnetic pulse sensor, reducing testing time by 20% through requirement analysis, design, and fabrication.
    - Automated data consolidation using a Python application, increasing productivity by streamlining data management.
    - Managed the production of 1000 units under tight deadlines, demonstrating leadership and problem-solving in high-pressure environments.
    """)

    # Education section
    st.write("## Education")
    
    st.write("### Bachelors in Electric and Electronic Engineering (2016 – 2023)")
    st.write("**Stellenbosch University**")
    st.write("""
    - Relevant Courses: Digital Control Systems, Signal Processing, Machine Learning, Embedded Systems.
    - Thesis: Designed and implemented a remote event tracking system using LoRa technology, with a custom PCB for a Raspberry Pi gateway and ESP32 Wrover node.
    """)
    
    st.write("### High School Diploma (2011 – 2015)")
    st.write("**Afrikaanse Hoër Seunskool**")
    st.write("Achieved 6 distinctions.")

    # Skills section
    st.write("## Skills")
    st.write("""
    - **Embedded Software Development**: Python, C++
    - **PCB Design**: KiCad
    - **IoT & LoRa Technology**
    - **Raspberry Pi Integration**
    - **Data Analysis & Visualization**: Plotly, Dash, Matlab
    - **Electronic Prototyping**
    - **Team Collaboration & Leadership**
    - **Problem-Solving**
    - **Jira & Confluence**
    - **LateX**
    - **Version Control**: Git, GitHub
    """)

    # Projects section
    st.write("## Projects")
    
    st.write("### Thesis – Remote Event Tracking System")
    st.write("""
    - Designed and implemented a remote event tracking system using LoRa technology with a Raspberry Pi gateway and ESP32 Wrover node.
    - Programmed the system with Python and C++ and developed a custom PCB for both the gateway and the node.
    - Created a user-friendly dashboard using Plotly and Dash for real-time event data visualization, and a coverage analysis tool using Matlab.
    """)

    # Languages section
    st.write("## Languages")
    st.write("""
    - **English**: Fluent
    - **Afrikaans**: Fluent
    """)

    # References section
    st.write("## References")
    st.write("Available upon request.")
    
# Call the main function
if __name__ == '__main__':
    main()
