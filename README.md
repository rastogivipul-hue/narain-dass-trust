# Narain Dass Rastogi Charitable Trust & NDR Schools, Kiratpur — Website

Static site for **Narain Dass Rastogi Charitable Trust** (registered Delhi, 09 August 1991) and its schools in **Mohalla Jhanda, Kiratpur, District Bijnor, U.P. – 246731**, founded **28 March 1990**.

Live: https://narain-dass-trust.vercel.app/ (Vercel; every push to `main` deploys).

## Schools
1. **Shri Narayan Das Rastogi Saraswati Shishu Mandir** — LKG–Class V, co-educational (UDISE+ 09030704709)
2. **Sri Narayan Das Rastogi Balika Vidya Mandir J.H. School** — girls, Classes VI–VIII (UDISE+ 09030704734)
3. **Shri Narayan Das Rastogi Balika Vidya Mandir Inter College** — girls, Classes IX–XII, UP Board; High School 2004, Intermediate 2006 (UDISE+ 09030704754)

Principal: Shri Devendra Singh (from 1 Aug 2026). 2026: 348 students, 15 teachers, 2 support staff.

## Statutory
- PAN AAATN1994L
- 12AB-equivalent: AAATN1994LE20261, s. 332(8) Income-tax Act 2025 — **provisional**, TY 2026–27 to 2028–29
- 80G-equivalent: AAATN1994LF20261, s. 354(4) Income-tax Act 2025 — **provisional**, TY 2026–27 to 2028–29
- CSR-1: CSR00117504 (SRN AC5909859) • NGO Darpan: DL/2026/1118189

## Structure
- `index.html` — single page (Tailwind Play CDN; no build step yet)
- `data/faculty.json` — faculty directory, rendered into `#faculty` at runtime
- `images/campus/` — campus photos (`*.webp` full size, `*-800.webp` thumbnails)
- `images/payment/` — slot for the bank-issued UPI QR (`upi-qr.png`)
- `js/qrcode.min.js` — vendored QR generator (qrcode-generator by Kazuhiko Arase, MIT)
- `llms.txt`, `llms-full.txt`, `sitemap.xml`

## Donations (KYC first)
The `#donate` section collects donor KYC in the browser (nothing is stored or sent by the site), then shows payment details, then opens a pre-filled email with the UTR for the 80G receipt. Donations go only to the Trust's account at Ujjivan Small Finance Bank, Noida Branch.

To turn on UPI, edit the constants at the top of the script in `index.html`:
```js
const UPI_VPA = "";            // set to the Trust's UPI ID to show the UPI block
const UPI_QR_MODE = "generate"; // or "image" to use images/payment/upi-qr.png
```
With `UPI_VPA = ""` only bank transfer is shown.

## Faculty updates
Edit `data/faculty.json` (same fields per person). Do not add phone numbers, dates of birth or home addresses. Add photos only with the person's consent.

## Photos
Do not publish photos where children's faces are identifiable until parental consent is on file.
