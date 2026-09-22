<?php

namespace Database\Seeders;

use App\Models\PageContent;
use App\Models\SeoSetting;
use Illuminate\Database\Seeder;

class TestimonialSeeder extends Seeder
{
    public function run(): void
    {
        $heroData = [
            'heading' => 'Client Success',
            'highlight' => 'Stories',
            'subheadline' => 'Hear directly from our partners about how Ceylon Talent Connect has helped them build high-performing teams and scale their operations successfully.',
        ];

        $videoReviewsData = [
            'sectionTitle' => 'Video Reviews',
            'items' => [
                [
                    'id' => 1,
                    'title' => 'ShadeLux',
                    'videoUrl' => 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                    'thumbnail' => '/uploads/testimonials/shadelux_card.png',
                    'quote' => 'A fantastic experience working with Ceylon Talent Connect.',
                    'authorName' => 'Shade Lux',
                    'authorRole' => 'Client',
                    'avatarInitials' => 'SL',
                    'avatarBg' => '#EF4444'
                ]
            ]
        ];

        $clientReviewsData = [
            'sectionTitle' => 'Client Reviews',
            'items' => [
                [
                    'id' => 1,
                    'clientName' => 'Caleb Hughes',
                    'clientRole' => 'Owner, Shadelux',
                    'company' => 'Shadelux',
                    'cardImage' => '/uploads/testimonials/caleb_card.png',
                    'rating' => 5,
                    'quote' => 'I am so pleased that I took a leap of faith and decided to give CTC a go. I must admit to being a little sceptical at first, but from the first meeting I felt completely at ease. Since then, my experience has been nothing other than professional, and very rewarding. Everyone in the team has been great to deal with, and my expectations have been exceeded. I have no hesitations in highly recommending.'
                ],
                [
                    'id' => 2,
                    'clientName' => 'Peter Solomon',
                    'clientRole' => 'COO, Moorup',
                    'company' => 'Moorup',
                    'cardImage' => '/uploads/testimonials/solomon_card_hq.png',
                    'rating' => 5,
                    'quote' => "As a small business, outsourcing to CTC has been one of our best decisions. Over the last few years they've helped us with admin, pricing, invoicing, and customer support, freeing up our time to focus on growing the business. Importantly, they are an integral part of our team. I would highly recommend to anyone involved in a SME business."
                ],
                [
                    'id' => 3,
                    'clientName' => 'Zac Freidin',
                    'clientRole' => 'Owner, Eye View Media',
                    'company' => 'Eye View Media',
                    'cardImage' => '/uploads/testimonials/zac_card.png',
                    'rating' => 5,
                    'quote' => 'The team at CTC have really helped me and my business over the last year. Their wide range of services like Virtual Assistants have created efficiency within my business doing all the admin work. I would highly recommend them to anyone with a service based business.'
                ]
            ]
        ];

        PageContent::updateOrCreate(
            ['page' => 'testimonials', 'key' => 'hero'],
            ['value' => $heroData]
        );

        PageContent::updateOrCreate(
            ['page' => 'testimonials', 'key' => 'videoReviews'],
            ['value' => $videoReviewsData]
        );

        PageContent::updateOrCreate(
            ['page' => 'testimonials', 'key' => 'clientReviews'],
            ['value' => $clientReviewsData]
        );

        SeoSetting::updateOrCreate(
            ['page' => 'testimonials'],
            [
                'meta_title' => 'Client Testimonials & Success Stories | Ceylon Talent Connect',
                'meta_description' => 'Discover how Ceylon Talent Connect empowers Australian businesses with top-tier Sri Lankan talent. Read verified client reviews and video testimonials.',
                'og_title' => 'Client Testimonials & Success Stories | Ceylon Talent Connect',
                'og_description' => 'Discover how Ceylon Talent Connect empowers Australian businesses with top-tier Sri Lankan talent. Read verified client reviews and video testimonials.',
                'focus_keyword' => 'Client Testimonials',
                'robots_index' => 'index',
                'robots_follow' => 'follow',
                'schema_type' => 'WebPage',
                'sitemap_priority' => 0.8,
                'sitemap_changefreq' => 'weekly'
            ]
        );
    }
}
