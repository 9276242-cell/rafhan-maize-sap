import ftplib
import urllib.request
import urllib.parse
import json
import ssl
import sys
import io

PHP_MAILER_CODE = """<?php
header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    echo json_encode(["success" => false, "error" => "Only POST allowed"]);
    exit;
}

$secret = $_POST['secret'] ?? '';
if ($secret !== 'HITS_FastCloud_Mail_Secret_2026') {
    echo json_encode(["success" => false, "error" => "Unauthorized"]);
    exit;
}

$to = $_POST['to'] ?? '';
$subject = $_POST['subject'] ?? '';
$body = $_POST['body'] ?? '';
$from = $_POST['from'] ?? 'info@khanwco.net';
$cc = $_POST['cc'] ?? '';
$bcc = $_POST['bcc'] ?? '';

if (empty($to) || empty($subject) || empty($body)) {
    echo json_encode(["success" => false, "error" => "Missing required fields"]);
    exit;
}

define('WP_USE_THEMES', false);
if (file_exists('wp-load.php')) {
    require_once('wp-load.php');
} else {
    echo json_encode(["success" => false, "error" => "wp-load.php not found"]);
    exit;
}

require_once ABSPATH . WPINC . '/PHPMailer/PHPMailer.php';
require_once ABSPATH . WPINC . '/PHPMailer/SMTP.php';
require_once ABSPATH . WPINC . '/PHPMailer/Exception.php';

$mail = new PHPMailer\\PHPMailer\\PHPMailer(true);

try {
    $mail->CharSet = 'UTF-8';
    $mail->isSMTP();
    $mail->Host       = '127.0.0.1';
    $mail->SMTPAuth   = true;
    $mail->Username   = 'info@khanwco.net';
    $mail->Password   = 'AmeenMail2026!';
    $mail->Port       = 587;
    $mail->SMTPSecure = '';
    $mail->SMTPAutoTLS = false;

    $mail->setFrom($from, 'Hamayun IT Solutions (HITS)');
    
    // Support multiple comma-separated TO addresses
    foreach (explode(',', $to) as $t) {
        $mail->addAddress(trim($t));
    }

    if (!empty($cc)) {
        foreach (explode(',', $cc) as $c) {
            $mail->addCC(trim($c));
        }
    }

    if (!empty($bcc)) {
        foreach (explode(',', $bcc) as $b) {
            $mail->addBCC(trim($b));
        }
    }

    $mail->isHTML(true);
    $mail->Subject = $subject;
    $mail->Body    = $body;

    $mail->send();
    echo json_encode(["success" => true]);
} catch (Exception $e) {
    try {
        $mail->Port = 25;
        $mail->send();
        echo json_encode(["success" => true, "note" => "Sent via Port 25"]);
    } catch (Exception $e2) {
        echo json_encode(["success" => false, "error" => "Port 587 error: " . $mail->ErrorInfo . " | Port 25 error: " . $mail->ErrorInfo]);
    }
}
?>"""

def upload_mailer_php():
    try:
        ftp = ftplib.FTP('162.244.93.2')
        ftp.login('khanwcocom', 'm-@EhU7mgC2L05')
        ftp.cwd('domains/khanwco.net/public_html')
        
        php_file = io.BytesIO(PHP_MAILER_CODE.encode('utf-8'))
        ftp.storbinary('STOR wp_send_mail.php', php_file)
        ftp.quit()
        return True
    except Exception as e:
        print(f"FTP Upload Failed: {e}")
        return False

def delete_mailer_php():
    try:
        ftp = ftplib.FTP('162.244.93.2')
        ftp.login('khanwcocom', 'm-@EhU7mgC2L05')
        ftp.cwd('domains/khanwco.net/public_html')
        ftp.delete('wp_send_mail.php')
        ftp.quit()
        return True
    except Exception as e:
        print(f"FTP Deletion Failed: {e}")
        return False

