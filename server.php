<?php

$publicPath = getcwd();

$uri = urldecode(
    parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH) ?? ''
);

// Serve existing static files (JS, CSS, images, fonts, etc.) directly.
if ($uri !== '/' && file_exists($publicPath.$uri) && !is_dir($publicPath.$uri)) {
    return false;
}

$formattedDateTime = date('D M j H:i:s Y');
$requestMethod     = $_SERVER['REQUEST_METHOD'];
$remoteAddress     = $_SERVER['REMOTE_ADDR'].':'.$_SERVER['REMOTE_PORT'];

file_put_contents('php://stdout', "[$formattedDateTime] $remoteAddress [$requestMethod] URI: $uri\n");

// Handle /ctc/* SPA routing at the server level so that non-prerendered
// pages (e.g. CMS blog posts) work on hard refresh without going through
// Laravel's route matching.
if (preg_match('#^/ctc(/(.*))?$#', $uri, $m)) {
    $sub = isset($m[2]) ? trim($m[2], '/') : '';

    // Serve a prerendered index.html if one exists for this exact path.
    if ($sub !== '') {
        $prerendered = $publicPath.'/ctc/'.$sub.'/index.html';
        if (file_exists($prerendered)) {
            header('Content-Type: text/html; charset=utf-8');
            readfile($prerendered);
            exit;
        }
    }

    // Fall back to the SPA shell — TanStack Router handles the route client-side.
    $shell = $publicPath.'/ctc/index.html';
    if (file_exists($shell)) {
        header('Content-Type: text/html; charset=utf-8');
        readfile($shell);
        exit;
    }
}

// All other requests (API calls, redirects, etc.) go through Laravel.
require_once $publicPath.'/index.php';
