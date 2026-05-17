# BIDLIFY

National & Western Cape tender hub — asbestos tenders nationally; painting, water purifying, roofing, gas, road marking, and automotive repair in the Western Cape.

## Features

- Ingests from **eTenders OCDS API** (from 1 May 2026) plus configurable government HTML sources
- Categories: `ASBESTOS`, `PAINTING`, `WATER_PURIFYING`, `ROOFING`, `GAS`, `ROADMARKING`, `AUTOMOTIVE_REPAIR`
- Auto-sync every **4 hours** (Vercel Cron or in-process scheduler)
- **Sync now** manual button (10-minute rate limit per client)
- Neon Adobe Express–inspired UI

## Preview (local)

**Windows:** double-click [`setup-and-preview.bat`](setup-and-preview.bat) in this folder.

**Cursor terminal** (`Ctrl+`` `):

```powershell
cd "C:\Users\God is Love\Projects\bidlify"
npm install
npx prisma db push
npm run dev
```

Then open [http://localhost:3000](http://localhost:3000) (Ctrl+click the link in the terminal).

See [PREVIEW.md](PREVIEW.md) if `npm` is not found or you don't see `node_modules`.

## Setup

```bash
cd bidlify
cp .env.example .env
npm install
npx prisma db push
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) and click **Sync now** for the first data load.

## Scripts

- `npm run dev` — development server
- `npm run sync` — run sync pipeline from CLI
- `npm run build` — production build

## Deploy (Vercel)

Set environment variables:

- `DATABASE_URL` — PostgreSQL recommended for production (update `prisma/schema.prisma` provider)
- `SYNC_SECRET` — random string for `/api/cron` and scheduled sync
- `NEXT_PUBLIC_APP_URL` — production URL
- `ENABLE_IN_PROCESS_CRON` — `false` when using Vercel Cron (`vercel.json` included)

## Reference aggregators

Footer links to Tender Alerts, Tender Bulletins, Easy Tenders, and Online Tenders for discovery (no paywall scraping in MVP).