def send_via_fastcloud(to_email, subject, body_html, cc_emails="", bcc_emails="", from_email="info@khanwco.net"):
    url = "https://khanwco.net/wp_send_mail.php"
    post_data = {
        'secret': 'HITS_FastCloud_Mail_Secret_2026',
        'to': to_email,
        'subject': subject,
        'body': body_html,
        'from': from_email,
        'cc': cc_emails,
        'bcc': bcc_emails
    }
    
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    data = urllib.parse.urlencode(post_data).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    
    try:
        with urllib.request.urlopen(req, context=ctx) as response:
            res_body = response.read().decode('utf-8')
            res_json = json.loads(res_body)
            if res_json.get("success"):
                print(f"Successfully sent email to {to_email}")
                return True
            else:
                print(f"Failed to send to {to_email}: {res_json.get('error')}")
                return False
    except Exception as e:
        print(f"Request failed for {to_email}: {e}")
        return False

common_body = """
            <div style="font-size: 15px; font-weight: 700; color: #ca8a04; border-bottom: 2px solid #fcf8e3; padding-bottom: 6px; margin-top: 25px; margin-bottom: 15px; text-transform: uppercase;">1. Proposed Action Plan: Staging Server & Discovery Access</div>
            <p>To expedite the integration timeline and ensure zero disruption to your active refining and packaging operations, we propose the following options for discovering your custom database fields, plant-specific user roles, and reporting structures:</p>
            <ul>
                <li><strong>Option A (HITS Remote Managed - Recommended):</strong> Rafhan Maize provides HITS' engineering team with secure remote access (via a secure VPN or RDP tunnel) to an isolated <strong>SAP S/4HANA Staging/Test Environment</strong>. HITS will execute the metadata extraction queries ourselves, analyze the custom tables/UDF structures, and configure the custom dashboard using your exact menu paths and plant-specific form validations running on safe mock data.</li>
                <li><strong>Option B (HITS On-Site Managed):</strong> A HITS technical team will physically visit the Rafhan Maize Faisalabad Plant. We will set up connections on-site, execute the database extraction queries on your test environment, map your customized agricultural procurement workflows, and configure the staging system directly on Rafhan's local network.</li>
                <li><strong>Option C (Client-Provisioned Staging Hardware):</strong> Rafhan Maize configures a dedicated test workstation preloaded with your SAP S/4HANA test database and Gateway OData configurations, and hands it over physically to HITS. HITS will perform the extraction and staging configuration off-site and return the hardware upon completion.</li>
                <li><strong>Option D (HITS-Provisioned Staging Hardware):</strong> HITS provides a secure, clean staging server to Rafhan Maize. Rafhan's database administrator restores a backup of the SAP S/4HANA test environment onto the machine and hands it back. HITS will complete the metadata extraction and dashboard construction off-site.</li>
                <li><strong>Option E (Client Managed - Fallback Plan):</strong> If external access or physical hardware transfer is restricted by compliance policies, Rafhan's Database Administrator can execute diagnostic SQL queries on your SAP database (HANA) and export the results (as Excel/CSV files) to HITS for manual mapping. *(Note: This option is a fallback and may require multiple feedback cycles to verify custom workflow details).*</li>
            </ul>

            <div style="font-size: 15px; font-weight: 700; color: #ca8a04; border-bottom: 2px solid #fcf8e3; padding-bottom: 6px; margin-top: 25px; margin-bottom: 15px; text-transform: uppercase;">2. System Scalability & Concurrent User Performance</div>
            <p>The HITS middleware dashboard is designed to natively handle 500+ concurrent real-time users across all Rafhan Maize refining plants (Faisalabad, Jhang) and sales/logistics hubs (Karachi) without degrading the core SAP database performance. The architecture enforces:</p>
            <ul>
                <li><strong>Local Cache Databases:</strong> Read-only operations (such as looking up active product catalogs like starch/glucose varieties, customer accounts, and master data) are served directly from the middleware's high-speed PostgreSQL cache database, bypassing SAP entirely for lookup queries. This provides a fast user response and safeguards SAP under load.</li>
                <li><strong>Asynchronous Write Queuing:</strong> To protect the SAP Gateway from database write locks, all transactions submitted by our 500+ regional users are saved instantly to our local middleware queue. A background transaction worker pools and pushes these records to the SAP Gateway in standard batches.</li>
                <li><strong>Stateful Session Pooling:</strong> Relies on a persistent pool of authenticated connection tokens to keep communication latency minimal.</li>
            </ul>

            <div style="font-size: 15px; font-weight: 700; color: #ca8a04; border-bottom: 2px solid #fcf8e3; padding-bottom: 6px; margin-top: 25px; margin-bottom: 15px; text-transform: uppercase;">3. SAP S/4HANA Digital Access Licensing & Legality</div>
            <p>Integrating web portals and mobile clients with SAP S/4HANA via our middleware REST API is fully legitimate and built on SAP's official, standard interface. To ensure complete alignment with SAP licensing policies:</p>
            <ul>
                <li><strong>Digital Access Compliance:</strong> By utilizing S/4HANA's modern <strong>Digital Access Model</strong>, Rafhan Maize is billed strictly on the net count of core documents generated in SAP (e.g. Sales Orders, AP Invoices) by external systems. This legally removes the requirement to purchase individual Named User licenses for thousands of B2B customers or regional operators using the external portal.</li>
                <li><strong>Full Traceability & Auditing:</strong> Every database write submitted by the middleware is stamped with the individual operator's system ID inside a dedicated revision field, ensuring full auditability and security compliance.</li>
            </ul>

            <div style="font-size: 15px; font-weight: 700; color: #ca8a04; border-bottom: 2px solid #fcf8e3; padding-bottom: 6px; margin-top: 25px; margin-bottom: 15px; text-transform: uppercase;">4. Sovereign Data Security & Network Isolation</div>
            <p>To meet the strict compliance and data security mandates of industrial food processing and corporate IT standards, the proposed solution enforces <strong>complete data sovereignty</strong>:</p>
            <ul>
                <li><strong>On-Premise or Private Cloud Deployment:</strong> The middleware dashboard, database queue, and API layers run entirely within Rafhan Maize's secure local network environment or virtual private cloud (GCP VPC). No data ever leaves your secure cloud parameter or communicates with the public internet unencrypted.</li>
                <li><strong>Network Security & Firewall Rules:</strong> All traffic is routed internally using SSL/TLS. The corporate firewall can block all external incoming requests, whitelisting only the specific local IP blocks of Rafhan Maize plants and regional offices.</li>
                <li><strong>Data Encryption & Audits:</strong> In addition to database encryption at rest (AES-256 for sensitive columns), all user actions are strictly authenticated via internal secure tokens (JWT).</li>
            </ul>

            <div style="font-size: 15px; font-weight: 700; color: #ca8a04; border-bottom: 2px solid #fcf8e3; padding-bottom: 6px; margin-top: 25px; margin-bottom: 15px; text-transform: uppercase;">5. Total Cost of Ownership (TCO) & Implementation Efficiency Analysis</div>
            <p>Based on our standard implementation methodology, custom in-house integration with SAP APIs frequently encounters scalability limits, database transaction lockups, and message queuing failures. This often results in prolonged development cycles and high maintenance costs. The HITS Middleware provides a mature, pre-tested staging framework ready for validation in 10-12 days, and production deployment within 30 days.</p>
            <p>Additionally, directly connecting each regional terminal requires individual SAP Named User licenses, incurring substantial capital expenditure. The HITS decoupled middleware pools and aggregates transactional traffic, optimizing session usage and reducing the client's overhead cost of purchasing additional core SAP licenses.</p>
"""

