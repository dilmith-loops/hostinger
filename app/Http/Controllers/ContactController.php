<?php

namespace App\Http\Controllers;

use App\Mail\EnquiryConfirmation;
use App\Mail\EnquiryNotification;
use App\Models\ContactEnquiry;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Mail;

class ContactController extends Controller
{
    public function index()
    {
        if (!Auth::check()) {
            return response()->json(['error' => 'Unauthorized'], 401);
        }

        $enquiries = ContactEnquiry::orderByDesc('created_at')->get();
        return response()->json($enquiries);
    }

    public function store(Request $request)
    {
        $data = $request->validate([
            'firstName'    => ['required', 'string', 'max:60'],
            'lastName'     => ['required', 'string', 'max:60'],
            'email'        => ['required', 'email', 'max:255'],
            'phone'        => ['required', 'string', 'min:6', 'max:30', 'regex:/^[+\d\s()\-]+$/'],
            'support'      => ['required', 'array', 'min:1'],
            'support.*'    => ['string'],
            'businessType' => ['required', 'string', 'max:100'],
            'timeline'     => ['required', 'string', 'max:50'],
            'notes'        => ['nullable', 'string', 'max:1000'],
        ]);

        $enquiry = ContactEnquiry::create([
            'first_name'    => $data['firstName'],
            'last_name'     => $data['lastName'],
            'email'         => $data['email'],
            'phone'         => $data['phone'],
            'support'       => $data['support'],
            'business_type' => $data['businessType'],
            'timeline'      => $data['timeline'],
            'notes'         => $data['notes'] ?? null,
        ]);

        // Confirmation to the submitter
        Mail::to($data['email'])->send(new EnquiryConfirmation($data));

        // Notification to the business
        Mail::to('info@ceylontalentconnect.com')
            ->send(new EnquiryNotification($data));

        return response()->json([
            'success' => true,
            'id'      => $enquiry->id,
        ], 201);
    }
}
