from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


OUT_PATH = r"C:\Users\ninit\OneDrive\Desktop\Resumes\Ninitha_P_PowerSchool_Resume.pdf"


def p(text, style):
    return Paragraph(text, style)


def main():
    doc = SimpleDocTemplate(
        OUT_PATH,
        pagesize=A4,
        rightMargin=0.5 * inch,
        leftMargin=0.5 * inch,
        topMargin=0.45 * inch,
        bottomMargin=0.45 * inch,
    )

    styles = getSampleStyleSheet()
    title = ParagraphStyle(
        "TitleCustom",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=16,
        leading=18,
        alignment=TA_LEFT,
        spaceAfter=3,
    )
    contact = ParagraphStyle(
        "ContactCustom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        leading=10.5,
        spaceAfter=1,
    )
    heading = ParagraphStyle(
        "HeadingCustom",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=10.2,
        leading=11.5,
        spaceBefore=5,
        spaceAfter=3,
    )
    body = ParagraphStyle(
        "BodyCustom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.8,
        leading=10.2,
        spaceAfter=1,
    )
    bullet = ParagraphStyle(
        "BulletCustom",
        parent=body,
        leftIndent=10,
        firstLineIndent=-7,
        bulletIndent=0,
        spaceAfter=0,
    )

    story = []
    story.append(p("NINITHA P", title))
    story.append(p("+91 8590296706 | ninithanini232@gmail.com | Bengaluru, India", contact))
    story.append(p("linkedin.com/in/ninithap | github.com/Ninitha-67", contact))

    story.append(p("TARGET ROLE", heading))
    story.append(p("Security Operations Center Associate Analyst | Information Security Engineer 1", body))

    story.append(p("PROFESSIONAL SUMMARY", heading))
    story.append(p(
        "Cybersecurity professional pursuing BCA in Cybersecurity, Ethical Hacking & Digital Forensics with hands-on experience in vulnerability assessment, security auditing, log analysis, threat research, and security documentation. Skilled in interpreting security findings, mapping CVEs to risk, and supporting detection and response workflows using Nmap, Wireshark, Nessus, Burp Suite, and Metasploit. Strong foundation in network security, incident support concepts, ISO 27001, and threat analysis.",
        body,
    ))

    story.append(p("CORE SKILLS", heading))
    story.append(p("Security Monitoring and Threat Analysis | Incident Triage and Runbook Support | Log Analysis and Vulnerability Interpretation | Network Security and Attack Surface Mapping | Risk Assessment and Remediation Tracking | Security Documentation and Reporting | Root Cause Analysis Support | Compliance and GRC Support | Scripting and Automation Basics | Web and API Security Testing", body))

    story.append(p("EXPERIENCE", heading))
    story.append(p("<b>Cybersecurity Researcher & Developer</b> | ZecurX Cybersecurity Pvt Ltd | Hybrid | Oct 2025 - Apr 2026", body))
    for t in [
        "Conducted research on attack vectors and threat landscapes to support security advisories and monitoring work.",
        "Authored structured reports and internal advisories aligned with compliance and risk needs.",
        "Mapped CVEs to risk profiles and documented vulnerabilities for internal review and remediation planning.",
    ]:
        story.append(p(f"- {t}", bullet))

    story.append(p("<b>Offensive Cybersecurity Intern</b> | InLighnX Global Pvt Ltd | Remote | Jun 2025 - Aug 2025", body))
    for t in [
        "Performed network reconnaissance, port scanning, and attack surface mapping using Nmap and Metasploit.",
        "Assisted in vulnerability research, penetration testing, and risk identification across systems and applications.",
        "Documented findings, mapped vulnerabilities to CVEs, and prepared remediation-focused reports.",
    ]:
        story.append(p(f"- {t}", bullet))

    story.append(p("<b>Cybersecurity Intern</b> | Corizo | Remote | Dec 2023 - Jan 2024", body))
    story.append(p("- Conducted vulnerability assessments and basic security checks in simulated environments.", bullet))
    story.append(p("- Documented findings and recommended risk mitigation strategies in structured reports.", bullet))

    story.append(p("RELEVANT PROJECTS", heading))
    story.append(p("<b>AIDER - Advanced Intrusion Detection & System Monitoring Tool</b> | Unix-based real-time process monitoring and anomalous activity detection tool aligned to IDS/IPS-style workflows.", body))
    story.append(p("<b>NetRecon - Network Reconnaissance Tool</b> | Automated host detection, port discovery, and service identification using Nmap with structured risk-ranked output.", body))
    story.append(p("<b>ISO/IEC 27001 Risk Register & SoA</b> | Built ISMS risk register and Statement of Applicability in Excel with likelihood-impact risk assessment and Annex A mapping.", body))

    story.append(p("TECHNICAL SKILLS", heading))
    story.append(p("Tools: Nessus, Nmap, Wireshark, Burp Suite, Metasploit, Nikto, Kali Linux, Parrot OS | Programming: Python, Bash, SQL, C/C++ | Networking: TCP/IP, HTTP/HTTPS, DNS, Firewall Concepts, VPN, IDS/IPS | Other: Security Report Writing, Threat Documentation, MS Office", body))

    story.append(p("CERTIFICATIONS", heading))
    story.append(p("Certified Junior SOC (JSOC) | Google Cybersecurity Professional Certificate | Certified ISO/IEC 27001 Information Security Associate | Certified Professional Penetration Tester (CPPT) | Certified Junior API Hacker (CAPIJ) | Certified Junior Vibe Pentester (JVP)", body))

    story.append(p("EDUCATION", heading))
    story.append(p("BCA, Cybersecurity, Ethical Hacking & Digital Forensics | Yenepoya University, Bengaluru | 2023 - 2026 | CGPA: 9.4/10", body))

    doc.build(story)


if __name__ == "__main__":
    main()