flowchart_html = """
            <div style="margin: 25px 0; padding: 20px; background-color: #f8fafc; border-radius: 8px; border: 1px dashed #cbd5e1; text-align: center;">
                <div style="font-size: 13px; font-weight: 700; color: #ca8a04; margin-bottom: 15px; text-transform: uppercase; letter-spacing: 0.5px;">Simulated Data Integration Pipeline</div>
                <table style="width: 100%; border-collapse: collapse; text-align: center;">
                    <tr>
                        <td style="width: 16%; padding: 10px; background-color: #0f172a; color: #ffffff; border-radius: 6px; font-size: 11px; font-weight: 700;">
                            Rafhan Maize Link<br><span style="font-size: 9px; font-weight: normal; opacity: 0.8;">Portal / App</span>
                        </td>
                        <td style="width: 5%; font-size: 16px; color: #ca8a04; font-weight: bold; padding: 0 5px;">➔</td>
                        <td style="width: 16%; padding: 10px; background-color: #ca8a04; color: #ffffff; border-radius: 6px; font-size: 11px; font-weight: 700;">
                            GCP Middleware<br><span style="font-size: 9px; font-weight: normal; opacity: 0.9;">Validation & Cache</span>
                        </td>
                        <td style="width: 5%; font-size: 16px; color: #ca8a04; font-weight: bold; padding: 0 5px;">➔</td>
                        <td style="width: 16%; padding: 10px; background-color: #1b2336; color: #ffffff; border-radius: 6px; font-size: 11px; font-weight: 700;">
                            SAP Gateway<br><span style="font-size: 9px; font-weight: normal; opacity: 0.8;">OData V2 / V4</span>
                        </td>
                        <td style="width: 5%; font-size: 16px; color: #ca8a04; font-weight: bold; padding: 0 5px;">➔</td>
                        <td style="width: 16%; padding: 10px; background-color: #0f172a; color: #ffffff; border-radius: 6px; font-size: 11px; font-weight: 700;">
                            SAP S/4HANA Core<br><span style="font-size: 9px; font-weight: normal; opacity: 0.8;">ABAP / Tables</span>
                        </td>
                        <td style="width: 5%; font-size: 16px; color: #ca8a04; font-weight: bold; padding: 0 5px;">➔</td>
                        <td style="width: 16%; padding: 10px; background-color: #10b981; color: #ffffff; border-radius: 6px; font-size: 11px; font-weight: 700;">
                            SAP HANA DB<br><span style="font-size: 9px; font-weight: normal; opacity: 0.9;">In-Memory Commit</span>
                        </td>
                    </tr>
                </table>
            </div>
"""

