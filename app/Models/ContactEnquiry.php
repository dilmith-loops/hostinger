<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class ContactEnquiry extends Model
{
    protected $fillable = [
        'first_name',
        'last_name',
        'email',
        'phone',
        'support',
        'business_type',
        'timeline',
        'notes',
    ];

    protected $casts = [
        'support' => 'array',
    ];
}
