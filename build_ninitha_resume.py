from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib import colors


OUT_PATH = r"C:\Users\ninit\OneDrive\Desktop\Resumes\Ninitha_P_Cybersecurity_Resume.pdf"


def p(text, style):
    return Paragraph(text, style)


def main():
    doc = SimpleDocTemplate(
        OUT_PATH,
        pagesize=A4,
        rightMargin=0.55 * inch,
        leftMargin=0.55 * inch,
        topMargin=0.5 * inch,
        bottomMargin=0.5 * inch,
    )

    styles = getSampleStyleSheet()
    title = ParagraphStyle(
        "TitleCustom",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=16,
        leading=18,
        alignment=TA_LEFT,
        textColor=colors.black,
        spaceAfter=4,
    )
    contact = ParagraphStyle(
        "ContactCustom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=11,
        spaceAfter=2,
    )
    heading = ParagraphStyle(
        "HeadingCustom",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=12,
        spaceBefore=6,
        spaceAfter=4,
        textColor=colors.black,
    )
    body = ParagraphStyle(
        "BodyCustom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.3,
        leading=11.3,
        spaceAfter=2,
    )
    bullet = ParagraphStyle(
        "BulletCustom",
        parent=body,
        leftIndent=12,
        firstLineIndent=-8,
        bulletIndent=0,
        spaceAfter=1,
    )

    story = []
    story.append(p("NINITHA P", title))
    story.append(p("+91 8590296706 | ninithanini232@gmail.com | Bengaluru, India", contact))
    story.append(p("linkedin.com/in/ninithap | github.com/Ninitha-67", contact))

    story.append(p("PROFESSIONAL SUMMARY", heading))
    story.append(p(
        "Cybersecurity professional pursuing BCA in Cybersecurity, Ethical Hacking & Digital Forensics with a strong academic record (CGPA: 9.4/10). Experienced in vulnerability assessment, security auditing, GRC documentation, compliance analysis, and threat research. Skilled in tools such as Nessus, Nmap, Wireshark, Burp Suite, and Metasploit, with a strong foundation in ISO 27001, network security, and risk management. Proven ability to support security research, documentation, and audit-related activities across offensive and compliance-focused environments.",
        body,
    ))

    story.append(p("EDUCATION", heading))
    story.append(p("<b>Bachelor of Computer Applications, Cybersecurity, Ethical Hacking & Digital Forensics</b> | 2023 - 2026", body))
    story.append(p("Yenepoya University, Bengaluru | CGPA: 9.4/10", body))
    story.append(p("<b>Higher Secondary Education</b> | 2019 - 2021", body))
    story.append(p("MSS Public School, Calicut, Kerala | 80%", body))
    story.append(p("<b>SSLC</b> | 2018 - 2019", body))
    story.append(p("Sacred Heart HSS, Kannur, Kerala | 99%", body))

    story.append(p("WORK EXPERIENCE", heading))
    story.append(p("<b>Cybersecurity Researcher & Developer</b> | ZecurX Cybersecurity Pvt Ltd, Hybrid | Oct 2025 - Apr 2026", body))
    for t in [
        "Conducted research on attack vectors, threat landscapes, and emerging security risks.",
        "Authored security reports and internal advisories to support compliance and risk strategy.",
        "Mapped CVEs to risk profiles and contributed to vulnerability advisory documentation.",
        "Supported policy review activities and prepared risk assessment summaries aligned with security standards.",
    ]:
        story.append(p(f"- {t}", bullet))

    story.append(p("<b>Offensive Cybersecurity Intern</b> | InLighnX Global Pvt Ltd, Remote | Jun 2025 - Aug 2025", body))
    for t in [
        "Performed network reconnaissance, port scanning, and attack surface mapping using Nmap and Metasploit in lab environments.",
        "Assisted in penetration testing, vulnerability research, and risk identification across systems and applications.",
        "Documented findings, mapped vulnerabilities to CVEs, and prepared remediation reports.",
    ]:
        story.append(p(f"- {t}", bullet))

    story.append(p("<b>Cybersecurity Intern</b> | Corizo, Remote | Dec 2023 - Jan 2024", body))
    for t in [
        "Conducted vulnerability assessments and basic security checks in simulated environments.",
        "Documented findings and recommended risk mitigation strategies in structured reports.",
    ]:
        story.append(p(f"- {t}", bullet))

    story.append(p("KEY PROJECTS", heading))
    projects = [
        ("AIDER - Advanced Intrusion Detection & System Monitoring Tool", [
            "Built a Unix-based tool for real-time process monitoring and anomalous activity detection.",
            "Simulated IDS/IPS workflows for continuous system surveillance and threat reporting.",
        ]),
        ("NetRecon - Network Reconnaissance Tool", [
            "Automated live host detection, port discovery, and service identification using Nmap.",
            "Produced structured output with risk-ranked findings similar to vulnerability assessment tools.",
        ]),
        ("ISO/IEC 27001 Risk Register & SoA", [
            "Built an ISMS risk register and Statement of Applicability in Excel.",
            "Performed likelihood-impact risk assessments and Annex A control mapping.",
        ]),
        ("QRPhish - Phishing Simulation Toolkit", [
            "Developed a QR-code-based phishing simulation tool for security awareness training.",
            "Modeled real-world social engineering attack vectors for human-risk analysis.",
        ]),
        ("ObfusPro - Payload Obfuscation Toolkit", [
            "Implemented XOR and Base64 obfuscation modules for controlled malware evasion research.",
            "Strengthened understanding of attacker techniques and threat modeling.",
        ]),
    ]
    for name, items in projects:
        story.append(p(f"<b>{name}</b>", body))
        for t in items:
            story.append(p(f"- {t}", bullet))

    story.append(p("TECHNICAL SKILLS", heading))
    skill_lines = [
        "<b>Security & Audit:</b> Vulnerability Assessment, Penetration Testing, Network Security, Risk Analysis, Threat Intelligence, Log Analysis, CVE/CERT Research, Security Documentation, Phishing Simulation, Compliance Analysis, Policy Review",
        "<b>GRC & Compliance:</b> ISO 27001, ISO 22301, ISO 9001, GDPR, DPDP Act 2023, Information Security Audit Support, Risk Assessment, Security Policy Documentation, Remediation Planning, Risk Registers, Audit Checklists, SOP Drafting",
        "<b>Tools:</b> Nessus, Metasploit, Nmap, Wireshark, Burp Suite, Nikto, Kali Linux, Parrot OS",
        "<b>Programming:</b> Python, Bash, SQL, C/C++",
        "<b>Networking:</b> TCP/IP, HTTP/HTTPS, DNS, Firewall Concepts, VPN, IDS/IPS, Network Reconnaissance, Proxy/Web Filtering Awareness, Gateway Security",
        "<b>Other:</b> MS Office, Security Report Writing, Threat Documentation",
        "<b>Soft Skills:</b> Analytical Thinking, Attention to Detail, Problem Solving, Team Leadership, Documentation & Reporting, Collaboration, Time Management",
    ]
    for line in skill_lines:
        story.append(p(line, body))

    story.append(p("CERTIFICATIONS", heading))
    certs = [
        "Certified Junior GRC Analyst (JGA) - 2026",
        "Certified Junior DevOps Engineer (JDE) - 2026",
        "Certified Junior SOC (JSOC)",
        "Certified Junior API Hacker (CAPIJ)",
        "Certified Junior Vibe Pentester (JVP)",
        "Certified Professional Penetration Tester (CPPT)",
        "Google Cybersecurity Professional Certificate - Google - 2025",
        "Certified ISO/IEC 27001 Information Security Associate - 2026",
        "GDPR & Compliance Foundation - Coursera - 2026",
        "Ethical Hacking Essentials (EHE) - EC-Council - 2024",
        "Cisco Network Security - Cisco Networking Academy - 2024",
        "Certified Cybersecurity Educator Professional (CCEP) - 2025",
        "Fundamentals of Cybersecurity - 2023",
    ]
    for c in certs:
        story.append(p(f"- {c}", bullet))

    story.append(p("ACHIEVEMENTS", heading))
    for a in [
        "Top 10 Finalist - IBM National Hackathon 2026",
        "1st Prize - Enigma Project, Yeniot Tech 2025",
        "1st Prize - Cybersecurity Poster Presentation, IBM ICE Day 2024",
        "2nd Prize - Technical Paper Presentation, IBM ICE Day 2025",
        "5th Rank - Triada CTF 2025",
    ]:
        story.append(p(f"- {a}", bullet))

    doc.build(story)


if __name__ == "__main__":
    main()