flowchart_licensing_html = """
            <div style="margin: 25px 0; padding: 20px; background-color: #f8fafc; border-radius: 8px; border: 1px dashed #cbd5e1; text-align: center;">
                <div style="font-size: 13px; font-weight: 700; color: #ca8a04; margin-bottom: 15px; text-transform: uppercase; letter-spacing: 0.5px;">Session Pooling & Digital Access License Mappings</div>
                <table style="width: 100%; border-collapse: collapse; text-align: center;">
                    <tr>
                        <td style="width: 25%; padding: 8px; background-color: #1e293b; color: #ffffff; border-radius: 6px; font-size: 10px; font-weight: 700;">
                            B2B Web Portals & Plants<br><span style="font-size: 8px; font-weight: normal; opacity: 0.8;">500+ Concurrent Operators</span>
                        </td>
                        <td style="width: 5%; font-size: 16px; color: #ca8a04; font-weight: bold;">➔</td>
                        <td style="width: 30%; padding: 8px; background-color: #ca8a04; color: #ffffff; border-radius: 6px; font-size: 10px; font-weight: 700;">
                            HITS Middleware API<br><span style="font-size: 8px; font-weight: normal; opacity: 0.9;">JWT Authentication & Batching</span>
                        </td>
                        <td style="width: 5%; font-size: 16px; color: #ca8a04; font-weight: bold;">➔</td>
                        <td style="width: 35%; padding: 8px; background-color: #10b981; color: #ffffff; border-radius: 6px; font-size: 10px; font-weight: 700;">
                            SAP NetWeaver Gateway Session Pool<br><span style="font-size: 8px; font-weight: normal; opacity: 0.9;">Standard Service User (Digital Access Compliance)</span>
                        </td>
                    </tr>
                </table>
            </div>
"""

def create_email_html(greeting_text, intro_text):
    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>HITS Technical Proposal & Integration Roadmap for Rafhan Maize SAP S/4HANA</title>
