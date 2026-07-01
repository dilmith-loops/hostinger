<?php

namespace App\Mail;

use Illuminate\Bus\Queueable;
use Illuminate\Mail\Mailable;
use Illuminate\Mail\Mailables\Content;
use Illuminate\Mail\Mailables\Envelope;
use Illuminate\Queue\SerializesModels;

class EnquiryNotification extends Mailable
{
    use Queueable, SerializesModels;

    public function __construct(public array $data) {}

    public function envelope(): Envelope
    {
        return new Envelope(
            subject: 'New Enquiry: ' . $this->data['firstName'] . ' ' . $this->data['lastName'],
        );
    }

    public function content(): Content
    {
        return new Content(
            view: 'mail.enquiry-notification',
        );
    }
}
