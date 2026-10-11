"""Venue copy for Urban Pickle.
"""

BRAND_NAME = "Urban Pickle"
TAGLINE = "Pickleball Club"

COURTSITE_CENTRE = (
    "https://www.courtsite.my/centre/Urban%20Pickle/"
    "cmcbibxfl08jw087xkm8ycrfv"
)
COURTSITE_BOOKING = (
    f"{COURTSITE_CENTRE}/select/hourly"
    "?serviceId=&categoryId=clc8tlc5bbt2p6ogmj1xm2h3a"
)
COURTSITE_AVAILABILITY = COURTSITE_BOOKING
PARKING_MAP = "https://go.courtsite.my/upparking"
INSTAGRAM = "https://www.instagram.com/urbanpicklemy/"

PHONE = "+60126002178"
PHONE_DISPLAY = "+60 12-600 2178"
WHATSAPP = "https://wa.me/60126002178"

ADDRESS = (
    "Urban Pickle, Jalan Tun Razak, Taman U Thant, "
    "Kuala Lumpur, Federal Territory of Kuala Lumpur"
)
CITY_STATE = "Kuala Lumpur, Wilayah Persekutuan Kuala Lumpur"
BUSINESS_NAME = "JD Urban Ventures Sdn Bhd"
BUSINESS_NUMBER = "202401042078"

# From notes.txt rate windows (latest bookable end is 12:00 AM)
HOURS = "7:00 AM – 12:00 AM daily"

LATITUDE = 3.1560055
LONGITUDE = 101.7228836
GOOGLE_MAPS_DIR = (
    f"https://www.google.com/maps/dir/?api=1"
    f"&destination={LATITUDE},{LONGITUDE}"
)
WAZE_DIR = (
    f"https://waze.com/ul?ll={LATITUDE},{LONGITUDE}&navigate=yes"
)
# Embed (no API key) — same coordinates as notes.txt
GOOGLE_MAPS_EMBED = (
    f"https://www.google.com/maps?q={LATITUDE},{LONGITUDE}&z=16&output=embed"
)

AMENITIES = [
    "AED",
    "Ball machine",
    "Parking",
    "Changing room",
    "Free parking",
    "Shower",
    "Food",
    "Drinks",
    "Street parking",
    "Pet-friendly",
    "Toiletries",
    "Toilets",
    "Paid parking",
]

# Aligned with notes.txt (text over gallery rate posters)
COURT_RATES = [
    {
        "title": "Covered court",
        "weekday_label": "Monday – Friday",
        "weekday": [
            {"hours": "07:00 AM – 05:00 PM", "price": "RM 50 / hour"},
            {"hours": "05:00 PM – 10:00 PM", "price": "RM 85 / hour"},
            {"hours": "10:00 PM – 12:00 AM", "price": "RM 50 / hour"},
        ],
        "weekend_label": "Saturday – Sunday & public holidays",
        "weekend": [
            {"hours": "07:00 AM – 12:00 AM", "price": "RM 70 / hour"},
        ],
    },
    {
        "title": "Covered court rental + ball machine",
        "weekday_label": "Monday – Friday",
        "weekday": [
            {"hours": "07:00 AM – 05:00 PM", "price": "RM 65 / hour"},
            {"hours": "05:00 PM – 12:00 AM", "price": "RM 100 / hour"},
        ],
        "weekend_label": "Saturday – Sunday & public holidays",
        "weekend": [
            {"hours": "07:00 AM – 12:00 AM", "price": "RM 85 / hour"},
        ],
    },
    {
        "title": "Open court",
        "weekday_label": "Monday – Friday",
        "weekday": [
            {"hours": "07:00 AM – 05:00 PM", "price": "RM 40 / hour"},
            {"hours": "05:00 PM – 10:00 PM", "price": "RM 75 / hour"},
            {"hours": "10:00 PM – 12:00 AM", "price": "RM 40 / hour"},
        ],
        "weekend_label": "Saturday – Sunday & public holidays",
        "weekend": [
            {"hours": "07:00 AM – 12:00 AM", "price": "RM 60 / hour"},
        ],
    },
]

EQUIPMENT = [
    {
        "label": "Paddle rental",
        "detail": "Per paddle, per session",
        "price": "RM 5",
    },
    {
        "label": "Ball for sale",
        "detail": "Over the counter",
        "price": "RM 10 / ball",
    },
]

EQUIPMENT_NOTE = (
    "Paddle rental and balls for sale are available over the counter."
)

ANNOUNCEMENT = (
    "Official parking partner: Ottomu Parking (facing the main road). "
    "Limited free parking at the entrance. "
    "RM4 flat rate at Ottomu (weekday after 5 PM; weekend all day) — "
    "validate at the counter."
)

POLICY_SECTIONS = [
    {
        "title": "Booking refunds & changes",
        "points": [
            "Strictly no refund or carry forward of the non-utilized sessions.",
            "72 hours advance notice must be given for any change of booking "
            "time. Any request to change the booking time is subject to court "
            "availability and can only be made once.",
        ],
    },
    {
        "title": "Rain-affected booking policy",
        "points": [
            "Rain-affected rescheduling requests must be made within 48 hours "
            "of the original booking. WhatsApp +60126002178 to reschedule.",
            "Rain-affected sessions under 35 mins can be rescheduled to a time "
            "within one month from the original booking date, subject to "
            "availability.",
        ],
    },
    {
        "title": "Others",
        "points": [
            "Please do not leave your valuables unattended. We will not be "
            "responsible for any theft.",
            "Kids 12 y/o and below are allowed to enter strictly with adult "
            "supervision only. Please note that the supervising adult is "
            "responsible for their safety and behavior.",
            "Courtsite/Urban Pickle takes no responsibility for any incidents "
            "especially kids aged 12 and below. Parents or guardians should "
            "ensure adequate supervision and take responsibility for their "
            "child's safety. Any damages caused will be charged accordingly.",
        ],
    },
]

HERO_IMAGE = (
    "wx6jgueCZ1hIjKRuvCvbGCmjT4B2-WhatsApp Image 2026-05-07 at 16.10.40.jpeg.webp"
)
COURT_IMAGE = (
    "wx6jgueCZ1hIjKRuvCvbGCmjT4B2-aa765d46-f019-4557-8796-37701b85395e.webp"
)
