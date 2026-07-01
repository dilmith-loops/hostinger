<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>New Enquiry</title>
</head>
<body style="margin:0;padding:0;background:#f4f6f9;font-family:'Inter',Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f6f9;padding:40px 0;">
  <tr>
    <td align="center">
      <table width="600" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:12px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.07);">

        <!-- Header -->
        <tr>
          <td style="background:#2D3E50;padding:36px 48px;">
            <p style="margin:0 0 4px;font-size:12px;font-weight:600;text-transform:uppercase;letter-spacing:0.12em;color:#EF4E4E;">New enquiry</p>
            <p style="margin:0;font-size:22px;font-weight:800;color:#ffffff;">
              {{ $data['firstName'] }} {{ $data['lastName'] }}
            </p>
          </td>
        </tr>

        <!-- Body -->
        <tr>
          <td style="padding:48px;">
            <p style="margin:0 0 24px;font-size:15px;color:#64748b;line-height:1.7;">
              A new contact form submission has been received on ceylontalentconnect.com.
            </p>

            <!-- Details -->
            <table width="100%" cellpadding="0" cellspacing="0" style="background:#f8fafc;border-radius:8px;margin-bottom:32px;">
              <tr><td style="padding:24px;">
                <p style="margin:0 0 16px;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;color:#94a3b8;">Contact details</p>
                <table width="100%" cellpadding="0" cellspacing="0">
                  <tr>
                    <td style="padding:7px 0;font-size:13px;color:#94a3b8;width:140px;border-bottom:1px solid #e2e8f0;">Name</td>
                    <td style="padding:7px 0;font-size:13px;font-weight:600;color:#2D3E50;border-bottom:1px solid #e2e8f0;">{{ $data['firstName'] }} {{ $data['lastName'] }}</td>
                  </tr>
                  <tr>
                    <td style="padding:7px 0;font-size:13px;color:#94a3b8;border-bottom:1px solid #e2e8f0;">Email</td>
                    <td style="padding:7px 0;font-size:13px;font-weight:600;border-bottom:1px solid #e2e8f0;">
                      <a href="mailto:{{ $data['email'] }}" style="color:#EF4E4E;text-decoration:none;">{{ $data['email'] }}</a>
                    </td>
                  </tr>
                  <tr>
                    <td style="padding:7px 0;font-size:13px;color:#94a3b8;border-bottom:1px solid #e2e8f0;">Phone</td>
                    <td style="padding:7px 0;font-size:13px;font-weight:600;color:#2D3E50;border-bottom:1px solid #e2e8f0;">
                      <a href="tel:{{ $data['phone'] }}" style="color:#2D3E50;text-decoration:none;">{{ $data['phone'] }}</a>
                    </td>
                  </tr>
                  <tr>
                    <td style="padding:7px 0;font-size:13px;color:#94a3b8;border-bottom:1px solid #e2e8f0;">Business type</td>
                    <td style="padding:7px 0;font-size:13px;font-weight:600;color:#2D3E50;border-bottom:1px solid #e2e8f0;">{{ $data['businessType'] }}</td>
                  </tr>
                  <tr>
                    <td style="padding:7px 0;font-size:13px;color:#94a3b8;border-bottom:1px solid #e2e8f0;">Timeline</td>
                    <td style="padding:7px 0;font-size:13px;font-weight:600;color:#2D3E50;border-bottom:1px solid #e2e8f0;">{{ $data['timeline'] }}</td>
                  </tr>
                  <tr>
                    <td style="padding:7px 0;font-size:13px;color:#94a3b8;border-bottom:1px solid #e2e8f0;vertical-align:top;">Support needed</td>
                    <td style="padding:7px 0;font-size:13px;font-weight:600;color:#2D3E50;border-bottom:1px solid #e2e8f0;">{{ implode(', ', $data['support']) }}</td>
                  </tr>
                  @if(!empty($data['notes']))
                  <tr>
                    <td style="padding:7px 0;font-size:13px;color:#94a3b8;vertical-align:top;">Notes</td>
                    <td style="padding:7px 0;font-size:13px;font-weight:600;color:#2D3E50;">{{ $data['notes'] }}</td>
                  </tr>
                  @endif
                </table>
              </td></tr>
            </table>

            <p style="margin:0;font-size:13px;color:#94a3b8;">
              Submitted on {{ now()->format('d M Y, g:i A') }} AEST
            </p>
          </td>
        </tr>

        <!-- Footer -->
        <tr>
          <td style="background:#f8fafc;padding:24px 48px;border-top:1px solid #e2e8f0;">
            <p style="margin:0;font-size:12px;color:#94a3b8;">
              Ceylon Talent Connect · ceylontalentconnect.com
            </p>
          </td>
        </tr>

      </table>
    </td>
  </tr>
</table>
</body>
</html>
