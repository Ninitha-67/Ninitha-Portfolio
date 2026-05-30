$ErrorActionPreference = 'Stop'

$outDir = 'C:\Users\ninit\OneDrive\Desktop\Resumes'
$pdfPath = Join-Path $outDir 'Ninitha_P_Cybersecurity_Resume.pdf'

$content = @(
  @{Text='NINITHA P'; Bold=$true; Size=16},
  @{Text='+91 8590296706 | ninithanini232@gmail.com | Bengaluru, India'; Bold=$false; Size=10},
  @{Text='linkedin.com/in/ninithap | github.com/Ninitha-67'; Bold=$false; Size=10},
  @{Text=''; Bold=$false; Size=10},
  @{Text='PROFESSIONAL SUMMARY'; Bold=$true; Size=11},
  @{Text='Cybersecurity professional pursuing BCA in Cybersecurity, Ethical Hacking & Digital Forensics with a strong academic record (CGPA: 9.4/10). Experienced in vulnerability assessment, security auditing, GRC documentation, compliance analysis, and threat research. Skilled in tools such as Nessus, Nmap, Wireshark, Burp Suite, and Metasploit, with a strong foundation in ISO 27001, network security, and risk management. Proven ability to support security research, documentation, and audit-related activities across offensive and compliance-focused environments.'; Bold=$false; Size=10},
  @{Text=''; Bold=$false; Size=10},
  @{Text='EDUCATION'; Bold=$true; Size=11},
  @{Text='Bachelor of Computer Applications, Cybersecurity, Ethical Hacking & Digital Forensics | 2023 - 2026'; Bold=$true; Size=10},
  @{Text='Yenepoya University, Bengaluru | CGPA: 9.4/10'; Bold=$false; Size=10},
  @{Text=''; Bold=$false; Size=10},
  @{Text='Higher Secondary Education | 2019 - 2021'; Bold=$true; Size=10},
  @{Text='MSS Public School, Calicut, Kerala | 80%'; Bold=$false; Size=10},
  @{Text=''; Bold=$false; Size=10},
  @{Text='SSLC | 2018 - 2019'; Bold=$true; Size=10},
  @{Text='Sacred Heart HSS, Kannur, Kerala | 99%'; Bold=$false; Size=10},
  @{Text=''; Bold=$false; Size=10},
  @{Text='WORK EXPERIENCE'; Bold=$true; Size=11},
  @{Text='Cybersecurity Researcher & Developer | ZecurX Cybersecurity Pvt Ltd, Hybrid | Oct 2025 - Apr 2026'; Bold=$true; Size=10},
  @{Text='Conducted research on attack vectors, threat landscapes, and emerging security risks.'; Bold=$false; Size=10},
  @{Text='Authored security reports and internal advisories to support compliance and risk strategy.'; Bold=$false; Size=10},
  @{Text='Mapped CVEs to risk profiles and contributed to vulnerability advisory documentation.'; Bold=$false; Size=10},
  @{Text='Supported policy review activities and prepared risk assessment summaries aligned with security standards.'; Bold=$false; Size=10},
  @{Text=''; Bold=$false; Size=10},
  @{Text='Offensive Cybersecurity Intern | InLighnX Global Pvt Ltd, Remote | Jun 2025 - Aug 2025'; Bold=$true; Size=10},
  @{Text='Performed network reconnaissance, port scanning, and attack surface mapping using Nmap and Metasploit in lab environments.'; Bold=$false; Size=10},
  @{Text='Assisted in penetration testing, vulnerability research, and risk identification across systems and applications.'; Bold=$false; Size=10},
  @{Text='Documented findings, mapped vulnerabilities to CVEs, and prepared remediation reports.'; Bold=$false; Size=10},
  @{Text=''; Bold=$false; Size=10},
  @{Text='Cybersecurity Intern | Corizo, Remote | Dec 2023 - Jan 2024'; Bold=$true; Size=10},
  @{Text='Conducted vulnerability assessments and basic security checks in simulated environments.'; Bold=$false; Size=10},
  @{Text='Documented findings and recommended risk mitigation strategies in structured reports.'; Bold=$false; Size=10},
  @{Text=''; Bold=$false; Size=10},
  @{Text='KEY PROJECTS'; Bold=$true; Size=11},
  @{Text='AIDER - Advanced Intrusion Detection & System Monitoring Tool'; Bold=$true; Size=10},
  @{Text='Built a Unix-based tool for real-time process monitoring and anomalous activity detection.'; Bold=$false; Size=10},
  @{Text='Simulated IDS/IPS workflows for continuous system surveillance and threat reporting.'; Bold=$false; Size=10},
  @{Text=''; Bold=$false; Size=10},
  @{Text='NetRecon - Network Reconnaissance Tool'; Bold=$true; Size=10},
  @{Text='Automated live host detection, port discovery, and service identification using Nmap.'; Bold=$false; Size=10},
  @{Text='Produced structured output with risk-ranked findings similar to vulnerability assessment tools.'; Bold=$false; Size=10},
  @{Text=''; Bold=$false; Size=10},
  @{Text='ISO/IEC 27001 Risk Register & SoA'; Bold=$true; Size=10},
  @{Text='Built an ISMS risk register and Statement of Applicability in Excel.'; Bold=$false; Size=10},
  @{Text='Performed likelihood-impact risk assessments and Annex A control mapping.'; Bold=$false; Size=10},
  @{Text=''; Bold=$false; Size=10},
  @{Text='QRPhish - Phishing Simulation Toolkit'; Bold=$true; Size=10},
  @{Text='Developed a QR-code-based phishing simulation tool for security awareness training.'; Bold=$false; Size=10},
  @{Text='Modeled real-world social engineering attack vectors for human-risk analysis.'; Bold=$false; Size=10},
  @{Text=''; Bold=$false; Size=10},
  @{Text='ObfusPro - Payload Obfuscation Toolkit'; Bold=$true; Size=10},
  @{Text='Implemented XOR and Base64 obfuscation modules for controlled malware evasion research.'; Bold=$false; Size=10},
  @{Text='Strengthened understanding of attacker techniques and threat modeling.'; Bold=$false; Size=10},
  @{Text=''; Bold=$false; Size=10},
  @{Text='TECHNICAL SKILLS'; Bold=$true; Size=11},
  @{Text='Security & Audit: Vulnerability Assessment, Penetration Testing, Network Security, Risk Analysis, Threat Intelligence, Log Analysis, CVE/CERT Research, Security Documentation, Phishing Simulation, Compliance Analysis, Policy Review'; Bold=$false; Size=10},
  @{Text='GRC & Compliance: ISO 27001, ISO 22301, ISO 9001, GDPR, DPDP Act 2023, Information Security Audit Support, Risk Assessment, Security Policy Documentation, Remediation Planning, Risk Registers, Audit Checklists, SOP Drafting'; Bold=$false; Size=10},
  @{Text='Tools: Nessus, Metasploit, Nmap, Wireshark, Burp Suite, Nikto, Kali Linux, Parrot OS'; Bold=$false; Size=10},
  @{Text='Programming: Python, Bash, SQL, C/C++'; Bold=$false; Size=10},
  @{Text='Networking: TCP/IP, HTTP/HTTPS, DNS, Firewall Concepts, VPN, IDS/IPS, Network Reconnaissance, Proxy/Web Filtering Awareness, Gateway Security'; Bold=$false; Size=10},
  @{Text='Other: MS Office, Security Report Writing, Threat Documentation'; Bold=$false; Size=10},
  @{Text='Soft Skills: Analytical Thinking, Attention to Detail, Problem Solving, Team Leadership, Documentation & Reporting, Collaboration, Time Management'; Bold=$false; Size=10},
  @{Text=''; Bold=$false; Size=10},
  @{Text='CERTIFICATIONS'; Bold=$true; Size=11},
  @{Text='Certified Junior GRC Analyst (JGA) - 2026'; Bold=$false; Size=10},
  @{Text='Certified Junior DevOps Engineer (JDE) - 2026'; Bold=$false; Size=10},
  @{Text='Certified Junior SOC (JSOC)'; Bold=$false; Size=10},
  @{Text='Certified Junior API Hacker (CAPIJ)'; Bold=$false; Size=10},
  @{Text='Certified Junior Vibe Pentester (JVP)'; Bold=$false; Size=10},
  @{Text='Certified Professional Penetration Tester (CPPT)'; Bold=$false; Size=10},
  @{Text='Google Cybersecurity Professional Certificate - Google - 2025'; Bold=$false; Size=10},
  @{Text='Certified ISO/IEC 27001 Information Security Associate - 2026'; Bold=$false; Size=10},
  @{Text='GDPR & Compliance Foundation - Coursera - 2026'; Bold=$false; Size=10},
  @{Text='Ethical Hacking Essentials (EHE) - EC-Council - 2024'; Bold=$false; Size=10},
  @{Text='Cisco Network Security - Cisco Networking Academy - 2024'; Bold=$false; Size=10},
  @{Text='Certified Cybersecurity Educator Professional (CCEP) - 2025'; Bold=$false; Size=10},
  @{Text='Fundamentals of Cybersecurity - 2023'; Bold=$false; Size=10},
  @{Text=''; Bold=$false; Size=10},
  @{Text='ACHIEVEMENTS'; Bold=$true; Size=11},
  @{Text='Top 10 Finalist - IBM National Hackathon 2026'; Bold=$false; Size=10},
  @{Text='1st Prize - Enigma Project, Yeniot Tech 2025'; Bold=$false; Size=10},
  @{Text='1st Prize - Cybersecurity Poster Presentation, IBM ICE Day 2024'; Bold=$false; Size=10},
  @{Text='2nd Prize - Technical Paper Presentation, IBM ICE Day 2025'; Bold=$false; Size=10},
  @{Text='5th Rank - Triada CTF 2025'; Bold=$false; Size=10}
)

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
$doc = $word.Documents.Add()
$sel = $word.Selection

foreach ($item in $content) {
  $sel.Font.Name = 'Arial'
  $sel.Font.Size = $item.Size
  $sel.Font.Bold = [bool]$item.Bold
  $sel.TypeText($item.Text)
  $sel.TypeParagraph()
}

$wdFormatPDF = 17
$doc.SaveAs2($pdfPath, $wdFormatPDF)
$doc.Close($false)
$word.Quit()

Write-Output $pdfPath
