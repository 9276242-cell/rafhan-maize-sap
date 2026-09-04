import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

FROM_EMAIL = "9276242@gmail.com"
APP_PASSWORD = "qiafameefgtypsno"
TO_RECIPIENTS = ["abdur.rub.khan@gmail.com", "anas1000@gmail.com"]
CC_EMAIL = ""
BCC_EMAIL = ""
SUBJECT = "Executive Architecture: Decoupled SAP CLM Middleware & 100% Legitimate Licensing Blueprint"

def generate_email_html():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SAP CLM Middleware Architecture & Licensing Compliance</title>
</head>
<body style="margin: 0; padding: 0; background-color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #1e293b; line-height: 1.6;">
    <div style="max-width: 720px; margin: 30px auto; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
        
        <!-- Header Banner -->
        <div style="background-color: #0f172a; padding: 32px 36px; border-bottom: 3px solid #ca8a04;">
            <div style="color: #ca8a04; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 6px;">
                Strategic Enterprise Architecture & Compliance
            </div>
            <h1 style="color: #ffffff; font-size: 22px; font-weight: 700; margin: 0; line-height: 1.3;">
                Decoupled SAP Contract Lifecycle Management (CLM)
            </h1>
            <div style="color: #94a3b8; font-size: 13px; margin-top: 6px;">
                Middleware Implementation Strategy, Cost Optimization & Audit-Proof SAP Licensing
            </div>
        </div>

        <!-- Main Content Canvas -->
        <div style="padding: 36px;">
            
            <p style="font-size: 15px; margin-top: 0; color: #334155;">
                Dear Mr. Abdur Rab Khan & Stakeholders,
            </p>
            <p style="font-size: 14px; color: #475569; margin-bottom: 24px;">
                Following our recent briefing on SAP CLM and CIPS procurement standards, this executive blueprint provides the in-depth technical architecture and legal licensing rationale for deploying a <strong>Decoupled Contract Lifecycle Management (CLM) System</strong> integrated with SAP S/4HANA / SAP Business One.
            </p>

            <!-- EXECUTIVE SUMMARY HIGHLIGHT BOX -->
            <div style="background-color: #f8fafc; border-left: 4px solid #ca8a04; padding: 16px 20px; border-radius: 0 6px 6px 0; margin-bottom: 28px;">
                <div style="font-weight: 700; color: #0f172a; font-size: 14px; margin-bottom: 4px;">CORE QUESTION & VERDICT:</div>
                <div style="font-size: 13px; color: #334155; line-height: 1.6;">
                    <strong>Can you deploy your own complete CLM in middleware and keep everything 100% legitimate with SAP?</strong><br>
                    <span style="color: #166534; font-weight: 700;">YES, 100%.</span> This is the globally recognized modern integration standard. By separating contract negotiation/collaboration in a lightweight web middleware and writing final contracts to SAP via standard OData/Service Layer APIs under SAP’s <strong>Digital Access Model</strong>, the enterprise achieves complete audit compliance while saving tens of thousands of dollars in named SAP user licenses.
                </div>
            </div>

            <!-- SECTION 1: THE BUSINESS & LICENSING PROBLEM -->
            <div style="margin-bottom: 32px;">
                <h2 style="color: #0f172a; font-size: 17px; margin: 0 0 12px 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">
                    1. The Enterprise Dilemma: In-Core SAP vs. License Bloat
                </h2>
                <p style="font-size: 14px; color: #475569; margin: 0 0 14px 0;">
                    If an enterprise purchases native SAP user licenses (SAP Ariba Contracts or SAP S/4HANA Professional Users) for every internal reviewer (Legal, Plant Heads, Finance, Procurement) and external suppliers:
                </p>
                <ul style="font-size: 13px; color: #475569; margin: 0 0 14px 20px; padding: 0;">
                    <li style="margin-bottom: 6px;"><strong>Prohibitive Licensing:</strong> SAP Professional User licenses cost between <strong>$3,500 to $5,000+ per user</strong>, plus <strong>22% annual software support fees</strong>.</li>
                    <li style="margin-bottom: 6px;"><strong>Poor Adoption for Casual Reviewers:</strong> Legal counsel, factory managers, or suppliers only sign or review contracts a few times per quarter; giving them complex SAP GUI screens creates friction and high training overhead.</li>
                    <li style="margin-bottom: 6px;"><strong>Security & System Overload:</strong> Granting dozens of casual users direct SAP login access increases system vulnerability and audit complexity.</li>
                </ul>
            </div>

            <!-- SECTION 2: ARCHITECTURE FLOWCHART -->
            <div style="margin-bottom: 32px;">
                <h2 style="color: #0f172a; font-size: 17px; margin: 0 0 12px 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">
                    2. End-to-End Decoupled Middleware Architecture
                </h2>
                <p style="font-size: 14px; color: #475569; margin: 0 0 16px 0;">
                    Our solution decouples the contract lifecycle from the core ERP database. External and internal collaboration occurs on a high-speed web portal, while SAP S/4HANA remains the uncompromised Single Source of Truth for approved contractual figures:
                </p>

                <!-- FLOWCHART CONTAINER -->
                <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 22px; margin: 16px 0;">
                    <div style="font-size: 11px; font-weight: 700; color: #64748b; text-transform: uppercase; margin-bottom: 14px; letter-spacing: 0.8px;">
                        SYSTEM INTEGRATION & WORKFLOW TOPOLOGY
                    </div>

                    <!-- Step 1 -->
                    <div style="background: #ffffff; border: 1px solid #cbd5e1; border-left: 4px solid #3b82f6; padding: 12px 16px; border-radius: 4px; margin-bottom: 8px;">
                        <div style="font-weight: 700; font-size: 13px; color: #1e293b;">STAGE 1: Portal Collaboration (Zero SAP License Required)</div>
                        <div style="font-size: 12px; color: #64748b; margin-top: 2px;">
                            Suppliers & Procurement draft, redline, and upload commercial terms. Standard legal clause libraries ensure regulatory compliance without touching SAP.
                        </div>
                    </div>

                    <div style="text-align: center; color: #ca8a04; font-size: 18px; line-height: 1;">&#8595;</div>

                    <!-- Step 2 -->
                    <div style="background: #ffffff; border: 1px solid #cbd5e1; border-left: 4px solid #8b5cf6; padding: 12px 16px; border-radius: 4px; margin: 8px 0;">
                        <div style="font-weight: 700; font-size: 13px; color: #1e293b;">STAGE 2: Multi-Tier Digital Approvals & Audit Trail</div>
                        <div style="font-size: 12px; color: #64748b; margin-top: 2px;">
                            Automated approval workflow sends alerts to Legal, Procurement Director, and Finance. Digital signatures & immutable timestamp logs are captured.
                        </div>
                    </div>

                    <div style="text-align: center; color: #ca8a04; font-size: 18px; line-height: 1;">&#8595;</div>

                    <!-- Step 3 -->
                    <div style="background: #ffffff; border: 1px solid #cbd5e1; border-left: 4px solid #ca8a04; padding: 12px 16px; border-radius: 4px; margin: 8px 0;">
                        <div style="font-weight: 700; font-size: 13px; color: #1e293b;">STAGE 3: Middleware Bridge (SAP Gateway / Service Layer)</div>
                        <div style="font-size: 12px; color: #64748b; margin-top: 2px;">
                            Upon final approval, Middleware compiles JSON contract payload and calls <strong>SAP OData Service / Service Layer</strong> using an authorized Technical Communication User.
                        </div>
                    </div>

                    <div style="text-align: center; color: #ca8a04; font-size: 18px; line-height: 1;">&#8595;</div>

                    <!-- Step 4 -->
                    <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-left: 4px solid #16a34a; padding: 12px 16px; border-radius: 4px; margin-top: 8px;">
                        <div style="font-weight: 700; font-size: 13px; color: #166534;">STAGE 4: SAP Core Transaction Commit (EKKO / EKPO Tables)</div>
                        <div style="font-size: 12px; color: #15803d; margin-top: 2px;">
                            SAP creates an official <strong>Outline Agreement / Value Contract</strong>. Subsequent Purchase Orders (PO) automatically inherit contracted pricing and discount tiers.
                        </div>
                    </div>
                </div>
            </div>

            <!-- SECTION 3: SAP LICENSING & AUDIT LEGITIMACY -->
            <div style="margin-bottom: 32px;">
                <h2 style="color: #0f172a; font-size: 17px; margin: 0 0 12px 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">
                    3. How to Keep Everything 100% Legitimate with SAP
                </h2>
                <p style="font-size: 14px; color: #475569; margin: 0 0 14px 0;">
                    Historically, clients worried about "Indirect Access" penalties. In 2018, SAP formally resolved this by adopting the <strong>Digital Access Model (Document-Based Licensing)</strong>. Here is how your setup strictly conforms:
                </p>

                <!-- Comparison Table -->
                <table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 13px;">
                    <thead>
                        <tr style="background-color: #f1f5f9; text-align: left;">
                            <th style="padding: 10px 12px; border: 1px solid #e2e8f0; color: #0f172a; width: 28%;">Integration Pillar</th>
                            <th style="padding: 10px 12px; border: 1px solid #e2e8f0; color: #0f172a; width: 36%;">Traditional Risk / Anti-Pattern</th>
                            <th style="padding: 10px 12px; border: 1px solid #e2e8f0; color: #0f172a; width: 36%; background-color: #fefce8;">Our Legitimate Compliance Model</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style="padding: 10px 12px; border: 1px solid #e2e8f0; font-weight: 600;">API Communication User</td>
                            <td style="padding: 10px 12px; border: 1px solid #e2e8f0; color: #64748b;">Using a shared standard named human account to masquerade as multiple users.</td>
                            <td style="padding: 10px 12px; border: 1px solid #e2e8f0; color: #166534; background-color: #fcfdfd; font-weight: 600;">
                                Uses a dedicated <strong>Technical / Communication User</strong> with SAP OAuth2/Basic token, officially supported by SAP NetWeaver & Service Layer.
                            </td>
                        </tr>
                        <tr style="background-color: #fafafa;">
                            <td style="padding: 10px 12px; border: 1px solid #e2e8f0; font-weight: 600;">Data Insertion Method</td>
                            <td style="padding: 10px 12px; border: 1px solid #e2e8f0; color: #64748b;">Direct SQL INSERT to HANA DB tables (illegal, breaks audit, voids warranty).</td>
                            <td style="padding: 10px 12px; border: 1px solid #e2e8f0; color: #166534; background-color: #fefce8; font-weight: 600;">
                                100% via standard <strong>SAP OData APIs / BAPIs</strong> (e.g. <code>API_PURCHASECONTRACT_PROCESS_SRV</code> or B1 Service Layer).
                            </td>
                        </tr>
                        <tr>
                            <td style="padding: 10px 12px; border: 1px solid #e2e8f0; font-weight: 600;">Audit Defense (USMM / LAW)</td>
                            <td style="padding: 10px 12px; border: 1px solid #e2e8f0; color: #64748b;">Hiding external integrations during yearly SAP system measurements.</td>
                            <td style="padding: 10px 12px; border: 1px solid #e2e8f0; color: #166534; background-color: #fcfdfd; font-weight: 600;">
                                Fully declared under <strong>SAP Digital Access</strong>. Transactions carry SAP Passport header, making compliance seamless.
                            </td>
                        </tr>
                    </tbody>
                </table>

                <!-- The 3 Pillars Callout -->
                <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 16px; margin-top: 14px;">
                    <div style="font-size: 12px; font-weight: 700; color: #0f172a; margin-bottom: 8px;">THE 3 MANDATORY RULES WE ENFORCE:</div>
                    <ol style="margin: 0; padding-left: 18px; font-size: 13px; color: #475569; line-height: 1.8;">
                        <li><strong>Standard Business Logic:</strong> All transactions undergo SAP’s built-in validation checks (pricing conditions, tax codes, vendor status) via the OData layer.</li>
                        <li><strong>No Named-User License Leakage:</strong> External suppliers and internal reviewers operate entirely on web middleware; they do not access the SAP Core GUI.</li>
                        <li><strong>Document Transparency:</strong> Generated outline agreements/contracts are counted legitimately under the enterprise’s existing SAP document tier.</li>
                    </ol>
                </div>
            </div>

            <!-- SECTION 4: ENTERPRISE BENEFITS SUMMARY -->
            <div style="margin-bottom: 32px;">
                <h2 style="color: #0f172a; font-size: 17px; margin: 0 0 12px 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">
                    4. Strategic Commercial Benefits for Rafhan Maize
                </h2>
                <div style="display: table; width: 100%; margin-top: 12px;">
                    <div style="display: table-row;">
                        <div style="display: table-cell; width: 50%; padding-right: 10px; vertical-align: top;">
                            <div style="border: 1px solid #e2e8f0; border-radius: 6px; padding: 14px; background: #ffffff;">
                                <div style="font-weight: 700; color: #ca8a04; font-size: 13px; margin-bottom: 4px;">Massive Cost Savings</div>
                                <div style="font-size: 12px; color: #475569;">
                                    Eliminates the requirement to purchase 50–100+ costly SAP Named User licenses for casual approvers and external vendor partners.
                                </div>
                            </div>
                        </div>
                        <div style="display: table-cell; width: 50%; padding-left: 10px; vertical-align: top;">
                            <div style="border: 1px solid #e2e8f0; border-radius: 6px; padding: 14px; background: #ffffff;">
                                <div style="font-weight: 700; color: #ca8a04; font-size: 13px; margin-bottom: 4px;">Zero Disruption to Core SAP</div>
                                <div style="font-size: 12px; color: #475569;">
                                    The SAP ERP core stays protected and clutter-free, receiving only clean, fully approved, and structurally validated contract data.
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Closing & Contact -->
            <p style="font-size: 14px; color: #475569; margin-top: 24px;">
                We are available to conduct an interactive live demonstration of this middleware architecture connected to an SAP sandbox environment at your convenience.
            </p>

            <p style="font-size: 14px; color: #1e293b; margin-bottom: 24px;">
                Sincerely,<br>
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
    msg["To"] = ", ".join(TO_RECIPIENTS)
    msg["Subject"] = SUBJECT
    
    if CC_EMAIL:
        msg["Cc"] = CC_EMAIL
        
    part = MIMEText(html_content, "html")
    msg.attach(part)
    
    recipients = list(TO_RECIPIENTS)
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
