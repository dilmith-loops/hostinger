<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>We received your enquiry</title>
</head>
<body style="margin:0;padding:0;background:#f4f6f9;font-family:'Inter',Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f6f9;padding:40px 0;">
  <tr>
    <td align="center">
      <table width="600" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:12px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.07);">

        <!-- Header -->
        <tr>
          <td style="background:#2D3E50;padding:32px 48px;text-align:center;">
            <img src="{{ $message->embed(public_path('logo.png')) }}" alt="Ceylon Talent Connect" width="180" style="display:block;margin:0 auto;max-width:180px;height:auto;" />
          </td>
        </tr>

        <!-- Body -->
        <tr>
          <td style="padding:48px;">
            <p style="margin:0 0 8px;font-size:13px;font-weight:600;text-transform:uppercase;letter-spacing:0.12em;color:#EF4E4E;">
              Enquiry received
            </p>
            <h1 style="margin:0 0 24px;font-size:28px;font-weight:800;color:#2D3E50;line-height:1.2;">
              Thanks, {{ $data['firstName'] }}. We'll be in touch shortly.
            </h1>
            <p style="margin:0 0 24px;font-size:15px;color:#64748b;line-height:1.7;">
              We've received your enquiry and one of our team members will reach out to you within 1–2 business days.
            </p>

            <!-- Summary box -->
            <table width="100%" cellpadding="0" cellspacing="0" style="background:#f8fafc;border-radius:8px;padding:0;margin-bottom:32px;">
              <tr><td style="padding:24px;">
                <p style="margin:0 0 16px;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;color:#94a3b8;">Your enquiry summary</p>
                <table width="100%" cellpadding="0" cellspacing="0">
                  <tr>
                    <td style="padding:6px 0;font-size:13px;color:#94a3b8;width:140px;">Name</td>
                    <td style="padding:6px 0;font-size:13px;font-weight:600;color:#2D3E50;">{{ $data['firstName'] }} {{ $data['lastName'] }}</td>
                  </tr>
                  <tr>
                    <td style="padding:6px 0;font-size:13px;color:#94a3b8;">Email</td>
                    <td style="padding:6px 0;font-size:13px;font-weight:600;color:#2D3E50;">{{ $data['email'] }}</td>
                  </tr>
                  <tr>
                    <td style="padding:6px 0;font-size:13px;color:#94a3b8;">Phone</td>
                    <td style="padding:6px 0;font-size:13px;font-weight:600;color:#2D3E50;">{{ $data['phone'] }}</td>
                  </tr>
                  <tr>
                    <td style="padding:6px 0;font-size:13px;color:#94a3b8;">Business type</td>
                    <td style="padding:6px 0;font-size:13px;font-weight:600;color:#2D3E50;">{{ $data['businessType'] }}</td>
                  </tr>
                  <tr>
                    <td style="padding:6px 0;font-size:13px;color:#94a3b8;">Timeline</td>
                    <td style="padding:6px 0;font-size:13px;font-weight:600;color:#2D3E50;">{{ $data['timeline'] }}</td>
                  </tr>
                  <tr>
                    <td style="padding:6px 0;font-size:13px;color:#94a3b8;vertical-align:top;">Support needed</td>
                    <td style="padding:6px 0;font-size:13px;font-weight:600;color:#2D3E50;">{{ implode(', ', $data['support']) }}</td>
                  </tr>
                  @if(!empty($data['notes']))
                  <tr>
                    <td style="padding:6px 0;font-size:13px;color:#94a3b8;vertical-align:top;">Notes</td>
                    <td style="padding:6px 0;font-size:13px;font-weight:600;color:#2D3E50;">{{ $data['notes'] }}</td>
                  </tr>
                  @endif
                </table>
              </td></tr>
            </table>

            <p style="margin:0 0 8px;font-size:15px;color:#64748b;line-height:1.7;">
              In the meantime, feel free to reach us directly:
            </p>
            <p style="margin:0;font-size:15px;color:#2D3E50;">
              📞 <strong>1300 241 103</strong><br/>
              ✉️ <a href="mailto:info@ceylontalentconnect.com" style="color:#EF4E4E;text-decoration:none;">info@ceylontalentconnect.com</a>
            </p>
          </td>
        </tr>

        <!-- Footer -->
        <tr>
          <td style="background:#f8fafc;padding:24px 48px;border-top:1px solid #e2e8f0;">
            <p style="margin:0;font-size:12px;color:#94a3b8;line-height:1.6;">
              © {{ date('Y') }} Ceylon Talent Connect · Melbourne, Australia &amp; Colombo, Sri Lanka
            </p>
          </td>
        </tr>

      </table>
    </td>
  </tr>
</table>
</body>
</html>