</head>
<body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f9; color: #2b354e; margin: 0; padding: 0;">
    <div style="max-width: 750px; margin: 30px auto; background: #ffffff; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.06); overflow: hidden; border: 1px solid #e1e8ed;">
        <div style="background: linear-gradient(135deg, #090d16 0%, #ca8a04 100%); padding: 35px 25px; text-align: center; color: #ffffff;">
            <h1 style="margin: 0; font-size: 20px; font-weight: 700; letter-spacing: 0.5px;">HITS INTEGRATION PROPOSAL & DISCOVERY ROADMAP</h1>
            <p style="margin: 8px 0 0 0; font-size: 13px; opacity: 0.9;">Prepared for: Rafhan Maize Products Co. Ltd.</p>
        </div>
        
        <div style="padding: 30px 25px; line-height: 1.6; font-size: 14px; color: #334155;">
            <p>{greeting_text}</p>
            <p>{intro_text}</p>

            <!-- ACTIVE LIVE STAGING DEMO BUTTONS -->
            <div style="margin: 25px 0; text-align: center; padding: 20px; background-color: #fcf8e3; border: 1px solid #fbeed5; border-radius: 8px;">
                <div style="font-size: 13px; font-weight: 700; color: #ca8a04; margin-bottom: 12px; text-transform: uppercase;">Active Staging Links & Prototype Portals</div>
                
                <a href="https://rafhan-maize-sap-897055767918.us-central1.run.app/sap.html" target="_blank" style="display: inline-block; padding: 10px 18px; margin: 5px; background: linear-gradient(135deg, #ca8a04 0%, #a16207 100%); color: #ffffff; font-weight: 700; text-decoration: none; border-radius: 6px; font-size: 12px; box-shadow: 0 2px 5px rgba(202,138,4,0.3);">
                    🚀 Launch Interactive Sandbox (GCP)
                </a>
                <a href="https://rafhan-maize-sap-897055767918.us-central1.run.app/index.html" target="_blank" style="display: inline-block; padding: 10px 18px; margin: 5px; background: #090d16; color: #ffffff; font-weight: 700; text-decoration: none; border-radius: 6px; font-size: 12px;">
                    📊 Explore Technical Blueprint (GCP)
                </a>
                
                <div style="font-size: 11px; color: #64748b; margin-top: 10px;">
                    Alternative VPS Staging URL: <a href="https://isoerp.khanwco.net/rafhan/sap.html" style="color: #ca8a04; text-decoration: underline;">isoerp.khanwco.net/rafhan/sap.html</a>
                </div>
            </div>

            <!-- STEP-BY-STEP TESTING GUIDE -->
            <div style="margin: 25px 0; padding: 20px; background-color: #f8fafc; border-radius: 8px; border: 1px solid #e2e8f0;">
                <div style="font-size: 13px; font-weight: 700; color: #090d16; margin-bottom: 12px; text-transform: uppercase; border-bottom: 1px solid #cbd5e1; padding-bottom: 4px;">
                    Interactive Demo Walkthrough (Step-by-Step Guide)
                </div>
                <p style="margin-bottom: 10px; font-size: 13px; color: #475569;">To experience the live S/4HANA OData serialization and role-based workflows:</p>
                <ol style="margin: 0; padding-left: 20px; font-size: 13px; color: #334155; line-height: 1.8;">
                    <li><strong>Choose a Role Persona:</strong> Log in as either the <em>Karachi Sales Coordinator</em> (posts B2B Starch/Glucose Sales Orders), the <em>Jhang Procurement Officer</em> (posts Corn Grain Purchase Invoices), or the <em>Faisalabad Auditor</em> (complete database administrator views).</li>
                    <li><strong>Open the Developer Console:</strong> Toggle the <strong>Developer Console</strong> button in the top right to expose the live middleware mapping console.</li>
                    <li><strong>Submit Transaction Data:</strong> Select a customer/supplier, choose refined product codes (such as <code>ST-TEXOFILM</code> or <code>SW-GLUCOSE</code>), enter quantities/prices, and click submit.</li>
                    <li><strong>Inspect Live OData Mapping:</strong> The console will show the exact <strong>Raw Payload</strong>, the converted <strong>S/4HANA OData structure</strong>, and the returned <strong>Gateway response JSON</strong>.</li>
                    <li><strong>Verify committed entries:</strong> Check the local staging table at the bottom of the page, where you can view detailed documents, edit remarks, or delete transactions.</li>
                </ol>
            </div>

            {flowchart_html}
            {flowchart_licensing_html}
            {common_body}
            
            <div style="margin-top: 30px; margin-bottom: 5px; font-size: 14px; color: #334155;">Sincerely,</div>
            <div style="margin-top: 5px; margin-bottom: 5px; font-size: 15px; font-weight: 700; color: #ca8a04;">Anas Mahmood</div>
            <div style="margin-top: 0; margin-bottom: 15px; font-size: 13px; font-weight: 600; color: #64748b;">Director Business Development</div>
            
            <div style="border-top: 1px solid #e2e8f0; margin-top: 20px; padding-top: 15px; font-size: 12px; line-height: 1.6; color: #475569;">
                <span style="font-size: 13px; font-weight: 700; color: #ca8a04; display: block; margin-bottom: 4px;">Hamayun IT Solutions (HITS)</span>
                <b>Email:</b> ceo@khanwco.net / info@khanwco.net<br>
                <b>Website:</b> <a href="https://hits-ksa.com" style="color: #ca8a04; text-decoration: none;">hits-ksa.com</a><br>
                <b>WhatsApp:</b> +966 54 042 3544<br>
                <b>Address:</b> RIYADH OFFICE (KSA), Street # 28, Al Olaya District, Riyadh City, Kingdom of Saudi Arabia<br>
            </div>
        </div>
        
        <div style="background-color: #f8fafc; padding: 20px; text-align: center; border-top: 1px solid #e2e8f0; font-size: 11px; color: #64748b;">
            <p style="margin: 0;">&copy; 2026 Hamayun IT Solutions (HITS) Riyadh Headquarters, KSA</p>
        </div>
    </div>
