# How to preview BIDLIFY

There is **no Install button** in the editor. Preview = install packages once, then start the dev server.

## Easiest way (Windows)

1. In File Explorer, open folder: `C:\Users\God is Love\Projects\bidlify`
2. **Double-click** `setup-and-preview.bat`
3. If it says Node is missing, install from https://nodejs.org (LTS), then double-click the file again
4. Your browser should open **http://localhost:3000**
5. Click **Sync now** on the site to load tenders

## In Cursor

1. **Terminal** menu → **New Terminal** (or press **Ctrl+`**)
2. Make sure the terminal path shows `bidlify` (if not, run):
   ```
   cd "C:\Users\God is Love\Projects\bidlify"
   ```
3. Run these one at a time:
   ```
   npm install
   npx prisma db push
   npm run dev
   ```
4. When you see `Local: http://localhost:3000`, hold **Ctrl** and click that link

### Open preview panel in Cursor

- **Ctrl+Shift+P** → type **Simple Browser: Show** → Enter
- URL: `http://localhost:3000`

## Why you don't see `node_modules`

`node_modules` is hidden by `.gitignore` until `npm install` finishes. After install, you may still not see it in the file tree unless you expand the folder or disable hiding ignored files.

## If `npm` is not recognized

Node.js is not installed or not on your PATH.

1. Install LTS from https://nodejs.org
2. **Close and reopen Cursor** (important)
3. Run `setup-and-preview.bat` again

## Still stuck?

In terminal, run:

```
node -v
npm -v
```

Copy the output and share it for help.
