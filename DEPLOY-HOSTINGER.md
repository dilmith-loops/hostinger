# Hostinger Deployment Guide — Ceylon Talent Connect

## Step 1 — Upload Files

Upload the contents of this folder to Hostinger via File Manager or FTP.

**Recommended structure on Hostinger:**
```
/home/u123456789/                    ← your account root
    ceylontalentconnect.com/         ← this is public_html or your domain root
        public_html/                 ← web root (must point here — see Step 2)
```

Upload the files like this:
- All files EXCEPT the `public/` folder → upload to `/home/u123456789/ctc-app/`
- Contents of `public/` folder → upload to your domain's `public_html/`
- Then update `public_html/index.php` to fix the path (see Step 3)

---

## Step 2 — Point Domain to public/ directory

In Hostinger hPanel:
1. Go to **Websites → Manage → Advanced → PHP Configuration**
2. Or use: **Domains → Manage → Point to folder → select `/ctc-app/public`**

If you cannot change the document root, use the workaround in Step 3.

---

## Step 3 — Fix index.php paths

Edit `public_html/index.php` and update these two lines to point to where you uploaded the app:

```php
require __DIR__.'/../ctc-app/vendor/autoload.php';
$app = require_once __DIR__.'/../ctc-app/bootstrap/app.php';
```

---

## Step 4 — Create .env

1. Copy `.env.production` to `.env` (rename it)
2. Fill in your Hostinger MySQL credentials:
   - DB_DATABASE, DB_USERNAME, DB_PASSWORD
3. Set your APP_URL to your actual domain

---

## Step 5 — Create the Database

In Hostinger hPanel → Databases → MySQL Databases:
1. Create a new database (e.g. `u123456789_ctc`)
2. Create a user and assign all privileges
3. Put these details in your .env

---

## Step 6 — Run Migrations via phpMyAdmin

Since shared hosting often lacks SSH, import the schema via phpMyAdmin:

1. Go to hPanel → Databases → phpMyAdmin
2. Select your database
3. Run the SQL from: `database/migrations/` (in order by date)

OR if Hostinger gives you SSH access:
```bash
php artisan migrate --force
php artisan db:seed --force
```

---

## Step 7 — Set Permissions

Via File Manager or SSH:
```bash
chmod -R 755 storage/
chmod -R 755 bootstrap/cache/
```

---

## Step 8 — Generate App Key (if needed)

If you changed the APP_KEY in .env, regenerate it:
```bash
php artisan key:generate --force
```

---

## Step 9 — Create Admin User

If the users table is empty, run via SSH or phpMyAdmin:
```sql
INSERT INTO users (name, email, password, created_at, updated_at)
VALUES (
  'Admin',
  'admin@ceylontalentconnect.com',
  '$2y$12$YOUR_BCRYPT_HASH_HERE',
  NOW(), NOW()
);
```

Or via SSH:
```bash
php artisan tinker
>>> App\Models\User::create(['name'=>'Admin','email'=>'admin@ceylontalentconnect.com','password'=>bcrypt('YourPassword123!')]);
```

---

## What's Included

| Folder/File | Purpose |
|---|---|
| `app/` | Laravel application code |
| `bootstrap/` | Laravel bootstrap |
| `config/` | Laravel configuration |
| `database/` | Migrations and seeders |
| `public/` | **Web root** — contains the pre-built React app under `public/ctc/` |
| `resources/views/` | Email templates |
| `routes/` | API and web routes |
| `storage/` | Laravel storage (logs, cache, sessions) |
| `vendor/` | PHP Composer dependencies |
| `artisan` | Laravel CLI tool |
| `.env.production` | Rename to `.env` and fill in credentials |

## What was EXCLUDED (dev only)

- `node_modules/` — 431 MB, only needed to build the React app
- `src/` — React source code, already compiled into `public/ctc/`
- `dist/` — Vite build output, already copied to `public/ctc/`
- `.git/` — 1.4 GB of git history, not needed on server
- Dev config files (vite, eslint, tsconfig, prettier, etc.)

---

## Admin Panel

Access at: `https://ceylontalentconnect.com/ctc/admin`

**SEO & Analytics setup:**
- Go to admin → SEO & Analytics tab
- Enter your Google Analytics 4 ID (G-XXXXXXXX)
- Enter Google Tag Manager ID (GTM-XXXXXXX)
- Enter Google Search Console verification code
- Enter Meta Pixel ID
- Save — tags inject automatically on every page

**Sitemap:** `https://ceylontalentconnect.com/sitemap.xml`  
**Robots.txt:** `https://ceylontalentconnect.com/robots.txt`
