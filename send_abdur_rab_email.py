import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

FROM_EMAIL = "9276242@gmail.com"
APP_PASSWORD = "qiafameefgtypsno"
TO_EMAIL = "abdur.rub.khan@gmail.com"
CC_EMAIL = ""
BCC_EMAIL = ""
SUBJECT = "Technical Guidance: SAP CLM Architecture & CIPS Level 4 Examination Roadmap"

def generate_email_html():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Technical Briefing: SAP CLM & CIPS Level 4</title>
</head>
<body style="margin: 0; padding: 0; background-color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #1e293b; line-height: 1.6;">
    <div style="max-width: 680px; margin: 30px auto; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
        
        <!-- Header Banner -->
        <div style="background-color: #0f172a; padding: 32px 36px; border-bottom: 3px solid #ca8a04;">
            <div style="color: #ca8a04; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 6px;">
                Executive Briefing & Technical Guidance
            </div>
            <h1 style="color: #ffffff; font-size: 22px; font-weight: 700; margin: 0; line-height: 1.3;">
                SAP Contract Lifecycle Management (CLM) & CIPS Level 4 Roadmap
            </h1>
        </div>

        <!-- Main Content Canvas -->
        <div style="padding: 36px;">
            
            <p style="font-size: 15px; margin-top: 0; color: #334155;">
                Dear Mr. Abdur Rab Khan,
            </p>
            <p style="font-size: 14px; color: #475569; margin-bottom: 24px;">
                Thank you for reaching out. Below is a comprehensive, layman-friendly yet technically thorough overview addressing both of your queries regarding:
                <br><strong>1. SAP CLM (Contract Lifecycle Management) Module and our enterprise capability</strong>
                <br><strong>2. CIPS Level 4 Diploma admission, exam structure, and November examination schedule</strong>
            </p>

            <!-- SECTION 1: SAP CLM -->
            <div style="margin-bottom: 36px;">
                <div style="display: flex; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">
                    <span style="background-color: #ca8a04; color: #ffffff; font-size: 12px; font-weight: 700; padding: 3px 8px; border-radius: 4px; margin-right: 10px;">PART 1</span>
                    <h2 style="color: #0f172a; font-size: 18px; margin: 0; font-weight: 700;">SAP Contract Lifecycle Management (CLM) Module</h2>
                </div>

                <h3 style="font-size: 15px; color: #1e293b; margin: 16px 0 8px 0;">1. What is SAP CLM in Simple Terms?</h3>
                <p style="font-size: 14px; color: #475569; margin: 0 0 12px 0;">
                    In layman's language, <strong>CLM (Contract Lifecycle Management)</strong> is an automated digital system for managing commercial, legal, and vendor agreements from initial negotiation to final expiry and renewal. Instead of relying on manual paper files, scanned PDFs, or unmonitored spreadsheets, CLM provides full governance over every stage of a contract.
                </p>

                <!-- Feature Matrix -->
                <table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 13px;">
                    <thead>
                        <tr style="background-color: #f1f5f9; text-align: left;">
                            <th style="padding: 10px 12px; border: 1px solid #e2e8f0; color: #0f172a; width: 30%;">Core Stage</th>
                            <th style="padding: 10px 12px; border: 1px solid #e2e8f0; color: #0f172a;">How It Protects & Automates Business Operations</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style="padding: 10px 12px; border: 1px solid #e2e8f0; font-weight: 600; color: #1e293b;">1. Standardized Drafting</td>
                            <td style="padding: 10px 12px; border: 1px solid #e2e8f0; color: #475569;">Legal teams pre-approve clause libraries, preventing unvetted terms from entering supplier agreements.</td>
                        </tr>
                        <tr style="background-color: #fafafa;">
                            <td style="padding: 10px 12px; border: 1px solid #e2e8f0; font-weight: 600; color: #1e293b;">2. Automated Approvals</td>
                            <td style="padding: 10px 12px; border: 1px solid #e2e8f0; color: #475569;">Routing of high-value contracts to Finance, Supply Chain Directors, and Legal via electronic signatures.</td>
                        </tr>
                        <tr>
                            <td style="padding: 10px 12px; border: 1px solid #e2e8f0; font-weight: 600; color: #1e293b;">3. SAP Operational Link</td>
                            <td style="padding: 10px 12px; border: 1px solid #e2e8f0; color: #475569;">Automatically links contracts directly to Purchase Orders (PO) in SAP MM / Sourcing so discounted rates and contracted quantities are enforced automatically.</td>
                        </tr>
                        <tr style="background-color: #fafafa;">
                            <td style="padding: 10px 12px; border: 1px solid #e2e8f0; font-weight: 600; color: #1e293b;">4. Expiration Alerts</td>
                            <td style="padding: 10px 12px; border: 1px solid #e2e8f0; color: #475569;">Automated notification 30/60/90 days prior to contract expiration, eliminating penalty risks and unmonitored lapses.</td>
                        </tr>
                    </tbody>
                </table>

                <!-- Flowchart Container -->
                <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 18px; margin: 18px 0;">
                    <div style="font-size: 11px; font-weight: 700; color: #64748b; text-transform: uppercase; margin-bottom: 12px; letter-spacing: 0.5px;">CLM to SAP Operational Flowchart</div>
                    
                    <div style="text-align: center; font-size: 13px; font-weight: 600; color: #1e293b;">
                        <div style="background: #ffffff; border: 1px solid #cbd5e1; padding: 8px 12px; border-radius: 4px; display: inline-block; width: 85%;">
                            1. Contract Authoring & Clause Negotiation (Buyer & Supplier)
                        </div>
                        <div style="color: #ca8a04; font-size: 14px; margin: 4px 0;">&#8595;</div>
                        <div style="background: #ffffff; border: 1px solid #cbd5e1; padding: 8px 12px; border-radius: 4px; display: inline-block; width: 85%;">
                            2. Digital Workflow Approvals & E-Signature
                        </div>
                        <div style="color: #ca8a04; font-size: 14px; margin: 4px 0;">&#8595;</div>
                        <div style="background: #ffffff; border: 1px solid #cbd5e1; padding: 8px 12px; border-radius: 4px; display: inline-block; width: 85%;">
                            3. Auto-Creation of SAP Outline Agreement / Contract in S/4HANA (EKKO / EKPO)
                        </div>
                        <div style="color: #ca8a04; font-size: 14px; margin: 4px 0;">&#8595;</div>
                        <div style="background: #ffffff; border: 1px solid #ca8a04; background-color: #fefce8; padding: 8px 12px; border-radius: 4px; display: inline-block; width: 85%; color: #854d0e;">
                            4. Purchase Orders (PO) Pull Pricing & Compliance Directly from SAP Contract
                        </div>
                    </div>
                </div>

                <h3 style="font-size: 15px; color: #1e293b; margin: 16px 0 8px 0;">2. Do We Have This Solution? (کیا ہمارے پاس ہے؟)</h3>
                <p style="font-size: 14px; color: #475569; margin: 0 0 12px 0;">
                    <strong>Yes, absolutely.</strong> We support Contract Lifecycle Management in two enterprise models:
                </p>
                <ul style="font-size: 13px; color: #475569; margin: 0 0 14px 20px; padding: 0;">
                    <li style="margin-bottom: 6px;"><strong>SAP S/4HANA Direct Integration:</strong> We integrate natively with SAP S/4HANA Sourcing & Procurement Outline Agreements (Value Contracts & Quantity Contracts) via standard OData APIs and BAPIs.</li>
                    <li style="margin-bottom: 6px;"><strong>Decoupled Web & Portal CLM:</strong> For organizations seeking a cost-effective, user-friendly contract repository without heavy per-user SAP licensing costs, we provide an intuitive web portal that synchronizes contracts seamlessly with SAP.</li>
                </ul>
            </div>

            <!-- SECTION 2: CIPS LEVEL 4 -->
            <div style="margin-bottom: 36px;">
                <div style="display: flex; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">
                    <span style="background-color: #ca8a04; color: #ffffff; font-size: 12px; font-weight: 700; padding: 3px 8px; border-radius: 4px; margin-right: 10px;">PART 2</span>
                    <h2 style="color: #0f172a; font-size: 18px; margin: 0; font-weight: 700;">CIPS Level 4 (Diploma in Procurement and Supply)</h2>
                </div>

                <h3 style="font-size: 15px; color: #1e293b; margin: 16px 0 8px 0;">1. What is CIPS?</h3>
                <p style="font-size: 14px; color: #475569; margin: 0 0 12px 0;">
                    <strong>CIPS (Chartered Institute of Procurement & Supply)</strong>, headquartered in the United Kingdom, is the world's premier professional body for procurement and supply chain management. 
                    <strong>Level 4 (Diploma)</strong> is the standard entry point for university graduates and procurement professionals, equivalent to first-year undergraduate university level and the first milestone towards full Chartered status (<strong>MCIPS</strong>).
                </p>

                <h3 style="font-size: 15px; color: #1e293b; margin: 16px 0 8px 0;">2. Level 4 Exam Structure (Total 8 Modules)</h3>
                <p style="font-size: 14px; color: #475569; margin: 0 0 12px 0;">
                    To complete Level 4, a candidate must pass a total of <strong>60 credits</strong> (8 modules):
                </p>

                <table style="width: 100%; border-collapse: collapse; margin: 14px 0; font-size: 13px;">
                    <thead>
                        <tr style="background-color: #f1f5f9; text-align: left;">
                            <th style="padding: 8px 10px; border: 1px solid #e2e8f0; color: #0f172a;">Module Code</th>
                            <th style="padding: 8px 10px; border: 1px solid #e2e8f0; color: #0f172a;">Module Title</th>
                            <th style="padding: 8px 10px; border: 1px solid #e2e8f0; color: #0f172a; width: 22%;">Assessment Type</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style="padding: 8px 10px; border: 1px solid #e2e8f0; font-weight: 600;">L4M1 (Core)</td>
                            <td style="padding: 8px 10px; border: 1px solid #e2e8f0;">Scope and Influence of Procurement and Supply</td>
                            <td style="padding: 8px 10px; border: 1px solid #e2e8f0;">Constructed Response (Essay)</td>
                        </tr>
                        <tr style="background-color: #fafafa;">
                            <td style="padding: 8px 10px; border: 1px solid #e2e8f0; font-weight: 600;">L4M2 (Core)</td>
                            <td style="padding: 8px 10px; border: 1px solid #e2e8f0;">Defining Business Needs</td>
                            <td style="padding: 8px 10px; border: 1px solid #e2e8f0;">Objective Response (MCQs)</td>
                        </tr>
                        <tr>
                            <td style="padding: 8px 10px; border: 1px solid #e2e8f0; font-weight: 600;">L4M3 (Core)</td>
                            <td style="padding: 8px 10px; border: 1px solid #e2e8f0;">Commercial Contracting</td>
                            <td style="padding: 8px 10px; border: 1px solid #e2e8f0;">Objective Response (MCQs)</td>
                        </tr>
                        <tr style="background-color: #fafafa;">
                            <td style="padding: 8px 10px; border: 1px solid #e2e8f0; font-weight: 600;">L4M4 (Core)</td>
                            <td style="padding: 8px 10px; border: 1px solid #e2e8f0;">Ethical and Responsible Sourcing</td>
                            <td style="padding: 8px 10px; border: 1px solid #e2e8f0;">Objective Response (MCQs)</td>
                        </tr>
                        <tr>
                            <td style="padding: 8px 10px; border: 1px solid #e2e8f0; font-weight: 600;">L4M5 (Core)</td>
                            <td style="padding: 8px 10px; border: 1px solid #e2e8f0;">Commercial Negotiation</td>
                            <td style="padding: 8px 10px; border: 1px solid #e2e8f0;">Objective Response (MCQs)</td>
                        </tr>
                        <tr style="background-color: #fafafa;">
                            <td style="padding: 8px 10px; border: 1px solid #e2e8f0; font-weight: 600;">L4M6 (Core)</td>
                            <td style="padding: 8px 10px; border: 1px solid #e2e8f0;">Supplier Relationships</td>
                            <td style="padding: 8px 10px; border: 1px solid #e2e8f0;">Objective Response (MCQs)</td>
                        </tr>
                        <tr>
                            <td style="padding: 8px 10px; border: 1px solid #e2e8f0; font-weight: 600;">L4M7 (Core)</td>
                            <td style="padding: 8px 10px; border: 1px solid #e2e8f0;">Whole Life Asset Management</td>
                            <td style="padding: 8px 10px; border: 1px solid #e2e8f0;">Objective Response (MCQs)</td>
                        </tr>
                        <tr style="background-color: #fafafa;">
                            <td style="padding: 8px 10px; border: 1px solid #e2e8f0; font-weight: 600;">L4M8 (Core)</td>
                            <td style="padding: 8px 10px; border: 1px solid #e2e8f0;">Procurement and Supply in Practice</td>
                            <td style="padding: 8px 10px; border: 1px solid #e2e8f0;">Constructed Response (Case Study)</td>
                        </tr>
                    </tbody>
                </table>

                <h3 style="font-size: 15px; color: #1e293b; margin: 16px 0 8px 0;">3. Step-by-Step Admission & Registration Process</h3>
                <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 16px; margin: 14px 0;">
                    <ol style="margin: 0; padding-left: 20px; font-size: 13px; color: #334155; line-height: 1.8;">
                        <li><strong>Step 1 - Register with CIPS:</strong> Visit <a href="https://www.cips.org" style="color: #ca8a04; font-weight: 600; text-decoration: none;">www.cips.org</a> and create a Student Membership account (annual subscription fee applies).</li>
                        <li><strong>Step 2 - Choose Study Route:</strong> You can either opt for <em>Self-Study</em> (order official CIPS course books) or register through an approved study centre in Pakistan (such as IBA Karachi, Wings, or recognized tuition providers).</li>
                        <li><strong>Step 3 - Book Examination:</strong> Log in to your MyCIPS portal, select Level 4 module(s) you wish to attempt in the November series, and make the exam fee payment online.</li>
                        <li><strong>Step 4 - Test Center Location:</strong> Exams in Pakistan are computer-based assessments conducted at accredited testing facilities (such as the <strong>British Council</strong> centres in Lahore, Karachi, and Islamabad).</li>
                    </ol>
                </div>

                <!-- CRITICAL TIMELINE ALERT -->
                <div style="background-color: #fffbeb; border-left: 4px solid #ca8a04; padding: 14px 18px; border-radius: 0 6px 6px 0; margin-top: 18px;">
                    <div style="font-weight: 700; color: #92400e; font-size: 13px; margin-bottom: 4px;">CRITICAL TIMELINE FOR NOVEMBER EXAMS:</div>
                    <div style="font-size: 13px; color: #78350f; line-height: 1.5;">
                        CIPS exam registration deadlines for the November exam window close <strong>several weeks in advance (typically mid-to-late September)</strong>. Because enrollment takes 2–3 days for verification, please register your student membership on <em>cips.org</em> immediately to avoid missing the November exam cut-off.
                    </div>
                </div>
            </div>

            <!-- Conclusion & Support -->
            <p style="font-size: 14px; color: #475569; margin-top: 24px;">
                Please feel free to reply directly to this email if you need syllabus past papers, study guidance, or a dedicated live demo of our SAP contract integration architecture.
            </p>

            <p style="font-size: 14px; color: #1e293b; margin-bottom: 24px;">
                Best regards,<br>
                <strong>Anas Mahmood</strong><br>
                <span style="font-size: 13px; color: #64748b;">Founder & Owner</span><br>
                <span style="font-size: 13px; color: #64748b;">Hamayun IT Solutions (HITS)</span>
            </p>

            <!-- Signature Card -->
            <div style="border-top: 1px solid #e2e8f0; margin-top: 24px; padding-top: 18px; font-size: 12px; line-height: 1.6; color: #475569;">
                <span style="font-size: 13px; font-weight: 700; color: #ca8a04; display: block; margin-bottom: 4px;">Hamayun IT Solutions (HITS)</span>
                <b>Email:</b> 9276242@gmail.com | ceo@hits-ksa.com<br>
                <b>Website:</b> <a href="https://hits-ksa.com" style="color: #ca8a04; text-decoration: none;">hits-ksa.com</a><br>
                <b>WhatsApp:</b> +92 300 9276242 | +966 54 042 3544<br>
                <b>Address:</b> RIYADH OFFICE (KSA), Street # 28, Al Olaya District, Riyadh City, Kingdom of Saudi Arabia<br>
            </div>
        </div>

        <!-- Footer -->
        <div style="background-color: #f8fafc; padding: 18px; text-align: center; border-top: 1px solid #e2e8f0; font-size: 11px; color: #64748b;">
            &copy; 2026 Hamayun IT Solutions (HITS). All rights reserved.
        </div>
    </div>
</body>
</html>"""

def send_email():
    html_content = generate_email_html()
    msg = MIMEMultipart("alternative")
    msg["From"] = f"Anas Mahmood <{FROM_EMAIL}>"
    msg["To"] = TO_EMAIL
    msg["Subject"] = SUBJECT
    
    if CC_EMAIL:
        msg["Cc"] = CC_EMAIL
        
    part = MIMEText(html_content, "html")
    msg.attach(part)
    
    recipients = [TO_EMAIL]
    if CC_EMAIL:
        recipients.extend([e.strip() for e in CC_EMAIL.split(",") if e.strip()])
    if BCC_EMAIL:
        recipients.extend([e.strip() for e in BCC_EMAIL.split(",") if e.strip()])

    print(f"Connecting to Gmail SMTP server for {FROM_EMAIL}...")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(FROM_EMAIL, APP_PASSWORD)
        server.sendmail(FROM_EMAIL, recipients, msg.as_string())
    print("Email sent successfully and recorded in Gmail Sent box!")

if __name__ == "__main__":
    # Will only be executed upon explicit user confirmation
    send_email()
