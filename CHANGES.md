# BaNNa Platform - Major Architecture Changes

## Changes Made

### 1. Removed User Authentication System
- No login/registration required
- **No buyer data storage** - completely anonymous purchases
- Customers contact directly after payment

### 2. Replaced Stripe Payment with QR Code System
- **UPI Payment**: Customers scan QR code or copy UPI ID (urmi@icici)
- **Crypto Payment**: TRC20 address with QR code support
- **No tracking** - customers make payment and contact directly
- No form submissions, no database storage of buyer information

### 3. Simplified Indicator System
- Removed ATAS indicators - **TradingView only**
- Removed `indicator_type` field from Indicator model
- All indicators are now generic TradingView indicators
- Added `price` and `download_link` fields to Indicator model

## Models

### PaymentInfo Model
Stores payment information displayed to customers:
- `upi_id` (default: "urmi@icici")
- `trc20_address` (TRC20 crypto address)
- `qr_code_upi` (UPI QR code image)
- `qr_code_crypto` (Crypto QR code image)

### Removed Models
- ❌ **PurchaseRequest** - No buyer data storage as per requirement

## Purchase Flow (Simplified)

1. **Customer browses indicators** on home page
2. **Clicks indicator** to view details and price
3. **Sees payment options**: UPI QR code or Crypto QR code
4. **Makes payment** using preferred method
5. **Contacts you directly** via email/WhatsApp with transaction details
6. **You manually send** download link after verification

**Note:** No forms, no data collection, completely anonymous!

## Files Modified

### Models (`BaNNa/main/models.py`)
- Updated `Indicator` model: removed `indicator_type`, added `price`, `download_link`
- Kept `PaymentInfo` model for displaying QR codes
- **Removed `PurchaseRequest` model** - no buyer data storage

### Views (`BaNNa/main/views.py`)
- Updated `home()`: shows all indicators (removed type filtering)
- Updated `indicator_detail()`: displays indicator and payment info only (no form handling)

### Forms (`BaNNa/main/forms.py`)
- **Removed `PurchaseRequestForm`** - no data collection

### URLs (`BaNNa/main/urls.py`)
- Added route: `indicator/<int:indicator_id>/` → `indicator_detail`

### Admin (`BaNNa/main/admin.py`)
- Updated `IndicatorAdmin`: removed `indicator_type` filter
- Added `PaymentInfoAdmin`: manages payment QR codes/addresses
- **Removed `PurchaseRequestAdmin`** - no buyer tracking

### Templates
- **home.html**: Removed ATAS section, simplified to show all indicators with prices
- **indicator_detail.html**: Shows indicator details, payment QR codes, contact information (no form)

### CSS (`BaNNa/static/css/style.css`)
- Added styles for indicator cards with price display
- Added hover effects for indicator cards
- Added responsive design for payment page

## Next Steps (Manual Actions Required)

1. **Run Migrations**:
   ```bash
   cd BaNNa
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Create PaymentInfo in Admin**:
   - Go to Django admin
   - Add PaymentInfo record
   - Upload UPI QR code image
   - Upload Crypto QR code image
   - Set UPI ID: urmi@icici
   - Set TRC20 address

3. **Update Existing Indicators** (if any):
   - Add price to each indicator
   - Add download link (Google Drive, Dropbox, etc.)
   - Remove any ATAS indicators

4. **Set Up Contact Method**:
   - Customers will use the contact form to reach you after payment
   - Or provide WhatsApp/Email in the indicator_detail template

## Features Removed
- User authentication (login/register/logout)
- Stripe payment integration
- ATAS indicator type
- Multi-type indicator filtering
- User account management
- **Purchase request tracking** - No buyer data storage
- **Payment proof uploads** - No form submissions

## Security & Privacy Notes
- **Zero data collection** - completely anonymous purchases
- No customer names, emails, or payment proofs stored
- Customers contact you directly after payment
- No database tracking of purchases
- Use temporary/expiring URLs for download links
- Payment verification is entirely manual via direct contact

## Simple Workflow
1. Customer sees indicator and price
2. Customer scans QR code and pays
3. Customer contacts you (email/WhatsApp) with transaction details
4. You verify payment manually
5. You send download link directly to customer

**No forms, no tracking, completely manual and private!**