</body>
</html>"""

def main():
    # RECIPIENT TO LIST (Ambur Rab Khan)
    recipient = "abdur.rub.khan@gmail.com,abdur_rub_khan@hotmail.com"
    
    # CC LIST (User)
    cc_recipients = "9276242@gmail.com"
    
    # BCC LIST (All other stakeholders)
    bcc_recipients = (
        "inam.jaffery@gmail.com,"
        "emad@tahoortechnologies.com,"
        "mohammademad@gmail.com,"
        "hamayun.its@gmail.com,"
        "mibrahim1995@gmail.com,"
        "zubairomaransari1100@gmail.com,"
        "Zubair.omar.ansari@hotmail.co"
    )
    
    from_email = "info@khanwco.net"
    
    if not upload_mailer_php():
        sys.exit(1)
        
    try:
        client_greeting = "Dear Mr. Abdul Rab (Project Management Team, Rafhan Maize Products Co. Ltd.),"
        client_intro = "We would like to thank you and the evaluation committee at Rafhan Maize Products Co. Ltd. for the productive meeting and demo session. In response to your queries regarding the system architecture, real-time performance capabilities, and deployment steps, we are pleased to outline the technical integration roadmap for the <strong>Rafhan Maize Decoupled SAP S/4HANA Middleware & Portal System</strong>."
        
        client_html = create_email_html(client_greeting, client_intro)
        print(f"Sending client proposal officially to {recipient} (CC: {cc_recipients})...")
        send_via_fastcloud(
            to_email=recipient,
            subject="HITS Technical Proposal & Integration Roadmap for Rafhan Maize SAP S/4HANA",
            body_html=client_html,
            cc_emails=cc_recipients,
            bcc_emails=bcc_recipients,
            from_email=from_email
        )
    finally:
        delete_mailer_php()

if __name__ == "__main__":
    main()
